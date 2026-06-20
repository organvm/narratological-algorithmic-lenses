"""Billing routes for paid checkout and subscription licenses."""

from __future__ import annotations

import json
import os
from typing import Literal

from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from pydantic import BaseModel, Field

from narratological_api.auth import (
    AccessTier,
    ApiAccount,
    TierEntitlements,
    require_api_key,
)
from narratological_api.billing import (
    BillingConfigurationError,
    BillingProvider,
    BillingProviderError,
    BillingWebhookResult,
    StripeBillingClient,
    WebhookSignatureError,
    billing_license_store,
    handle_stripe_event,
    stripe_webhook_secret,
    verify_stripe_signature,
)

router = APIRouter()
API_ACCOUNT_DEPENDENCY = Depends(require_api_key)


def _checkout_available(tier: AccessTier) -> bool:
    """Return whether the API process has enough Stripe config for this tier."""
    price_env_by_tier = {
        AccessTier.CREATOR: "NARRATOLOGICAL_STRIPE_CREATOR_PRICE_ID",
        AccessTier.STUDIO: "NARRATOLOGICAL_STRIPE_STUDIO_PRICE_ID",
    }
    price_env = price_env_by_tier.get(tier)
    return bool(
        price_env
        and os.environ.get("NARRATOLOGICAL_STRIPE_SECRET_KEY", "").strip()
        and os.environ.get(price_env, "").strip()
    )


class BillingTierResponse(BaseModel):
    """Public billing metadata for one tier."""

    tier: AccessTier
    entitlements: TierEntitlements
    checkout_available: bool


class CheckoutCreateRequest(BaseModel):
    """Request to start a paid checkout flow."""

    tier: AccessTier = Field(..., description="Paid tier to purchase")
    email: str | None = Field(None, description="Optional customer email prefill")
    success_url: str | None = Field(None, description="Optional post-checkout success URL")
    cancel_url: str | None = Field(None, description="Optional checkout cancellation URL")


class CheckoutCreateResponse(BaseModel):
    """Response containing the provider-hosted checkout URL."""

    provider: BillingProvider
    checkout_session_id: str
    checkout_url: str
    tier: AccessTier
    mode: Literal["subscription"]


class CheckoutLicenseResponse(BaseModel):
    """License material provisioned after a completed checkout session."""

    license_key: str
    account_id: str
    tier: AccessTier
    status: str
    license_fingerprint: str


class SubscriptionStatusResponse(BaseModel):
    """Current subscription/license status for an authenticated API key."""

    account_id: str
    tier: AccessTier
    entitlements: TierEntitlements
    active: bool
    source: str
    subscription_status: str | None
    billing_provider: str | None
    license_fingerprint: str


@router.get("/tiers", response_model=list[BillingTierResponse])
async def list_billing_tiers() -> list[BillingTierResponse]:
    """List public tier metadata for pricing and checkout UIs."""
    from narratological_api.auth import TIER_ENTITLEMENTS

    return [
        BillingTierResponse(
            tier=tier,
            entitlements=entitlements,
            checkout_available=_checkout_available(tier),
        )
        for tier, entitlements in TIER_ENTITLEMENTS.items()
    ]


@router.post("/checkout", response_model=CheckoutCreateResponse)
async def create_checkout_session(request: CheckoutCreateRequest) -> CheckoutCreateResponse:
    """Create a Stripe-hosted checkout session for Creator or Studio."""
    if request.tier == AccessTier.FREE_TRIAL:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": "CHECKOUT_NOT_REQUIRED",
                "message": "The free trial tier does not require checkout.",
            },
        )

    try:
        checkout_session = StripeBillingClient().create_checkout_session(
            tier=request.tier,
            customer_email=request.email,
            success_url=request.success_url,
            cancel_url=request.cancel_url,
        )
    except BillingConfigurationError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "BILLING_NOT_CONFIGURED", "message": str(e)},
        ) from e
    except BillingProviderError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={"code": "BILLING_PROVIDER_ERROR", "message": str(e)},
        ) from e

    return CheckoutCreateResponse(
        provider=BillingProvider.STRIPE,
        checkout_session_id=checkout_session.id,
        checkout_url=checkout_session.url,
        tier=request.tier,
        mode="subscription",
    )


@router.get(
    "/checkout-sessions/{checkout_session_id}/license",
    response_model=CheckoutLicenseResponse,
)
async def get_checkout_license(checkout_session_id: str) -> CheckoutLicenseResponse:
    """Return the license provisioned by a completed checkout session."""
    record = billing_license_store.get_by_checkout_session(checkout_session_id)
    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "LICENSE_NOT_READY",
                "message": "No paid license has been provisioned for this checkout session yet.",
            },
        )

    return CheckoutLicenseResponse(
        license_key=record.license_key,
        account_id=record.account_id,
        tier=record.tier,
        status=record.status,
        license_fingerprint=record.license_key_fingerprint,
    )


@router.get("/subscription", response_model=SubscriptionStatusResponse)
async def get_subscription_status(
    account: ApiAccount = API_ACCOUNT_DEPENDENCY,
) -> SubscriptionStatusResponse:
    """Return the entitlement status for the supplied API/license key."""
    return SubscriptionStatusResponse(
        account_id=account.account_id,
        tier=account.tier,
        entitlements=account.entitlements,
        active=account.premium_access_active,
        source=account.source.value,
        subscription_status=account.subscription_status,
        billing_provider=account.billing_provider,
        license_fingerprint=account.key_fingerprint,
    )


@router.post("/webhooks/stripe", response_model=BillingWebhookResult)
async def receive_stripe_webhook(
    request: Request,
    stripe_signature: str | None = Header(None, alias="Stripe-Signature"),
) -> BillingWebhookResult:
    """Verify and apply Stripe subscription webhooks."""
    payload = await request.body()
    try:
        verify_stripe_signature(
            payload=payload,
            signature_header=stripe_signature,
            endpoint_secret=stripe_webhook_secret(),
        )
    except BillingConfigurationError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "BILLING_WEBHOOK_NOT_CONFIGURED", "message": str(e)},
        ) from e
    except WebhookSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "STRIPE_SIGNATURE_INVALID", "message": str(e)},
        ) from e

    try:
        event = json.loads(payload)
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "STRIPE_EVENT_INVALID", "message": "Webhook body is not valid JSON."},
        ) from e

    return handle_stripe_event(event)

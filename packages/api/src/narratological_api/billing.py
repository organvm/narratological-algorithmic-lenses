"""Billing checkout, webhook, and subscription-license helpers."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import secrets
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from narratological_api.auth import AccessTier, AccountSource, ApiAccount, _fingerprint_key


class BillingProvider(StrEnum):
    """Supported billing provider identifiers."""

    STRIPE = "stripe"


class BillingConfigurationError(Exception):
    """Raised when billing cannot run because environment configuration is incomplete."""


class BillingProviderError(Exception):
    """Raised when the billing provider rejects or fails a request."""


class WebhookSignatureError(Exception):
    """Raised when a webhook signature is absent, expired, or invalid."""


ACTIVE_SUBSCRIPTION_STATUSES = {"active", "trialing"}
STRIPE_CHECKOUT_SESSION_URL = "https://api.stripe.com/v1/checkout/sessions"


class StripeCheckoutSession(BaseModel):
    """Minimal Stripe Checkout Session fields needed by clients."""

    id: str
    url: str


class BillingWebhookResult(BaseModel):
    """Structured result of webhook event handling."""

    received: bool = True
    event_type: str
    action: str
    license_fingerprint: str | None = None
    subscription_status: str | None = None


class BillingLicenseRecord(BaseModel):
    """A billing-issued API license tied to a provider subscription."""

    license_key: str = Field(..., exclude=True)
    license_key_fingerprint: str
    tier: AccessTier
    account_id: str
    status: str
    billing_provider: BillingProvider = BillingProvider.STRIPE
    customer_email: str | None = None
    external_customer_id: str | None = None
    external_subscription_id: str | None = None
    checkout_session_id: str | None = None
    label: str | None = None
    created_at: datetime
    updated_at: datetime

    @property
    def active(self) -> bool:
        """Return whether the subscription currently unlocks paid entitlements."""
        return self.status in ACTIVE_SUBSCRIPTION_STATUSES

    def to_api_account(self) -> ApiAccount:
        """Convert this license into an authentication account context."""
        return ApiAccount(
            account_id=self.account_id,
            tier=self.tier,
            label=self.label,
            key_fingerprint=self.license_key_fingerprint,
            source=AccountSource.BILLING,
            subscription_status=self.status,
            billing_provider=self.billing_provider.value,
            external_customer_id=self.external_customer_id,
            external_subscription_id=self.external_subscription_id,
        )


def _now() -> datetime:
    return datetime.now(UTC)


def _coerce_stripe_id(value: Any) -> str | None:
    """Return a Stripe object ID from either a string or embedded object."""
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and isinstance(value.get("id"), str):
        return value["id"]
    return None


def _coerce_tier(value: Any) -> AccessTier | None:
    """Normalize a provider metadata tier value."""
    if not isinstance(value, str):
        return None
    try:
        tier = AccessTier(value)
    except ValueError:
        return None
    if tier == AccessTier.FREE_TRIAL:
        return None
    return tier


def _generate_license_key() -> str:
    """Generate a user-facing license key suitable for API authentication."""
    return f"nal_{secrets.token_urlsafe(24)}"


class InMemoryBillingLicenseStore:
    """Process-local subscription license store.

    This mirrors the existing quota-store scope. Production deployments should
    back this with a durable database keyed by license fingerprint and provider
    subscription ID.
    """

    def __init__(self) -> None:
        self._records_by_license_key: dict[str, BillingLicenseRecord] = {}
        self._license_key_by_checkout_session: dict[str, str] = {}
        self._license_key_by_subscription: dict[str, str] = {}
        self._lock = threading.Lock()

    def reset(self) -> None:
        """Clear all process-local license records."""
        with self._lock:
            self._records_by_license_key.clear()
            self._license_key_by_checkout_session.clear()
            self._license_key_by_subscription.clear()

    def load_api_accounts(self) -> dict[str, ApiAccount]:
        """Expose billing licenses to the API-key auth layer."""
        with self._lock:
            return {
                license_key: record.to_api_account()
                for license_key, record in self._records_by_license_key.items()
            }

    def get_by_checkout_session(self, checkout_session_id: str) -> BillingLicenseRecord | None:
        """Return a provisioned license by Checkout Session ID."""
        with self._lock:
            license_key = self._license_key_by_checkout_session.get(checkout_session_id)
            if not license_key:
                return None
            return self._records_by_license_key.get(license_key)

    def issue_from_checkout_session(
        self,
        *,
        tier: AccessTier,
        status: str,
        checkout_session_id: str,
        external_subscription_id: str | None,
        external_customer_id: str | None,
        customer_email: str | None,
    ) -> BillingLicenseRecord:
        """Create or return the idempotent license for a completed checkout session."""
        account_id = external_subscription_id or checkout_session_id
        label = customer_email or f"{tier.value} subscription"
        with self._lock:
            existing_key = self._license_key_by_checkout_session.get(checkout_session_id)
            if existing_key:
                existing = self._records_by_license_key[existing_key]
                existing.status = status
                existing.external_subscription_id = (
                    external_subscription_id or existing.external_subscription_id
                )
                existing.external_customer_id = external_customer_id or existing.external_customer_id
                existing.customer_email = customer_email or existing.customer_email
                existing.updated_at = _now()
                if external_subscription_id:
                    self._license_key_by_subscription[external_subscription_id] = existing_key
                return existing

            license_key = _generate_license_key()
            record = BillingLicenseRecord(
                license_key=license_key,
                license_key_fingerprint=_fingerprint_key(license_key),
                tier=tier,
                account_id=account_id,
                status=status,
                customer_email=customer_email,
                external_customer_id=external_customer_id,
                external_subscription_id=external_subscription_id,
                checkout_session_id=checkout_session_id,
                label=label,
                created_at=_now(),
                updated_at=_now(),
            )
            self._records_by_license_key[license_key] = record
            self._license_key_by_checkout_session[checkout_session_id] = license_key
            if external_subscription_id:
                self._license_key_by_subscription[external_subscription_id] = license_key
            return record

    def update_subscription_status(
        self,
        *,
        external_subscription_id: str,
        status: str,
        tier: AccessTier | None = None,
    ) -> BillingLicenseRecord | None:
        """Update an existing license by provider subscription ID."""
        with self._lock:
            license_key = self._license_key_by_subscription.get(external_subscription_id)
            if not license_key:
                return None
            record = self._records_by_license_key[license_key]
            record.status = status
            if tier is not None:
                record.tier = tier
            record.updated_at = _now()
            return record


billing_license_store = InMemoryBillingLicenseStore()


def _stripe_secret_key() -> str:
    key = os.environ.get("NARRATOLOGICAL_STRIPE_SECRET_KEY", "").strip()
    if not key:
        raise BillingConfigurationError("Set NARRATOLOGICAL_STRIPE_SECRET_KEY to enable checkout.")
    return key


def stripe_webhook_secret() -> str:
    """Return configured Stripe webhook signing secret."""
    secret = os.environ.get("NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET", "").strip()
    if not secret:
        raise BillingConfigurationError(
            "Set NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET to verify Stripe webhooks."
        )
    return secret


def _stripe_price_id(tier: AccessTier) -> str:
    env_by_tier = {
        AccessTier.CREATOR: "NARRATOLOGICAL_STRIPE_CREATOR_PRICE_ID",
        AccessTier.STUDIO: "NARRATOLOGICAL_STRIPE_STUDIO_PRICE_ID",
    }
    env_name = env_by_tier.get(tier)
    if env_name is None:
        raise BillingConfigurationError("Checkout is only available for paid tiers.")
    price_id = os.environ.get(env_name, "").strip()
    if not price_id:
        raise BillingConfigurationError(f"Set {env_name} to enable {tier.value} checkout.")
    return price_id


def checkout_success_url(override: str | None = None) -> str:
    """Return a success URL that preserves Stripe's Checkout Session ID token."""
    url = (
        override
        or os.environ.get("NARRATOLOGICAL_CHECKOUT_SUCCESS_URL", "").strip()
        or "http://localhost:3000/billing/success?session_id={CHECKOUT_SESSION_ID}"
    )
    if "{CHECKOUT_SESSION_ID}" not in url:
        separator = "&" if "?" in url else "?"
        url = f"{url}{separator}session_id={{CHECKOUT_SESSION_ID}}"
    return url


def checkout_cancel_url(override: str | None = None) -> str:
    """Return the configured Checkout cancellation URL."""
    return (
        override
        or os.environ.get("NARRATOLOGICAL_CHECKOUT_CANCEL_URL", "").strip()
        or "http://localhost:3000/billing"
    )


class StripeBillingClient:
    """Small Stripe REST client for hosted Checkout sessions."""

    def create_checkout_session(
        self,
        *,
        tier: AccessTier,
        customer_email: str | None = None,
        success_url: str | None = None,
        cancel_url: str | None = None,
    ) -> StripeCheckoutSession:
        """Create a hosted Stripe Checkout Session for a paid subscription tier."""
        secret_key = _stripe_secret_key()
        price_id = _stripe_price_id(tier)
        params = {
            "mode": "subscription",
            "success_url": checkout_success_url(success_url),
            "cancel_url": checkout_cancel_url(cancel_url),
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": "1",
            "allow_promotion_codes": "true",
            "metadata[tier]": tier.value,
            "subscription_data[metadata][tier]": tier.value,
        }
        if customer_email:
            params["customer_email"] = customer_email

        encoded = urllib.parse.urlencode(params).encode("utf-8")
        auth = base64.b64encode(f"{secret_key}:".encode()).decode("ascii")
        request = urllib.request.Request(
            STRIPE_CHECKOUT_SESSION_URL,
            data=encoded,
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            raise BillingProviderError(f"Stripe checkout request failed: {body}") from e
        except urllib.error.URLError as e:
            raise BillingProviderError(f"Stripe checkout request failed: {e.reason}") from e

        session_id = payload.get("id")
        session_url = payload.get("url")
        if not isinstance(session_id, str) or not isinstance(session_url, str):
            raise BillingProviderError("Stripe checkout response did not include id and url.")
        return StripeCheckoutSession(id=session_id, url=session_url)


def verify_stripe_signature(
    *,
    payload: bytes,
    signature_header: str | None,
    endpoint_secret: str,
    tolerance_seconds: int = 300,
) -> None:
    """Verify a Stripe webhook signature without requiring the Stripe SDK."""
    if not signature_header:
        raise WebhookSignatureError("Stripe-Signature header is required.")

    timestamp: int | None = None
    signatures: list[str] = []
    for part in signature_header.split(","):
        key, separator, value = part.partition("=")
        if not separator:
            continue
        if key == "t":
            try:
                timestamp = int(value)
            except ValueError as e:
                raise WebhookSignatureError("Stripe webhook timestamp is invalid.") from e
        elif key == "v1":
            signatures.append(value)

    if timestamp is None or not signatures:
        raise WebhookSignatureError("Stripe webhook signature is missing required fields.")
    if abs(time.time() - timestamp) > tolerance_seconds:
        raise WebhookSignatureError("Stripe webhook signature timestamp is outside tolerance.")

    signed_payload = f"{timestamp}.".encode() + payload
    expected = hmac.new(
        endpoint_secret.encode("utf-8"),
        signed_payload,
        hashlib.sha256,
    ).hexdigest()
    if not any(hmac.compare_digest(expected, signature) for signature in signatures):
        raise WebhookSignatureError("Stripe webhook signature verification failed.")


def _customer_email_from_session(session: dict[str, Any]) -> str | None:
    customer_details = session.get("customer_details")
    if isinstance(customer_details, dict) and isinstance(customer_details.get("email"), str):
        return customer_details["email"]
    customer_email = session.get("customer_email")
    return customer_email if isinstance(customer_email, str) else None


def _handle_checkout_completed(session: dict[str, Any]) -> BillingWebhookResult:
    metadata = session.get("metadata") if isinstance(session.get("metadata"), dict) else {}
    tier = _coerce_tier(metadata.get("tier"))
    session_id = _coerce_stripe_id(session.get("id"))
    if tier is None or session_id is None:
        return BillingWebhookResult(
            event_type="checkout.session.completed",
            action="ignored_missing_tier_or_session",
        )

    subscription_id = _coerce_stripe_id(session.get("subscription"))
    customer_id = _coerce_stripe_id(session.get("customer"))
    record = billing_license_store.issue_from_checkout_session(
        tier=tier,
        status="active",
        checkout_session_id=session_id,
        external_subscription_id=subscription_id,
        external_customer_id=customer_id,
        customer_email=_customer_email_from_session(session),
    )
    return BillingWebhookResult(
        event_type="checkout.session.completed",
        action="license_provisioned",
        license_fingerprint=record.license_key_fingerprint,
        subscription_status=record.status,
    )


def _handle_subscription_event(event_type: str, subscription: dict[str, Any]) -> BillingWebhookResult:
    subscription_id = _coerce_stripe_id(subscription.get("id"))
    if not subscription_id:
        return BillingWebhookResult(event_type=event_type, action="ignored_missing_subscription")

    metadata = subscription.get("metadata") if isinstance(subscription.get("metadata"), dict) else {}
    tier = _coerce_tier(metadata.get("tier"))
    status_value = subscription.get("status")
    status = status_value if isinstance(status_value, str) else "inactive"
    if event_type == "customer.subscription.deleted":
        status = "canceled"

    record = billing_license_store.update_subscription_status(
        external_subscription_id=subscription_id,
        status=status,
        tier=tier,
    )
    if record is None:
        return BillingWebhookResult(
            event_type=event_type,
            action="ignored_unknown_subscription",
            subscription_status=status,
        )
    return BillingWebhookResult(
        event_type=event_type,
        action="subscription_status_updated",
        license_fingerprint=record.license_key_fingerprint,
        subscription_status=record.status,
    )


def _handle_invoice_event(event_type: str, invoice: dict[str, Any]) -> BillingWebhookResult:
    subscription_id = _coerce_stripe_id(invoice.get("subscription"))
    if not subscription_id:
        return BillingWebhookResult(event_type=event_type, action="ignored_missing_subscription")

    status_by_event = {
        "invoice.paid": "active",
        "invoice.payment_succeeded": "active",
        "invoice.payment_failed": "past_due",
    }
    status = status_by_event.get(event_type, "inactive")
    record = billing_license_store.update_subscription_status(
        external_subscription_id=subscription_id,
        status=status,
    )
    if record is None:
        return BillingWebhookResult(
            event_type=event_type,
            action="ignored_unknown_subscription",
            subscription_status=status,
        )
    return BillingWebhookResult(
        event_type=event_type,
        action="subscription_status_updated",
        license_fingerprint=record.license_key_fingerprint,
        subscription_status=record.status,
    )


def handle_stripe_event(event: dict[str, Any]) -> BillingWebhookResult:
    """Apply a verified Stripe webhook event to the license store."""
    event_type = event.get("type")
    data = event.get("data")
    obj = data.get("object") if isinstance(data, dict) else None
    if not isinstance(event_type, str) or not isinstance(obj, dict):
        return BillingWebhookResult(event_type="unknown", action="ignored_invalid_event")

    if event_type == "checkout.session.completed":
        return _handle_checkout_completed(obj)
    if event_type in {
        "customer.subscription.created",
        "customer.subscription.updated",
        "customer.subscription.deleted",
    }:
        return _handle_subscription_event(event_type, obj)
    if event_type in {"invoice.paid", "invoice.payment_succeeded", "invoice.payment_failed"}:
        return _handle_invoice_event(event_type, obj)

    return BillingWebhookResult(event_type=event_type, action="ignored_unhandled_event")

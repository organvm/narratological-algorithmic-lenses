"""Tests for Stripe checkout and billing-issued subscription licenses."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any

import pytest
from fastapi.testclient import TestClient

from narratological_api.auth import quota_store
from narratological_api.billing import (
    StripeBillingClient,
    StripeCheckoutSession,
    billing_license_store,
)

SCRIPT = """INT. WRITERS ROOM - DAY

A writer pins beat cards to a wall.

WRITER
The problem is not the ending. It is the engine.

EXT. STUDIO LOT - NIGHT

The writer crosses the lot with a new stack of pages.
"""


@pytest.fixture(autouse=True)
def billing_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep billing tests isolated from developer shell configuration."""
    for env_name in (
        "NARRATOLOGICAL_API_KEYS",
        "NARRATOLOGICAL_STRIPE_SECRET_KEY",
        "NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET",
        "NARRATOLOGICAL_STRIPE_CREATOR_PRICE_ID",
        "NARRATOLOGICAL_STRIPE_STUDIO_PRICE_ID",
        "NARRATOLOGICAL_CHECKOUT_SUCCESS_URL",
        "NARRATOLOGICAL_CHECKOUT_CANCEL_URL",
    ):
        monkeypatch.delenv(env_name, raising=False)
    billing_license_store.reset()
    quota_store.reset()


def _payload(event: dict[str, Any]) -> bytes:
    return json.dumps(event, separators=(",", ":")).encode("utf-8")


def _stripe_signature(payload: bytes, secret: str = "whsec_test") -> str:
    timestamp = int(time.time())
    signed = f"{timestamp}.".encode() + payload
    digest = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    return f"t={timestamp},v1={digest}"


def _checkout_completed_event() -> dict[str, Any]:
    return {
        "id": "evt_checkout_completed",
        "type": "checkout.session.completed",
        "data": {
            "object": {
                "id": "cs_test_creator",
                "mode": "subscription",
                "metadata": {"tier": "creator"},
                "subscription": "sub_creator",
                "customer": "cus_creator",
                "customer_details": {"email": "writer@example.com"},
            }
        },
    }


def _subscription_deleted_event() -> dict[str, Any]:
    return {
        "id": "evt_subscription_deleted",
        "type": "customer.subscription.deleted",
        "data": {
            "object": {
                "id": "sub_creator",
                "status": "canceled",
                "metadata": {"tier": "creator"},
            }
        },
    }


def _post_signed_stripe_event(client: TestClient, event: dict[str, Any]) -> Any:
    payload = _payload(event)
    return client.post(
        "/billing/webhooks/stripe",
        content=payload,
        headers={
            "Content-Type": "application/json",
            "Stripe-Signature": _stripe_signature(payload),
        },
    )


def _provision_creator_license(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> str:
    monkeypatch.setenv("NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET", "whsec_test")
    response = _post_signed_stripe_event(client, _checkout_completed_event())
    assert response.status_code == 200
    assert response.json()["action"] == "license_provisioned"

    license_response = client.get("/billing/checkout-sessions/cs_test_creator/license")
    assert license_response.status_code == 200
    return license_response.json()["license_key"]


def test_checkout_rejects_free_trial(client: TestClient) -> None:
    response = client.post("/billing/checkout", json={"tier": "free_trial"})

    assert response.status_code == 400
    assert response.json()["detail"]["code"] == "CHECKOUT_NOT_REQUIRED"


def test_checkout_creates_stripe_subscription_session(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    def fake_create_checkout_session(
        self: StripeBillingClient,
        **kwargs: Any,
    ) -> StripeCheckoutSession:
        _ = self
        captured.update(kwargs)
        return StripeCheckoutSession(
            id="cs_test_checkout",
            url="https://checkout.stripe.test/session",
        )

    monkeypatch.setattr(
        StripeBillingClient,
        "create_checkout_session",
        fake_create_checkout_session,
    )

    response = client.post(
        "/billing/checkout",
        json={"tier": "creator", "email": "writer@example.com"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["provider"] == "stripe"
    assert payload["mode"] == "subscription"
    assert payload["checkout_url"] == "https://checkout.stripe.test/session"
    assert captured["tier"] == "creator"
    assert captured["customer_email"] == "writer@example.com"


def test_stripe_webhook_provisions_license_that_unlocks_full_suite(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    license_key = _provision_creator_license(client, monkeypatch)

    subscription = client.get(
        "/billing/subscription",
        headers={"Authorization": f"Bearer {license_key}"},
    )
    assert subscription.status_code == 200
    assert subscription.json()["source"] == "billing"
    assert subscription.json()["active"] is True

    response = client.post(
        "/analysis/narrative-suite",
        headers={"X-API-Key": license_key},
        json={
            "title": "Feature",
            "content": SCRIPT,
            "include_algorithm_details": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["tier"] == "creator"
    assert payload["suite"]["selected_algorithm_count"] == 92
    assert payload["suite"]["full_suite"] is True


def test_subscription_deletion_revokes_paid_license(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    license_key = _provision_creator_license(client, monkeypatch)

    deleted = _post_signed_stripe_event(client, _subscription_deleted_event())
    assert deleted.status_code == 200
    assert deleted.json()["subscription_status"] == "canceled"

    subscription = client.get("/billing/subscription", headers={"X-API-Key": license_key})
    assert subscription.status_code == 200
    assert subscription.json()["active"] is False

    response = client.post(
        "/analysis/narrative-suite",
        headers={"X-API-Key": license_key},
        json={"title": "Feature", "content": SCRIPT},
    )

    assert response.status_code == 402
    assert response.json()["detail"]["code"] == "SUBSCRIPTION_INACTIVE"


def test_stripe_webhook_rejects_invalid_signature(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET", "whsec_test")
    payload = _payload(_checkout_completed_event())

    response = client.post(
        "/billing/webhooks/stripe",
        content=payload,
        headers={"Stripe-Signature": "t=1,v1=bad"},
    )

    assert response.status_code == 400
    assert response.json()["detail"]["code"] == "STRIPE_SIGNATURE_INVALID"

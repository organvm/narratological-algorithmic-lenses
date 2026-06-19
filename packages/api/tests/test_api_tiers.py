"""Tests for API key tiers and quota-gated suite analysis."""

from __future__ import annotations

import json

import pytest
from fastapi.testclient import TestClient

from narratological_api.auth import quota_store

SCRIPT = """INT. WRITERS ROOM - DAY

A writer pins beat cards to a wall.

WRITER
The problem is not the ending. It is the engine.

EXT. STUDIO LOT - NIGHT

The writer crosses the lot with a new stack of pages.
"""


@pytest.fixture(autouse=True)
def api_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    """Configure deterministic API keys for gated route tests."""
    monkeypatch.setenv(
        "NARRATOLOGICAL_API_KEYS",
        json.dumps(
            {
                "free-key": {"tier": "free_trial", "account_id": "trial-acct"},
                "creator-key": {"tier": "creator", "account_id": "creator-acct"},
                "studio-key": {"tier": "studio", "account_id": "studio-acct"},
            }
        ),
    )
    quota_store.reset()


def test_narrative_suite_requires_api_key(client: TestClient) -> None:
    """The commercial endpoint should reject anonymous callers."""
    response = client.post(
        "/analysis/narrative-suite",
        json={"title": "Pilot", "content": SCRIPT},
    )

    assert response.status_code == 401
    assert response.json()["detail"]["code"] == "API_KEY_REQUIRED"


def test_free_trial_returns_preview_and_quota_headers(client: TestClient) -> None:
    """Free trial keys should receive a limited algorithm preview."""
    response = client.post(
        "/analysis/narrative-suite",
        headers={"X-API-Key": "free-key"},
        json={"title": "Pilot", "content": SCRIPT},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "preview"
    assert payload["tier"] == "free_trial"
    assert payload["suite"]["contracted_algorithm_count"] == 92
    assert payload["suite"]["selected_algorithm_count"] == 8
    assert payload["suite"]["full_suite"] is False
    assert len(payload["algorithms"]) == 8
    assert payload["quota"]["used"] == 1
    assert response.headers["X-Quota-Remaining"] == "2"


def test_creator_key_returns_full_92_suite_manifest(client: TestClient) -> None:
    """Creator keys should unlock the full contracted suite."""
    response = client.post(
        "/analysis/narrative-suite",
        headers={"X-API-Key": "creator-key"},
        json={
            "title": "Feature",
            "content": SCRIPT,
            "include_algorithm_details": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ready"
    assert payload["tier"] == "creator"
    assert payload["suite"]["selected_algorithm_count"] == 92
    assert payload["suite"]["full_suite"] is True
    assert len(payload["algorithms"]) == 92
    assert payload["input"]["scene_count"] == 2


def test_quota_gate_rejects_after_monthly_limit(client: TestClient) -> None:
    """The free-trial quota should reject the fourth request in a month."""
    for _ in range(3):
        response = client.post(
            "/analysis/narrative-suite",
            headers={"X-API-Key": "free-key"},
            json={"title": "Pilot", "content": SCRIPT},
        )
        assert response.status_code == 200

    response = client.post(
        "/analysis/narrative-suite",
        headers={"X-API-Key": "free-key"},
        json={"title": "Pilot", "content": SCRIPT},
    )

    assert response.status_code == 429
    detail = response.json()["detail"]
    assert detail["code"] == "MONTHLY_QUOTA_EXCEEDED"
    assert detail["quota"]["used"] == 3
    assert detail["quota"]["remaining"] == 0


def test_studio_key_allows_bearer_auth(client: TestClient) -> None:
    """Bearer auth should work for studio integrations."""
    response = client.post(
        "/analysis/narrative-suite",
        headers={"Authorization": "Bearer studio-key"},
        json={"title": "Studio Draft", "content": SCRIPT},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["tier"] == "studio"
    assert payload["entitlements"]["price_monthly_usd"] == 999

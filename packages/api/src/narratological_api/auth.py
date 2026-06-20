"""API key authentication and tier quota helpers."""

from __future__ import annotations

import hashlib
import json
import os
import threading
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field, ValidationError


class AccessTier(StrEnum):
    """Commercial access tiers for the API."""

    FREE_TRIAL = "free_trial"
    CREATOR = "creator"
    STUDIO = "studio"


class AccountSource(StrEnum):
    """Where an authenticated API account came from."""

    STATIC = "static"
    BILLING = "billing"


class TierEntitlements(BaseModel):
    """Limits and feature gates attached to an access tier."""

    tier: AccessTier = Field(..., description="Machine-readable tier identifier")
    label: str = Field(..., description="Public tier label")
    price_monthly_usd: int = Field(..., ge=0, description="Monthly list price in USD")
    monthly_quota: int = Field(..., ge=1, description="Analysis requests per month")
    max_input_chars: int = Field(..., ge=1, description="Maximum input size per request")
    algorithm_limit: int = Field(..., ge=1, description="Algorithms exposed per request")
    full_suite: bool = Field(..., description="Whether the full 92-algorithm suite is enabled")
    support: str = Field(..., description="Support level included with the tier")


TIER_ENTITLEMENTS: dict[AccessTier, TierEntitlements] = {
    AccessTier.FREE_TRIAL: TierEntitlements(
        tier=AccessTier.FREE_TRIAL,
        label="Free trial",
        price_monthly_usd=0,
        monthly_quota=3,
        max_input_chars=20_000,
        algorithm_limit=8,
        full_suite=False,
        support="Self-serve preview access",
    ),
    AccessTier.CREATOR: TierEntitlements(
        tier=AccessTier.CREATOR,
        label="Creator",
        price_monthly_usd=99,
        monthly_quota=50,
        max_input_chars=120_000,
        algorithm_limit=92,
        full_suite=True,
        support="Email support for individual writers and producers",
    ),
    AccessTier.STUDIO: TierEntitlements(
        tier=AccessTier.STUDIO,
        label="Studio",
        price_monthly_usd=999,
        monthly_quota=1_000,
        max_input_chars=600_000,
        algorithm_limit=92,
        full_suite=True,
        support="Priority support for studios and production teams",
    ),
}


class ApiKeyRecord(BaseModel):
    """Configuration record for a single API key."""

    tier: AccessTier
    account_id: str | None = None
    label: str | None = None


class ApiAccount(BaseModel):
    """Authenticated API account context exposed to routes."""

    account_id: str
    tier: AccessTier
    label: str | None = None
    key_fingerprint: str
    source: AccountSource = AccountSource.STATIC
    subscription_status: str | None = None
    billing_provider: str | None = None
    external_customer_id: str | None = None
    external_subscription_id: str | None = None

    @property
    def entitlements(self) -> TierEntitlements:
        """Return the entitlements attached to this account's tier."""
        return TIER_ENTITLEMENTS[self.tier]

    @property
    def premium_access_active(self) -> bool:
        """Return whether the account can use paid-tier entitlements."""
        if self.tier == AccessTier.FREE_TRIAL:
            return True
        if self.source == AccountSource.STATIC:
            return self.subscription_status not in {"canceled", "inactive", "past_due", "unpaid"}
        return self.subscription_status in {"active", "trialing"}


class QuotaSnapshot(BaseModel):
    """Current quota position after an attempted debit."""

    tier: AccessTier
    period: str
    limit: int
    used: int
    remaining: int


class ApiKeyConfigurationError(Exception):
    """Raised when API key configuration cannot be parsed."""


class QuotaExceededError(Exception):
    """Raised when an account has exhausted its monthly quota."""

    def __init__(self, snapshot: QuotaSnapshot) -> None:
        self.snapshot = snapshot
        super().__init__("Monthly analysis quota exceeded")


def _fingerprint_key(api_key: str) -> str:
    """Return a short non-secret fingerprint for logs and responses."""
    return hashlib.sha256(api_key.encode("utf-8")).hexdigest()[:12]


def _coerce_key_record(value: Any) -> ApiKeyRecord:
    """Normalize supported API-key configuration shapes."""
    if isinstance(value, str):
        return ApiKeyRecord(tier=AccessTier(value))
    if isinstance(value, dict):
        return ApiKeyRecord.model_validate(value)
    raise ApiKeyConfigurationError("API key entries must be tier strings or objects")


def _parse_json_api_keys(raw: str) -> dict[str, ApiAccount]:
    """Parse JSON API key configuration."""
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ApiKeyConfigurationError(f"Invalid JSON API key configuration: {e}") from e

    if not isinstance(payload, dict):
        raise ApiKeyConfigurationError("NARRATOLOGICAL_API_KEYS must be a JSON object")

    accounts: dict[str, ApiAccount] = {}
    for api_key, value in payload.items():
        if not isinstance(api_key, str) or not api_key:
            raise ApiKeyConfigurationError("API key names must be non-empty strings")
        try:
            record = _coerce_key_record(value)
        except (ValidationError, ValueError) as e:
            raise ApiKeyConfigurationError(f"Invalid record for API key {api_key!r}: {e}") from e
        accounts[api_key] = ApiAccount(
            account_id=record.account_id or _fingerprint_key(api_key),
            tier=record.tier,
            label=record.label,
            key_fingerprint=_fingerprint_key(api_key),
        )
    return accounts


def _parse_shorthand_api_keys(raw: str) -> dict[str, ApiAccount]:
    """Parse comma-delimited API key configuration.

    Format: key:tier[:account_id[:label]],key2:tier2
    """
    accounts: dict[str, ApiAccount] = {}
    for entry in raw.split(","):
        entry = entry.strip()
        if not entry:
            continue
        parts = [part.strip() for part in entry.split(":", 3)]
        if len(parts) < 2 or not parts[0]:
            raise ApiKeyConfigurationError(
                "Shorthand API keys must use key:tier[:account_id[:label]]"
            )
        api_key, tier = parts[0], parts[1]
        account_id = parts[2] if len(parts) >= 3 and parts[2] else _fingerprint_key(api_key)
        label = parts[3] if len(parts) == 4 and parts[3] else None
        try:
            access_tier = AccessTier(tier)
        except ValueError as e:
            raise ApiKeyConfigurationError(f"Invalid tier {tier!r} for API key") from e
        accounts[api_key] = ApiAccount(
            account_id=account_id,
            tier=access_tier,
            label=label,
            key_fingerprint=_fingerprint_key(api_key),
        )
    return accounts


def load_api_accounts() -> dict[str, ApiAccount]:
    """Load API accounts from environment configuration.

    ``NARRATOLOGICAL_API_KEYS`` supports either JSON:
    {"key": {"tier": "creator", "account_id": "acct"}}

    or a shorthand form:
    key:creator:acct,key2:studio:studio-acct
    """
    raw = os.environ.get("NARRATOLOGICAL_API_KEYS", "").strip()
    accounts: dict[str, ApiAccount] = {}
    if raw:
        if raw.startswith("{"):
            accounts.update(_parse_json_api_keys(raw))
        else:
            accounts.update(_parse_shorthand_api_keys(raw))

    from narratological_api.billing import billing_license_store

    accounts.update(billing_license_store.load_api_accounts())
    return accounts


class InMemoryQuotaStore:
    """Simple monthly quota store for the API sample gate.

    This is process-local by design. Production deployments should replace this
    with a shared store such as Redis or a billing-system usage ledger.
    """

    def __init__(self) -> None:
        self._usage: dict[tuple[str, str], int] = {}
        self._lock = threading.Lock()

    def _period(self, now: datetime | None = None) -> str:
        current = now or datetime.now(UTC)
        return current.strftime("%Y-%m")

    def snapshot(self, account: ApiAccount) -> QuotaSnapshot:
        """Return current usage without changing it."""
        entitlements = account.entitlements
        period = self._period()
        key = (account.key_fingerprint, period)
        with self._lock:
            used = self._usage.get(key, 0)
        return QuotaSnapshot(
            tier=account.tier,
            period=period,
            limit=entitlements.monthly_quota,
            used=used,
            remaining=max(entitlements.monthly_quota - used, 0),
        )

    def consume(self, account: ApiAccount, units: int = 1) -> QuotaSnapshot:
        """Debit an account quota and return the resulting usage snapshot."""
        entitlements = account.entitlements
        period = self._period()
        key = (account.key_fingerprint, period)
        with self._lock:
            used = self._usage.get(key, 0)
            if used + units > entitlements.monthly_quota:
                raise QuotaExceededError(
                    QuotaSnapshot(
                        tier=account.tier,
                        period=period,
                        limit=entitlements.monthly_quota,
                        used=used,
                        remaining=max(entitlements.monthly_quota - used, 0),
                    )
                )
            used += units
            self._usage[key] = used
        return QuotaSnapshot(
            tier=account.tier,
            period=period,
            limit=entitlements.monthly_quota,
            used=used,
            remaining=max(entitlements.monthly_quota - used, 0),
        )

    def reset(self) -> None:
        """Clear all process-local usage records."""
        with self._lock:
            self._usage.clear()


quota_store = InMemoryQuotaStore()

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
bearer_auth = HTTPBearer(auto_error=False)
API_KEY_HEADER_DEPENDENCY = Depends(api_key_header)
BEARER_AUTH_DEPENDENCY = Depends(bearer_auth)


async def require_api_key(
    header_key: str | None = API_KEY_HEADER_DEPENDENCY,
    bearer_credentials: HTTPAuthorizationCredentials | None = BEARER_AUTH_DEPENDENCY,
) -> ApiAccount:
    """Authenticate a request using X-API-Key or Authorization: Bearer."""
    api_key = header_key
    if api_key is None and bearer_credentials is not None:
        api_key = bearer_credentials.credentials

    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "code": "API_KEY_REQUIRED",
                "message": "Provide an API key with X-API-Key or Authorization: Bearer.",
            },
        )

    try:
        accounts = load_api_accounts()
    except ApiKeyConfigurationError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "code": "API_KEYS_MISCONFIGURED",
                "message": str(e),
            },
        ) from e

    if not accounts:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "code": "API_KEYS_NOT_CONFIGURED",
                "message": "Set NARRATOLOGICAL_API_KEYS before using gated API routes.",
            },
        )

    account = accounts.get(api_key)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "code": "API_KEY_INVALID",
                "message": "The supplied API key is not recognized.",
            },
        )

    return account

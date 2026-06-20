# Narratological API Pricing and Access

This document defines the commercial API gate for the 92-algorithm narrative
analysis suite. The implementation lives in `packages/api` and supports both
operator-configured API keys and Stripe-issued subscription licenses.

## Tiers

| Tier | Price | Monthly quota | Request size | Suite access | Intended user |
| --- | ---: | ---: | ---: | --- | --- |
| Free trial | $0 | 3 analyses | 20,000 characters | 8-algorithm preview | Evaluation and sandbox integrations |
| Creator | $99/month | 50 analyses | 120,000 characters | Full contracted 92-algorithm suite | Individual scriptwriters, producers, and consultants |
| Studio | $999/month | 1,000 analyses | 600,000 characters | Full contracted 92-algorithm suite | Studios, production companies, and batch evaluation workflows |

The source compendium can contain more algorithms than the original commercial
contract. The gated endpoint preserves the public `narratological-92` contract by
selecting a deterministic 92-algorithm suite from the 14 legacy studies.

## API Key And License Configuration

Set `NARRATOLOGICAL_API_KEYS` in the API process for free trials, local
development, or manually issued enterprise licenses. Do not commit live keys.

JSON format:

```bash
export NARRATOLOGICAL_API_KEYS='{
  "trial-example-key": {"tier": "free_trial", "account_id": "trial-local"},
  "creator-example-key": {"tier": "creator", "account_id": "creator-local"},
  "studio-example-key": {"tier": "studio", "account_id": "studio-local"}
}'
```

Shorthand format:

```bash
export NARRATOLOGICAL_API_KEYS='trial-key:free_trial:trial-local,creator-key:creator:creator-local,studio-key:studio:studio-local'
```

Clients may authenticate with either:

```http
X-API-Key: <key>
```

or:

```http
Authorization: Bearer <key>
```

Stripe checkout provisions license keys that use the same headers. Billing
licenses are active only while their subscription status is `active` or
`trialing`; canceled, unpaid, inactive, or past-due paid licenses receive
`402 SUBSCRIPTION_INACTIVE` on premium routes. Free trial keys keep their preview
access and quota behavior.

## Stripe Checkout Configuration

Configure Stripe in the API process:

```bash
export NARRATOLOGICAL_STRIPE_SECRET_KEY='sk_test_...'
export NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET='whsec_...'
export NARRATOLOGICAL_STRIPE_CREATOR_PRICE_ID='price_creator_monthly'
export NARRATOLOGICAL_STRIPE_STUDIO_PRICE_ID='price_studio_monthly'
export NARRATOLOGICAL_CHECKOUT_SUCCESS_URL='http://localhost:3000/billing/success'
export NARRATOLOGICAL_CHECKOUT_CANCEL_URL='http://localhost:3000/billing'
```

`NARRATOLOGICAL_CHECKOUT_SUCCESS_URL` automatically receives a
`session_id={CHECKOUT_SESSION_ID}` query parameter if one is not already present.

Create a paid checkout session:

```bash
curl -X POST http://localhost:8000/billing/checkout \
  -H "Content-Type: application/json" \
  -d '{"tier": "creator", "email": "writer@example.com"}'
```

The response includes `checkout_url`. After the customer completes checkout,
Stripe sends `checkout.session.completed` to:

```text
POST /billing/webhooks/stripe
```

The API verifies the `Stripe-Signature` header with
`NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET`, provisions a subscription license, and
tracks later `customer.subscription.*` and invoice payment events.

After the success redirect, retrieve the generated API license:

```bash
curl http://localhost:8000/billing/checkout-sessions/cs_test_123/license
```

The React dashboard exposes this flow at `/billing` and reads the completed
Checkout Session ID on `/billing/success`.

Check any key or license:

```bash
curl http://localhost:8000/billing/subscription \
  -H "Authorization: Bearer $NARRATOLOGICAL_API_KEY"
```

## Sample Endpoint

`POST /analysis/narrative-suite`

```bash
curl -X POST http://localhost:8000/analysis/narrative-suite \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $NARRATOLOGICAL_API_KEY" \
  -d '{
    "title": "Feature Draft",
    "format": "Feature",
    "content": "INT. ROOM - DAY\n\nA writer faces a wall of cards.",
    "include_algorithm_details": true
  }'
```

The response includes:

- `analysis_id`: deterministic ID for the submitted text and account.
- `tier` and `entitlements`: the active tier contract.
- `quota`: current monthly usage after the request is accepted.
- `input`: lightweight Fountain parse summary.
- `suite`: contracted, catalog, selected, and full-suite status.
- `studies`: per-study coverage across the selected algorithm suite.
- `algorithms`: selected algorithm metadata when requested or when the tier is a preview.

Current behavior is a synchronous manifest/preview. It validates the key or
billing license, enforces subscription status for paid tiers, enforces request-size
limits, debits monthly quota, and returns the suite selection that a future async
LLM runner can execute behind the same gate.

## Production Notes

The quota and billing license stores are process-local and reset when the API
process restarts. Replace `InMemoryQuotaStore` and
`InMemoryBillingLicenseStore` with Redis, Postgres, or the billing ledger before
charging external users.

The API returns raw Stripe-issued license keys from the checkout-session license
endpoint so customers can authenticate. Internally, route responses use short
SHA-256 key fingerprints. Keep static raw keys and Stripe secrets in a secret
manager or deployment environment, not in source control.

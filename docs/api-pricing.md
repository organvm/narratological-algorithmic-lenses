# Narratological API Pricing and Access

This document defines the initial commercial API gate for the 92-algorithm narrative
analysis suite. The implementation lives in `packages/api` and is intentionally
API-key based so scriptwriters, producers, and studios can integrate before a full
billing provider is added.

## Tiers

| Tier | Price | Monthly quota | Request size | Suite access | Intended user |
| --- | ---: | ---: | ---: | --- | --- |
| Free trial | $0 | 3 analyses | 20,000 characters | 8-algorithm preview | Evaluation and sandbox integrations |
| Creator | $99/month | 50 analyses | 120,000 characters | Full contracted 92-algorithm suite | Individual scriptwriters, producers, and consultants |
| Studio | $999/month | 1,000 analyses | 600,000 characters | Full contracted 92-algorithm suite | Studios, production companies, and batch evaluation workflows |

The source compendium can contain more algorithms than the original commercial
contract. The gated endpoint preserves the public `narratological-92` contract by
selecting a deterministic 92-algorithm suite from the 14 legacy studies.

## API Key Configuration

Set `NARRATOLOGICAL_API_KEYS` in the API process. Do not commit live keys.

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

Current behavior is a synchronous manifest/preview. It validates the key, enforces
request-size limits, debits monthly quota, and returns the suite selection that a
future async LLM runner can execute behind the same gate.

## Production Notes

The quota store is process-local and resets when the API process restarts. Replace
`InMemoryQuotaStore` with Redis, Postgres, or the billing ledger before charging
external users.

The API stores and returns only short SHA-256 key fingerprints internally. Keep the
raw keys in a secret manager or deployment environment, not in source control.

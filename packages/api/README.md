# narratological-api

FastAPI backend for narratological analysis.

## Installation

```bash
pip install narratological-api
```

## Usage

```bash
# Start the server
uvicorn narratological_api.main:app --reload

# API documentation available at http://localhost:8000/docs
```

For gated commercial routes, configure API keys before starting the server:

```bash
export NARRATOLOGICAL_API_KEYS='trial-key:free_trial:trial-local,creator-key:creator:creator-local,studio-key:studio:studio-local'
```

See [../../docs/api-pricing.md](../../docs/api-pricing.md) for tier limits, pricing, and
production notes.

## Endpoints

- `GET /studies/` - List all studies
- `GET /studies/{study_id}` - Get a specific study
- `GET /studies/{study_id}/axioms` - Get study axioms
- `GET /studies/{study_id}/algorithms` - Get study algorithms
- `GET /studies/search/axioms?q=query` - Search axioms
- `POST /analysis/scene` - Analyze a scene
- `POST /analysis/narrative-suite` - API-key gated 92-algorithm suite sample endpoint
- `GET /diagnostics/metrics` - Get diagnostic metrics

# Repository Guidelines

Global policy: /Users/4jp/AGENTS.md applies and cannot be overridden.

## Project Structure & Module Organization
- `specs/` holds the narrative source material, templates, and JSON exports used by the software layer.
- `packages/core/` is the Python library (Pydantic models, algorithms, diagnostics).
- `packages/cli/` is the Typer CLI wrapper around the core library.
- `packages/api/` is the FastAPI service.
- `packages/web/` is the React + Vite UI.
- `open-view-analysis/` contains research drafts and worksheets.
- Tests live under `packages/*/tests` (currently `packages/core/tests`).

## Build, Test, and Development Commands
```bash
# Python workspace
uv sync
uv run pytest
uv run narratological --help
uv run uvicorn narratological_api.main:app --reload

# Web app (from repo root)
npm run web:dev
npm run web:build
npm run web:test

# Or from packages/web
npm install
npm run dev
npm run test
```

## Coding Style & Naming Conventions
- Python: 4-space indent, type hints everywhere, `ruff` line length 100 (Py3.11), `mypy` runs in strict mode.
- TypeScript/React: follow existing 2-space indent and single-quote style in `packages/web/src`.
- Naming: snake_case for Python modules/functions, PascalCase for classes and React components, `useX` prefix for hooks.

## Testing Guidelines
- Pytest is configured with `testpaths = ["packages/*/tests"]`.
- Add tests when changing models or algorithms; mirror expected data in `specs/03-structured-data/`.
- Web tests use Vitest: `npm run test` or `npm run test:coverage` in `packages/web`.

## Commit & Pull Request Guidelines
- Commits are descriptive sentence-case summaries (see git history); use a body with bullets for multi-part changes.
- Include `Co-Authored-By:` when pairing.
- PRs should explain intent, link relevant issues/specs, and include UI screenshots for web changes.
- Mention test commands executed and any skipped coverage.

## Configuration & Secrets
- LLM providers require `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`; use the mock provider for tests where possible.
- Keep large spec JSONs under `specs/` and avoid duplicating data in code.

<!-- ORGANVM:AUTO:START -->
## Agent Context (auto-generated — do not edit)

This repo participates in the **ORGAN-I (Theory)** swarm.

### Active Subscriptions
- Event: `governance.updated` → Action: Check compliance with updated governance rules
- Event: `health-audit.completed` → Action: Review audit findings for this repo

### Production Responsibilities
- **Produce** `dependency` for organvm-ii-poiesis/art-from--narratological-algorithmic-lenses

### External Dependencies
- *No external dependencies*

### Governance Constraints
- Adhere to unidirectional flow: I→II→III
- Never commit secrets or credentials

*Last synced: 2026-06-06T01:01:09Z*
<!-- ORGANVM:AUTO:END -->

# Narratological Algorithmic Lenses

[![CI](https://github.com/a-organvm/narratological-algorithmic-lenses/actions/workflows/ci.yml/badge.svg)](https://github.com/a-organvm/narratological-algorithmic-lenses/actions/workflows/ci.yml)

Narratological Algorithmic Lenses turns narrative craft theory into executable
analysis. It formalizes principles from Aristotle, Bharata Muni, Bergman,
Tarkovsky, Pixar, Zelda, Alan Moore, Phoebe Waller-Bridge, South Park, and other
traditions as structured algorithms that can inspect scripts, diagnose weak
structure, generate reports, and power API or UI workflows.

The repository is both a research corpus and a software stack:

- `specs/` contains completed studies, templates, source material, protocol
  documentation, and case-study drafts.
- `packages/core/` loads the compendium, models studies with Pydantic, parses
  Fountain, runs diagnostics, and exposes algorithm registries.
- `packages/cli/` provides the `narratological` Typer CLI.
- `packages/api/` exposes FastAPI routes, including the gated commercial
  `narratological-92` sample endpoint.
- `packages/web/` provides a React + Vite dashboard for exploration and analysis.

The source compendium currently includes 28 completed studies and 141 algorithms.
The commercial API surface preserves a stable 92-algorithm product shape by
selecting a deterministic suite from 14 legacy studies.

## What It Is

Narrative feedback is usually subjective, prose-heavy, and hard to repeat across
drafts. This project treats narrative principles as inspectable rules:

- **Axioms** express a creator or tradition's craft premise.
- **Algorithms** define inputs, outputs, and pseudocode for applying that premise.
- **Diagnostics** convert craft failure modes into measurable checks.
- **Protocols** scale analysis from quick triage to a full multi-role review.
- **Script Doctor workflows** combine creator lenses into paired consultations.

The result is a toolkit for asking concrete questions such as:

- Are scenes causally bound by "therefore" and "but" relationships, or merely
  sequenced as "and then" events?
- Which scenes are reorderable or removable without damaging the story?
- Which framework best exposes a script's current failure mode?
- What would two incompatible craft traditions agree on, and where would they
  disagree?

## Who Pays

The open repository is useful to researchers, students, and developers, but the
commercial buyer is the person or organization that needs repeatable narrative
analysis at production speed.

| Buyer | Why they pay | Best fit |
| --- | --- | --- |
| Individual screenwriters, producers, script consultants, and narrative designers | They need structured feedback across drafts without turning every pass into a bespoke consulting engagement. | Creator |
| Studios, production companies, writers' rooms, game studios, and development teams | They need consistent batch evaluation, larger request sizes, and predictable support. | Studio |
| Evaluators, students, and integration developers | They need to test the suite shape, auth contract, and response payload before paying. | Free trial |

Scholars and educators can use the compendium and core library directly for
comparative narrative work. Revenue is expected to come from API access and
production integrations, not from restricting the research notes.

## Core Capabilities

### Compendium

The compendium captures formalized narrative frameworks across classical theory,
film, television, games, comics, oral epic, and meta-analysis. Examples include:

- Classical: Aristotle, Bharata Muni, Ovid, Plato, Horace, African Oral Epic.
- Film: Tarkovsky, Bergman, Tarantino, Lynch, Kubrick.
- Television: Phoebe Waller-Bridge, Larry David, South Park.
- Games: Zelda, Final Fantasy.
- Comics and prose: Alan Moore, Grant Morrison, Jack Kirby, Neil Gaiman, Tolkien.
- Meta frameworks: 8-role analyst system and attention mechanics.

### Diagnostics

The diagnostic layer evaluates structural health through checks such as:

- **Causal binding:** ratio of causal connectors versus sequential connectors.
- **Reorderability:** scenes that can move without breaking causality.
- **Necessity:** scenes that serve no irreplaceable plot, character, or thematic
  function.
- **Information economy:** redundant exposition, missing setup, and weak payoff
  structure.

### Protocols

Seven protocol levels from `specs/08-protocol-framework/` scale analysis depth:

| Level | Purpose |
| --- | --- |
| P1-P2 | Triage and diagnostic awareness |
| P3-P4 | Craft analysis and character-focused review |
| P5-P6 | Thematic synthesis and revision planning |
| P7 | Full multi-role analysis and framework extension |

### Interfaces

- **CLI:** local study exploration, algorithm execution, diagnostics, protocol
  runs, and Script Doctor consultations.
- **API:** FastAPI service for studies, diagnostics, and the gated
  `/analysis/narrative-suite` commercial integration target.
- **Web:** React dashboard for browsing studies, viewing algorithms, running
  diagnostics, and working with Script Doctor flows.
- **MCP and VS Code packages:** integration surfaces for model tools and editor
  workflows.

## Install

### Prerequisites

- Python 3.11+
- `uv`
- Node.js and `npm` for the web dashboard
- Optional LLM provider access:
  - local Ollama server for the default `ollama` provider
  - `OPENAI_API_KEY` for OpenAI
  - `ANTHROPIC_API_KEY` for Anthropic

### Workspace Setup

```bash
git clone https://github.com/a-organvm/narratological-algorithmic-lenses.git
cd narratological-algorithmic-lenses

uv sync
npm install
```

### API Key And Billing Setup For Gated Routes

The public commercial sample endpoint accepts either operator-configured API keys
or Stripe-issued subscription licenses. Use development keys locally; do not
commit live keys.

```bash
export NARRATOLOGICAL_API_KEYS='trial-key:free_trial:trial-local,creator-key:creator:creator-local,studio-key:studio:studio-local'
export NARRATOLOGICAL_API_KEY='trial-key'
```

JSON configuration is also supported:

```bash
export NARRATOLOGICAL_API_KEYS='{
  "trial-example-key": {"tier": "free_trial", "account_id": "trial-local"},
  "creator-example-key": {"tier": "creator", "account_id": "creator-local"},
  "studio-example-key": {"tier": "studio", "account_id": "studio-local"}
}'
```

For paid self-serve checkout, configure Stripe in the API process:

```bash
export NARRATOLOGICAL_STRIPE_SECRET_KEY='sk_test_...'
export NARRATOLOGICAL_STRIPE_WEBHOOK_SECRET='whsec_...'
export NARRATOLOGICAL_STRIPE_CREATOR_PRICE_ID='price_creator_monthly'
export NARRATOLOGICAL_STRIPE_STUDIO_PRICE_ID='price_studio_monthly'
```

Stripe checkout is exposed at `POST /billing/checkout`, webhooks land at
`POST /billing/webhooks/stripe`, and completed sessions expose the generated API
license at `GET /billing/checkout-sessions/{session_id}/license`. The web
dashboard includes `/billing` and `/billing/success` screens for the same flow.

## Usage

### CLI

Explore the compendium:

```bash
uv run narratological info
uv run narratological study list
uv run narratological study show bergman
uv run narratological algorithm list --study pixar
uv run narratological algorithm show pixar.engineer_empathy
```

Run diagnostics on a Fountain or text script:

```bash
uv run narratological diagnose all my_script.fountain
uv run narratological diagnose causal my_script.fountain --target 0.8
uv run narratological diagnose framework my_script.fountain bergman
```

Generate analysis reports:

```bash
uv run narratological analyze script my_script.fountain --framework pixar --reports coverage,beatmap
uv run narratological analyze protocol my_script.fountain --level P3
```

Run a Script Doctor consultation:

```bash
uv run narratological analyze script-doctor my_script.fountain --sequence B
uv run narratological analyze script-doctor my_script.fountain --primary larry-david --secondary aristotle
```

Most analysis commands use the `ollama` provider by default. To use another
provider:

```bash
uv run narratological diagnose all my_script.fountain --provider openai --model gpt-4o
uv run narratological analyze protocol my_script.fountain --provider anthropic
uv run narratological diagnose all my_script.fountain --provider mock
```

### API

Start the FastAPI service:

```bash
uv run uvicorn narratological_api.main:app --reload
```

Open the interactive docs at `http://localhost:8000/docs`.

Call the gated commercial suite endpoint:

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

The current endpoint validates the key or billing license, enforces active paid
subscriptions for premium tiers, enforces tier limits, debits monthly quota,
parses the input lightly, and returns the selected suite manifest. It is the
synchronous integration target for the future async LLM execution pipeline.

### Web Dashboard

```bash
npm run web:dev
```

Then open the Vite URL printed by the command, usually
`http://localhost:5173/`.

Build and test the web package:

```bash
npm run web:build
npm run web:test
```

## Pricing And Monetization

The implemented tier model lives in `packages/api/src/narratological_api/auth.py`
and the Stripe checkout/license flow lives in
`packages/api/src/narratological_api/billing.py`. Both are documented in
[docs/api-pricing.md](docs/api-pricing.md).

| Tier | Price | Monthly quota | Request size | Suite access | Intended user |
| --- | ---: | ---: | ---: | --- | --- |
| Free trial | $0 | 3 analyses | 20,000 characters | 8-algorithm preview | Evaluation and sandbox integrations |
| Creator | $99/month | 50 analyses | 120,000 characters | Full contracted 92-algorithm suite | Individual scriptwriters, producers, and consultants |
| Studio | $999/month | 1,000 analyses | 600,000 characters | Full contracted 92-algorithm suite | Studios, production companies, and batch evaluation workflows |

Monetization is centered on API access:

- **Free trial** proves payload shape, authentication, quotas, and basic preview
  value.
- **Creator** converts individual practitioners who need full-suite analysis
  without studio-scale volume.
- **Studio** supports higher-volume script intake, larger documents, batch review,
  and priority support.

The quota and billing license stores are currently process-local and reset when
the API process restarts. Before charging external users, replace
`InMemoryQuotaStore` and `InMemoryBillingLicenseStore` with a shared billing or
usage ledger such as Redis, Postgres, or a billing provider meter.

## Repository Layout

```text
narratological-algorithmic-lenses/
├── specs/                          # Narrative source material and structured data
│   ├── 00-chat-transcripts/        # Conversation archive
│   ├── 02-completed-studies/       # Markdown source of truth for studies
│   ├── 03-structured-data/         # Validated JSON extracts and unified compendium
│   ├── 08-protocol-framework/      # P1-P7 protocol framework
│   ├── 09-protocol-skills/         # Protocol skill implementations
│   └── 10-project-manifests/       # ORGANVM integration manifests
├── packages/
│   ├── core/                       # Python library
│   ├── cli/                        # Typer CLI
│   ├── api/                        # FastAPI service
│   ├── mcp/                        # Model Context Protocol server
│   ├── vscode/                     # VS Code extension
│   └── web/                        # React + Vite dashboard
├── docs/
│   ├── adr/                        # Architecture Decision Records
│   ├── plans/                      # Roadmaps
│   └── api-pricing.md              # Commercial API tier model
└── open-view-analysis/             # Research drafts and worksheets
```

## Development

Run Python tests and checks:

```bash
uv run pytest
uv run ruff check .
uv run mypy packages
```

Run web checks:

```bash
npm run web:test
npm run web:build
```

Validate compendium synchronization after changing study data:

```bash
uv run narratological validate compendium
uv run narratological validate sync
```

## Project Status

This is a v0.1.0 system built from a Claude Desktop open-view research project
into a monorepo with a Python core, CLI, API, MCP package, VS Code package, and
React dashboard.

Several routes and workflows are intentionally staged:

- Local compendium exploration, algorithm lookup, diagnostics, and protocol
  commands are available through the CLI.
- `/analysis/narrative-suite` is the implemented gated API sample endpoint.
- Some broader API analysis endpoints are present as route contracts but return
  structured `501` responses until the async execution pipeline is added.

See [There and Back Again](docs/plans/there+back-again.md) for the roadmap.

<!-- SYSTEM-NAV-START -->

---

<sub>[Portfolio](https://4444j99.github.io/portfolio/) · [System Directory](https://4444j99.github.io/portfolio/directory/) · [ORGAN I · Theoria](https://organvm-i-theoria.github.io/) · Part of the <a href="https://4444j99.github.io/portfolio/directory/">ORGANVM eight-organ system</a></sub>

<!-- SYSTEM-NAV-END -->

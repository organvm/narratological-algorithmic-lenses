# Narratological Algorithmic Lenses

## Project Overview

**Narratological Algorithmic Lenses** is a computational narratology system designed to formalize narrative craft into implementable algorithmic frameworks. The project extracts "narrative algorithms" from primary sources (Aristotle, McKee) and master works (Tarkovsky, Pixar, Zelda), codifying them into a queryable database and a set of analysis tools.

This repository serves as both a **research archive** (containing the studies and extracted data) and a **software monorepo** (containing the tools to parse, analyze, and visualize narrative structures).

## Technology Stack

- **Core Logic:** Python 3.11+
- **Package Management:** `uv` (Python workspace), `npm` (JavaScript)
- **Backend/API:** FastAPI
- **CLI:** Python (Typer/Click-based)
- **Frontend:** TypeScript, React, Vite
- **Testing & Quality:** `pytest`, `ruff`, `mypy`, `vitest`

## Repository Structure

### Software Packages (`packages/`)
The codebase is organized as a monorepo managed by `uv`.

- **`packages/core`**: The foundational library. Contains Pydantic models for Studies, Axioms, and Algorithms, as well as the logic for loading and searching the compendium.
- **`packages/api`**: A FastAPI backend that exposes the core logic via REST endpoints (`/studies`, `/analysis`, `/diagnostics`).
- **`packages/cli`**: The command-line interface (`narratological`) for interacting with the system directly from the terminal.
- **`packages/web`**: A React-based visualization dashboard for exploring studies and running interactive analyses.

### Research & Data (`specs/`)
The knowledge base of the system.

- **`01-primary-sources/`**: Raw texts (Aristotle's Poetics, etc.).
- **`02-completed-studies/`**: Markdown documents detailing specific analytical lenses (e.g., `pixar-narratological-algorithms.md`).
- **`03-structured-data/`**: JSON extracts of the studies, ready for computational use.
- **`04-templates/`**: Standardized templates for creating new analyses.

### Case Studies (`open-view-analysis/`)
Example applications of the system. Contains comprehensive analysis of the "Open View" screenplay using the defined protocols.

## Development & Usage

### Prerequisites
- Python 3.11+
- Node.js & npm
- `uv` (Universal Python Package Installer)

### Setup
1.  **Initialize Python Workspace:**
    ```bash
    uv sync
    ```
2.  **Initialize Web Workspace:**
    ```bash
    npm install
    ```

### Running the System

**1. Command Line Interface (CLI)**
Explore studies and search axioms directly:
```bash
# List all available studies
uv run narratological study list

# Search for specific narrative concepts
uv run narratological study search "irony"
```

**2. Backend API**
Start the API server (default: `http://localhost:8000`):
```bash
uv run uvicorn narratological_api.main:app --reload
```

**3. Web Dashboard**
Start the frontend development server:
```bash
npm run web:dev
```

### Testing & Linting

**Python (Core, API, CLI):**
```bash
# Run tests
uv run pytest

# Linting and Formatting
uv run ruff check .
uv run mypy .
```

**Web Frontend:**
```bash
npm run web:test
```

## Workflow

1.  **Extraction**: Narrative principles are researched and documented in `specs/02-completed-studies/`.
2.  **Codification**: these principles are converted into structured JSON in `specs/03-structured-data/`.
3.  **Implementation**: The `core` library loads these definitions.
4.  **Application**: Users employ the `cli`, `api`, or `web` tools to apply these algorithms to new stories (as seen in `open-view-analysis/`).

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-I (Theory) | **Tier:** standard | **Status:** GRADUATED
**Org:** `a-organvm` | **Repo:** `narratological-algorithmic-lenses`

### Edges
- **Produces** → `organvm-ii-poiesis/art-from--narratological-algorithmic-lenses`: dependency

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `.github`, `nexus--babel-alexandria`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `linguistic-atomization-framework`, `my-knowledge-base`, `scalable-lore-expert` ... and 10 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-06-06T01:01:09Z*

## Active Handoff Protocol

If `.conductor/active-handoff.md` exists, **READ IT FIRST** before doing any work.
It contains constraints, locked files, conventions, and completed work from the
originating agent. You MUST honor all constraints listed there.

If the handoff says "CROSS-VERIFICATION REQUIRED", your self-assessment will
NOT be trusted. A different agent will verify your output against these constraints.

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## System Library

Plans: 269 indexed | Chains: 5 available | SOPs: 18 active
Discover: `organvm plans search <query>` | `organvm chains list` | `organvm sop lifecycle`
Library: `~/Code/organvm/praxis-perpetua/library`


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | atomic-clock | The Atomic Clock |
| system | any | execution-sequence | Execution Sequence |
| system | any | multi-agent-dispatch | Multi-Agent Dispatch |
| system | any | session-handoff-avalanche | Session Handoff Avalanche |
| system | any | system-loops | System Loops |
| system | any | prompting-standards | Prompting Standards |
| system | any | prompting-standards | Prompting Standards |
| system | any | prompting-standards | Prompting Standards |
| system | any | background-task-resilience | background-task-resilience |
| system | any | context-window-conservation | context-window-conservation |
| system | any | session-self-critique | session-self-critique |
| system | any | the-descent-protocol | the-descent-protocol |
| system | any | the-membrane-protocol | the-membrane-protocol |
| system | any | theory-to-concrete-gate | theory-to-concrete-gate |
| system | any | triangulation-protocol | triangulation-protocol |

Linked skills: SOP-TRIADIC-REVIEW-PROTOCOL, cicd-resilience-and-recovery, continuous-learning-agent, evaluation-to-growth, genesis-dna, multi-agent-workforce-planner, promotion-and-state-transitions, quality-gate-baseline-calibration, repo-onboarding-and-habitat-creation, session-self-critique, structural-integrity-audit, the-membrane-protocol, triple-reference


**Prompting (Google)**: context 1M tokens (Gemini 1.5 Pro), format: markdown, thinking: thinking mode (thinkingConfig)


## Atomization Pipeline

Run `organvm atoms pipeline --write && organvm atoms fanout --write` to generate task queue.


## System Density (auto-generated)

AMMOI: 25% | Edges: 0 | Tensions: 0 | Clusters: 0 | Adv: 27 | Events(24h): 38774
Structure: 8 organs / 149 repos / 1654 components (depth 17) | Inference: 0% | Organs: META-ORGANVM:63%, ORGAN-I:53%, ORGAN-II:48%, ORGAN-III:55% +5 more
Last pulse: 2026-06-06T01:01:02 | Δ24h: n/a | Δ7d: n/a


## Dialect Identity (Trivium)

**Dialect:** FORMAL_LOGIC | **Classical Parallel:** Logic | **Translation Role:** The Grammar — defines well-formedness in any dialect

Strongest translations: III (formal), IV (formal), META (formal)

Scan: `organvm trivium scan I <OTHER>` | Matrix: `organvm trivium matrix` | Synthesize: `organvm trivium synthesize`


## Logos Documentation Layer

**Status:** PRESENT | **Symmetry:** 1.0

Nature demands a documentation counterpart. This formation maintains its narrative record in `docs/logos/`.

### The Tetradic Counterpart
- **[Telos (Idealized Form)](../docs/logos/telos.md)** — The dream and theoretical grounding.
- **[Pragma (Concrete State)](../docs/logos/pragma.md)** — The honest account of what exists.
- **[Praxis (Remediation Plan)](../docs/logos/praxis.md)** — The attack vectors for evolution.
- **[Receptio (Reception)](../docs/logos/receptio.md)** — The account of the constructed polis.

### Alchemical I/O
- **[Source & Transmutation](../docs/logos/alchemical-io.md)** — Narrative of inputs, process, and returns.



*Compliance: Formation is present. All five Logos documents established in `docs/logos/`.*

<!-- ORGANVM:AUTO:END -->















## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.

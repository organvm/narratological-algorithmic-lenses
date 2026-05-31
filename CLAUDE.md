# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Narratological Algorithmic Lenses is a **comprehensive software system** that transforms theoretical narrative craft methodologies into implementable tools. The system provides:

- **Narrative Analysis Tool** - Analyze scripts/stories using formalized algorithms
- **AI/LLM Integration Library** - Enable AI systems to apply narratological frameworks
- **Interactive Reference App** - Browse, search, and apply specifications
- **Code Generation Framework** - Generate narrative structures algorithmically

## Architecture

**Hybrid: Python core + TypeScript web app**

```
narratological-algorithmic-lenses/
├── specs/                    # Theoretical specifications (14 studies, templates, sources)
│   ├── 01-primary-sources/
│   ├── 02-completed-studies/
│   ├── 03-structured-data/   # JSON exports + unified compendium
│   ├── 04-templates/
│   ├── 05-secondary-sources/
│   └── 07-skill-documentation/
│
├── packages/
│   ├── core/                 # Python core library (Pydantic models, algorithms)
│   ├── cli/                  # Python CLI application (typer)
│   ├── api/                  # FastAPI backend
│   └── web/                  # TypeScript/React web app (Vite)
│
├── pyproject.toml            # Python workspace root (uv)
└── package.json              # Node.js workspace root
```

## Build Commands

### Python Packages (using uv)

```bash
# Install all Python dependencies
uv sync

# Install specific package in development mode
uv pip install -e packages/core
uv pip install -e packages/cli
uv pip install -e packages/api

# Run CLI
uv run narratological --help

# Run API server
uv run uvicorn narratological_api.main:app --reload
```

### TypeScript Web App

```bash
# Install dependencies
cd packages/web && npm install

# Development server
npm run dev

# Build for production
npm run build

# Type checking
npm run typecheck
```

## Test Commands

### Python Tests (pytest)

```bash
# Run all Python tests
uv run pytest

# Run specific package tests
uv run pytest packages/core/tests/
uv run pytest packages/cli/tests/
uv run pytest packages/api/tests/

# Run with coverage
uv run pytest --cov=narratological --cov-report=html

# Run specific test file
uv run pytest packages/core/tests/test_models.py -v
```

### TypeScript Tests (vitest)

```bash
cd packages/web

# Run tests
npm test

# Run with coverage
npm run test:coverage

# Watch mode
npm run test:watch
```

## Key Files

### Specifications
- **`specs/03-structured-data/narratological-algorithms-unified.json`** - All 14 studies in machine-readable format (~209 KB)
- **`specs/03-structured-data/CROSS-REFERENCE-TABLE.md`** - Study inventory with axiom counts
- **`specs/07-skill-documentation/SKILL.md`** - Complete 8-role analyst methodology

### Core Library
- **`packages/core/src/narratological/models/`** - Pydantic data models
- **`packages/core/src/narratological/algorithms/`** - Algorithm implementations
- **`packages/core/src/narratological/diagnostics/`** - Diagnostic test runners
- **`packages/core/src/narratological/generators/`** - Report generators

## Data Model

**14 studies** containing:
- ~79 axioms (foundational principles)
- ~92 algorithms (formalized processes with pseudo-code)
- Structural hierarchies (nested organizational levels)
- Diagnostic questions (self-assessment prompts)
- Theoretical correspondences (mappings to Aristotle, McKee, Campbell, etc.)

**7 sequence pairs** linking related studies:
- A: Ovid ↔ Gaiman (anthology, myth-remix)
- B: Tarkovsky ↔ Bergman (cinematic interiority)
- C: Moore ↔ Morrison (formalism vs hypersigil)
- D: Kirby ↔ Tolkien (mythopoeia, cosmic dualism)
- E: Zelda ↔ Final Fantasy (interactive narrative)
- F: Tarantino ↔ Ovid (non-linear structure)
- G: Pixar ↔ Final Fantasy (emotional engineering)

## Development Workflow

### Working with Core Library

1. Models are defined in `packages/core/src/narratological/models/`
2. Algorithms implement the pseudo-code from studies
3. Tests validate against the unified JSON data

### Adding New Algorithms

1. Reference the algorithm spec in `specs/02-completed-studies/`
2. Implement in `packages/core/src/narratological/algorithms/`
3. Add tests that validate inputs/outputs match spec

### Working with Web App

1. API endpoints defined in `packages/api/src/narratological_api/routes/`
2. React components consume API in `packages/web/src/`
3. Shared types can be generated from Pydantic models

## Study JSON Schema

Studies in `specs/03-structured-data/json-extracts/` use this schema:

```json
{
  "id": "creator-work",
  "creator": "Name",
  "work": "Work Title",
  "category": "Category",
  "axioms": [
    {
      "id": "XX-A0",
      "name": "Axiom Name",
      "statement": "The principle statement",
      "derivations": ["Implication 1", "Implication 2"]
    }
  ],
  "structural_hierarchy": {
    "levels": [
      {
        "level": 1,
        "name": "Level Name",
        "description": "Level description",
        "elements": ["Element 1", "Element 2"]
      }
    ]
  },
  "core_algorithms": [
    {
      "name": "Algorithm Name",
      "purpose": "What it does",
      "pseudocode": "The implementation logic",
      "inputs": ["input1", "input2"],
      "outputs": ["output1", "output2"]
    }
  ],
  "diagnostic_questions": [
    {
      "id": "Q1",
      "question": "The diagnostic question",
      "valid_if": "Criteria for validity"
    }
  ],
  "theoretical_correspondences": {
    "maps_to": ["Theory 1", "Theory 2"],
    "sequence_pairs": ["paired-study-id"]
  },
  "quick_reference": {
    "core_operations": ["Operation 1", "Operation 2"],
    "key_constraints": ["Constraint 1", "Constraint 2"]
  }
}
```

## 8-Role Analyst System

Script analysis uses eight distinct analytical perspectives:

| Role | Focus |
|------|-------|
| AESTHETE | Form, beauty, style, sensory patterns |
| DRAMATURGIST | Structure, rhythm, dramatic tension |
| NARRATOLOGIST | Narrative mechanisms, causal binding |
| ART HISTORIAN | Historical context, influences, lineages |
| CINEPHILE | Comparable works, genre conventions |
| RHETORICIAN | Argument structure, dialogue craft |
| PRODUCER | Practical feasibility, budget implications |
| ACADEMIC | Theoretical frameworks, rigor |
| FIRST-READER | Emotional response, engagement |

See `specs/07-skill-documentation/SKILL.md` for complete methodology.

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-I (Theory) | **Tier:** standard | **Status:** GRADUATED
**Org:** `organvm-i-theoria` | **Repo:** `narratological-algorithmic-lenses`

### Edges
- **Produces** → `organvm-ii-poiesis/art-from--narratological-algorithmic-lenses`: dependency

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `.github`, `nexus--babel-alexandria`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `linguistic-atomization-framework`, `my-knowledge-base`, `scalable-lore-expert` ... and 10 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-05-23T00:26:31Z*

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

Plans: 269 indexed | Chains: 5 available | SOPs: 8 active
Discover: `organvm plans search <query>` | `organvm chains list` | `organvm sop lifecycle`
Library: `/Users/4jp/Code/organvm/praxis-perpetua/library`


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | atomic-clock | The Atomic Clock |
| system | any | execution-sequence | Execution Sequence |
| system | any | multi-agent-dispatch | Multi-Agent Dispatch |
| system | any | session-handoff-avalanche | Session Handoff Avalanche |
| system | any | system-loops | System Loops |
| system | any | prompting-standards | Prompting Standards |
| system | any | background-task-resilience | background-task-resilience |
| system | any | context-window-conservation | context-window-conservation |
| system | any | session-self-critique | session-self-critique |
| system | any | the-descent-protocol | the-descent-protocol |
| system | any | the-membrane-protocol | the-membrane-protocol |
| system | any | theory-to-concrete-gate | theory-to-concrete-gate |
| system | any | triangulation-protocol | triangulation-protocol |

Linked skills: SOP-TRIADIC-REVIEW-PROTOCOL, cicd-resilience-and-recovery, continuous-learning-agent, evaluation-to-growth, genesis-dna, multi-agent-workforce-planner, promotion-and-state-transitions, quality-gate-baseline-calibration, repo-onboarding-and-habitat-creation, session-self-critique, structural-integrity-audit, the-membrane-protocol, triple-reference


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)


## Atomization Pipeline

Run `organvm atoms pipeline --write && organvm atoms fanout --write` to generate task queue.


## System Density (auto-generated)

AMMOI: 25% | Edges: 0 | Tensions: 0 | Clusters: 0 | Adv: 27 | Events(24h): 37975
Structure: 8 organs / 148 repos / 1654 components (depth 17) | Inference: 0% | Organs: META-ORGANVM:63%, ORGAN-I:53%, ORGAN-II:48%, ORGAN-III:54% +5 more
Last pulse: 2026-05-23T00:26:28 | Δ24h: n/a | Δ7d: n/a


## Dialect Identity (Trivium)

**Dialect:** FORMAL_LOGIC | **Classical Parallel:** Logic | **Translation Role:** The Grammar — defines well-formedness in any dialect

Strongest translations: III (formal), IV (formal), META (formal)

Scan: `organvm trivium scan I <OTHER>` | Matrix: `organvm trivium matrix` | Synthesize: `organvm trivium synthesize`


## Logos Documentation Layer

**Status:** ACTIVE | **Symmetry:** 0.5 (DREAM)

Nature demands a documentation counterpart. This formation maintains its narrative record in `docs/logos/`.

### The Tetradic Counterpart
- **[Telos (Idealized Form)](../docs/logos/telos.md)** — The dream and theoretical grounding.
- **[Pragma (Concrete State)](../docs/logos/pragma.md)** — The honest account of what exists.
- **[Praxis (Remediation Plan)](../docs/logos/praxis.md)** — The attack vectors for evolution.
- **[Receptio (Reception)](../docs/logos/receptio.md)** — The account of the constructed polis.

### Alchemical I/O
- **[Source & Transmutation](../docs/logos/alchemical-io.md)** — Narrative of inputs, process, and returns.



*Compliance: Record exists without implementation.*

<!-- ORGANVM:AUTO:END -->












## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.
# Narratological Algorithmic Lenses

[![CI](https://github.com/a-organvm/narratological-algorithmic-lenses/actions/workflows/ci.yml/badge.svg)](https://github.com/a-organvm/narratological-algorithmic-lenses/actions/workflows/ci.yml)

A computational engine for formalizing, analyzing, and applying narrative craft.

This system transforms abstract storytelling principles—from **Aristotle's** *Poetics* to **Phoebe Waller-Bridge's** *Fleabag*—into executable algorithms that can diagnose scripts, identify structural weaknesses, and simulate "Script Doctor" consultations.

## Core Capabilities

### 1. The Compendium
A living library of 28 formalized narrative frameworks, including:
- **Classical**: Aristotle, Bharata Muni (Natyasastra), Ovid, Plato, Horace, African Oral Epic.
- **Film**: Tarkovsky (Time-Pressure), Bergman (Interiority), Tarantino (Discovery Writing), Lynch (Dream Logic), Kubrick (Non-Submersible Units).
- **Television**: Phoebe Waller-Bridge (Layered Obstacles), Larry David (Comedy Geometry), South Park (Therefore/But).
- **Global**: Kishōtenketsu (Conflict-Agnostic), Heroine's Journey (Internal Integration).
- **Interactive**: Zelda (Exploration), Final Fantasy (Ensemble).
- **Comics**: Alan Moore (Formalism), Grant Morrison (Hypersigil), Kirby (Mythopoeia).
- **Meta**: 8-Role Analyst System, Attention Mechanics.

### 2. Deep Diagnostics
Quantitative and qualitative analysis of script structure:
- **Causal Binding**: Measures the ratio of "THEREFORE/BUT" connections vs. "AND THEN" (Target > 60%).
- **Reorderability**: Identifies scenes that can be moved without breaking causality (lower is better).
- **Necessity**: Flags scenes that serve no structural or character function.
- **Information Economy**: Detects redundant exposition and missing setups.

### 3. The Script Doctor
Collaborative AI analysis that simulates a writers' room with master creators:
- **Pairings**: Ask **Tarkovsky** and **Bergman** to debate your script's pacing.
- **Consultations**: Get a "prescription" for your second act from **Phoebe Waller-Bridge**.
- **Dialogue**: Receive feedback formatted as a philosophical debate between conflicting narrative schools.

### 4. Fountain Integration
Native support for the **Fountain** screenplay format, allowing direct ingestion of professional scripts from Highland 2, Fade In, or VS Code.

### 5. Protocol Framework
Seven-level skill progression (P1–P7) from `specs/08-protocol-framework/`:
- **P1–P2**: Foundational awareness of narrative structure
- **P3–P4**: Diagnostic application to real scripts
- **P5–P6**: Multi-framework synthesis and Script Doctor facilitation
- **P7**: Autonomous framework extension and study creation

---

## Repository Layout

```text
narratological-algorithmic-lenses/
├── specs/                          # The Knowledge Base
│   ├── 00-chat-transcripts/        # Claude Desktop conversation archive (27 threads)
│   ├── 01-primary-sources/         # Original source documents
│   ├── 02-completed-studies/       # Markdown source of truth (28 studies)
│   ├── 03-structured-data/         # Validated JSON extracts & unified compendium
│   ├── 04-templates/               # Study and analysis templates
│   ├── 05-secondary-sources/       # Supplementary research materials
│   ├── 06-open-view-drafts/        # Case study screenplays
│   ├── 07-skill-documentation/     # 8-Role Analyst methodology (SKILL.md)
│   ├── 08-protocol-framework/      # P1–P7 skill progression framework
│   ├── 09-protocol-skills/         # Protocol skill implementations
│   ├── 10-project-manifests/       # Organvm integration manifests
│   ├── 11-el-series/               # Extended Lore supplements
│   └── 12-mythological-sources/    # Mythological reference materials
├── packages/                       # The Software Stack
│   ├── core/                       # Python library (models, parsers, diagnostics, LLM)
│   ├── cli/                        # Command-line interface (Typer)
│   ├── api/                        # FastAPI service
│   ├── mcp/                        # Model Context Protocol server (FastMCP)
│   ├── vscode/                     # VS Code extension (Snippets & Tagging)
│   └── web/                        # React + Vite visualization dashboard
└── docs/                           # Documentation
    ├── adr/                        # Architecture Decision Records
    └── plans/                      # Roadmaps and planning documents
```

## Project History

Built across 8 phases from a Claude Desktop open-view project (52 files, 27 conversation threads):

| Phase | Name | Highlights |
|-------|------|------------|
| 0 | Platinum Sprint | CI/CD, CHANGELOG, ADR documentation |
| 1 | Foundation | Pydantic models, JSON loader, 14 initial studies, 65 tests |
| 2 | Promotion | Fountain parser, Causal Binding, study promotions, Script Doctor |
| 3 | Engine | 4 generators, 8-role analyst, 5 diagnostic runners, 243 tests |
| 4 | Debate | CLI wiring, LLM providers, multi-agent debate, 290 tests |
| 5 | Interface | FastAPI routes, React dashboard, MCP server, VS Code extension |
| 6 | Omega Synthesis | Documentation, v0.1.0 release, organvm integration |
| 7 | Intake | Full Claude Desktop archive import (119 files) |

See [There and Back Again](docs/plans/there+back-again.md) for the complete roadmap.

---

## Getting Started

### Prerequisites
- Python 3.11+
- `uv` (Universal Python Package Installer)
- `npm` (for web dashboard)

### Installation

```bash
# Initialize Python workspace
uv sync

# Initialize Web workspace
npm install
```

### Key Commands

**1. Analyze a Script**
Run deep diagnostics on a Fountain or text script:
```bash
# Full battery (Causal, Reorderability, Necessity)
uv run narratological diagnose all my_script.fountain

# Targeted Causal Binding check
uv run narratological diagnose causal my_script.fountain --target 0.8
```

**2. Consult the Script Doctor**
Simulate a creative consultation between two masters:
```bash
# Consult Tarkovsky and Bergman (Sequence B)
uv run narratological analyze script-doctor my_script.fountain --sequence B

# Custom pairing: Larry David vs. Aristotle
uv run narratological analyze script-doctor my_script.fountain --primary larry-david --secondary aristotle
```

**3. Explore the Compendium**
```bash
# List all available studies
uv run narratological info

# Validate data integrity
uv run narratological validate compendium
```

## Development

### Data Synchronization
The system maintains strict synchronization between Markdown research files and JSON computational models.
If you edit a study in `specs/02-completed-studies/`, run:
```bash
uv run narratological validate sync
```

### Testing
```bash
uv run pytest                  # Run all Python tests
uv run ruff check .            # Linting
npm run web:test               # Run frontend tests
```

---

*There and Back Again — [the roadmap](docs/plans/there+back-again.md).*

<!-- SYSTEM-NAV-START -->

---

<sub>[Portfolio](https://4444j99.github.io/portfolio/) · [System Directory](https://4444j99.github.io/portfolio/directory/) · [ORGAN I · Theoria](https://organvm-i-theoria.github.io/) · Part of the <a href="https://4444j99.github.io/portfolio/directory/">ORGANVM eight-organ system</a></sub>

<!-- SYSTEM-NAV-END -->

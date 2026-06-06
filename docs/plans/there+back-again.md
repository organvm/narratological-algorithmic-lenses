# There and Back Again

## A Macro → Micro → Macro Roadmap for Narratological Algorithmic Lenses

**Status:** Living Document
**Created:** February 15, 2026
**Last Updated:** February 15, 2026
**Origin:** Claude Desktop Project (52 files, 27 threads, Jan–Feb 2026)

---

## ACT I — MACRO: The Journey There

*A chronicle of how the system was built, phase by phase.*

### 1.1 Genesis

The project began as a Claude Desktop "open-view" project: a sustained dialogue across **27 conversation threads** that produced **52 project files** between January and February 2026.

**Core thesis:** Attention is the ur-currency of narrative. Every storytelling tradition, from Aristotle's *Poetics* to Zelda's open-world exploration, manages the same finite resource — the audience's willingness to keep paying attention.

The open-view phase produced:

- 5 primary source studies (the first formalizations)
- 10 algorithm documents (pseudo-code for narrative operations)
- Research reports, creative work, and the 8-Role Analyst methodology
- The Protocol Framework (P1–P7 skill levels)
- The EL Series (extended lore supplements)

All of this material was ingested into the repository at commit `2e1029f` and now lives in `specs/00-chat-transcripts/` through `specs/12-mythological-sources/`.

### 1.2 Phase Map

| Phase | Name | Commits | Key Deliverables |
|-------|------|---------|------------------|
| 0 | Platinum Sprint | `7bc9982`–`4c2df46` | CI workflow, CHANGELOG, ADR-001/002, badge row |
| 1 | Foundation | `ed5a5a8` | Pydantic models, JSON loader, 14 studies, 65 tests |
| 2 | Promotion | `ff93834`–`a4820e9` | Fountain parser, Causal Binding thresholds, Bharata Muni/Aristotle/Waller-Bridge/Larry David promotions, Script Doctor layer |
| 3 | Engine | `acbc172`–`69a7dd4` | 4 report generators, 8-role analyst system, 5 diagnostic runners, algorithm engine, Kubrick + remaining study promotions, 243 tests |
| 4 | Debate | `3ecfee0`–`9dd2e3f` | CLI wiring (4 command groups), LLM providers (Anthropic/OpenAI/Ollama), parser module, multi-agent debate mode, 290 tests |
| 5 | Interface | `0c3a781` | FastAPI routes, React dashboard, MCP server (FastMCP), VS Code extension (snippets) |
| 6 | Omega Synthesis | `115fbdc`–`5aacbb7` | Unified web workbench, cross-framework sequence pairing, v0.1.0 release documentation |
| 7 | Intake | `2e1029f` | 119 files imported: 19 text docs, 27 threads, 9 PDFs, 45 EL bonus files, 19 JSON extracts |

### 1.3 Current State Inventory

| Layer | Count | Location |
|-------|-------|----------|
| Completed studies | 28 (+ 1 research report) | `specs/02-completed-studies/` |
| JSON extracts | 28 | `specs/03-structured-data/json-extracts/` |
| Unified compendium | 1 (~295 KB) | `specs/03-structured-data/` |
| Core Python modules | 41 `.py` files | `packages/core/` |
| CLI commands | 4 groups (diagnose, analyze, generate, algorithm) | `packages/cli/` |
| API routes | Studies, analysis, diagnostics | `packages/api/` |
| Web components | 4 (StudyExplorer, AlgorithmViewer, DiagnosticRunner, ScriptDoctorWorkbench) | `packages/web/` |
| MCP server | FastMCP wrapper | `packages/mcp/` |
| VS Code extension | 2 snippet files | `packages/vscode/` |
| Spec directories | 13 (00–12) | `specs/` |
| Tests | 290+ passing | `packages/core/tests/`, `packages/cli/tests/` |

### 1.4 Study Roster

**28 formalized narrative frameworks:**

| # | Creator / Framework | Work / Tradition | Category |
|---|---------------------|------------------|----------|
| 1 | Aristotle | *Poetics* | Classical |
| 2 | Bharata Muni | *Natyasastra* | Classical |
| 3 | Horace | *Ars Poetica* | Classical |
| 4 | Plato | *Republic* / *Ion* | Classical |
| 5 | Ovid | *Metamorphoses* | Classical |
| 6 | Tarkovsky | *Sculpting in Time* | Film |
| 7 | Bergman | *Persona* / *Seventh Seal* | Film |
| 8 | Kubrick | *2001* / *Full Metal Jacket* | Film |
| 9 | Lynch | *Mulholland Drive* / *Twin Peaks* | Film |
| 10 | Tarantino | *Pulp Fiction* / Discovery Writing | Film |
| 11 | Phoebe Waller-Bridge | *Fleabag* / Layered Obstacles | Television |
| 12 | Larry David | *Curb* / Comedy Geometry | Television |
| 13 | South Park | Therefore/But Logic | Television |
| 14 | Bret Easton Ellis | *American Psycho* / Affectless Narration | Literature |
| 15 | Neil Gaiman | *Sandman* / Myth-Remix Anthology | Comics/Literature |
| 16 | Alan Moore | *Watchmen* / Formalism | Comics |
| 17 | Grant Morrison | *The Invisibles* / Hypersigil | Comics |
| 18 | Jack Kirby | *New Gods* / Cosmic Mythopoeia | Comics |
| 19 | J.R.R. Tolkien | *Lord of the Rings* / Mythopoeia | Literature |
| 20 | Pixar | Emotional Engineering | Animation |
| 21 | Robert McKee | *Story* | Theory |
| 22 | Zelda (Nintendo) | Exploration Narrative | Interactive |
| 23 | Final Fantasy (Square) | Ensemble Narrative | Interactive |
| 24 | Kishōtenketsu | East Asian Structure | Global |
| 25 | Heroine's Journey | Maureen Murdock | Global |
| 26 | African Oral Epic | Mwindo / Sundiata | Global |
| 27 | 8-Role Analyst System | Meta-Framework | Meta |
| 28 | Attention Mechanics | Ur-Currency Theory | Meta |

**7 sequence pairs** for comparative analysis:

| Pair | Study A | Study B | Shared Axis |
|------|---------|---------|-------------|
| A | Ovid | Gaiman | Anthology, myth-remix |
| B | Tarkovsky | Bergman | Cinematic interiority |
| C | Moore | Morrison | Formalism vs. hypersigil |
| D | Kirby | Tolkien | Mythopoeia, cosmic dualism |
| E | Zelda | Final Fantasy | Interactive narrative |
| F | Tarantino | Ovid | Non-linear structure |
| G | Pixar | Final Fantasy | Emotional engineering |

---

## ACT II — MICRO: The Milestones Ahead

*Concrete, actionable milestones from current state to True Omega.*

### Milestone 1: The Scouring (Housekeeping)

**Status:** This session

- [x] Create this roadmap document
- [x] README.md: fix stale study count (27+ → 28), expand repo layout, add protocol framework
- [x] CHANGELOG.md: add intake + roadmap session entries

### Milestone 2: Data Integrity Hardening

- [x] Validate all 28 JSON extracts load cleanly via `uv run narratological validate compendium`
- [x] Ensure `ovid-study-research-report.md` is correctly classified (research report, not a study)
- [x] Verify Bharata Muni supplement/extended in `05-secondary-sources/` are properly cross-referenced
- [x] Confirm unified compendium JSON matches all 28 individual extracts
- [x] Run `uv run narratological validate sync` — fix any drift

### Milestone 3: Package Hardening

- [x] **CLI**: Verify all command groups work end-to-end with a real `.fountain` file
- [x] **API**: Smoke-test all routes with `uvicorn` + `curl`
- [x] **Web**: `npm run build` succeeds; basic component rendering verified
- [x] **MCP**: Server starts, tool discovery works, at least one tool invocation succeeds
- [x] **VS Code**: Snippets load in VS Code, fountain syntax triggers

### Milestone 4: CI/CD Pipeline

- [x] Verify `.github/workflows/ci.yml` runs: lint, type-check, test
- [x] Add web build step to CI
- [x] Add MCP server test step
- [x] Badge in README reflects real CI status

### Milestone 5: Protocol Framework Integration

- [ ] Wire `specs/08-protocol-framework/` docs into the software layer
- [ ] P1–P7 protocol skills (`specs/09-protocol-skills/`) available via CLI/API
- [ ] Protocol invocation: `uv run narratological analyze protocol --level P3 my_script.fountain`

### Milestone 6: New Study Pipeline

- [ ] Document the end-to-end flow: markdown study → JSON extract → compendium → algorithm registry
- [ ] Automate JSON extraction from markdown studies
- [ ] Identify next candidates for formalization (from PF-029/030 target list)

### Milestone 7: Deployment

- [ ] Web dashboard deployed (Vercel or similar)
- [ ] MCP server registered in Claude Desktop
- [ ] PyPI package published (`pip install narratological`)
- [ ] npm package published (web components)

### Milestone 8: True Omega

- [ ] Self-sustaining pipeline: new study auto-flows through entire system
- [ ] Community contribution pathway documented
- [ ] Academic paper readiness (formal methodology description)
- [ ] Complete test coverage across all packages
- [ ] Performance benchmarks for diagnostic analysis

---

## ACT III — MACRO: The Journey Back

*How the system returns enriched — the feedback loop from software to theory.*

### 3.1 The Feedback Loop

The software system is not merely an encoding of theory. It enriches and extends the theory in ways the original studies could not:

**Diagnostic Discovery.** Running Causal Binding analysis across multiple scripts reveals empirical thresholds (30% / 60% / 80%) that no single study predicted. The system generates theoretical knowledge.

**Cross-Study Emergence.** When the Algorithm Engine processes a script through all 28 frameworks simultaneously, patterns emerge that are invisible in any individual study. Sequence pair debates (Tarkovsky vs. Bergman on pacing) produce novel synthesis.

**Script Doctor Dialectics.** The multi-agent debate mode (Thesis → Antithesis → Synthesis) doesn't just apply existing theory — it generates new theoretical positions through structured disagreement between frameworks.

### 3.2 The Organvm Integration

This project sits within the organvm ecosystem as a node in **Organ I (Theoria)**:

- **Theoria → Poiesis:** The compendium and algorithms feed directly into creative production tools
- **Governance (Organ IV):** Subscription to org-wide standards, health audits, compliance
- **Feedback:** Diagnostic results from Organ II creative work flow back into Theoria as empirical data

The project is at **PRODUCTION/CANDIDATE** status within the organvm eight-organ system.

### 3.3 The Omega State

True Omega is not a fixed endpoint. It is a self-sustaining state where:

1. **New narrative knowledge flows in automatically** — a new study enters the pipeline and propagates through JSON extraction, compendium update, algorithm registration, and diagnostic integration without manual intervention.

2. **Analysis capabilities expand without architectural changes** — adding a 29th study requires no code changes, only a new markdown file and its JSON extract.

3. **The system validates and enriches its own theoretical foundations** — diagnostic results feed back into the compendium as empirical data, closing the loop.

4. **The Bilbo Principle** — *There and Back Again.* The system ventures out from theory into software, gathers experience (data, patterns, edge cases), and returns to theory enriched. The journey changes the traveler.

---

*There and Back Again.*

# Narratological Algorithms Project Manifest

> **Project Title**: Narratological Algorithms Collection  
> **Domain**: Narrative Theory, Screenwriting, Computational Storytelling  
> **Generated**: 2026-01-25 | **Amended**: 2026-02-15  
> **Total Project Files**: 52  
> **Total Conversation Threads**: 27  

---

## Amendment Log

| Version | Date | Files | Threads | Delta |
|---------|------|-------|---------|-------|
| v1 | 2026-01-25 | 36 | 19 | â€” (baseline) |
| v2 | 2026-02-05 | 47 | 23 | +11 files, +4 threads |
| **v3** | **2026-02-15** | **52** | **27** | **+16 files (+44%), +8 threads (+42%) from v1** |

**v3 Amendment Summary**: Added 16 new project files (PF-037 through PF-052) spanning analysis protocol framework documents, mythological source materials, narrative enumeration research, and a previously uncatalogued collection of "EL" screenplay drafts (2017â€“2020) with reader feedback. Added 8 new conversation threads (CT-020 through CT-027) covering protocol framework design, P7 comprehensive analysis application, mythological/autobiographical source research, narrative structure enumeration, two manifest maintenance sessions, and a critical epistemological discussion about the project's relationship to novelty.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [File Taxonomy](#file-taxonomy)
3. [Project Files Catalog](#project-files-catalog)
   - [Primary Source Texts](#primary-source-texts)
   - [Narratological Algorithm Documents](#narratological-algorithm-documents)
   - [Research Reports](#research-reports)
   - [Source Analysis Documents](#source-analysis-documents)
   - [Skills & Templates](#skills--templates)
   - [Protocol Framework Documents](#protocol-framework-documents)
   - [Meta-Frameworks](#meta-frameworks)
   - [Creative Work â€” Open View](#creative-work--open-view)
   - [Creative Work â€” EL / A Girl and Her Dogs](#creative-work--el--a-girl-and-her-dogs)
   - [Mythological Source Materials](#mythological-source-materials)
4. [Conversation Threads Catalog](#conversation-threads-catalog)
5. [Cross-Reference Indices](#cross-reference-indices)
6. [Dependency Graph](#dependency-graph)
7. [Summary Statistics](#summary-statistics)

---

## Project Overview

This project systematically extracts, formalizes, and organizes narrative craft principles from diverse sourcesâ€”classical theorists, contemporary practitioners, and working screenwritersâ€”into implementable algorithmic frameworks. The methodology converts prose-based creative advice into structured decision trees, pseudocode functions, diagnostic protocols, and quick-reference materials.

**Core Thesis**: Attention is the "ur-currency" of narrative, transcending specific mediums and serving as the unifying substrate across all storytelling forms.

---

## File Taxonomy

| Tag | Description | Count |
|-----|-------------|-------|
| `SOURCE` | Primary/classical source texts | 5 |
| `ALGO` | Formalized narratological algorithm documents | 10 |
| `RESEARCH` | Research reports and analyses | 5 |
| `SOURCE_ANALYSIS` | Source analysis documents feeding algo extraction | 3 |
| `SKILL` | Skill definitions and templates | 7 |
| `PROTOCOL` | Analysis protocol framework documents | 6 |
| `META` | Meta-frameworks and study guides | 3 |
| `CREATIVE` | Original creative work (screenplays) | 10 |
| `MYTH_SOURCE` | Mythological reference materials | 2 |
| `MANIFEST` | Project documentation/maintenance | 1 |

---

## Project Files Catalog

### Primary Source Texts

---

#### PF-001: McKee Story

| Field | Value |
|-------|-------|
| **ID** | `PF-001` |
| **Filename** | `McKee_Story.txt` |
| **Size** | 815K |
| **Tags** | `SOURCE`, `SCREENWRITING`, `CONTEMPORARY` |
| **Format** | OCR-extracted text |

**Annotation**: Complete text extraction of Robert McKee's *Story: Substance, Structure, Style, and the Principles of Screenwriting* (1997). Foundational contemporary screenwriting manual covering scene design, the Gap, progressive complications, crisis/climax/resolution, and character arc construction. Serves as the primary reference for `mckee_narratological_algorithms_complete.md`. OCR quality varies; some passages may contain transcription artifacts.

**Cross-references**: `PF-006`, `CT-017`, `CT-018`

---

#### PF-002: Aristotle Poetics

| Field | Value |
|-------|-------|
| **ID** | `PF-002` |
| **Filename** | `aristotle_poetics.txt` |
| **Size** | 81K |
| **Tags** | `SOURCE`, `CLASSICAL`, `GREEK` |
| **Format** | S.H. Butcher translation |

**Annotation**: Complete text of Aristotle's *Poetics* (c. 335 BCE) in the Butcher translation. Establishes foundational Western dramatic theory including the six elements of tragedy (plot, character, thought, diction, song, spectacle), unity principles, probability and necessity, reversal (peripeteia), recognition (anagnorisis), and catharsis. Source text for `aristotle_narratological_algorithms.md`.

**Cross-references**: `PF-008`, `CT-012`

---

#### PF-003: Plato Republic

| Field | Value |
|-------|-------|
| **ID** | `PF-003` |
| **Filename** | `plato_republic.txt` |
| **Size** | 665K |
| **Tags** | `SOURCE`, `CLASSICAL`, `GREEK` |
| **Format** | Plain text translation |

**Annotation**: Complete text of Plato's *Republic*. Narratologically relevant content concentrated in Books II, III, and X, covering mimesis theory, the tripartite soul, content regulation for poetry, and the critique of imitation as "thrice removed from truth." Provides counter-position to Aristotelian poetics regarding the social function of narrative. Source for `plato_narratological_algorithms.md`.

**Cross-references**: `PF-009`, `CT-011`

---

#### PF-004: Horace Ars Poetica

| Field | Value |
|-------|-------|
| **ID** | `PF-004` |
| **Filename** | `horace_ars-poetica.txt` |
| **Size** | 231K |
| **Tags** | `SOURCE`, `CLASSICAL`, `ROMAN` |
| **Format** | Plain text with commentary |

**Annotation**: Horace's *Ars Poetica* (c. 19 BCE). Roman verse epistle offering practical craft instruction including the genius-plus-labor requirement, "no mediocrity" threshold, nine-year revision rule, character age-stage profiles, and critic function diagnostics. Bridges Greek theory to Roman pragmatism. Source for `horace_narratological_algorithms.md`.

**Cross-references**: `PF-010`, `CT-010`

---

#### PF-005: Bharata Muni Natyasastra

| Field | Value |
|-------|-------|
| **ID** | `PF-005` |
| **Filename** | `bharata-muni_natyasastra.txt` |
| **Size** | 1.5M |
| **Tags** | `SOURCE`, `CLASSICAL`, `SANSKRIT`, `INDIAN` |
| **Format** | Plain text translation (~41,000 lines) |

**Annotation**: Complete text of Bharata Muni's *Natyasastra* (c. 200 BCEâ€“200 CE), the foundational Sanskrit treatise on dramatic arts. Covers 36 chapters including rasa-bhava theory (8 sentiments, 49 emotional states), abhinaya (four modes of representation), plot structure mechanics, character typologies, 108 karanas (dance units), and failure mode diagnostics (ghata). Most comprehensive classical dramatic theory text in the collection. Source for three algorithm documents: primary, supplement, and extended.

**Cross-references**: `PF-011`, `PF-012`, `PF-016`, `CT-008`, `CT-009`

---

### Narratological Algorithm Documents

---

#### PF-006: McKee Narratological Algorithms Complete

| Field | Value |
|-------|-------|
| **ID** | `PF-006` |
| **Filename** | `mckee_narratological_algorithms_complete.md` |
| **Size** | 62K |
| **Tags** | `ALGO`, `CONTEMPORARY`, `SCREENWRITING` |
| **Format** | Markdown with pseudocode |

**Annotation**: Comprehensive 23-section algorithmic distillation of McKee's *Story*. Covers all 19 chapters including the Gap Algorithm, Value Charge System, scene design protocols, and exposition management. Features pseudocode implementations, decision tables, formal definitions, and quick-reference cards. Core document for contemporary Western screenwriting methodology.

**Derived from**: `PF-001`  
**Cross-references**: `CT-017`, `CT-018`

---

#### PF-007: Larry David Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `PF-007` |
| **Filename** | `larry_david_narratological_algorithms.md` |
| **Size** | 25K |
| **Tags** | `ALGO`, `CONTEMPORARY`, `COMEDY`, `TELEVISION` |
| **Format** | Markdown with pseudocode |

**Annotation**: 12-section formalization of Larry David's "cascading consequences" comedy architecture from *Seinfeld* and *Curb Your Enthusiasm*. Documents the "no hugging, no learning" meta-principle, four-phase episode architecture, retrofit plotting, storyline independence tests, collision design rules, and the "amoral karma engine." Traces method ancestry to Georges Feydeau's French farce.

**Derived from**: `PF-035`  
**Cross-references**: `CT-016`

---

#### PF-008: Aristotle Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `PF-008` |
| **Filename** | `aristotle_narratological_algorithms.md` |
| **Size** | 34K |
| **Tags** | `ALGO`, `CLASSICAL`, `GREEK`, `DRAMA` |
| **Format** | Markdown with pseudocode |

**Annotation**: 13-section algorithmic distillation of Aristotle's *Poetics*. Formalizes the six elements hierarchy, unity principle, probability/necessity tests, reversal/recognition mechanics, catharsis conditions, and character requirements. Includes Homer's authorial restraint rule and "art of skillful lies" principle. Foundational reference for all other algorithm documents.

**Derived from**: `PF-002`  
**Cross-references**: `CT-012`

---

#### PF-009: Plato Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `PF-009` |
| **Filename** | `plato_narratological_algorithms.md` |
| **Size** | 47K |
| **Tags** | `ALGO`, `CLASSICAL`, `GREEK`, `PHILOSOPHY` |
| **Format** | Markdown with pseudocode |

**Annotation**: 13-section formalization of Plato's narrative theory from *The Republic*. Covers the three modes of narration (diegesis, mimesis, mixed), ontological hierarchy of imitation, tripartite soul theory, content regulation algorithms, and the mimesis-as-contagion counter-argument to Aristotelian catharsis. Documents fundamental divergence from Aristotle on poetry's social function.

**Derived from**: `PF-003`  
**Cross-references**: `CT-011`

---

#### PF-010: Horace Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `PF-010` |
| **Filename** | `horace_narratological_algorithms.md` |
| **Size** | 31K |
| **Tags** | `ALGO`, `CLASSICAL`, `ROMAN`, `CRAFT` |
| **Format** | Markdown with pseudocode |

**Annotation**: 12-section algorithmic distillation of Horace's *Ars Poetica*. Formalizes the dual genius-labor requirement, "no mediocrity" threshold, nine-year revision rule, character age-stage profiles, beginning *in medias res* principle, and critic function diagnostics. Includes key Latin phrases with applications.

**Derived from**: `PF-004`  
**Cross-references**: `CT-010`

---

#### PF-011: Bharata Muni Narratological Algorithms (Primary)

| Field | Value |
|-------|-------|
| **ID** | `PF-011` |
| **Filename** | `bharata_muni_narratological_algorithms.md` |
| **Size** | 38K |
| **Tags** | `ALGO`, `CLASSICAL`, `SANSKRIT`, `INDIAN`, `RASA` |
| **Format** | Markdown with pseudocode |

**Annotation**: Primary document covering core *Natyasastra* theory: rasa-bhava mechanics (8 rasas, 49 bhavas), abhinaya (4 modes), plot structure with sandhis (5 junctures) and sandhyangas (64 elements), dramatic forms classification, character typologies, and success conditions. Establishes foundational Indian dramatic architecture.

**Derived from**: `PF-005`  
**Cross-references**: `PF-012`, `PF-016`, `CT-008`, `CT-009`

---

#### PF-012: Bharata Muni Narratological Algorithms (Supplement)

| Field | Value |
|-------|-------|
| **ID** | `PF-012` |
| **Filename** | `bharata_muni_narratological_algorithms_supplement.md` |
| **Size** | 26K |
| **Tags** | `ALGO`, `CLASSICAL`, `SANSKRIT`, `INDIAN`, `ADVANCED` |
| **Format** | Markdown with pseudocode |

**Annotation**: Supplementary document covering advanced *Natyasastra* topics: ghata (failure modes/blemishes), temporal construction constraints, purvaranga (preliminary ritual sequences), rasa combination rules, and structural unity principles. Extends primary document with compositional rules and failure prevention diagnostics.

**Derived from**: `PF-005`  
**Cross-references**: `PF-011`, `PF-016`, `CT-008`

---

#### PF-013: South Park Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `PF-013` |
| **Filename** | `south_park_narratological_algorithms.md` |
| **Size** | 24K |
| **Tags** | `ALGO`, `CONTEMPORARY`, `COMEDY`, `TELEVISION`, `ANIMATION` |
| **Format** | Markdown with pseudocode |

**Annotation**: 15-section formalization of Trey Parker and Matt Stone's "but/therefore" rule. Covers the three-word diagnostic system, shuffle test, status quo test, single A-story principle, causal chain templates, and writers' room axioms. Includes canonical episode breakdowns ("Scott Tenorman Must Die," "Make Love Not Warcraft"). Maps to classical narrative theory from Aristotle through McKee.

**Derived from**: `PF-036`  
**Cross-references**: `CT-015`

---

#### PF-014: Phoebe Waller-Bridge Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `PF-014` |
| **Filename** | `phoebe_waller_bridge_narratological_algorithms.md` |
| **Size** | 18K |
| **Tags** | `ALGO`, `CONTEMPORARY`, `DRAMA`, `COMEDY`, `TELEVISION` |
| **Format** | Markdown with pseudocode |

**Annotation**: 11-section formalization of the "three things going on" technique from *Fleabag*. Covers the four-layer scene construction protocol (intention + physical + interpersonal + internal obstacles), obstacle taxonomies with interaction matrices, and genre-specific applications. Maps to Sorkin, Mamet, and McKee scene theory.

**Derived from**: `PF-020`  
**Cross-references**: `CT-014`

---

#### PF-016: Bharata Muni Narratological Algorithms (Extended)

| Field | Value |
|-------|-------|
| **ID** | `PF-016` |
| **Filename** | `bharata_muni_narratological_algorithms_extended.md` |
| **Size** | 31K |
| **Tags** | `ALGO`, `CLASSICAL`, `SANSKRIT`, `INDIAN`, `PERFORMANCE` |
| **Format** | Markdown with pseudocode |

**Annotation**: Tertiary document completing *Natyasastra* coverage with performance-integrated systems: dhruva (musical-narrative cues), special representation protocols for abstract concepts, stage zone grammar, character movement algorithms, playhouse construction (Chapters 2â€“5), gesture vocabulary (67 hand gestures), and 108 karanas (dance units).

**Derived from**: `PF-005`  
**Cross-references**: `PF-011`, `PF-012`, `CT-009`

---

### Research Reports

---

#### PF-017: Stanley Kubrick Narratological Philosophy

| Field | Value |
|-------|-------|
| **ID** | `PF-017` |
| **Filename** | `Stanley_Kubrick_s_Narratological_Philosophy__Primary_Sources_and_Extractable_Principles.md` |
| **Size** | 32K |
| **Tags** | `RESEARCH`, `FILM`, `ADAPTATION`, `CONTEMPORARY` |
| **Format** | Markdown research report |

**Annotation**: Comprehensive research report on Kubrick's "non-submersible units" theory derived from primary source interviews (1960â€“1999). Documents the 6â€“8 sequence structure, systematic removal of explanatory elements from source materials, preservation of productive ambiguity, and subconscious engagement prioritization. Includes film-by-film adaptation analyses for *2001*, *A Clockwork Orange*, *Barry Lyndon*, *The Shining*, and *Eyes Wide Shut*.

**Cross-references**: `CT-013`

---

#### PF-018: Tarantino Genre Philosophy Research Report

| Field | Value |
|-------|-------|
| **ID** | `PF-018` |
| **Filename** | `tarantino_genre_philosophy_research_report.md` |
| **Size** | 22K |
| **Tags** | `RESEARCH`, `FILM`, `GENRE`, `CONTEMPORARY` |
| **Format** | Markdown research report |

**Annotation**: Primary source research report on Tarantino's genre philosophy. Documents "sub-genres of my life" concept, invention of new genre categories ("the Southern"), genre mixing methodology, and music as mandatory genre element. Based on extensive interview documentation from The Talks, UPI, NPR, and *Cinema Speculation*.

**Cross-references**: `PF-019`, `CT-006`

---

#### PF-019: Tarantino Genre Conventions as Structure

| Field | Value |
|-------|-------|
| **ID** | `PF-019` |
| **Filename** | `tarantino_genre_conventions_as_structure.md` |
| **Size** | 25K |
| **Tags** | `RESEARCH`, `FILM`, `GENRE`, `WRITING_PROCESS` |
| **Format** | Markdown research report |

**Annotation**: Focused analysis of Tarantino's discovery-based writing process where genre conventions serve as structural scaffolding. Documents the "knowing destinations while discovering routes" methodology, genre endpoints as navigation aids, and non-outline approach to screenplay construction. Derived from documented statements about writing *Kill Bill*, *Inglourious Basterds*, and *Django Unchained*.

**Cross-references**: `PF-018`, `CT-006`

---

#### PF-020: The Three Things Going On Technique (Source)

| Field | Value |
|-------|-------|
| **ID** | `PF-020` |
| **Filename** | `The_Three_Things_Going_On_Technique__Phoebe_Waller-Bridge_and_Scene_Construction_Through_Layered_Obstacles.md` |
| **Size** | 16K |
| **Tags** | `RESEARCH`, `TELEVISION`, `SCENE_DESIGN` |
| **Format** | Markdown analysis |

**Annotation**: Source analysis document tracing Phoebe Waller-Bridge's scene construction methodology from the 2019 Deadline interview through specific *Fleabag* scene breakdowns. Connects technique to broader screenwriting theory. Basis for `phoebe_waller_bridge_narratological_algorithms.md`.

**Cross-references**: `PF-014`, `CT-014`, `CT-019`

---

#### PF-043: Are There a Finite Number of Stories?

| Field | Value |
|-------|-------|
| **ID** | `PF-043` |
| **Filename** | `__Are_there_a_finite_number_of_stories__The_enduring_quest_to_enumerate_narrative` |
| **Size** | 22K |
| **Tags** | `RESEARCH`, `NARRATIVE_THEORY`, `ENUMERATION`, `COMPUTATIONAL` |
| **Format** | Markdown research report |
| **Added** | v3 (2026-02-15) |

**Annotation**: Comprehensive research report examining the longstanding claim that human narratives reduce to a finite number of basic story types. Surveys major taxonomies: Polti's 36 dramatic situations, Propp's 31 narrative functions, Campbell's 17-stage monomyth, Booker's 7 basic plots, Tobias's 20 master plots. Covers computational validation, particularly the University of Vermont study identifying six core emotional arcs via sentiment analysis on 1,327 storiesâ€”validating Kurt Vonnegut's rejected 1947 thesis. Includes critiques of Jungian foundations, cultural bias in Western enumeration schemes, and assessment of computational tractability for algorithmic formalization (Propp most tractable; Booker best for classification).

**Cross-references**: `CT-025`

---

### Source Analysis Documents

---

#### PF-035: Comedy Geometry Larry David

| Field | Value |
|-------|-------|
| **ID** | `PF-035` |
| **Filename** | `Comedy_Geometry__Larry_David_s_Architecture_of_Cascading_Consequences.md` |
| **Size** | 19K |
| **Tags** | `SOURCE_ANALYSIS`, `COMEDY`, `TELEVISION` |
| **Format** | Markdown analysis |

**Annotation**: Source analysis document for Larry David's comedy methodology. Traces the "cascading consequences" architecture through documented interviews and episode analysis. Basis for `larry_david_narratological_algorithms.md`.

**Cross-references**: `PF-007`, `CT-016`, `CT-019`

---

#### PF-036: South Park But/Therefore Rule

| Field | Value |
|-------|-------|
| **ID** | `PF-036` |
| **Filename** | `The_South_Park_But_Therefore_Rule__A_Complete_Craft_Analysis.md` |
| **Size** | 21K |
| **Tags** | `SOURCE_ANALYSIS`, `COMEDY`, `ANIMATION` |
| **Format** | Markdown analysis |

**Annotation**: Complete craft analysis of the Parker/Stone "but/therefore" rule from 2011 NYU lecture. Documents the diagnostic system, canonical episode breakdowns, and theoretical lineage. Basis for `south_park_narratological_algorithms.md`.

**Cross-references**: `PF-013`, `CT-015`, `CT-019`

---

### Skills & Templates

---

#### PF-021: SKILL.md (Script Analysis Dramaturgical)

| Field | Value |
|-------|-------|
| **ID** | `PF-021` |
| **Filename** | `SKILL.md` |
| **Size** | 48K |
| **Tags** | `SKILL`, `ANALYSIS`, `DRAMATURGICAL`, `TEMPLATE` |
| **Format** | Markdown skill definition |

**Annotation**: Complete skill package for script analysis and dramaturgical coverage. Enforces complete script ingestion before analysis. Delivers eight core documents: Coverage Report, Beat Map, Structural Analysis, Character Atlas, Thematic Architecture, Diagnostic Report, Theoretical Correspondence, and Revision Roadmap. Integrates nine analytical perspectives: aesthete, dramaturgist, narratologist, art historian, cinephile, rhetorician, producer, academic, first-reader.

**Cross-references**: `PF-022`, `CT-003`

---

#### PF-022: SKILL-preview.md (Narratological Algorithms)

| Field | Value |
|-------|-------|
| **ID** | `PF-022` |
| **Filename** | `SKILL-preview.md` |
| **Size** | 4.5K |
| **Tags** | `SKILL`, `EXTRACTION`, `METHODOLOGY` |
| **Format** | Markdown skill preview |

**Annotation**: Skill definition for distilling artist/theorist narrative principles into formal algorithmic frameworks. 8-step workflow covering source classification, primary source prioritization, principle extraction protocol, document structuring, formalization patterns, axiom identification, validation checks, and cross-medium adaptation.

**Cross-references**: `CT-007`

---

#### PF-023: Coverage Template

| Field | Value |
|-------|-------|
| **ID** | `PF-023` |
| **Filename** | `coverage-template.md` |
| **Size** | 4.5K |
| **Tags** | `TEMPLATE`, `ANALYSIS`, `COVERAGE` |
| **Format** | Markdown template |

**Annotation**: Template for executive-level script coverage reports. Includes logline, synopsis, tone/genre classification, comparative references, and pass/consider/recommend recommendation with justification.

---

#### PF-024: Beat Map Template

| Field | Value |
|-------|-------|
| **ID** | `PF-024` |
| **Filename** | `beat-map-template.md` |
| **Size** | 6.5K |
| **Tags** | `TEMPLATE`, `ANALYSIS`, `STRUCTURE` |
| **Format** | Markdown template |

**Annotation**: Template for exhaustive scene-by-scene beat mapping. Documents scene headers, dramatic function, causal connectors (but/therefore), and value changes. Supports South Park diagnostic testing.

---

#### PF-025: Structural Template

| Field | Value |
|-------|-------|
| **ID** | `PF-025` |
| **Filename** | `structural-template.md` |
| **Size** | 12K |
| **Tags** | `TEMPLATE`, `ANALYSIS`, `ARCHITECTURE` |
| **Format** | Markdown template with ASCII diagrams |

**Annotation**: Template for act/movement architecture analysis. Includes ASCII structural diagrams, turning point identification, tension curves, and parallel plotline mapping.

---

#### PF-026: Character Template

| Field | Value |
|-------|-------|
| **ID** | `PF-026` |
| **Filename** | `character-template.md` |
| **Size** | 8.0K |
| **Tags** | `TEMPLATE`, `ANALYSIS`, `CHARACTER` |
| **Format** | Markdown template |

**Annotation**: Template for comprehensive character atlas. Documents character arcs, relationships, scene presence statistics, and want/need/wound triads.

---

#### PF-027: Diagnostic Template

| Field | Value |
|-------|-------|
| **ID** | `PF-027` |
| **Filename** | `diagnostic-template.md` |
| **Size** | 9.0K |
| **Tags** | `TEMPLATE`, `ANALYSIS`, `TESTING` |
| **Format** | Markdown template |

**Annotation**: Template for structural diagnostic reports. Integrates multiple framework tests: McKee Gap analysis, South Park but/therefore test, Phoebe Waller-Bridge layering check, attention mechanics audit.

---

### Protocol Framework Documents

---

#### PF-037: Analysis Protocols Framework

| Field | Value |
|-------|-------|
| **ID** | `PF-037` |
| **Filename** | `analysis_protocols_framework.md` |
| **Size** | 46K |
| **Tags** | `PROTOCOL`, `FRAMEWORK`, `METHODOLOGY`, `CORE` |
| **Format** | Markdown framework document (825 lines) |
| **Added** | v3 (2026-02-15) |

**Annotation**: Master document defining the seven-protocol analytical framework (P1â€“P7) for applying narratological lenses to creative work at differentiated depth levels. P1 Triage (30â€“60 min, 2 roles, 1 doc) through P7 Comprehensive (8â€“12 hrs, 9 roles, 13 docs). Includes protocol taxonomy, specifications for each level, role activation matrices, document generation rules, protocol selection logic, escalation paths between protocols, cross-protocol integration strategies, and quick-reference cards. Establishes the architecture that enables scaling analysis depth based on purpose and time constraints.

**Cross-references**: `PF-038`, `PF-039`, `PF-040`, `PF-041`, `PF-042`, `CT-021`

---

#### PF-038: Protocol-Specific Templates

| Field | Value |
|-------|-------|
| **ID** | `PF-038` |
| **Filename** | `protocol_specific_templates.md` |
| **Size** | 12K |
| **Tags** | `PROTOCOL`, `TEMPLATE` |
| **Format** | Markdown template collection |
| **Added** | v3 (2026-02-15) |

**Annotation**: Templates for document types unique to specific protocols and not covered by the base template set (PF-023 through PF-027). Includes Market Positioning Report (P5), Mechanism Extraction Report (P6), and other protocol-specific deliverable formats.

**Cross-references**: `PF-037`, `CT-021`

---

#### PF-039: Protocol Invocation Guide

| Field | Value |
|-------|-------|
| **ID** | `PF-039` |
| **Filename** | `protocol_invocation_guide.md` |
| **Size** | 37K |
| **Tags** | `PROTOCOL`, `GUIDE`, `WORKFLOW` |
| **Format** | Markdown guide with worked examples |
| **Added** | v3 (2026-02-15) |

**Annotation**: Practical workflow guide for invoking analysis protocols. Covers hub-and-spoke skill architecture (master router + individual protocol skills), natural language trigger patterns mapped to appropriate protocols, worked examples for each protocol level, and integration points with existing narratological algorithm documents.

**Cross-references**: `PF-037`, `PF-042`, `CT-022`

---

#### PF-040: Protocol Invocation Prompts

| Field | Value |
|-------|-------|
| **ID** | `PF-040` |
| **Filename** | `protocol_invocation_prompts.md` |
| **Size** | 5.0K |
| **Tags** | `PROTOCOL`, `PROMPTS`, `QUICK_START` |
| **Format** | Markdown prompt collection (120 lines) |
| **Added** | v3 (2026-02-15) |

**Annotation**: Ready-to-use AI prompts for triggering analysis protocols. Three invocation tiers: minimal single-line triggers ("Analyze this using Protocol P3"), standard invocations with parameter specification, and embeddable system instructions for persistent protocol configuration. Natural language variants map common user requests to appropriate protocol levels.

**Cross-references**: `PF-037`, `CT-021`

---

#### PF-041: Quick Reference Card

| Field | Value |
|-------|-------|
| **ID** | `PF-041` |
| **Filename** | `quick-reference.md` |
| **Size** | 5.5K |
| **Tags** | `PROTOCOL`, `REFERENCE`, `QUICK_START` |
| **Format** | Markdown reference card (100 lines) |
| **Added** | v3 (2026-02-15) |

**Annotation**: Single-page quick-select reference for the protocol framework. ASCII-formatted protocol selection card mapping common user questions to protocol levels, comparison matrix showing reads/roles/docs/time for each protocol, and role activation summary.

**Cross-references**: `PF-037`

---

#### PF-042: Integration Guide

| Field | Value |
|-------|-------|
| **ID** | `PF-042` |
| **Filename** | `integration-guide.md` |
| **Size** | 7.5K |
| **Tags** | `PROTOCOL`, `INTEGRATION`, `ARCHITECTURE` |
| **Format** | Markdown guide with ASCII diagrams (182 lines) |
| **Added** | v3 (2026-02-15) |

**Annotation**: Technical integration document showing how protocol skills connect to the existing narratological algorithms project infrastructure. Covers the hub-and-spoke architecture with creative-analysis router, data flow between protocols and algorithm documents, and configuration for the 8-skill installation (1 router + 7 protocol skills).

**Cross-references**: `PF-037`, `PF-039`, `CT-022`

---

### Meta-Frameworks

---

#### PF-028: Attention Mechanics Meta-Principles

| Field | Value |
|-------|-------|
| **ID** | `PF-028` |
| **Filename** | `attention_mechanics_meta_principles.md` |
| **Size** | 43K |
| **Tags** | `META`, `THEORY`, `CROSS-MEDIA`, `FOUNDATIONAL` |
| **Format** | Markdown framework document |

**Annotation**: Cross-media attention algorithm serving as meta-principles document above individual artist/theorist algorithms. Establishes six foundational axioms with attention as "ur-currency." Maps medium-specific attention mechanisms, formalizes "involuntary response hierarchy" (comedy/horror as epistemologically privileged), defines prediction modes (anticipation-satisfaction vs. prediction-failure-recalibration), and provides diagnostic protocols. Unifying theoretical substrate for entire project.

**Cross-references**: `CT-005`

---

#### PF-029: Narratological Study Prompts

| Field | Value |
|-------|-------|
| **ID** | `PF-029` |
| **Filename** | `narratological_study_prompts.md` |
| **Size** | 33K |
| **Tags** | `META`, `METHODOLOGY`, `STUDY_GUIDE` |
| **Format** | Markdown prompt collection |

**Annotation**: Reference document containing 14 comprehensive study prompts for future algorithm extraction. Covers: Ovid (*Metamorphoses*), Tarkovsky, Bergman, Tarantino, Lynch, Alan Moore, Neil Gaiman (*Sandman*), Grant Morrison, Warren Ellis, Jack Kirby (*New Gods*), Tolkien, Zelda, Final Fantasy, Pixar. Each prompt includes primary/secondary sources, 5 extraction targets, candidate axioms, and theoretical correspondence mapping.

**Cross-references**: `CT-001`

---

#### PF-030: Study List Narratological Algorithm Sources

| Field | Value |
|-------|-------|
| **ID** | `PF-030` |
| **Filename** | `Study_List__Narratological_Algorithm_Sources` |
| **Size** | 3.5K |
| **Tags** | `META`, `INDEX`, `PLANNING` |
| **Format** | Markdown table |

**Annotation**: Categorized table of artists/sources for future algorithmic analysis. Organized by medium: Classical/Foundational (Ovid), Film/Cinematic (Tarkovsky, Bergman, Tarantino, Lynch), Comics/Graphic Narrative (Moore, Gaiman, Morrison, Ellis, Kirby), Literature/Worldbuilding (Tolkien), Interactive/Ludic (Zelda, Final Fantasy), Animation/Studio (Pixar). Lists core narrative signatures and potential algorithm focus areas.

**Cross-references**: `CT-001`

---

### Creative Work â€” Open View

---

#### PF-031: Open View First Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-031` |
| **Filename** | `2018-03-29_-_open_view_-_first_draft.md` |
| **Size** | 58K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `DRAFT_1`, `SURVEILLANCE_THRILLER` |
| **Format** | Markdown screenplay |

**Annotation**: First draft screenplay of surveillance thriller "Open View" (dated 2018-03-29). Features dysfunctional family trapped in smart home subjected to psychological tests by external surveillance apparatus (HQ). Employs innovative found-footage aesthetic with constant camera source notation. Quadrant opening sequence merges four separate character loops. Mythological substrate drawn from Athamas and Ino legend. Analyzed comprehensively in CT-004 and CT-023.

**Cross-references**: `PF-032`, `PF-033`, `PF-034`, `PF-044`, `PF-045`, `CT-004`, `CT-023`, `CT-024`

---

#### PF-032: Open View Second Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-032` |
| **Filename** | `2019-10-21_-_open_view_-_second_draft.md` |
| **Size** | 84K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `DRAFT_2`, `SURVEILLANCE_THRILLER` |
| **Format** | Markdown screenplay |

**Annotation**: Second draft screenplay (dated 2019-10-21). Substantial expansion from first draft (84K vs 58K). More abstracted and meta-textual, treating the family as entertainment product across multiple parallel "shows." Continued development of surveillance thriller narrative with increased formal experimentation.

**Cross-references**: `PF-031`, `PF-033`, `PF-034`, `CT-024`

---

#### PF-033: Open View Third Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-033` |
| **Filename** | `2019-10-31_-_open_view_-_third_draft.md` |
| **Size** | 7.0K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `DRAFT_3`, `SURVEILLANCE_THRILLER`, `PARTIAL` |
| **Format** | Markdown screenplay |

**Annotation**: Third draft screenplay (dated 2019-10-31). Significantly shorter than second draft (7.0K vs 84K), representing an incomplete restart. Characters explicitly described as clones in a virtual worldâ€”a conceptual pivot from the realist-dystopian frame of earlier drafts. Approximately 250 lines before stalling.

**Cross-references**: `PF-031`, `PF-032`, `PF-034`, `CT-024`

---

#### PF-034: Open View Complete Structural Analysis

| Field | Value |
|-------|-------|
| **ID** | `PF-034` |
| **Filename** | `open_view_complete_structural_analysis.md` |
| **Size** | 80K |
| **Tags** | `ANALYSIS`, `SCREENPLAY`, `STRUCTURAL`, `CREATIVE` |
| **Format** | Markdown analysis document |

**Annotation**: Comprehensive structural breakdown of "Open View" first draft. Documents 117 discrete beats across five-movement European art cinema structure. Identifies hybrid nature: domestic chamber drama, techno-thriller, reality TV critique, body horror. Includes character arcs, parallel structure mapping, camera grammar breakdown, thematic architecture (6 layers), and prioritized revision recommendations.

**Cross-references**: `PF-031`, `CT-004`

---

### Creative Work â€” EL / A Girl and Her Dogs

---

#### PF-047: A Girl and Her Dogs (Early Draft)

| Field | Value |
|-------|-------|
| **ID** | `PF-047` |
| **Filename** | `20171117_a_girl_and_her_dogs.pdf` |
| **Size** | 9.8M |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `EL_SERIES`, `DRAFT_EARLY`, `PDF` |
| **Format** | PDF screenplay |
| **Added** | v3 (2026-02-15) |

**Annotation**: Earliest dated document in the "EL" screenplay series (November 2017). Title "A Girl and Her Dogs" suggests an early conceptual phase before the project adopted the "EL" working title. Large file size (9.8M) indicates possible embedded images or high-resolution scanned pages. Represents the origin point of a separate creative work distinct from "Open View," sharing autobiographical concerns with family dynamics but through a different narrative frame.

**Cross-references**: `PF-048`, `PF-049`, `PF-050`, `PF-051`, `PF-052`, `PF-046`, `CT-024`

---

#### PF-048: Tale of EL Second Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-048` |
| **Filename** | `20171208__tale_of_el__second_draft.pdf` |
| **Size** | 11M |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `EL_SERIES`, `DRAFT_2`, `PDF` |
| **Format** | PDF screenplay |
| **Added** | v3 (2026-02-15) |

**Annotation**: Second draft of "Tale of EL" (December 2017). Largest file in the EL series at 11M. The "Tale of" framing suggests mythological or fabulist narrative register. Created approximately three weeks after PF-047, indicating rapid early-phase iteration.

**Cross-references**: `PF-047`, `PF-049`, `PF-050`, `PF-051`, `PF-052`, `PF-046`

---

#### PF-049: EL Fifth Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-049` |
| **Filename** | `20190407__el__fifth_draft.pdf` |
| **Size** | 9.7M |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `EL_SERIES`, `DRAFT_5`, `PDF` |
| **Format** | PDF screenplay |
| **Added** | v3 (2026-02-15) |

**Annotation**: Fifth draft of "EL" screenplay (April 2019). Represents a ~16-month gap from the December 2017 second draft, with intervening drafts 3 and 4 absent from the collection. Contemporaneous with Open View development (drafts 2 and 3 written October 2019). Title simplified to "EL" from earlier "Tale of EL."

**Cross-references**: `PF-047`, `PF-048`, `PF-050`, `PF-051`, `PF-052`, `PF-046`

---

#### PF-050: EL (Draft, April 2019)

| Field | Value |
|-------|-------|
| **ID** | `PF-050` |
| **Filename** | `20190429__el.pdf` |
| **Size** | 9.4M |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `EL_SERIES`, `DRAFT_REVISION`, `PDF` |
| **Format** | PDF screenplay |
| **Added** | v3 (2026-02-15) |

**Annotation**: EL screenplay revision dated April 29, 2019â€”just 22 days after the fifth draft (PF-049). Undated draft number suggests either a polish pass or intermediate revision between numbered drafts. Close temporal proximity to PF-049 indicates active revision period.

**Cross-references**: `PF-047`, `PF-048`, `PF-049`, `PF-051`, `PF-052`, `PF-046`

---

#### PF-051: EL Seventh Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-051` |
| **Filename** | `20190801__el__seventh_draft.pdf` |
| **Size** | 8.9M |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `EL_SERIES`, `DRAFT_7`, `PDF` |
| **Format** | PDF screenplay |
| **Added** | v3 (2026-02-15) |

**Annotation**: Seventh draft of "EL" screenplay (August 2019). Last numbered draft in the collection. Three-month gap from the April revision cluster, suggesting a longer revision cycle. File size slightly smaller than earlier drafts (8.9M vs 9.4â€“11M), potentially indicating tightening of material. Missing draft 6 suggests it may exist outside the current collection.

**Cross-references**: `PF-047`, `PF-048`, `PF-049`, `PF-050`, `PF-052`, `PF-046`

---

#### PF-052: EL First Scene (Revision, 2020)

| Field | Value |
|-------|-------|
| **ID** | `PF-052` |
| **Filename** | `20200122__el__first_scene.pdf` |
| **Size** | 604K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `EL_SERIES`, `FRAGMENT`, `PDF` |
| **Format** | PDF screenplay fragment |
| **Added** | v3 (2026-02-15) |

**Annotation**: Isolated first scene of "EL" screenplay (January 2020). Dramatically smaller than full drafts (604K vs 8.9â€“11M), confirming this is a single-scene excerpt or rewrite attempt. Five-month gap from the seventh draft. May represent a restart attempt focused on the openingâ€”a common revision strategy when a project has stalled. Last dated document in the EL series.

**Cross-references**: `PF-047`, `PF-048`, `PF-049`, `PF-050`, `PF-051`, `PF-046`

---

#### PF-046: EL Nicholl Reader Comments

| Field | Value |
|-------|-------|
| **ID** | `PF-046` |
| **Filename** | `EL_Nicholl_Reader_Comments.pdf` |
| **Size** | 227K |
| **Tags** | `CREATIVE`, `FEEDBACK`, `EL_SERIES`, `COMPETITION`, `PDF` |
| **Format** | PDF reader feedback |
| **Added** | v3 (2026-02-15) |

**Annotation**: Reader comments from the Academy Nicholl Fellowships in Screenwriting competition for the "EL" screenplay. External professional feedback on the script, providing third-party assessment of commercial and artistic viability. Represents the only formal industry evaluation document in the project collection. The Nicholl Fellowship is among the most prestigious screenwriting competitions in the industry (administered by the Academy of Motion Picture Arts and Sciences).

**Cross-references**: `PF-047`, `PF-048`, `PF-049`, `PF-050`, `PF-051`, `PF-052`

---

### Mythological Source Materials

---

#### PF-044: Athamasino (Source Material)

| Field | Value |
|-------|-------|
| **ID** | `PF-044` |
| **Filename** | `athamasino.pdf` |
| **Size** | 699K |
| **Tags** | `MYTH_SOURCE`, `GREEK`, `ADAPTATION`, `CREATIVE` |
| **Format** | PDF (mixed mediaâ€”AI-generated images with stylized text) |
| **Added** | v3 (2026-02-15) |

**Annotation**: Creative retelling of the Athamas and Ino myth framed through contemporary aestheticâ€”corporate notifications and glitch-text communications. Serves as mythological substrate for "Open View" screenplay. The Athamas-Ino legend (madness, infanticide, divine punishment of a family) maps directly onto Open View's family dynamics: Athamas â†’ absent/destructive father, Ino â†’ protective yet complicit mother, Learchus/Melicerta â†’ endangered children, Furies/Juno â†’ surveillance apparatus.

**Cross-references**: `PF-045`, `PF-031`, `CT-024`

---

#### PF-045: Athamas & Ino (Source Material)

| Field | Value |
|-------|-------|
| **ID** | `PF-045` |
| **Filename** | `Athamas__Ino.pdf` |
| **Size** | 1.4M |
| **Tags** | `MYTH_SOURCE`, `GREEK`, `ADAPTATION`, `CREATIVE` |
| **Format** | PDF (mixed media archive) |
| **Added** | v3 (2026-02-15) |

**Annotation**: Larger companion document to PF-044, containing additional Athamas and Ino source material including AI-generated imagery and stylized digital retellings. Together with PF-044, provides the mythological framework connecting autobiographical family material (divorce, father's pattern of absence, sibling dynamics) to the classical tragedy structure adapted in "Open View."

**Cross-references**: `PF-044`, `PF-031`, `CT-024`

---

## Conversation Threads Catalog

---

### CT-001: Building Narratological Algorithms from Cinema and Games

| Field | Value |
|-------|-------|
| **ID** | `CT-001` |
| **Title** | Building narratological algorithms from cinema and games |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-25T03:49:06Z |
| **Tags** | `PLANNING`, `STUDY_GUIDE`, `MULTI-MEDIA` |

**Annotation**: Established comprehensive study framework for future algorithm extraction across multiple media. Categorized artists by medium (film, comics, literature, games, animation) with core narrative signatures and potential algorithm focus areas. Generated 14 detailed study prompts following established methodology. Includes cross-reference recommendations for productive study sequences.

**Files Generated**: 
- `narratological_study_prompts.md` (PF-029)
- `Study_List__Narratological_Algorithm_Sources` (PF-030)

---

### CT-002: Research Roles and Documents for Artistic Analysis

| Field | Value |
|-------|-------|
| **ID** | `CT-002` |
| **Title** | Research roles and documents for artistic analysis |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-25T03:44:19Z |
| **Tags** | `METHODOLOGY`, `FEEDBACK_ROLES`, `TEMPLATES` |

**Annotation**: Comprehensive research on nine critical feedback roles (aesthete, dramaturgist, narratologist, art historian, cinephile, rhetorician, producer, academic, first-reader). Ranked roles by formalization potential. Created 28-template collection for professional artistic feedback practices. Established that descriptive elements are more formalizable than evaluative elements.

**Files Generated**: 28 feedback templates (embedded in SKILL.md)

---

### CT-003: Comprehensive Script Analysis and Dramaturgical Breakdown

| Field | Value |
|-------|-------|
| **ID** | `CT-003` |
| **Title** | Comprehensive script analysis and dramaturgical breakdown |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-24T14:15:46Z |
| **Tags** | `SKILL_CREATION`, `ANALYSIS`, `DRAMATURGICAL` |

**Annotation**: Created complete skill package "script-analysis-dramaturgical" synthesizing existing narratological algorithms framework. Eight core deliverable documents with role-tagged observations. Integrates McKee, Aristotle, South Park, Phoebe Waller-Bridge, Larry David, and Attention Mechanics frameworks.

**Files Generated**: 
- `SKILL.md` (PF-021)
- 5 template files (PF-023 through PF-027)

---

### CT-004: First Draft Feedback on Open View

| Field | Value |
|-------|-------|
| **ID** | `CT-004` |
| **Title** | First draft feedback on open view |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-24T13:49:44Z |
| **Tags** | `CREATIVE_WORK`, `FEEDBACK`, `STRUCTURAL_ANALYSIS` |

**Annotation**: Comprehensive first-reader analysis of "Open View" surveillance thriller screenplay. Documented 117 beats across five-movement structure. Identified hybrid genre nature and key structural issues (underdeveloped HQ subplot, undramatized climax, setup gaps). Discovered missed section containing critical plot element (Lef's death, Black Box thesis statement).

**Files Generated**: 
- `open_view_complete_structural_analysis.md` (PF-034)

---

### CT-005: Attention Economy Across Media Forms

| Field | Value |
|-------|-------|
| **ID** | `CT-005` |
| **Title** | Attention economy across media forms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-24T04:24:07Z |
| **Tags** | `META_THEORY`, `ATTENTION`, `CROSS-MEDIA` |

**Annotation**: Developed meta-theoretical framework positioning attention as "ur-currency" of narrative. Identified comedy and horror as "pure" genres providing binary verification through involuntary physiological responses. Created 11-section cross-media attention algorithm document. Established theoretical substrate unifying all individual artist/theorist algorithms.

**Files Generated**: 
- `attention_mechanics_meta_principles.md` (PF-028)

---

### CT-006: Tarantino's Genre Taxonomy and Creative Methodology

| Field | Value |
|-------|-------|
| **ID** | `CT-006` |
| **Title** | Tarantino's genre taxonomy and creative methodology |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-24T02:54:33Z |
| **Tags** | `RESEARCH`, `FILM`, `GENRE`, `TARANTINO` |

**Annotation**: Two comprehensive research reports on Tarantino's filmmaking philosophy. First report: genre philosophy ("sub-genres of my life," "the Southern" invention, genre mixing methodology). Second report: discovery-based writing process using genre conventions as structural scaffolding rather than outlining. Based on primary source interviews.

**Files Generated**: 
- `tarantino_genre_philosophy_research_report.md` (PF-018)
- `tarantino_genre_conventions_as_structure.md` (PF-019)

---

### CT-007: Narratological Algorithms from Artistic Principles

| Field | Value |
|-------|-------|
| **ID** | `CT-007` |
| **Title** | Narratological algorithms from artistic principles |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-24T02:29:04Z |
| **Tags** | `SKILL_CREATION`, `METHODOLOGY`, `CORE` |

**Annotation**: Created foundational skill package "narratological-algorithms" for distilling artist/theorist principles into formal frameworks. 8-step workflow, three reference files (output template, formalization patterns, theoretical correspondences). Established canonical document structure used across all algorithm documents.

**Files Generated**: 
- `SKILL-preview.md` (PF-022)

---

### CT-008: Bharata-Muni's Narrative Principles as Algorithms (Primary + Supplement)

| Field | Value |
|-------|-------|
| **ID** | `CT-008` |
| **Title** | Bharata-Muni's narrative principles as algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-23T15:55:11Z |
| **Tags** | `CLASSICAL`, `INDIAN`, `RASA`, `NATYASASTRA` |

**Annotation**: Primary and supplementary algorithmic distillation of Bharata Muni's *Natyasastra*. Primary document: rasa-bhava theory, abhinaya, plot structure, character typologies. Supplement: ghata (failure modes), temporal constraints, purvaranga, rasa combination rules.

**Files Generated**: 
- `bharata_muni_narratological_algorithms.md` (PF-011)
- `bharata_muni_narratological_algorithms_supplement.md` (PF-012)

---

### CT-009: Bharata-Muni's Narrative Principles as Algorithms (Extended)

| Field | Value |
|-------|-------|
| **ID** | `CT-009` |
| **Title** | Bharata-Muni's narrative principles as algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-23T15:27:49Z |
| **Tags** | `CLASSICAL`, `INDIAN`, `PERFORMANCE`, `NATYASASTRA` |

**Annotation**: Extended document completing *Natyasastra* coverage. Performance-integrated systems: Chapters 2â€“5 (playhouse construction), 8â€“13 (dance/gesture), 14â€“19 (speech/prosody), 23â€“25 (costumes), 27 (success theory). Includes 108 karanas, 67 hand gestures, and production protocols.

**Files Generated**: 
- `bharata_muni_narratological_algorithms_extended.md` (PF-016)

---

### CT-010: Horace's Poetic Principles as Narrative Algorithms

| Field | Value |
|-------|-------|
| **ID** | `CT-010` |
| **Title** | Horace's poetic principles as narrative algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-23T05:01:22Z |
| **Tags** | `CLASSICAL`, `ROMAN`, `CRAFT` |

**Annotation**: Algorithmic distillation of Horace's *Ars Poetica*. 12-section document capturing practical craft instructions: genius-plus-labor, "no mediocrity" threshold, nine-year rule, character age-stages, critic function diagnostics. Key Latin phrases preserved with applications.

**Files Generated**: 
- `horace_narratological_algorithms.md` (PF-010)

---

### CT-011: Plato's Principles as Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `CT-011` |
| **Title** | Plato's principles as narratological algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-23T04:36:07Z |
| **Tags** | `CLASSICAL`, `GREEK`, `PHILOSOPHY`, `MIMESIS` |

**Annotation**: Algorithmic distillation of Plato's narrative theory from *The Republic* (Books II, III, X). 13-section document covering three modes of narration, ontological hierarchy, tripartite soul, content regulation, mimesis-as-contagion. Documents fundamental Plato-Aristotle divergence on catharsis.

**Files Generated**: 
- `plato_narratological_algorithms.md` (PF-009)

---

### CT-012: Aristotle's Poetics as Narrative Algorithms

| Field | Value |
|-------|-------|
| **ID** | `CT-012` |
| **Title** | Aristotle's poetics as narrative algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-23T04:32:57Z |
| **Tags** | `CLASSICAL`, `GREEK`, `FOUNDATIONAL` |

**Annotation**: Comprehensive 13-section algorithmic distillation of Aristotle's *Poetics*. Six elements hierarchy, unity principle, probability/necessity, reversal/recognition, catharsis conditions. Includes Homer's restraint rule, "art of skillful lies," validation checklists in Python-style pseudocode. Foundational reference for all other algorithm documents.

**Files Generated**: 
- `aristotle_narratological_algorithms.md` (PF-008)

---

### CT-013: Kubrick's Non-Submersible Narrative Units

| Field | Value |
|-------|-------|
| **ID** | `CT-013` |
| **Title** | Kubrick's non-submersible narrative units |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T22:50:19Z |
| **Tags** | `RESEARCH`, `FILM`, `KUBRICK`, `ADAPTATION` |

**Annotation**: Research report on Kubrick's "non-submersible units" theory from primary source interviews (1960â€“1999). 6â€“8 sequence structure, explanatory element removal, productive ambiguity preservation. Film-by-film adaptation analyses: *2001*, *A Clockwork Orange*, *Barry Lyndon*, *The Shining*, *Eyes Wide Shut*. Eight extractable principles in pseudocode format.

**Files Generated**: 
- `Stanley_Kubrick_s_Narratological_Philosophy__Primary_Sources_and_Extractable_Principles.md` (PF-017)

---

### CT-014: Narratological Algorithms from Layered Obstacles

| Field | Value |
|-------|-------|
| **ID** | `CT-014` |
| **Title** | Narratological algorithms from layered obstacles |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T21:47:50Z |
| **Tags** | `ALGO`, `TELEVISION`, `SCENE_DESIGN`, `PWB` |

**Annotation**: Algorithmic distillation of Phoebe Waller-Bridge's "three things going on" technique. 11-section document: four-layer scene construction, obstacle taxonomies, interaction matrices, genre-specific applications. Maps to McKee, Sorkin, Mamet scene theory.

**Files Generated**: 
- `phoebe_waller_bridge_narratological_algorithms.md` (PF-014)

---

### CT-015: South Park's Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `CT-015` |
| **Title** | South Park's narratological algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T21:38:25Z |
| **Tags** | `ALGO`, `COMEDY`, `ANIMATION`, `CAUSALITY` |

**Annotation**: 15-section formalization of Parker/Stone "but/therefore" rule. Three-word diagnostic system, shuffle test, status quo test, single A-story principle, causal chain templates. Canonical episode breakdowns: "Scott Tenorman Must Die," "Make Love Not Warcraft." Maps to Aristotle through McKee.

**Files Generated**: 
- `south_park_narratological_algorithms.md` (PF-013)

---

### CT-016: David's Comedic Rules as Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `CT-016` |
| **Title** | David's comedic rules as narratological algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T21:32:30Z |
| **Tags** | `ALGO`, `COMEDY`, `TELEVISION`, `LARRY_DAVID` |

**Annotation**: 12-section algorithmic distillation of Larry David's comedy methodology. "No hugging, no learning" meta-principle, four-phase episode architecture, retrofit plotting, collision design, "amoral karma engine." Episode templates and Feydeau ancestry documented.

**Files Generated**: 
- `larry_david_narratological_algorithms.md` (PF-007)

---

### CT-017: McKee's Narratological Algorithms

| Field | Value |
|-------|-------|
| **ID** | `CT-017` |
| **Title** | McKee's narratological algorithms |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T21:00:23Z |
| **Tags** | `ALGO`, `SCREENWRITING`, `MCKEE`, `FOUNDATIONAL` |

**Annotation**: Comprehensive 23-section algorithmic distillation of McKee's *Story*. All 19 chapters covered: Gap Algorithm, Value Charge System, scene design protocols, exposition management. Pseudocode implementations, decision tables, verification tables, quick-reference materials.

**Files Generated**: 
- `mckee_narratological_algorithms_complete.md` (PF-006)

---

### CT-018: McKee's Narrative Principles Formalized (OCR Session)

| Field | Value |
|-------|-------|
| **ID** | `CT-018` |
| **Title** | McKee's narrative principles formalized |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T15:15:07Z |
| **Tags** | `SOURCE_EXTRACTION`, `OCR`, `MCKEE` |

**Annotation**: Initial OCR extraction session for McKee's *Story* book (427-page scanned PDF). Converted PDF pages to images and ran OCR to capture key principles. Basis for PF-001 and subsequent CT-017 algorithm work.

**Files Generated**: 
- `McKee_Story.txt` (PF-001)

---

### CT-019: Scene Complications as Narrative Protocol (Initial Research)

| Field | Value |
|-------|-------|
| **ID** | `CT-019` |
| **Title** | Scene complications as narrative protocol |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-22T14:42:06Z |
| **Tags** | `RESEARCH`, `INITIAL`, `MULTI-TECHNIQUE` |

**Annotation**: Foundational research session exploring three distinct storytelling methodologies: (1) Phoebe Waller-Bridge "three things going on" from Fleabag, (2) Larry David "cascading consequences" from Seinfeld/Curb, (3) Parker/Stone "but/therefore" from South Park. Initial research reports that became source documents for subsequent algorithm distillations.

**Files Generated**: 
- `The_Three_Things_Going_On_Technique__Phoebe_Waller-Bridge_and_Scene_Construction_Through_Layered_Obstacles.md` (PF-020)
- `Comedy_Geometry__Larry_David_s_Architecture_of_Cascading_Consequences.md` (PF-035)
- `The_South_Park_But_Therefore_Rule__A_Complete_Craft_Analysis.md` (PF-036)

---

### CT-020: Original Manifest Creation

| Field | Value |
|-------|-------|
| **ID** | `CT-020` |
| **Title** | Claude project manifest with annotated bibliography |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-25T09:18:03Z |
| **Tags** | `MANIFEST`, `DOCUMENTATION`, `PROJECT_MANAGEMENT` |
| **Added** | v3 (2026-02-15) |

**Annotation**: Created the original v1 project manifest cataloging 33 project files and 18 conversation threads. Established the annotated bibliography format with unique identifiers (PF-### for files, CT-### for threads), tag taxonomy, cross-reference indices, dependency graph, and summary statistics. Manifest structure designed for incremental amendment as project grows.

**Files Generated**: 
- `narratological_project_manifest.md` (this document, v1)

---

### CT-021: Designing Multi-Lens Protocols for Project Review

| Field | Value |
|-------|-------|
| **ID** | `CT-021` |
| **Title** | Designing multi-lens protocols for project review |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-25T10:21:38Z |
| **Tags** | `PROTOCOL_DESIGN`, `METHODOLOGY`, `FRAMEWORK` |
| **Added** | v3 (2026-02-15) |

**Annotation**: Comprehensive review of all 31 project files and 18 threads to design differentiated analysis protocols. Produced the seven-protocol framework (P1â€“P7) with role activation matrices, document generation rules, protocol selection logic, and escalation paths. Delivered three core documents: main protocols framework, protocol-specific templates, and invocation guide. Subsequently expanded with ready-to-use invocation prompts mapping natural language to protocol levels.

**Files Generated**: 
- `analysis_protocols_framework.md` (PF-037)
- `protocol_specific_templates.md` (PF-038)
- `protocol_invocation_guide.md` (PF-039)
- `protocol_invocation_prompts.md` (PF-040)

---

### CT-022: Applying Analysis Protocols to Creative Work

| Field | Value |
|-------|-------|
| **ID** | `CT-022` |
| **Title** | Applying analysis protocols to creative work |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-25T21:43:10Z |
| **Tags** | `SKILL_CREATION`, `PROTOCOL_IMPLEMENTATION`, `ARCHITECTURE` |
| **Added** | v3 (2026-02-15) |

**Annotation**: Designed and installed an 8-skill architecture implementing the P1â€“P7 analysis protocols as AI skills. Hub-and-spoke design: master routing skill "creative-analysis" parses user intent and selects appropriate protocol, plus seven individual protocol skills (P1-TRIAGE through P7-COMPREHENSIVE) invocable directly or via router. Created supporting reference documents: quick-reference card and integration guide.

**Files Generated**: 
- `quick-reference.md` (PF-041)
- `integration-guide.md` (PF-042)
- 8 skill files (installed to skills directory)

---

### CT-023: P7 Comprehensive Analysis of Open View

| Field | Value |
|-------|-------|
| **ID** | `CT-023` |
| **Title** | Script analysis for open view draft |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-25T22:23:29Z |
| **Tags** | `CREATIVE_WORK`, `P7_COMPREHENSIVE`, `ANALYSIS`, `OPEN_VIEW` |
| **Added** | v3 (2026-02-15) |

**Annotation**: First application of the full Protocol 7 analytical treatment. All 9 analyst roles activated; 13 discrete documents produced (~37,500 words total). Confirmed script's formal ambitions (inventive quadrant opening, sophisticated thematic architecture around surveillance) while diagnosing critical structural problems: incomplete third act terminating mid-climax, unintegrated HQ subplot, weak causal logic, dangling threads. Positioned work for A24/Neon acquisition profile contingent on structural revision. Produced detailed beat mapping of all 87 scenes, character arc analysis, theoretical correspondence across multiple frameworks, and structured revision roadmap.

**Files Generated**: 
- 13 analysis documents (delivered in-thread, not as separate project files)

---

### CT-024: Family Trauma and Mythological Adaptation

| Field | Value |
|-------|-------|
| **ID** | `CT-024` |
| **Title** | Family trauma and mythological adaptation |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-26T20:57:34Z |
| **Tags** | `CREATIVE_WORK`, `AUTOBIOGRAPHY`, `MYTHOLOGY`, `OPEN_VIEW`, `EL_SERIES` |
| **Added** | v3 (2026-02-15) |

**Annotation**: Critical autobiographical context session. User shared two key inspirations for "Open View": family experience with divorce (father's pattern of "running away," younger brother born after 9/11) and the Greek myth of Athamas and Ino. Claude read all three Open View drafts and examined mythological source materials (PF-044, PF-045). Identified clear correspondences: Athamas â†’ father, Ino â†’ mother, Learchus/Melicerta â†’ siblings, Furies/Juno â†’ surveillance apparatus. Documented the evolution across drafts from realist-dystopian (Draft 1) through meta-textual (Draft 2) to virtual-world restart (Draft 3). Also the thread that introduced the EL screenplay series to the project, with user uploading all six EL drafts and reader comments for the first time.

**Files Generated**: 
- None directly; but introduced PF-044 through PF-052 to the project

---

### CT-025: Enumerating Fundamental Narrative Structures

| Field | Value |
|-------|-------|
| **ID** | `CT-025` |
| **Title** | Enumerating fundamental narrative structures |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-01-27T03:37:11Z |
| **Tags** | `RESEARCH`, `NARRATIVE_THEORY`, `ENUMERATION`, `COMPUTATIONAL` |
| **Added** | v3 (2026-02-15) |

**Annotation**: Comprehensive research into whether narratives reduce to a finite set of basic story types. Covered three dimensions: theoretical taxonomy (Polti, Propp, Campbell, Booker, Tobias), empirical/computational validation (University of Vermont six emotional arcs study confirming Vonnegut's thesis), and application angles for algorithmic formalization. Assessed Propp's morphology as most computationally tractable for story generation, Booker's framework for classification tasks. Included critiques of Jungian foundations and cultural bias in Western enumeration schemes.

**Files Generated**: 
- `__Are_there_a_finite_number_of_stories__The_enduring_quest_to_enumerate_narrative` (PF-043)

---

### CT-026: First Manifest Amendment Session

| Field | Value |
|-------|-------|
| **ID** | `CT-026` |
| **Title** | Organizing project manifest with file annotations |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-02-05T00:09:55Z |
| **Tags** | `MANIFEST`, `DOCUMENTATION`, `AMENDMENT` |
| **Added** | v3 (2026-02-15) |

**Annotation**: First manifest amendment session (v2). Performed delta analysis identifying 5 new threads and 14 new files since v1. Assigned IDs PF-037 through PF-053 and CT-020 through CT-024. Amendment was produced in-thread but not persisted back to the project file on diskâ€”necessitating the current v3 comprehensive update to reconcile all changes.

**Files Generated**: 
- Manifest amendment (in-thread only; not persisted to project files)

---

### CT-027: Balancing Novelty Against Comparative Analysis

| Field | Value |
|-------|-------|
| **ID** | `CT-027` |
| **Title** | Balancing novelty against comparative analysis |
| **URL** | [personal conversation link redacted] |
| **Updated** | 2026-02-05T16:19:09Z |
| **Tags** | `EPISTEMOLOGY`, `CRITIQUE`, `PROJECT_LIMITATIONS`, `METHODOLOGY` |
| **Added** | v3 (2026-02-15) |

**Annotation**: Critical epistemological discussion prompted by a peer's critique: does a framework built on existing theories necessarily "problematize the new"â€”measuring innovative work against established norms and flagging deviation as deficiency when it may be virtue? Analysis addressed three failure modes (false positives, misdiagnosis, scope collapse) and genuine blind spots. Key insight: the system can accommodate novel *implementations* of known mechanisms (via prediction modes from anticipation-satisfaction through "full jazz") but cannot recognize entirely novel *mechanisms*. Proposed architectural extensions including innovation detection protocols and explicit "framework doesn't apply" exit conditions. Reframed the system as diagnostic infrastructure rather than evaluative instrument.

**Files Generated**: 
- None (discussion thread; no documents produced)

---

## Cross-Reference Indices

### By Theoretical Tradition

| Tradition | Files | Threads |
|-----------|-------|---------|
| **Greek Classical** | PF-002, PF-003, PF-008, PF-009 | CT-011, CT-012 |
| **Roman Classical** | PF-004, PF-010 | CT-010 |
| **Indian Classical** | PF-005, PF-011, PF-012, PF-016 | CT-008, CT-009 |
| **Contemporary Screenwriting** | PF-001, PF-006 | CT-017, CT-018 |
| **Television Comedy** | PF-007, PF-013, PF-014, PF-035, PF-036 | CT-014, CT-015, CT-016 |
| **Film Auteur** | PF-017, PF-018, PF-019 | CT-006, CT-013 |
| **Narrative Enumeration** | PF-043 | CT-025 |
| **Meta-Framework** | PF-028, PF-029, PF-030 | CT-001, CT-005 |
| **Greek Mythology** | PF-044, PF-045 | CT-024 |

### By Document Type

| Type | Files | Count |
|------|-------|-------|
| **Primary Source Texts** | PF-001, PF-002, PF-003, PF-004, PF-005 | 5 |
| **Algorithm Documents** | PF-006, PF-007, PF-008, PF-009, PF-010, PF-011, PF-012, PF-013, PF-014, PF-016 | 10 |
| **Research Reports** | PF-017, PF-018, PF-019, PF-020, PF-043 | 5 |
| **Source Analysis** | PF-035, PF-036 | 2 |
| **Skills & Templates** | PF-021, PF-022, PF-023, PF-024, PF-025, PF-026, PF-027 | 7 |
| **Protocol Framework** | PF-037, PF-038, PF-039, PF-040, PF-041, PF-042 | 6 |
| **Meta-Documents** | PF-028, PF-029, PF-030 | 3 |
| **Creative Work (Open View)** | PF-031, PF-032, PF-033, PF-034 | 4 |
| **Creative Work (EL Series)** | PF-046, PF-047, PF-048, PF-049, PF-050, PF-051, PF-052 | 7 |
| **Mythological Sources** | PF-044, PF-045 | 2 |
| **Manifest** | This document | 1 |

### By Thread Function

| Function | Threads | Count |
|----------|---------|-------|
| **Algorithm Extraction** | CT-008â€“CT-017 | 10 |
| **Research** | CT-006, CT-013, CT-019, CT-025 | 4 |
| **Skill Creation** | CT-003, CT-007, CT-022 | 3 |
| **Protocol Design** | CT-021 | 1 |
| **Creative Work Analysis** | CT-004, CT-023, CT-024 | 3 |
| **Meta-Theory** | CT-005, CT-027 | 2 |
| **Planning** | CT-001, CT-002 | 2 |
| **Manifest/Documentation** | CT-020, CT-026 | 2 |

### Chronological Thread Sequence

| Date | Thread | Primary Output |
|------|--------|----------------|
| 2026-01-22 | CT-019 | Initial research (PWB, LD, SP) |
| 2026-01-22 | CT-018 | McKee OCR extraction |
| 2026-01-22 | CT-017 | McKee algorithms |
| 2026-01-22 | CT-016 | Larry David algorithms |
| 2026-01-22 | CT-015 | South Park algorithms |
| 2026-01-22 | CT-014 | PWB algorithms |
| 2026-01-22 | CT-013 | Kubrick research |
| 2026-01-23 | CT-012 | Aristotle algorithms |
| 2026-01-23 | CT-011 | Plato algorithms |
| 2026-01-23 | CT-010 | Horace algorithms |
| 2026-01-23 | CT-009 | Bharata Muni extended |
| 2026-01-23 | CT-008 | Bharata Muni primary+supplement |
| 2026-01-24 | CT-007 | Core skill creation |
| 2026-01-24 | CT-006 | Tarantino research |
| 2026-01-24 | CT-005 | Attention mechanics |
| 2026-01-24 | CT-004 | Open View feedback |
| 2026-01-24 | CT-003 | Script analysis skill |
| 2026-01-25 | CT-002 | Feedback roles research |
| 2026-01-25 | CT-001 | Study prompts |
| 2026-01-25 | CT-020 | **Manifest v1 creation** |
| 2026-01-25 | CT-021 | **Protocol framework design** |
| 2026-01-25 | CT-022 | **Protocol skills installation** |
| 2026-01-25 | CT-023 | **P7 analysis of Open View** |
| 2026-01-26 | CT-024 | **Mythological/autobiographical sources** |
| 2026-01-27 | CT-025 | **Narrative enumeration research** |
| 2026-02-05 | CT-026 | **Manifest v2 amendment** |
| 2026-02-05 | CT-027 | **Novelty vs. comparative analysis** |

---

### EL Series Chronology

| Date | File | Draft | Notes |
|------|------|-------|-------|
| 2017-11-17 | PF-047 | "A Girl and Her Dogs" | Origin title; conceptual phase |
| 2017-12-08 | PF-048 | "Tale of EL" 2nd draft | Mythological register; rapid iteration |
| 2019-04-07 | PF-049 | EL 5th draft | 16-month gap; drafts 3â€“4 absent |
| 2019-04-29 | PF-050 | EL (unnumbered) | 22-day revision pass |
| 2019-08-01 | PF-051 | EL 7th draft | Last numbered draft; draft 6 absent |
| 2020-01-22 | PF-052 | EL first scene | Fragment; possible restart attempt |
| â€” | PF-046 | Nicholl Reader Comments | Industry competition feedback |

---

## Dependency Graph

```
                        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                        â”‚     ATTENTION MECHANICS (PF-028)         â”‚
                        â”‚         Meta-Principles Layer            â”‚
                        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                            â”‚
          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
          â”‚                                 â”‚                                 â”‚
          â–¼                                 â–¼                                 â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   CLASSICAL          â”‚       â”‚  CONTEMPORARY        â”‚       â”‚     AUTEUR           â”‚
â”‚   TRADITION          â”‚       â”‚  SCREENWRITING       â”‚       â”‚     STUDIES          â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤       â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤       â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ Aristotle   (PF-008)â”‚       â”‚ McKee       (PF-006)â”‚       â”‚ Kubrick     (PF-017)â”‚
â”‚ Plato       (PF-009)â”‚       â”‚ Larry David (PF-007)â”‚       â”‚ Tarantino            â”‚
â”‚ Horace      (PF-010)â”‚       â”‚ South Park  (PF-013)â”‚       â”‚  (PF-018/019)        â”‚
â”‚ Bharata              â”‚       â”‚ PWB         (PF-014)â”‚       â”‚                      â”‚
â”‚  (PF-011/12/16)      â”‚       â”‚                      â”‚       â”‚                      â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
          â”‚                                 â”‚                                 â”‚
          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                            â”‚
                                            â–¼
                  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                  â”‚           NARRATIVE ENUMERATION (PF-043)          â”‚
                  â”‚    Polti Â· Propp Â· Campbell Â· Booker Â· Vonnegut   â”‚
                  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                         â”‚
                                         â–¼
                        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                        â”‚     PROTOCOL FRAMEWORK (PF-037â€“042)      â”‚
                        â”‚       P1 Triage â†’ P7 Comprehensive       â”‚
                        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                            â”‚
                                            â–¼
                        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                        â”‚         SKILL LAYER (PF-021/022)         â”‚
                        â”‚   Script Analysis + Algorithm Distill.   â”‚
                        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                            â”‚
                    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                    â–¼                       â–¼                       â–¼
          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
          â”‚   OPEN VIEW     â”‚   â”‚    EL SERIES         â”‚   â”‚  FUTURE ARTIST  â”‚
          â”‚   (PF-031â€“034)  â”‚   â”‚   (PF-046â€“052)       â”‚   â”‚  STUDIES        â”‚
          â”‚   + Myth Sourcesâ”‚   â”‚   + Nicholl Feedback  â”‚   â”‚  (PF-029/030)   â”‚
          â”‚   (PF-044/045)  â”‚   â”‚                       â”‚   â”‚                 â”‚
          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **Total Project Files** | **52** |
| Primary Source Texts | 5 |
| Algorithm Documents | 10 |
| Research Reports | 5 |
| Source Analysis Documents | 2 |
| Skills & Templates | 7 |
| Protocol Framework Documents | 6 |
| Meta-Documents | 3 |
| Creative Works (Open View) | 4 |
| Creative Works (EL Series) | 7 |
| Mythological Source Materials | 2 |
| Manifest | 1 |
| | |
| **Total Conversation Threads** | **27** |
| Algorithm extraction threads | 10 |
| Research threads | 4 |
| Skill creation threads | 3 |
| Protocol design/implementation | 2 |
| Creative work analysis | 3 |
| Meta-theory/epistemology | 2 |
| Planning/methodology | 2 |
| Manifest/documentation | 2 |
| | |
| **Growth from v1** | |
| New files since v1 (2026-01-25) | +16 (+44%) |
| New threads since v1 | +8 (+42%) |
| | |
| **Total File Size (Project)** | ~56 MB |
| Largest file | `20171208__tale_of_el__second_draft.pdf` (11M) |
| Largest source text | `bharata-muni_natyasastra.txt` (1.5M) |
| Largest algorithm doc | `mckee_narratological_algorithms_complete.md` (62K) |
| Largest protocol doc | `analysis_protocols_framework.md` (46K) |

---

*Manifest v3 generated 2026-02-15. Previous versions: v1 (2026-01-25, CT-020), v2 (2026-02-05, CT-026, in-thread only). Updates required when new files or threads are added.*

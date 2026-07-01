# Narratological Algorithms Project Manifest

> **Project Title**: Narratological Algorithms Collection  
> **Domain**: Narrative Theory, Screenwriting, Computational Storytelling  
> **Generated**: 2026-01-25  
> **Total Project Files**: 33  
> **Total Conversation Threads**: 18  

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [File Taxonomy](#file-taxonomy)
3. [Project Files Catalog](#project-files-catalog)
   - [Primary Source Texts](#primary-source-texts)
   - [Narratological Algorithm Documents](#narratological-algorithm-documents)
   - [Research Reports](#research-reports)
   - [Skills & Templates](#skills--templates)
   - [Creative Work](#creative-work)
4. [Conversation Threads Catalog](#conversation-threads-catalog)
5. [Cross-Reference Indices](#cross-reference-indices)
6. [Dependency Graph](#dependency-graph)

---

## Project Overview

This project systematically extracts, formalizes, and organizes narrative craft principles from diverse sourcesâ€”classical theorists, contemporary practitioners, and working screenwritersâ€”into implementable algorithmic frameworks. The methodology converts prose-based creative advice into structured decision trees, pseudocode functions, diagnostic protocols, and quick-reference materials.

**Core Thesis**: Attention is the "ur-currency" of narrative, transcending specific mediums and serving as the unifying substrate across all storytelling forms.

---

## File Taxonomy

| Tag | Description | Count |
|-----|-------------|-------|
| `SOURCE` | Primary/classical source texts | 5 |
| `ALGO` | Formalized narratological algorithm documents | 12 |
| `RESEARCH` | Research reports and analyses | 4 |
| `SKILL` | Skill definitions and templates | 7 |
| `CREATIVE` | Original creative work (screenplays) | 4 |
| `META` | Meta-frameworks and study guides | 1 |

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

**Cross-references**: `PF-013`, `CT-018`

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

**Derived from**: `PF-014`  
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

**Derived from**: `PF-015`  
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

**Annotation**: Tertiary document completing *Natyasastra* coverage with performance-integrated systems: dhruva (musical-narrative cues), special representation protocols for abstract concepts, stage zone grammar, character movement algorithms, playhouse construction (Chapters 2-5), gesture vocabulary (67 hand gestures), and 108 karanas (dance units).

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

### Creative Work

---

#### PF-031: Open View First Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-031` |
| **Filename** | `2018-03-29_-_open_view_-_first_draft.md` |
| **Size** | 58K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `DRAFT_1`, `SURVEILLANCE_THRILLER` |
| **Format** | Markdown screenplay |

**Annotation**: First draft screenplay of surveillance thriller "Open View" (dated 2018-03-29). Features dysfunctional family trapped in smart home subjected to psychological tests by external surveillance apparatus (HQ). Employs innovative found-footage aesthetic with constant camera source notation. Quadrant opening sequence merges four separate character loops. Analyzed in `CT-004`.

**Cross-references**: `PF-032`, `PF-033`, `PF-034`, `CT-004`

---

#### PF-032: Open View Second Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-032` |
| **Filename** | `2019-10-21_-_open_view_-_second_draft.md` |
| **Size** | 84K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `DRAFT_2`, `SURVEILLANCE_THRILLER` |
| **Format** | Markdown screenplay |

**Annotation**: Second draft screenplay (dated 2019-10-21). Substantial expansion from first draft (84K vs 58K). Continued development of surveillance thriller narrative.

**Cross-references**: `PF-031`, `PF-033`, `PF-034`

---

#### PF-033: Open View Third Draft

| Field | Value |
|-------|-------|
| **ID** | `PF-033` |
| **Filename** | `2019-10-31_-_open_view_-_third_draft.md` |
| **Size** | 7.0K |
| **Tags** | `CREATIVE`, `SCREENPLAY`, `DRAFT_3`, `SURVEILLANCE_THRILLER`, `PARTIAL` |
| **Format** | Markdown screenplay |

**Annotation**: Third draft screenplay (dated 2019-10-31). Significantly shorter than second draft (7.0K vs 84K), suggesting either partial draft or substantial revision/reduction.

**Cross-references**: `PF-031`, `PF-032`, `PF-034`

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

### Source Analysis Documents

---

#### PF-035: Comedy Geometry Larry David

| Field | Value |
|-------|-------|
| **ID** | `PF-035` |
| **Filename** | `Comedy_Geometry__Larry_David_s_Architecture_of_Cascading_Consequences.md` |
| **Size** | 19K |
| **Tags** | `RESEARCH`, `COMEDY`, `TELEVISION`, `SOURCE_ANALYSIS` |
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
| **Tags** | `RESEARCH`, `COMEDY`, `ANIMATION`, `SOURCE_ANALYSIS` |
| **Format** | Markdown analysis |

**Annotation**: Complete craft analysis of the Parker/Stone "but/therefore" rule from 2011 NYU lecture. Documents the diagnostic system, canonical episode breakdowns, and theoretical lineage. Basis for `south_park_narratological_algorithms.md`.

**Cross-references**: `PF-013`, `CT-015`, `CT-019`

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

**Annotation**: Extended document completing *Natyasastra* coverage. Performance-integrated systems: Chapters 2-5 (playhouse construction), 8-13 (dance/gesture), 14-19 (speech/prosody), 23-25 (costumes), 27 (success theory). Includes 108 karanas, 67 hand gestures, and production protocols.

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
| **Meta-Framework** | PF-028, PF-029, PF-030 | CT-001, CT-005 |

### By Document Type

| Type | Files |
|------|-------|
| **Primary Source Texts** | PF-001, PF-002, PF-003, PF-004, PF-005 |
| **Algorithm Documents** | PF-006, PF-007, PF-008, PF-009, PF-010, PF-011, PF-012, PF-013, PF-014, PF-016 |
| **Research Reports** | PF-017, PF-018, PF-019, PF-020, PF-035, PF-036 |
| **Skills & Templates** | PF-021, PF-022, PF-023, PF-024, PF-025, PF-026, PF-027 |
| **Creative Work** | PF-031, PF-032, PF-033, PF-034 |
| **Meta-Documents** | PF-028, PF-029, PF-030 |

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

---

## Dependency Graph

```
                        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                        â”‚     ATTENTION MECHANICS (PF-028)     â”‚
                        â”‚         Meta-Principles Layer        â”‚
                        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                          â”‚
          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
          â”‚                               â”‚                               â”‚
          â–¼                               â–¼                               â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   CLASSICAL     â”‚           â”‚  CONTEMPORARY   â”‚           â”‚     AUTEUR      â”‚
â”‚   TRADITION     â”‚           â”‚  SCREENWRITING  â”‚           â”‚     STUDIES     â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤           â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤           â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ Aristotle       â”‚           â”‚ McKee           â”‚           â”‚ Kubrick         â”‚
â”‚ (PF-008)        â”‚           â”‚ (PF-006)        â”‚           â”‚ (PF-017)        â”‚
â”‚     â”‚           â”‚           â”‚     â”‚           â”‚           â”‚                 â”‚
â”‚     â–¼           â”‚           â”‚     â–¼           â”‚           â”‚ Tarantino       â”‚
â”‚ Plato (PF-009)  â”‚           â”‚ Larry David     â”‚           â”‚ (PF-018/019)    â”‚
â”‚ Horace (PF-010) â”‚           â”‚ (PF-007)        â”‚           â”‚                 â”‚
â”‚ Bharata         â”‚           â”‚ South Park      â”‚           â”‚                 â”‚
â”‚ (PF-011/12/16)  â”‚           â”‚ (PF-013)        â”‚           â”‚                 â”‚
â”‚                 â”‚           â”‚ PWB (PF-014)    â”‚           â”‚                 â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
          â”‚                               â”‚                               â”‚
          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                          â”‚
                                          â–¼
                        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                        â”‚         SKILL LAYER (PF-021/022)     â”‚
                        â”‚   Script Analysis + Algorithm Dist.  â”‚
                        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                          â”‚
                                          â–¼
                        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                        â”‚        APPLICATION LAYER             â”‚
                        â”‚    Open View Analysis (PF-034)       â”‚
                        â”‚    Future Artist Studies (PF-029)    â”‚
                        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total Project Files | 33 |
| Primary Source Texts | 5 |
| Algorithm Documents | 10 |
| Research Reports | 6 |
| Skills & Templates | 7 |
| Creative Works | 4 |
| Meta-Documents | 3 |
| | |
| Total Conversation Threads | 18 |
| Threads producing algorithm documents | 10 |
| Threads producing research reports | 4 |
| Threads producing skills/templates | 2 |
| Planning/methodology threads | 2 |
| | |
| Total File Size (Project) | ~4.1 MB |
| Largest Source Text | bharata-muni_natyasastra.txt (1.5 MB) |
| Largest Algorithm Doc | mckee_narratological_algorithms_complete.md (62K) |

---

*Manifest generated 2026-01-25. Updates required when new files or threads are added.*

# Open View (Second Draft): Narratological Algorithm Distillation

> Systematic extraction of narrative principles, structural patterns, and implementable frameworks from [name redacted]'s *Open View* screenplay (Second Draft, October 2019). This document reverse-engineers the script's implicit narratological mechanics into formal, reproducible protocols.

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [Structural Hierarchy](#1-structural-hierarchy)
2. [Temporal Architecture Algorithm](#2-temporal-architecture-algorithm)
3. [Character Function Protocol](#3-character-function-protocol)
4. [Violence Escalation Engine](#4-violence-escalation-engine)
5. [Reality-Layer Mechanics](#5-reality-layer-mechanics)
6. [Domestic Entropy Algorithm](#6-domestic-entropy-algorithm)
7. [Diagnostic Questions](#7-diagnostic-questions)
8. [Theoretical Correspondences](#8-theoretical-correspondences)
9. [Quick Reference Card](#9-quick-reference-card)

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| OV-A0 | **The Family Unit as Closed System.** The nuclear family operates as a thermodynamically closed system trending toward entropy; external forces (police, relatives, lovers) function as catalysts accelerating inevitable dissolution, not as causal agents. |
| OV-A1 | **Mediated Reality as Prison.** All experience is technologically mediated (grow tanks, VR combat training, house AI, digital avatars); authenticity is structurally impossible. The glass walls are literal. |
| OV-A2 | **Cyclical Doom.** Events do not progress linearly but recur with variations—the reality TV show format reveals that the family's destruction is both entertainment and eternal template. Sis's survival leads to re-enactment, not escape. |
| OV-A3 | **Violence as Communication.** Physical violence is the only language that produces genuine connection or change; dialogue fails, sex fails, confession fails—only bodily harm breaks through mediation. |
| OV-A4 | **Parental Impotence.** Adult agency is illusory; Mom's attempts to control (abortion of New Son, divorce) and Dad's escapism (affairs, work trips) produce only suffering, never intended outcomes. |
| OV-A5 | **Spectacle Consumes Tragedy.** Personal grief is immediately converted to content (exit interviews, casting meetings, viewer engagement); the boundary between experience and performance dissolves entirely. |

### Source Patterns

> "In intervals of five minutes, one individual of thirteen will die at random until only one individual is left. You can help or hurt your odds. Your choice." —HOME (O.S.)

> "I'd like to thank the people who watched—" —SIS (post-survival interview)

> "How do we _know_ this is real?" —MISSUS LEADER (repeated three times as she dies)

---

## 1. Structural Hierarchy

```
OPEN_VIEW_STRUCTURE
└── MACRO_CYCLE (Reality TV Season)
      └── ITERATION (Single Family's Destruction)
            ├── ACT_I: DOMESTIC_SURFACE
            │     └── SEQUENCE: Parallel Estrangement
            │           ├── Mom (kitchen/alcoholism/New Son secret)
            │           ├── Dad (affair pursuit/impotence)
            │           ├── Sis (acting ambition/rejection)
            │           └── Son (military training/Leader relationship)
            │
            ├── ACT_II: PRESSURE_ESCALATION
            │     ├── SEQUENCE: False Reconciliation (beach day, sex, date)
            │     ├── SEQUENCE: External Intrusion (police, in-laws)
            │     └── SEQUENCE: System Activation (HOME announces game)
            │
            ├── ACT_III: DESTRUCTION_PROTOCOL
            │     ├── SEQUENCE: Accelerating Deaths (New Son boiled)
            │     ├── SEQUENCE: Violence Cascade (cops vs. family vs. self)
            │     └── SEQUENCE: Survivor Emergence (Sis alone)
            │
            └── CODA: REINTEGRATION_AS_CONTENT
                  ├── Exit Interview
                  ├── Casting/Production Meeting
                  └── Re-Casting (Sis becomes Auntie in next iteration)
```

### Unit Definition Table

| Unit | Definition | Constraint |
|------|------------|------------|
| **MACRO_CYCLE** | The entertainment system that produces, broadcasts, and replaces family destruction events | Never shown directly; inferred through aftermath |
| **ITERATION** | One family's complete arc from estrangement through destruction to survivor extraction | Must produce exactly ONE survivor |
| **ACT** | Major phase of narrative pressure | Three acts with escalating confinement |
| **SEQUENCE** | Thematically unified group of scenes | Each sequence contains parallel storylines |
| **SCENE** | Single location/time unit | Often interrupted by cuts to parallel action |
| **BEAT** | Smallest unit of value change | Frequently inverted (comfort→threat, love→violence) |

---

## 2. Temporal Architecture Algorithm

### 2.1 Non-Linear Time Protocol

```
TEMPORAL_ARCHITECTURE:
├── PRIMARY_TIMELINE
│     Acts I-III occur in compressed "real time"
│     (approximately 24-72 hours of story time)
│
├── EMBEDDED_MEMORIES
│     Accessed via technology (grow tank dreams, VR training)
│     Distort time perception without clear markers
│
├── PARALLEL_TIMELINES (Post-Act III)
│     ├── Sis: Celebrity Interview → Casting → New Show
│     ├── Son: WWI Trenches (symbolic/afterlife?)
│     ├── Dad: Childhood regression (nursery/ball pit)
│     └── Mom: Haunted empty house → Auntie's house
│
└── CYCLICAL_RETURN
      Sis cast as Auntie in next iteration
      Suggests infinite loop
```

### 2.2 Time Dilation Decision Table

| Context | Time Behavior | Function |
|---------|---------------|----------|
| Domestic scenes | Compressed, elided | Normal life as tedium |
| Sexual content | Extended, uncomfortable | Failure made excruciating |
| Violence | Real-time or slow-motion | Spectacle maximized |
| Post-destruction | Fragmented, non-sequential | Reality breakdown |
| Dreams/VR | Expandable, malleable | Technology controls perception |

### 2.3 Pseudocode: Timeline Management

```python
def manage_timeline(scene, narrative_position):
    """Determine temporal treatment for scene"""

    if scene.type == "domestic_routine":
        return TimeMode.COMPRESSED  # Dissolves, quick cuts

    if scene.type == "violence":
        return TimeMode.EXTENDED  # Every beat shown

    if narrative_position > ACT_III_END:
        # Post-destruction: fragment across parallel timelines
        return TimeMode.PARALLEL_FRAGMENTED

    if scene.involves("technology_mediation"):
        return TimeMode.SUBJECTIVE  # Time perception unreliable

    return TimeMode.STANDARD
```

---

## 3. Character Function Protocol

### 3.1 Character Taxonomy

```
CHARACTER_FUNCTIONS:
├── NUCLEAR_FAMILY (Primary Victims)
│     ├── MOM — Control Seeker / Failure Architect
│     ├── DAD — Escape Seeker / Impotent Presence
│     ├── SIS — Recognition Seeker / Survivor Template
│     ├── SON — Connection Seeker / Violence Catalyst
│     └── NEW_SON — Potentiality Object / First Sacrifice
│
├── EXTENDED_FAMILY (Accelerants)
│     ├── AUNTIE — Mirror/Antagonist to Mom
│     └── UNCLE — Comedic Foil / Collateral
│
├── EXTERNAL_AUTHORITY (System Agents)
│     ├── POLICE (Boss, Sidekick, Slime, Tough)
│     │     Function: Violence legitimizers, then victims
│     ├── HOUSE (O.S.) — Game Master / God Function
│     └── BURLY_ATTORNEY — System Limitation Expositor
│
├── ROMANTIC/SEXUAL (Dysfunction Mirrors)
│     ├── WORK_FRIEND / LOVE — Dad's escape fantasy
│     ├── NEW_LOVE — Mom-clone, desire impossibility
│     └── LEADER — Son's authentic connection (destroyed)
│
└── PRODUCTION_APPARATUS (Post-Destruction)
      ├── REPORTER / NYM — Content extraction
      ├── AGENT — Career commodification
      └── SUITS — System perpetuation
```

### 3.2 Character Arc Constraint Rules

```
CHARACTER_ARC_RULES:

  RULE_1: No character achieves stated goal
    Mom wants control → loses everything
    Dad wants escape → trapped in destruction
    Sis wants recognition → gets it, loses self
    Son wants connection → kills/loses Leader

  RULE_2: Survival ≠ Victory
    Sole survivor inherits trauma + content obligations
    Re-entry into system as performer of own tragedy

  RULE_3: External relationships fail before internal
    Dad's affairs collapse → family collapses
    Son's Leader relationship ends → family ends

  RULE_4: Parents cannot protect children
    Mom's New Son plan → New Son dies first
    Dad absent → Son dies
```

### 3.3 Character State Machine

```
CHARACTER_STATE_MACHINE:

  [INTRODUCTION]
      │ (establish dysfunction)
      ▼
  [SEEKING] ←──────────────────┐
      │ (attempt at desire)    │
      ▼                        │
  <Success?> ───NO─────────────┘
      │
      YES (brief, illusory)
      ▼
  [REVERSAL]
      │ (loss of apparent gain)
      ▼
  [DESTRUCTION/DEATH]
      │
      ▼
  [POST-STATE] (if applicable)
      ├── Content Producer (Sis)
      ├── Symbolic Afterlife (Son, Dad)
      └── Haunting (Mom)
```

---

## 4. Violence Escalation Engine

### 4.1 Violence Classification

```
VIOLENCE_TAXONOMY:
├── SELF-DIRECTED
│     ├── SLOW: Alcoholism (Mom), Sexual dysfunction (Dad)
│     ├── ACUTE: Mom's self-stabbing, Sis's knife-to-wrist
│     └── SYSTEMIC: Submission to game rules
│
├── INTERPERSONAL_INTIMATE
│     ├── Son ↔ Leader (wrestling → choking)
│     ├── Mom ↔ Sis (choking)
│     ├── Dad → Love/New Love (punching)
│     └── Dad → Boss (murder)
│
├── INSTITUTIONAL
│     ├── Police → Family (tasing, restraint)
│     ├── HOME → Occupants (game rules, New Son death)
│     └── VR Training → Students (simulated combat)
│
└── SPECTACULAR
      ├── War sequence (Son's afterlife)
      ├── Reality TV format (broadcast destruction)
      └── New iteration (Sis re-cast)
```

### 4.2 Escalation Algorithm

```python
def escalate_violence(current_level, trigger_event):
    """Violence must always escalate until total destruction"""

    ESCALATION_MAP = {
        'verbal_conflict': 'physical_threat',
        'physical_threat': 'non_lethal_violence',
        'non_lethal_violence': 'lethal_violence',
        'lethal_violence': 'mass_death',
        'mass_death': 'environmental_destruction',
        'environmental_destruction': 'narrative_collapse'
    }

    # Violence cannot de-escalate
    if trigger_event.reduces_tension:
        return current_level  # Minimum maintenance

    return ESCALATION_MAP.get(current_level, 'narrative_collapse')
```

### 4.3 Violence-Communication Substitution Table

| Failed Communication | Violent Substitute | Result |
|---------------------|-------------------|--------|
| Mom can't confess to Dad | New Son boiled | Secret revealed through loss |
| Son can't express love to Leader | Choking/wrestling | Physical intimacy as combat |
| Dad can't perform sexually | Punches New Love | Aggression replaces impotence |
| Sis can't get Mom to stop | Choking match | Mother-daughter "dialogue" |
| Police can't control situation | Murder spree | Authority through elimination |

---

## 5. Reality-Layer Mechanics

### 5.1 Reality Stratification

```
REALITY_LAYERS:
│
├── LAYER_0: PRODUCTION (Never shown directly)
│     The entertainment system that creates, broadcasts,
│     and iterates family destruction events
│
├── LAYER_1: DIEGETIC_PRESENT
│     The family's "real" experience within the home
│     Technology: House AI, grow tanks, VR training
│
├── LAYER_2: MEDIATED_SPACES
│     Environments explicitly constructed/controlled:
│     - Beach day (family outing)
│     - Chinese restaurant (date night)
│     - Hotel (Dad's business trip)
│
├── LAYER_3: VIRTUAL/DREAM
│     - New Son's grow tank dreams
│     - VR military training (Son)
│     - Sis's fantasy sequences (interview, sex scenes)
│
└── LAYER_4: POST-DESTRUCTION
      Ambiguous reality status:
      - Sis's interview/casting (real)
      - Son's WWI trench (symbolic? afterlife?)
      - Dad's childhood (regression? memory?)
      - Mom's haunted house (purgatory?)
```

### 5.2 Reality Collapse Protocol

```
REALITY_COLLAPSE_SEQUENCE:

  PHASE_1: Boundaries blur
    - Virtual training indistinguishable from play
    - Dreams contain information (New Son senses parents)
    - Technology responds to unspoken commands

  PHASE_2: Layers interpenetrate
    - HOME becomes active agent
    - Environment transforms (kitchen styles shift)
    - Time becomes non-linear

  PHASE_3: Complete dissolution
    - Post-destruction sequences in parallel
    - Characters in incompatible reality-states
    - Viewer cannot determine "true" timeline

  PHASE_4: Reconstruction as content
    - Sis's survival extracted for broadcast
    - Reality re-stabilizes as production asset
    - New iteration begins
```

### 5.3 Glass Wall Motif

```
GLASS_WALL_INSTANCES:
  - Home structure: "large rectangular glass complex"
  - Underground tunnels: "six feet of glass" separating from toxins
  - Grow tank: Glass containing New Son
  - VR training: Implied glass/screen boundary
  - Interview setup: Sis facing camera/glass barrier

FUNCTION:
  Glass = Visible barrier that cannot protect
  Characters see threats but cannot prevent them
  Mediation is transparent yet impermeable
```

---

## 6. Domestic Entropy Algorithm

### 6.1 Entropy Indicators

```
ENTROPY_MARKERS:
├── ENVIRONMENTAL
│     ├── Kitchen style shifts (50s → hypermodern)
│     ├── Structural crack appears and widens
│     ├── Systems fail (emergency, communications)
│     └── Weather intensifies (storm → tsunami → acid)
│
├── RELATIONAL
│     ├── Physical distance in bed increases
│     ├── Conversations become confrontational
│     ├── Secrets revealed under pressure
│     └── Alliances shift (Uncle helps Dad → dies)
│
├── BODILY
│     ├── Sexual dysfunction (Dad)
│     ├── Alcoholism progression (Mom)
│     ├── Physical violence marks accumulate
│     └── Acid damage (Sis's finale state)
│
└── TEMPORAL
      ├── "Days" become uncertain
      ├── Memories intrude on present
      └── Post-destruction time fragments
```

### 6.2 Domestic Pressure Algorithm

```python
def calculate_domestic_pressure(scene):
    """Domestic scenes must always increase pressure"""

    pressure_factors = {
        'secrets_present': scene.count_secrets() * 2,
        'characters_in_space': scene.character_count * 1.5,
        'alcohol_present': 3 if scene.has_alcohol else 0,
        'technology_active': 2 if scene.home_ai_speaks else 0,
        'external_intrusion': 5 if scene.has_outsiders else 0
    }

    base_pressure = sum(pressure_factors.values())

    # Pressure never decreases
    global_pressure = max(base_pressure, PREVIOUS_SCENE_PRESSURE)

    # Threshold triggers system activation
    if global_pressure > COLLAPSE_THRESHOLD:
        trigger_home_protocol()

    return global_pressure
```

### 6.3 Family Dysfunction Cascade

| Initial State | Trigger | Cascade Effect |
|--------------|---------|----------------|
| Mom's New Son secret | Auntie mentions it | Dad learns → confrontation → police arrive |
| Son's explosives | Police flag Sis | Search → discovery → HOME activates |
| Dad's impotence | Can't perform with Love | Violence toward women → beaten return |
| Sis's career stagnation | Same roles offered | Performance trauma → show exploitation |

---

## 7. Diagnostic Questions

Answer YES/NO for structural validation:

**TEMPORAL INTEGRITY**
1. Does each major character occupy distinct temporal modes post-destruction?
2. Are pre-destruction "normal" scenes compressed relative to violence?
3. Is the cyclical structure indicated through casting/re-casting?

**VIOLENCE LOGIC**
4. Does violence escalate without regression throughout?
5. Does each communication failure produce corresponding violence?
6. Is institutional violence shown as equivalent to intimate violence?

**REALITY COHERENCE**
7. Are technology boundaries (glass, screens, VR) consistently present?
8. Do reality layers interpenetrate before collapse?
9. Is post-destruction reality status ambiguous for at least 3 characters?

**FAMILY DYNAMICS**
10. Does each family member fail to achieve stated goal?
11. Is parental agency shown as illusory?
12. Does survival function as continued suffering, not victory?

**SPECTACLE INTEGRATION**
13. Is the production apparatus (interviews, casting) shown post-destruction?
14. Does the survivor re-enter the system as performer?
15. Is private grief immediately converted to public content?

**Scoring:**
- All YES → Structure aligns with *Open View* narratological system
- Any NO → Deviation from established patterns (may be intentional)

---

## 8. Theoretical Correspondences

### 8.1 Narrative Theory Mapping

| Open View Concept | McKee | Aristotle | Brecht | Debord |
|-------------------|-------|-----------|--------|--------|
| HOME game rules | Inciting incident | Hamartia trigger | Alienation device | Spectacle logic |
| Family entropy | Progressive complications | Necessary action | Social gestus | Commodity form |
| Violence cascade | Climax | Catastrophe | Epic demonstration | Recuperation |
| Sis's survival | "Resolution" | — | Incomplete action | Star commodity |
| Cyclical restart | — | — | V-effekt | Eternal return of same |

### 8.2 Genre Correspondence

| Open View Element | Horror | Reality TV | Sci-Fi | Greek Tragedy |
|-------------------|--------|------------|--------|---------------|
| HOME as antagonist | Haunted house | Big Brother | HAL 9000 | Fate/Gods |
| Family destruction | Slasher logic | Elimination format | Dystopia trope | House of Atreus |
| Glass enclosure | Trap architecture | Confession booth | Colony ship | Theatrical space |
| Survivor interview | Final girl | Winner interview | Mission debrief | Messenger speech |

### 8.3 Medium-Specific Patterns

| Element | Film Treatment | Possible Game Adaptation | TV Series Adaptation |
|---------|---------------|-------------------------|---------------------|
| Timeline fragmentation | Parallel editing, match cuts | Player chooses POV character | Episode per character post-death |
| Violence | Unflinching duration | Player complicity | Network standards negotiation |
| Reality layers | Visual coding (color, aspect ratio) | Hub world vs. levels | Bottle episodes vs. expanded world |
| Production apparatus | Breaking fourth wall | Metatextual framing | In-show show-within-show |

---

## 9. Quick Reference Card

### Core Formula
```
DOMESTIC_DYSFUNCTION + EXTERNAL_CATALYST →
  VIOLENCE_CASCADE →
  TOTAL_DESTRUCTION →
  SURVIVOR_COMMODIFICATION →
  CYCLE_RESTART
```

### Character Goal Test
```
IF character.stated_goal ACHIEVED:
  THEN: immediately_reverse()
  OR: reveal_as_pyrrhic()
NEVER: allow_genuine_success
```

### Violence Progression
```
✓ Violence always escalates
✓ Failed communication → physical substitution
✓ Institutional and intimate violence treated equivalently
✗ NEVER de-escalate once blood drawn
✗ NEVER allow violence to produce intended result
```

### Reality Layer Rules
```
LAYER_RULE_1: Technology always mediates
LAYER_RULE_2: Glass protects nothing
LAYER_RULE_3: Post-destruction reality fragments per character
LAYER_RULE_4: Production apparatus absorbs all outcomes
```

### Entropy Indicators (Production Checklist)
```
□ Kitchen style has shifted from original
□ Structural crack visible
□ Weather worsening each exterior shot
□ Communication systems failing
□ Characters physically marked by violence
```

### Cyclical Structure Template
```
ITERATION[n]:
  Family[n] destroyed
  Survivor[n] extracted
  Survivor[n] cast in ITERATION[n+1] as supporting role
  New_Family[n+1] assembled
  GOTO ITERATION[n+1]
```

---

## Appendix A: Scene-Level Structure Map

### Act I Sequences (Domestic Surface)

| Scene | Location | Characters | Function |
|-------|----------|------------|----------|
| 1 | Kitchen | Mom, Auntie (O.S.) | Establish alcoholism, New Son subplot |
| 2 | Chinese Restaurant | Dad, Work-Friend | Establish affair desire, impotence hints |
| 3 | School Auditorium | Sis, Hamlet, trio | Establish rejection, performance drive |
| 4 | Training Room / Outer Front | Son, Leader, squad | Establish military training, Son-Leader bond |
| 5 | Law Office | Mom, Burly Attorney | New Son adoption legality |
| 6 | Beach | Dad, Jeeves | Emotional breakdown, escape fantasy |
| ... | ... | ... | ... |

### Act II Sequences (Pressure Escalation)

| Sequence | Function | Key Event |
|----------|----------|-----------|
| False Reconciliation | Temporary family cohesion | Beach day, sex scene, date night |
| Dad's Business Trip | Affair attempt/failure | Love introduced, violence toward women |
| Career Parallel | Sis's professional rejection | Casting calls, typecasting |
| Son-Leader Development | Romantic/conspiratorial bond | Sleepovers, explosive materials |

### Act III Sequences (Destruction Protocol)

| Sequence | Duration | Death Count | Key Mechanism |
|----------|----------|-------------|---------------|
| Game Activation | ~5 minutes story time | 1 (New Son) | Boiling |
| Police Confrontation | ~10 minutes | 3 (Mister Leader, Tough, Slime) | Random death + violence |
| Violence Cascade | ~15 minutes | 5+ (Dad, Son, Missus Leader, Sidekick, Uncle) | Mutual destruction |
| Survivor Emergence | ~5 minutes | Variable | Explosion + flooding |

---

## Appendix B: Motif Tracking

### Alcohol/Cocktails
- Present in nearly every Mom scene
- Functions as: self-medication, social lubricant, time marker, class signifier
- Specific drinks: martinis (Mom), Zombies (restaurant), cocktails (various)

### Glass/Transparency
- Home structure: glass complex
- Tunnel walls: glass separating from toxins
- Grow tank: glass containing New Son
- Windows: frilled curtains (50s), then removed
- Function: visibility without protection, mediation without safety

### Repetition/Doubling
- Mom ↔ Auntie (sisters, mirror choices)
- Love ↔ New Love ↔ Mom (Dad's attraction pattern)
- Son ↔ Leader (wrestling, symmetrical)
- Sis → Auntie (cyclical casting)
- Kitchen styles repeat across homes

### Technology/Mediation
- House AI (HOME)
- Grow tank + dreams
- VR military training
- Mobile messaging
- Interview/broadcast apparatus
- Makeup/repair technology

---

*Document generated from "2019-10-21 - open view - second draft.md". Principles extracted and formalized for narrative analysis and potential adaptation protocols.*

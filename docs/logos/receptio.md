# Receptio — Reception

The account of the constructed polis.

## Audience

The project serves three primary audiences:

### Practitioners (Screenwriters, Showrunners, Game Designers)
- **Need:** Actionable feedback grounded in craft theory, not generic advice
- **Value:** Protocol-driven analysis that scales from quick triage to deep craft review
- **Entry point:** CLI (`narratological analyze protocol script.fountain`) or Web dashboard

### Scholars (Narratologists, Film Studies, Comparative Literature)
- **Need:** Formalized frameworks for comparative analysis across traditions
- **Value:** 28 completed studies spanning Western and Eastern traditions, with traceable axioms
- **Entry point:** Core library (`narratological.load_compendium()`) or structured data exports

### Students (Learning craft through analysis)
- **Need:** Understandable explanations of narrative principles with concrete examples
- **Value:** Multi-perspective analysis through 9 analyst roles, each explaining through their lens
- **Entry point:** Web dashboard with study explorer

## Adoption Path

```
Primary Sources (txt)
    ↓ extraction
Completed Studies (md)
    ↓ modeling
Core Library (Pydantic models, algorithms)
    ↓ execution
CLI + API + Web
    ↓ delivery
Practitioner feedback, Scholar analysis, Student learning
```

## Current Reach

- **Public repository:** github.com/a-organvm/narratological-algorithmic-lenses
- **Part of:** ORGANVM eight-organ ecosystem (ORGAN-I Theory layer)
- **Downstream consumer:** `organvm-ii-poiesis/art-from--narratological-algorithmic-lenses`

## Feedback Mechanisms

- **GitHub Issues:** Bug reports, feature requests
- **Protocol output quality:** Practitioner feedback on analysis usefulness
- **Study completeness:** Scholar feedback on coverage gaps
- **Dashboard usability:** Student feedback on accessibility

## Success Metrics

| Metric | Current | Target (v1.0) |
|--------|---------|----------------|
| Studies completed | 28 | 50+ |
| Protocol levels | 7 | 7 (stable) |
| Analyst roles | 9 | 9 (stable) |
| CLI tests | 48 | 100+ |
| Web component tests | 1 (smoke) | 20+ |
| API tests | 5 | 20+ |
| Primary sources | 5 | 10+ |

"""Protocol Runner - coordinates and executes P1-P7 analysis protocols.

Runs appropriate combinations of generators and diagnostic suites based
on the selected protocol level.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from narratological.diagnostics.models import DiagnosticContext
from narratological.diagnostics.runner import DiagnosticRunner
from narratological.generators.beat_map import BeatMapReportGenerator
from narratological.generators.character_atlas import CharacterAtlasReportGenerator
from narratological.generators.coverage import CoverageReportGenerator
from narratological.generators.structural import StructuralReportGenerator
from narratological.models.protocol import ProtocolLevel, ProtocolSpec
from narratological.protocols.prompts import (
    build_market_positioning_prompt,
    build_mechanism_extraction_prompt,
    build_revision_roadmap_prompt,
    build_thematic_architecture_prompt,
    build_theoretical_correspondence_prompt,
    build_triage_prompt,
)
from narratological.protocols.registry import get_protocol

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script
    from narratological.models.report import (
        BeatMapReport,
        CharacterAtlasReport,
        CoverageReport,
        DiagnosticReport,
        StructuralReport,
    )


class ProtocolRunner:
    """Orchestrates execution of the P1-P7 protocol framework."""

    def __init__(self, provider: LLMProvider, compendium: Any = None):
        """Initialize the protocol runner.

        Args:
            provider: LLM provider for analysis tasks.
            compendium: Study compendium for framework analysis.
        """
        self.provider = provider
        self.compendium = compendium

    def run(self, script: Script, level: str | ProtocolLevel) -> dict[str, Any]:
        """Execute the specified analysis protocol on a script.

        Args:
            script: The parsed Script to analyze.
            level: The protocol level to run (e.g. 'P3' or ProtocolLevel.P3).

        Returns:
            Dict containing individual reports and the consolidated master Markdown.
        """
        spec = get_protocol(level)
        level = spec.level
        results: dict[str, Any] = {}
        markdown_sections: list[str] = []

        # P1-P7 documents mapping
        # 1. Coverage Report (abbreviated or full)
        if level in (ProtocolLevel.P1, ProtocolLevel.P5):
            # Abbreviated Coverage
            cov_gen = CoverageReportGenerator(self.provider)
            cov_report = cov_gen.generate(script, include_role_notes=False)
            results["coverage"] = cov_report
            markdown_sections.append(self._format_coverage_to_md(cov_report, abbreviated=True))
        elif level in (ProtocolLevel.P2, ProtocolLevel.P3, ProtocolLevel.P7):
            # Full Coverage
            cov_gen = CoverageReportGenerator(self.provider)
            cov_report = cov_gen.generate(script, include_role_notes=True)
            results["coverage"] = cov_report
            markdown_sections.append(self._format_coverage_to_md(cov_report, abbreviated=False))

        # 2. Beat Map
        if level == ProtocolLevel.P7:
            bm_gen = BeatMapReportGenerator(self.provider)
            bm_report = bm_gen.generate(script)
            results["beatmap"] = bm_report
            markdown_sections.append(self._format_beat_map_to_md(bm_report))

        # 3. Structural Analysis
        if level in (ProtocolLevel.P2, ProtocolLevel.P3, ProtocolLevel.P4, ProtocolLevel.P6, ProtocolLevel.P7):
            str_gen = StructuralReportGenerator(self.provider)
            str_report = str_gen.generate(script)
            results["structural"] = str_report
            markdown_sections.append(self._format_structural_to_md(str_report, abbreviated=(level == ProtocolLevel.P6)))

        # 4. Character Atlas
        if level in (ProtocolLevel.P3, ProtocolLevel.P7):
            ca_gen = CharacterAtlasReportGenerator(self.provider)
            ca_report = ca_gen.generate(script)
            results["character_atlas"] = ca_report
            markdown_sections.append(self._format_character_atlas_to_md(ca_report))

        # 5. Diagnostic Report
        if level in (ProtocolLevel.P2, ProtocolLevel.P3, ProtocolLevel.P4, ProtocolLevel.P7):
            diag_runner = DiagnosticRunner(self.provider, self.compendium)
            diag_context = DiagnosticContext.from_script(script)
            diag_report = diag_runner.run_all(diag_context)
            results["diagnostic"] = diag_report
            markdown_sections.append(self._format_diagnostic_to_md(diag_report))

        # Custom markdown documents generated via specific LLM prompts
        # 6. Triage Decision (P1)
        if level == ProtocolLevel.P1:
            prompt = build_triage_prompt(script)
            res = self.provider.complete(prompt)
            results["triage_decision"] = res.content
            markdown_sections.append(res.content)

        # 7. Market Positioning (P5, P7)
        if level in (ProtocolLevel.P5, ProtocolLevel.P7):
            prompt = build_market_positioning_prompt(script)
            res = self.provider.complete(prompt)
            results["market_positioning"] = res.content
            markdown_sections.append(res.content)

        # 8. Mechanism Extraction (P6)
        if level == ProtocolLevel.P6:
            prompt = build_mechanism_extraction_prompt(script)
            res = self.provider.complete(prompt)
            results["mechanism_extraction"] = res.content
            markdown_sections.append(res.content)

        # 9. Thematic Architecture (P4, P7)
        if level in (ProtocolLevel.P4, ProtocolLevel.P7):
            prompt = build_thematic_architecture_prompt(script)
            res = self.provider.complete(prompt)
            results["thematic_architecture"] = res.content
            markdown_sections.append(res.content)

        # 10. Theoretical Correspondence (P4, P6, P7)
        if level in (ProtocolLevel.P4, ProtocolLevel.P6, ProtocolLevel.P7):
            prompt = build_theoretical_correspondence_prompt(script)
            res = self.provider.complete(prompt)
            results["theoretical_correspondence"] = res.content
            markdown_sections.append(res.content)

        # 11. Revision Roadmap (P3, P7)
        if level in (ProtocolLevel.P3, ProtocolLevel.P7):
            prompt = build_revision_roadmap_prompt(script)
            res = self.provider.complete(prompt)
            results["revision_roadmap"] = res.content
            markdown_sections.append(res.content)

        # Combine everything
        combined = self._consolidate_markdown(script, spec, markdown_sections)
        results["combined_markdown"] = combined

        return results

    def _consolidate_markdown(self, script: Script, spec: ProtocolSpec, sections: list[str]) -> str:
        """Consolidate all generated markdown sections into a master report."""
        roles_str = ", ".join(r.value.upper() for r in spec.roles)
        docs_str = ", ".join(spec.documents)

        header = f"""# Narratological Analysis Report
## Protocol {spec.level}: {spec.name}

**Project / Title:** {script.title}
**Analytical Purpose:** {spec.purpose}
**Time Estimate:** {spec.time_estimate}
**Activated Roles:** {roles_str}
**Generated Documents:** {docs_str}

---
"""
        body = "\n\n---\n\n".join(sections)
        return header + "\n" + body

    def _format_coverage_to_md(self, report: CoverageReport, abbreviated: bool) -> str:
        """Format CoverageReport model to Markdown."""
        notes_section = ""
        if not abbreviated:
            notes_section = f"""
### Analyst Role Observations
* **First Reader:** {report.first_reader_notes or "N/A"}
* **Dramaturgist:** {report.dramaturgist_notes or "N/A"}
* **Narratologist:** {report.narratologist_notes or "N/A"}
* **Cinephile:** {report.cinephile_notes or "N/A"}
* **Rhetorician:** {report.rhetorician_notes or "N/A"}
* **Producer:** {report.producer_notes or "N/A"}
* **Academic:** {report.academic_notes or "N/A"}
* **Art Historian:** {report.art_historian_notes or "N/A"}
* **Aesthete:** {report.aesthete_notes or "N/A"}
"""

        strengths = "\n".join(f"- {s}" for s in report.strengths)
        weaknesses = "\n".join(f"- {w}" for w in report.weaknesses)
        opps = "\n".join(f"- {o}" for o in report.opportunities)
        comps = ", ".join(report.comparables)

        return f"""## Coverage Summary

**Title:** {report.title}
**Recommendation:** **{report.recommendation.value}**
**Logline:** {report.logline}

### Synopsis
{report.synopsis}

### Ratings (1-10 Scale)
| Dimension | Rating |
|-----------|--------|
| Premise | {report.premise_rating}/10 |
| Structure | {report.structure_rating}/10 |
| Character | {report.character_rating}/10 |
| Dialogue | {report.dialogue_rating}/10 |
| Originality | {report.originality_rating}/10 |
| Marketability | {report.marketability_rating}/10 |
| **Weighted Score** | **{report.overall_score():.2f}/10** |

### Key Strengths
{strengths}

### Key Weaknesses
{weaknesses}

### Opportunities
{opps}

### Comparable Titles
{comps}
{notes_section}
"""

    def _format_beat_map_to_md(self, report: BeatMapReport) -> str:
        """Format BeatMapReport model to Markdown."""
        entries = []
        for e in report.entries:
            connector = e.connector.value if e.connector else "—"
            entries.append(
                f"| {e.scene_number} | {e.slug} | {e.function.value} | {connector} | {e.tension}/10 | {e.summary} |"
            )

        entries_str = "\n".join(entries)

        return f"""## Scene-by-Scene Beat Map

**Total Scenes:** {report.total_scenes}
**Total Pages:** {report.total_pages or "N/A"}

| Scene # | Heading | Primary Function | Connector | Tension | Summary |
|---------|---------|------------------|-----------|---------|---------|
{entries_str}
"""

    def _format_structural_to_md(self, report: StructuralReport, abbreviated: bool) -> str:
        """Format StructuralReport model to Markdown."""
        acts = []
        for act in report.acts:
            events = ", ".join(act.key_events) if act.key_events else "None"
            acts.append(f"""
#### Act {act.number} (Scenes {act.start_scene}–{act.end_scene})
* **Percentage of Script:** {act.percentage:.1%}
* **Summary:** {act.summary}
* **Key Events:** {events}
""")

        acts_str = "\n".join(acts)

        if abbreviated:
            return f"""## Structural Analysis (Abbreviated)

**Structure Type:** {report.structure_type}
**Act Count:** {report.act_count}

{acts_str}
"""

        issues = "\n".join(f"- {i}" for i in report.structural_issues)

        return f"""## Structural Architecture

**Structure Type:** {report.structure_type}
**Act Count:** {report.act_count}

### Act Breakdown
{acts_str}

### Key Dramatic Turning Points
* **Opening Image:** Scene {report.opening_image or "N/A"}
* **Inciting Incident:** Scene {report.inciting_incident or "N/A"}
* **First Act Break:** Scene {report.first_act_break or "N/A"}
* **Midpoint:** Scene {report.midpoint or "N/A"}
* **All Is Lost:** Scene {report.all_is_lost or "N/A"}
* **Second Act Break:** Scene {report.second_act_break or "N/A"}
* **Climax:** Scene {report.climax or "N/A"}
* **Resolution:** Scene {report.resolution or "N/A"}
* **Closing Image:** Scene {report.closing_image or "N/A"}

### Pacing and Proportion Notes
{report.pacing_notes or "N/A"}

### Identified Structural Issues
{issues or "None"}
"""

    def _format_character_atlas_to_md(self, report: CharacterAtlasReport) -> str:
        """Format CharacterAtlasReport model to Markdown."""
        characters = []
        relationships = []

        for c in report.entries:
            arc_str = c.arc_type.value if c.arc_type else "N/A"
            characters.append(f"""
### {c.name} ({c.role})
* **Want (Conscious Goal):** {c.want or "N/A"}
* **Need (Unconscious Need):** {c.need or "N/A"}
* **Believed Lie:** {c.lie or "N/A"}
* **Learned Truth:** {c.truth or "N/A"}
* **Arc Type:** {arc_str}
* **Arc Description:** {c.arc_description}
""")
            for r in c.relationships:
                relationships.append(
                    f"- **{r.character_a}** & **{r.character_b}** ({r.relationship_type}): {r.description}"
                )

        chars_str = "\n".join(characters)
        # Deduplicate relationships since they might be listed on both characters
        relations_str = "\n".join(sorted(set(relationships)))

        return f"""## Character Atlas

{chars_str}

### Key Relationships and Dynamics
{relations_str or "None"}
"""

    def _format_diagnostic_to_md(self, report: DiagnosticReport) -> str:
        """Format DiagnosticReport model to Markdown."""
        issues = []
        for i in report.issues:
            issues.append(f"""
* **[{i.severity.value.upper()}] {i.description}**
  * **Category:** {i.category}
  * **Location:** {i.location or "Global"}
  * **Fix:** {i.recommendation}
  * **Framework Source:** {i.framework_source or "N/A"}
""")

        issues_str = "\n".join(issues)
        fixes_str = "\n".join(f"{i+1}. {fix}" for i, fix in enumerate(report.priority_fixes))

        return f"""## Diagnostic Report

### Structural Health Metrics
* **Causal Binding Ratio (BUT/THEREFORE):** {report.causal_binding_ratio:.1%} (Target: >80.0%)
* **Reorderability Score (Lower is better):** {report.reorderability_score:.1%}
* **Necessity Score (Higher is better):** {report.necessity_score:.1%}
* **Information Economy Score:** {report.information_economy_score:.1%}

**Overall Health Summary:** {report.overall_health}
* **Critical Issues:** {report.critical_count}
* **Warnings:** {report.warning_count}

### Priority Fixes List
{fixes_str or "None"}

### Detailed Diagnostics Issues
{issues_str or "No issues identified."}
"""

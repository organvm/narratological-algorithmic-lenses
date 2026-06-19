"""Tests for LLM orchestration helpers and script-doctor analysis."""

from narratological.llm import AnalysisOrchestrator, MockProvider
from narratological.llm.script_doctor import ScriptDoctorAnalyst
from narratological.models.analysis import (
    ArcClassification,
    BeatFunction,
    Character,
    ConnectorType,
    Scene,
    Script,
)
from narratological.models.analyst import ActivationLayer, AnalystContext
from narratological.models.report import BeatMapReport, CharacterAtlasReport
from narratological.models.study import Algorithm, Axiom, Category, Study


def make_study(study_id: str, creator: str, algorithm_name: str) -> Study:
    """Create a compact creator study for script-doctor tests."""
    return Study(
        id=study_id,
        creator=creator,
        work=f"{creator} Selected Work",
        category=Category.FILM,
        axioms=[
            Axiom(
                id=f"{study_id.upper()}-A0",
                name="Core Pressure",
                statement=f"{creator} treats pressure as structure.",
            )
        ],
        core_algorithms=[
            Algorithm(
                name=algorithm_name,
                purpose="Surface narrative pressure.",
                pseudocode="RETURN pressure",
            )
        ],
    )


def make_annotated_script() -> Script:
    """Create a script with enough annotations for non-LLM report generation."""
    return Script(
        title="Workbench Script",
        format="Feature",
        page_count=12,
        primary_genre="Drama",
        tone="Controlled",
        logline="An engineer learns to ask for help.",
        scenes=[
            Scene(
                number=1,
                slug="INT. LAB - NIGHT",
                summary="Ava hides a failed test from her team.",
                function=BeatFunction.SETUP,
                characters_present=["AVA", "LEE"],
                connector_to_next=ConnectorType.BUT,
                tension_level=4,
            ),
            Scene(
                number=2,
                slug="EXT. ROOF - DAWN",
                summary="Lee forces Ava to confront the cost of secrecy.",
                function=BeatFunction.CLIMAX,
                characters_present=["AVA", "LEE"],
                tension_level=8,
            ),
        ],
        characters=[
            Character(
                name="AVA",
                role="protagonist",
                description="A guarded engineer.",
                first_appearance=1,
                want="To complete the test alone",
                need="To trust her collaborators",
                arc_classification=ArcClassification.POSITIVE,
            ),
            Character(
                name="LEE",
                role="ally",
                description="A colleague who sees the hidden cost.",
                first_appearance=1,
            ),
        ],
    )


def test_script_doctor_builds_debate_prompt_and_returns_structured_result():
    """ScriptDoctorAnalyst should preserve pair metadata and request debate rounds."""
    provider = MockProvider()
    provider.set_response(
        "",
        structured_data={
            "pair": {
                "primary_id": "primary",
                "secondary_id": "secondary",
                "theme": "Pressure and release",
            },
            "dialogue": [
                {"creator": "Primary Creator", "feedback": "Tighten the pressure line."}
            ],
            "debate_rounds": [
                {"round": 1, "content": "The structure needs a sharper conflict."}
            ],
            "joint_recommendations": ["Compress the midpoint choice."],
            "creative_tension": ["Lyric ambiguity vs causal clarity"],
            "final_prescription": "Rewrite the midpoint as a forced public decision.",
        },
    )
    primary = make_study("primary", "Primary Creator", "Pressure Lens")
    secondary = make_study("secondary", "Secondary Creator", "Release Lens")
    context = AnalystContext(
        title="Pressure Draft",
        text="A guarded engineer hides a failed test.",
        genre="Drama",
        tone="Controlled",
        scene_summaries=["Ava hides the test.", "Lee confronts her."],
    )

    result = ScriptDoctorAnalyst(provider).analyze(
        context,
        primary,
        secondary,
        theme="Pressure and release",
        debate_mode=True,
    )

    call = provider.get_last_call()
    assert result.pair.primary_id == "primary"
    assert result.pair.secondary_id == "secondary"
    assert result.debate_rounds is not None
    assert result.final_prescription.startswith("Rewrite the midpoint")
    assert call is not None
    assert call["method"] == "complete_structured"
    assert "DEBATE TASK" in call["prompt"]
    assert "Primary Creator" in call["system"]
    assert "Pressure Lens" in call["system"]
    assert "Release Lens" in call["system"]


def test_analysis_orchestrator_returns_partial_results_without_provider():
    """Full analysis should keep successful algorithmic reports when LLM-only reports fail."""
    script = make_annotated_script()

    results = AnalysisOrchestrator().full_analysis(
        script,
        activation_layer=ActivationLayer.ESSENTIAL,
    )

    assert isinstance(results["beat_map"], BeatMapReport)
    assert results["beat_map"].total_scenes == 2
    assert isinstance(results["character_atlas"], CharacterAtlasReport)
    assert results["character_atlas"].protagonist == "AVA"
    assert "structural report requires an LLM provider" in results["structural_error"]
    assert "coverage report requires an LLM provider" in results["coverage_error"]
    assert results["multi_role"].role_count() == len(ActivationLayer.ESSENTIAL.roles)

"""API routes for script/narrative analysis."""

from typing import Any, NoReturn

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


class SceneAnalysisRequest(BaseModel):
    """Request model for scene analysis."""

    text: str = Field(..., min_length=1, max_length=100000, description="Scene text to analyze")
    framework: str | None = Field(None, description="Framework/study to apply")


class SceneAnalysisResponse(BaseModel):
    """Response model for scene analysis."""

    function: str = Field(..., description="Primary beat function")
    secondary_function: str | None = Field(None, description="Secondary function")
    tension_level: int = Field(..., ge=1, le=10, description="Tension level")
    connector_suggested: str = Field(..., description="Suggested connector to next scene")
    notes: str = Field(..., description="Analysis notes")


class ScriptUploadRequest(BaseModel):
    """Request model for script upload."""

    title: str = Field(..., min_length=1, max_length=255, description="Script title")
    content: str = Field(..., min_length=1, max_length=5000000, description="Script content")
    format: str = Field("Feature", min_length=1, max_length=50, description="Script format")


class AnalysisStatusResponse(BaseModel):
    """Response model for analysis status."""

    status: str = Field(..., description="Analysis status")
    progress: float = Field(..., ge=0, le=1, description="Progress (0-1)")
    message: str | None = Field(None, description="Status message")


class NotImplementedResponse(BaseModel):
    """Structured response payload for unimplemented endpoints."""

    status: str = Field("not_implemented", description="Endpoint implementation status")
    code: str = Field("ANALYSIS_NOT_IMPLEMENTED", description="Machine-readable error code")
    message: str = Field(..., description="User-facing explanation")
    planned: str = Field(..., description="Planned implementation area")


def _raise_not_implemented(message: str, planned: str) -> NoReturn:
    """Raise a standardized 501 error payload."""
    raise HTTPException(
        status_code=501,
        detail=NotImplementedResponse(
            status="not_implemented",
            code="ANALYSIS_NOT_IMPLEMENTED",
            message=message,
            planned=planned,
        ).model_dump(),
    )


NOT_IMPLEMENTED_RESPONSES: dict[int | str, dict[str, Any]] = {
    501: {
        "model": NotImplementedResponse,
        "description": "Endpoint exists but implementation is not available yet.",
    }
}


@router.post("/scene", responses=NOT_IMPLEMENTED_RESPONSES)
async def analyze_scene(request: SceneAnalysisRequest) -> dict[str, Any]:
    """Analyze a single scene.

    Note: Full analysis requires LLM integration. This endpoint
    returns a placeholder response showing the expected structure.
    """
    _ = request
    _raise_not_implemented(
        message="Full scene analysis requires LLM orchestration and script context.",
        planned="scene-analysis-pipeline",
    )


@router.post("/script", responses=NOT_IMPLEMENTED_RESPONSES)
async def upload_script(request: ScriptUploadRequest) -> dict[str, Any]:
    """Upload a script for analysis.

    Returns an analysis ID that can be used to track progress
    and retrieve results.
    """
    # In a full implementation, this would:
    # 1. Parse and validate the script
    # 2. Queue it for analysis
    # 3. Return an analysis ID

    _ = request
    _raise_not_implemented(
        message="Script upload and analysis queueing are not implemented yet.",
        planned="script-ingestion-and-job-queue",
    )


@router.get("/script/{analysis_id}/status", responses=NOT_IMPLEMENTED_RESPONSES)
async def get_analysis_status(analysis_id: str) -> AnalysisStatusResponse:
    """Get the status of a script analysis."""
    _ = analysis_id
    _raise_not_implemented(
        message="Analysis status tracking is not implemented yet.",
        planned="analysis-status-tracking",
    )


@router.get("/script/{analysis_id}/reports", responses=NOT_IMPLEMENTED_RESPONSES)
async def get_analysis_reports(analysis_id: str) -> dict[str, Any]:
    """Get all available reports for a completed analysis."""
    _ = analysis_id
    _raise_not_implemented(
        message="Analysis reports are not available until the analysis pipeline is implemented.",
        planned="report-generation-pipeline",
    )


@router.get("/script/{analysis_id}/reports/coverage", responses=NOT_IMPLEMENTED_RESPONSES)
async def get_coverage_report(analysis_id: str) -> dict[str, Any]:
    """Get the coverage report for a completed analysis."""
    _ = analysis_id
    _raise_not_implemented(
        message="Coverage report generation is not implemented yet.",
        planned="coverage-report-generator",
    )


@router.get("/script/{analysis_id}/reports/beat-map", responses=NOT_IMPLEMENTED_RESPONSES)
async def get_beat_map(analysis_id: str) -> dict[str, Any]:
    """Get the beat map for a completed analysis."""
    _ = analysis_id
    _raise_not_implemented(
        message="Beat map generation is not implemented yet.",
        planned="beat-map-generator",
    )


@router.get("/script/{analysis_id}/reports/structural", responses=NOT_IMPLEMENTED_RESPONSES)
async def get_structural_report(analysis_id: str) -> dict[str, Any]:
    """Get the structural analysis report."""
    _ = analysis_id
    _raise_not_implemented(
        message="Structural analysis reporting is not implemented yet.",
        planned="structural-report-generator",
    )


@router.get("/script/{analysis_id}/reports/character-atlas", responses=NOT_IMPLEMENTED_RESPONSES)
async def get_character_atlas(analysis_id: str) -> dict[str, Any]:
    """Get the character atlas for a completed analysis."""
    _ = analysis_id
    _raise_not_implemented(
        message="Character atlas generation is not implemented yet.",
        planned="character-atlas-generator",
    )


class ScriptDoctorRequest(BaseModel):
    """Request model for Script Doctor consultation."""

    content: str = Field(..., min_length=1, max_length=5000000, description="Script content (Fountain or text)")
    primary_id: str = Field(..., min_length=1, max_length=100, description="ID of the primary study")
    secondary_id: str = Field(..., min_length=1, max_length=100, description="ID of the secondary study")
    debate_mode: bool = Field(False, description="Enable exhaustive debate mode")
    provider: str = Field("ollama", min_length=1, max_length=50, description="LLM provider")
    model: str | None = Field(None, description="LLM model")


@router.post("/script-doctor")
async def script_doctor_consultation(request: ScriptDoctorRequest) -> dict[str, Any]:
    """Perform a collaborative 'Script Doctor' analysis using creator pairs."""
    from narratological.llm.providers import get_provider
    from narratological.llm.script_doctor import ScriptDoctorAnalyst
    from narratological.loader import load_compendium
    from narratological.models.analyst import AnalystContext
    from narratological.parsers.fountain import parse_fountain

    # Load data
    compendium = load_compendium()
    s1 = compendium.get_study(request.primary_id)
    s2 = compendium.get_study(request.secondary_id)

    if not s1 or not s2:
        raise HTTPException(
            status_code=404,
            detail=f"One or both studies not found: {request.primary_id}, {request.secondary_id}"
        )

    # Parse script
    try:
        script = parse_fountain(request.content)
        context = AnalystContext.from_script(script)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse script: {e}") from e

    # Get provider and analyst
    try:
        llm = get_provider(request.provider, model=request.model)
        doctor = ScriptDoctorAnalyst(llm)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Initialization failed: {e}") from e

    # Perform consultation
    try:
        result = doctor.analyze(context, s1, s2, debate_mode=request.debate_mode)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}") from e


@router.get("/frameworks")
async def list_analysis_frameworks() -> list[dict[str, Any]]:
    """List available frameworks for analysis."""
    from narratological.loader import load_compendium

    compendium = load_compendium()

    return [
        {
            "id": s.id,
            "creator": s.creator,
            "category": s.category.value,
            "algorithm_count": len(s.core_algorithms),
            "question_count": len(s.diagnostic_questions),
        }
        for s in compendium.studies.values()
    ]

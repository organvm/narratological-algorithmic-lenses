"""API routes for script/narrative analysis."""

from collections import Counter
from typing import Any, Literal, NoReturn

from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, Field

from narratological_api.auth import (
    AccessTier,
    ApiAccount,
    QuotaExceededError,
    QuotaSnapshot,
    TierEntitlements,
    quota_store,
    require_api_key,
)

router = APIRouter()
API_ACCOUNT_DEPENDENCY = Depends(require_api_key)

CORE_92_SUITE_ID = "narratological-92"
CORE_92_ALGORITHM_TARGET = 92
CORE_92_STUDY_IDS = (
    "bergman",
    "tarkovsky",
    "pixar",
    "zelda",
    "alan-moore",
    "morrison",
    "final-fantasy",
    "kirby-new-gods",
    "tolkien",
    "ovid-metamorphoses",
    "gaiman-sandman",
    "tarantino",
    "warren-ellis",
    "david-lynch",
)


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


class NarrativeSuiteRequest(BaseModel):
    """Request model for the commercial narrative-analysis suite endpoint."""

    title: str = Field(..., min_length=1, description="Script or project title")
    content: str = Field(..., min_length=1, description="Script content, preferably Fountain")
    format: str = Field("Feature", description="Script format")
    include_algorithm_details: bool = Field(
        False,
        description="Include selected algorithm names, purposes, inputs, and outputs",
    )


class NarrativeInputSummary(BaseModel):
    """Lightweight parse summary for the submitted script."""

    title: str
    format: str
    characters: int
    words: int
    estimated_pages: int
    scene_count: int
    named_character_count: int


class NarrativeSuiteCatalog(BaseModel):
    """Metadata for the 92-algorithm commercial suite."""

    suite_id: str
    contracted_algorithm_count: int
    catalog_algorithm_count: int
    selected_algorithm_count: int
    full_suite: bool
    capped_reason: str | None = None


class NarrativeSuiteStudySummary(BaseModel):
    """Per-study summary of selected algorithms."""

    study_id: str
    creator: str
    category: str
    selected_algorithm_count: int


class NarrativeSuiteAlgorithmCard(BaseModel):
    """Public metadata for one selected algorithm."""

    study_id: str
    study_creator: str
    name: str
    purpose: str
    inputs: list[str]
    outputs: list[str]


class NarrativeSuiteResponse(BaseModel):
    """Response from the sample 92-algorithm analysis endpoint."""

    analysis_id: str
    status: Literal["preview", "ready"]
    tier: AccessTier
    entitlements: TierEntitlements
    quota: QuotaSnapshot
    input: NarrativeInputSummary
    suite: NarrativeSuiteCatalog
    studies: list[NarrativeSuiteStudySummary]
    algorithms: list[NarrativeSuiteAlgorithmCard] = Field(default_factory=list)
    next_step: str


def _word_count(text: str) -> int:
    """Count rough word tokens without pulling in NLP dependencies."""
    return len([token for token in text.replace("\n", " ").split(" ") if token.strip()])


def _select_core_92_algorithms() -> tuple[list[Any], int]:
    """Select the stable commercial suite from the growing compendium.

    The source compendium may contain more than the original commercial contract.
    This endpoint preserves the public 92-algorithm product shape by taking a
    deterministic slice from the 14 legacy studies.
    """
    from narratological.algorithms import get_registry

    registry = get_registry()
    catalog_algorithms = []
    for study_id in CORE_92_STUDY_IDS:
        catalog_algorithms.extend(registry.list_by_study(study_id))
    return catalog_algorithms[:CORE_92_ALGORITHM_TARGET], len(catalog_algorithms)


def _build_study_summaries(algorithms: list[Any]) -> list[NarrativeSuiteStudySummary]:
    """Build per-study algorithm counts for the selected suite."""
    from narratological.loader import load_compendium

    compendium = load_compendium()
    counts = Counter(algo.study_id for algo in algorithms)
    summaries = []
    for study_id in CORE_92_STUDY_IDS:
        selected_count = counts.get(study_id, 0)
        if selected_count == 0:
            continue
        study = compendium.get_study(study_id)
        creator = study.creator if study else study_id
        category = study.category.value if study else "Unknown"
        summaries.append(
            NarrativeSuiteStudySummary(
                study_id=study_id,
                creator=creator,
                category=category,
                selected_algorithm_count=selected_count,
            )
        )
    return summaries


def _build_algorithm_cards(algorithms: list[Any]) -> list[NarrativeSuiteAlgorithmCard]:
    """Build public algorithm metadata for response payloads."""
    return [
        NarrativeSuiteAlgorithmCard(
            study_id=algo.study_id,
            study_creator=algo.study_creator,
            name=algo.name,
            purpose=algo.purpose,
            inputs=algo.inputs,
            outputs=algo.outputs,
        )
        for algo in algorithms
    ]


def _build_analysis_id(account: ApiAccount, request: NarrativeSuiteRequest) -> str:
    """Create a deterministic, non-secret analysis identifier."""
    import hashlib

    source = f"{account.key_fingerprint}:{request.title}:{request.content}"
    return hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]


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


@router.post("/narrative-suite", response_model=NarrativeSuiteResponse)
async def analyze_with_narrative_suite(
    request: NarrativeSuiteRequest,
    response: Response,
    account: ApiAccount = API_ACCOUNT_DEPENDENCY,
) -> NarrativeSuiteResponse:
    """Run the gated 92-algorithm narrative-analysis sample endpoint.

    The current implementation exposes the suite manifest, input parse summary,
    and tier gate that downstream async LLM execution will use. It intentionally
    avoids provider calls so integrations can test billing/quota behavior without
    requiring Anthropic or OpenAI credentials.
    """
    from narratological.parsers.fountain import parse_fountain

    entitlements = account.entitlements
    if len(request.content) > entitlements.max_input_chars:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail={
                "code": "INPUT_TOO_LARGE",
                "message": (
                    f"{entitlements.label} allows up to "
                    f"{entitlements.max_input_chars} characters per request."
                ),
                "tier": account.tier.value,
                "max_input_chars": entitlements.max_input_chars,
            },
        )

    try:
        quota = quota_store.consume(account)
    except QuotaExceededError as e:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={
                "code": "MONTHLY_QUOTA_EXCEEDED",
                "message": "Monthly narrative-suite quota exhausted for this API key.",
                "quota": e.snapshot.model_dump(mode="json"),
            },
        ) from e

    response.headers["X-Quota-Limit"] = str(quota.limit)
    response.headers["X-Quota-Used"] = str(quota.used)
    response.headers["X-Quota-Remaining"] = str(quota.remaining)
    response.headers["X-Quota-Period"] = quota.period

    script = parse_fountain(request.content).model_copy(
        update={"title": request.title, "format": request.format}
    )
    selected_suite, catalog_count = _select_core_92_algorithms()
    tier_algorithm_limit = min(entitlements.algorithm_limit, CORE_92_ALGORITHM_TARGET)
    selected_algorithms = selected_suite[:tier_algorithm_limit]
    full_suite = entitlements.full_suite and len(selected_algorithms) >= CORE_92_ALGORITHM_TARGET

    capped_reason = None
    if catalog_count > CORE_92_ALGORITHM_TARGET:
        capped_reason = (
            "The source catalog contains additional algorithms; this endpoint caps "
            "the commercial suite at the contracted 92-algorithm product shape."
        )
    if not full_suite:
        capped_reason = (
            f"{entitlements.label} exposes a {tier_algorithm_limit}-algorithm preview. "
            "Upgrade to Creator or Studio for the full suite."
        )

    include_details = request.include_algorithm_details or not full_suite
    algorithm_cards = _build_algorithm_cards(selected_algorithms) if include_details else []

    status_value: Literal["preview", "ready"] = "ready" if full_suite else "preview"

    return NarrativeSuiteResponse(
        analysis_id=_build_analysis_id(account, request),
        status=status_value,
        tier=account.tier,
        entitlements=entitlements,
        quota=quota,
        input=NarrativeInputSummary(
            title=request.title,
            format=request.format,
            characters=len(request.content),
            words=_word_count(request.content),
            estimated_pages=script.page_count or 1,
            scene_count=script.scene_count or 0,
            named_character_count=len(script.characters),
        ),
        suite=NarrativeSuiteCatalog(
            suite_id=CORE_92_SUITE_ID,
            contracted_algorithm_count=CORE_92_ALGORITHM_TARGET,
            catalog_algorithm_count=catalog_count,
            selected_algorithm_count=len(selected_algorithms),
            full_suite=full_suite,
            capped_reason=capped_reason,
        ),
        studies=_build_study_summaries(selected_algorithms),
        algorithms=algorithm_cards,
        next_step=(
            "Use this gated response as the synchronous integration target; production "
            "LLM execution can enqueue the returned suite selection behind the same key "
            "and quota gate."
        ),
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

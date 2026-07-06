"""API routes for diagnostic tests."""

from typing import Any

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

router = APIRouter()


class CausalBindingRequest(BaseModel):
    """Request model for causal binding analysis."""

    scenes: list[dict[str, Any]] = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="List of scenes with connectors",
    )


class CausalBindingResponse(BaseModel):
    """Response model for causal binding analysis."""

    total_scenes: int = Field(..., description="Total scenes analyzed")
    causal_count: int = Field(..., description="BUT/THEREFORE count")
    episodic_count: int = Field(..., description="AND THEN count")
    binding_ratio: float = Field(..., ge=0, le=1, description="Causal binding ratio")
    target_met: bool = Field(..., description="Whether target ratio is met")
    weak_links: list[int] = Field(..., description="Scene numbers with weak links")


class DiagnosticResultItem(BaseModel):
    """A single diagnostic test result."""

    question_id: str = Field(..., description="Diagnostic question ID")
    question: str = Field(..., description="The diagnostic question")
    valid_if: str = Field(..., description="Validity criteria")
    passed: bool | None = Field(None, description="Whether test passed")
    notes: str | None = Field(None, description="Diagnostic notes")


@router.get("/frameworks/{study_id}/questions")
async def get_diagnostic_questions(study_id: str) -> list[dict[str, Any]]:
    """Get diagnostic questions for a specific framework."""
    from narratological.loader import load_study

    try:
        study = load_study(study_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

    return [q.model_dump() for q in study.diagnostic_questions]


@router.post("/causal-binding")
async def analyze_causal_binding(
    request: CausalBindingRequest,
    target: float = Query(0.80, ge=0, le=1, description="Target ratio"),
) -> dict[str, Any]:
    """Analyze causal binding in a sequence of scenes.

    Calculates the ratio of causal connectors (BUT/THEREFORE)
    to episodic connectors (AND THEN).
    """
    causal = 0
    episodic = 0
    weak_links = []

    for i, scene in enumerate(request.scenes):
        connector = scene.get("connector", "").upper()
        if connector in ("BUT", "THEREFORE"):
            causal += 1
        elif connector == "AND THEN":
            episodic += 1
            weak_links.append(scene.get("number", i + 1))

    total = causal + episodic
    ratio = causal / total if total > 0 else 0.0

    return CausalBindingResponse(
        total_scenes=len(request.scenes),
        causal_count=causal,
        episodic_count=episodic,
        binding_ratio=ratio,
        target_met=ratio >= target,
        weak_links=weak_links,
    ).model_dump()


@router.get("/metrics")
async def get_diagnostic_metrics() -> dict[str, Any]:
    """Get descriptions of all diagnostic metrics."""
    return {
        "causal_binding_ratio": {
            "name": "Causal Binding Ratio",
            "description": "Ratio of BUT/THEREFORE to AND THEN connectors",
            "target": 0.80,
            "interpretation": "Higher is better; indicates strong cause-effect structure",
        },
        "reorderability_score": {
            "name": "Reorderability Score",
            "description": "Percentage of scenes that could be reordered",
            "target": 0.10,
            "interpretation": "Lower is better; indicates scenes are causally linked",
        },
        "necessity_score": {
            "name": "Necessity Score",
            "description": "Percentage of scenes that are strictly necessary",
            "target": 0.95,
            "interpretation": "Higher is better; indicates no filler scenes",
        },
        "information_economy": {
            "name": "Information Economy Score",
            "description": "Efficiency of information delivery",
            "target": 0.80,
            "interpretation": "Higher is better; no wasted exposition",
        },
    }


@router.post("/run/{study_id}")
async def run_framework_diagnostics(
    study_id: str,
    analysis_id: str = Query(..., description="Analysis ID to diagnose"),
) -> dict[str, Any]:
    """Run all diagnostic questions from a framework against an analysis.

    Requires a completed script analysis.
    """
    from narratological.loader import load_study

    try:
        study = load_study(study_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

    # In a full implementation, this would run each diagnostic
    # against the analyzed script

    return {
        "study_id": study_id,
        "analysis_id": analysis_id,
        "status": "pending",
        "message": "Full diagnostic requires completed script analysis",
        "questions_count": len(study.diagnostic_questions),
        "questions": [
            DiagnosticResultItem(
                question_id=q.id,
                question=q.question,
                valid_if=q.valid_if,
                passed=None,
                notes="Requires analysis data",
            ).model_dump()
            for q in study.diagnostic_questions
        ],
    }


@router.get("/all-questions")
async def get_all_diagnostic_questions(
    category: str | None = Query(None, description="Filter by category"),
) -> list[dict[str, Any]]:
    """Get all diagnostic questions from all studies."""
    from narratological.loader import load_compendium
    from narratological.models.study import Category

    compendium = load_compendium()

    if category:
        try:
            cat = Category(category)
            studies = compendium.get_studies_by_category(cat)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid category: {category}",
            ) from None
    else:
        studies = list(compendium.studies.values())

    results = []
    for study in studies:
        for q in study.diagnostic_questions:
            results.append({
                "study_id": study.id,
                "study_creator": study.creator,
                "category": study.category.value,
                "question_id": q.id,
                "question": q.question,
                "valid_if": q.valid_if,
            })

    return results

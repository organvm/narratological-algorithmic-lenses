"""MCP server for Narratological Algorithmic Lenses.

Exposes script diagnostics, script doctoring, and compendium search
as standardized tools for AI agents.
"""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from narratological.diagnostics.models import DiagnosticContext
from narratological.diagnostics.runner import create_diagnostic_runner
from narratological.llm.providers import get_provider
from narratological.llm.script_doctor import ScriptDoctorAnalyst
from narratological.loader import load_compendium
from narratological.models.analyst import AnalystContext
from narratological.parsers.fountain import parse_fountain

# Initialize FastMCP server
mcp = FastMCP("Narratological")

@mcp.tool()
def get_available_studies() -> list[dict[str, str]]:
    """List all available narratological studies in the compendium."""
    compendium = load_compendium()
    return [
        {
            "id": s.id,
            "creator": s.creator,
            "work": s.work,
            "category": s.category.value
        }
        for s in compendium.studies.values()
    ]

@mcp.tool()
def search_axioms(query: str) -> list[dict[str, Any]]:
    """Search for foundational narrative principles (axioms) across all studies."""
    compendium = load_compendium()
    results = compendium.search_axioms(query)
    return [
        {
            "study_id": study_id,
            "axiom_id": axiom.id,
            "name": axiom.name,
            "statement": axiom.statement
        }
        for study_id, axiom in results
    ]

@mcp.tool()
def diagnose_script(
    script_content: str,
    title: str = "Untitled Script",
    provider: str = "ollama",
    model: str | None = None
) -> dict[str, Any]:
    """Perform a full structural diagnostic on a script.

    Checks for Causal Binding, Reorderability, and Scene Necessity.
    Supports Fountain and raw text formats.
    """
    # Parse script
    script = parse_fountain(script_content)
    script.title = title

    # Initialize provider and runner
    llm = get_provider(provider, model=model)
    runner = create_diagnostic_runner(llm)

    # Run analysis
    context = DiagnosticContext.from_script(script)
    report = runner.run_all(context)

    return report.model_dump()

@mcp.tool()
def consult_script_doctor(
    script_content: str,
    primary_study_id: str,
    secondary_study_id: str,
    debate_mode: bool = False,
    provider: str = "ollama",
    model: str | None = None
) -> dict[str, Any]:
    """Consult a pair of master creators for collaborative feedback on a script.

    Example pairs: 'tarkovsky' & 'bergman', 'pixar' & 'tarantino', 'aristotle' & 'larry-david'.
    Set debate_mode=True for an exhaustive dialectical exchange.
    """
    # Load data
    compendium = load_compendium()
    s1 = compendium.get_study(primary_study_id)
    s2 = compendium.get_study(secondary_study_id)

    if not s1 or not s2:
        return {"error": f"One or both studies not found: {primary_study_id}, {secondary_study_id}"}

    # Parse script
    script = parse_fountain(script_content)
    context = AnalystContext.from_script(script)

    # Initialize doctor
    llm = get_provider(provider, model=model)
    doctor = ScriptDoctorAnalyst(llm)

    # Perform consultation
    result = doctor.analyze(context, s1, s2, debate_mode=debate_mode)

    return result.model_dump()

def main():
    """Entry point for the MCP server."""
    mcp.run()

if __name__ == "__main__":
    main()

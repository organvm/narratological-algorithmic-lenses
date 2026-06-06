"""Loader for narratological algorithm studies.

Provides functions to load studies from the unified JSON compendium
or individual study files.
"""

from __future__ import annotations

import json
from importlib import resources
from pathlib import Path
from typing import TYPE_CHECKING

from narratological.models.study import Compendium, Study

if TYPE_CHECKING:
    from os import PathLike


import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from os import PathLike


def _get_compendium_path() -> Path | None:
    """Resolve the path to the unified compendium.

    Priority:
    1. NARRATOLOGICAL_COMPENDIUM env var
    2. Local development path (specs/03-structured-data/...)
    3. Package resource (bundled JSON)
    """
    # 1. Check environment variable
    env_path = os.environ.get("NARRATOLOGICAL_COMPENDIUM")
    if env_path:
        p = Path(env_path)
        if p.exists():
            return p

    # 2. Check for local development path relative to this file
    # This works when running from the repo root
    dev_path = Path(__file__).parent.parent.parent.parent / "specs/03-structured-data/narratological-algorithms-unified.json"
    if dev_path.exists():
        return dev_path

    # 3. Check for bundled resource
    try:
        resource = resources.files("narratological").joinpath(
            "data/narratological-algorithms-unified.json"
        )
        if resource.is_file():
            # Return as a Path object if possible, though resources.files may return a Traversable
            return Path(str(resource))
    except (ImportError, AttributeError):
        pass

    return None


def load_compendium(path: str | PathLike[str] | None = None) -> Compendium:
    """Load the complete narratological algorithm compendium.

    Args:
        path: Explicit path to the unified JSON file. If None, uses automatic resolution.

    Returns:
        Compendium object containing all studies and cross-references.

    Raises:
        FileNotFoundError: If the compendium file cannot be found.
        ValidationError: If the JSON doesn't match the expected schema.
    """
    file_path: Path | None = Path(path) if path else _get_compendium_path()

    if file_path is None or not Path(file_path).exists():
        raise FileNotFoundError(
            "Could not find narratological-algorithms-unified.json. "
            "Set NARRATOLOGICAL_COMPENDIUM environment variable or ensure "
            "the file is present in the expected locations."
        )

    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    return Compendium.model_validate(data)


def load_study(study_id: str, compendium_path: str | PathLike[str] | None = None) -> Study:
    """Load a single study by ID.

    Args:
        study_id: The study identifier (e.g., 'bergman', 'zelda').
        compendium_path: Path to unified JSON. If None, uses default.

    Returns:
        Study object for the requested study.

    Raises:
        KeyError: If the study ID is not found.
        FileNotFoundError: If the compendium cannot be found.
    """
    compendium = load_compendium(compendium_path)
    study = compendium.get_study(study_id)

    if study is None:
        available = ", ".join(compendium.list_study_ids())
        raise KeyError(
            f"Study '{study_id}' not found. Available studies: {available}"
        )

    return study


def load_study_from_file(path: str | PathLike[str]) -> Study:
    """Load a study from an individual JSON file.

    Args:
        path: Path to the study JSON file.

    Returns:
        Study object.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValidationError: If the JSON doesn't match the expected schema.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return Study.model_validate(data)


def list_available_studies(compendium_path: str | PathLike[str] | None = None) -> list[str]:
    """List all available study IDs.

    Args:
        compendium_path: Path to unified JSON. If None, uses default.

    Returns:
        List of study IDs.
    """
    compendium = load_compendium(compendium_path)
    return compendium.list_study_ids()


def get_study_summary(compendium_path: str | PathLike[str] | None = None) -> list[dict[str, str]]:
    """Get a summary of all available studies.

    Returns:
        List of dicts with id, creator, work, category for each study.
    """
    compendium = load_compendium(compendium_path)
    return [
        {
            "id": study.id,
            "creator": study.creator,
            "work": study.work,
            "category": study.category.value,
            "axiom_count": str(len(study.axioms)),
            "algorithm_count": str(len(study.core_algorithms)),
        }
        for study in compendium.studies.values()
    ]

"""Tests for study-to-Markdown validation."""

from narratological.models.study import (
    Algorithm,
    Axiom,
    Category,
    DiagnosticQuestion,
    HierarchyLevel,
    StructuralHierarchy,
    Study,
)
from narratological.validation import ValidationIssue, ValidationReport, validate_study


def make_study() -> Study:
    """Create a compact study fixture for validation tests."""
    return Study(
        id="ada-writer",
        creator="Ada Writer",
        work="The Test Draft",
        category=Category.FILM,
        axioms=[
            Axiom(
                id="AW-A0",
                name="Memory Echo",
                statement="Every image should return under pressure.",
            )
        ],
        structural_hierarchy=StructuralHierarchy(
            levels=[
                HierarchyLevel(
                    level=1,
                    name="Nested Echo",
                    description="A repeating image structure.",
                )
            ]
        ),
        core_algorithms=[
            Algorithm(
                name="Memory Algorithm",
                purpose="Track recursive images.",
                pseudocode="RETURN echoes",
            )
        ],
        diagnostic_questions=[
            DiagnosticQuestion(
                id="Q1",
                question='Does "memory" recur?',
                valid_if="The image returns with changed meaning.",
            )
        ],
    )


def test_validate_study_accepts_synchronized_markdown(tmp_path):
    """Matching Markdown should produce a valid report with no warnings."""
    markdown = tmp_path / "ada-writer.md"
    markdown.write_text(
        """# Ada Writer - The Test Draft

## Axioms
AW-A0: Every image should return under pressure.

## Core Algorithms
### Memory
Track recursive images through the draft.

## Structural Hierarchy
Nested Echo

## Diagnostic Questions
Does “memory” recur?
""",
        encoding="utf-8",
    )

    report = validate_study(make_study(), markdown)

    assert report.is_valid is True
    assert report.errors == []
    assert report.warnings == []


def test_validate_study_reports_missing_markdown_as_error(tmp_path):
    """A missing Markdown source should fail validation, not just warn."""
    missing = tmp_path / "missing.md"

    report = validate_study(make_study(), missing)

    assert report.is_valid is False
    assert len(report.errors) == 1
    assert report.errors[0].field == "markdown_file"
    assert "not found" in report.errors[0].message


def test_validate_study_collects_content_mismatches_as_warnings(tmp_path):
    """Content mismatches should be warnings so a report can list all drift at once."""
    markdown = tmp_path / "ada-writer.md"
    markdown.write_text(
        """# Different Creator

## Axioms
No matching IDs here.

## Notes
This document intentionally omits the synchronized structure.
""",
        encoding="utf-8",
    )

    report = validate_study(make_study(), markdown)

    assert report.is_valid is True
    fields = {issue.field for issue in report.warnings}
    assert fields == {
        "creator",
        "axioms",
        "core_algorithms",
        "structural_hierarchy",
        "diagnostic_questions",
    }
    assert {issue.item_id for issue in report.warnings if issue.item_id} == {
        "AW-A0",
        "Memory Algorithm",
        "Nested Echo",
        "Q1",
    }


def test_validation_report_properties_split_errors_and_warnings(tmp_path):
    """ValidationReport convenience properties should classify issue severity."""
    report = ValidationReport(
        study_id="sample",
        markdown_path=tmp_path / "sample.md",
        issues=[
            ValidationIssue(field="a", message="warning", severity="warning"),
            ValidationIssue(field="b", message="error", severity="error"),
        ],
    )

    assert report.is_valid is False
    assert [issue.field for issue in report.warnings] == ["a"]
    assert [issue.field for issue in report.errors] == ["b"]

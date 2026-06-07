"""Tests for narrative analysis protocols.

Tests cover:
- ProtocolLevel enum and ProtocolSpec models
- Protocol registry lookup (get_protocol)
- ProtocolRunner execution with mock LLM provider
"""

import pytest

from narratological.llm import MockProvider
from narratological.models.analysis import BeatFunction, Character, ConnectorType, Scene, Script
from narratological.models.protocol import ProtocolLevel
from narratological.protocols.registry import get_protocol
from narratological.protocols.runner import ProtocolRunner


@pytest.fixture
def simple_script():
    """Create a simple script for testing."""
    return Script(
        title="Test Script",
        format="Feature",
        page_count=100,
        primary_genre="Drama",
        tone="Serious",
        logline="A test script for unit testing.",
        scenes=[
            Scene(
                number=1,
                slug="INT. HOUSE - DAY",
                summary="We meet the protagonist",
                function=BeatFunction.SETUP,
                characters_present=["JOHN"],
                connector_to_next=ConnectorType.THEREFORE,
                tension_level=3,
            ),
            Scene(
                number=2,
                slug="EXT. STREET - DAY",
                summary="The inciting incident occurs",
                function=BeatFunction.INCITE,
                characters_present=["JOHN"],
                tension_level=6,
            ),
        ],
        characters=[
            Character(
                name="JOHN",
                role="protagonist",
                description="The hero of the story",
            )
        ],
    )


@pytest.fixture
def mock_provider():
    """Create a mock LLM provider."""
    return MockProvider(default_response="Mocked protocol output content")


def test_get_protocol():
    """Test retrieving protocol specifications."""
    p1 = get_protocol("P1")
    assert p1.level == ProtocolLevel.P1
    assert p1.name == "Triage"
    assert len(p1.roles) == 2
    assert "Triage Decision" in p1.documents

    p3 = get_protocol(ProtocolLevel.P3)
    assert p3.level == ProtocolLevel.P3
    assert p3.name == "Craft"
    assert len(p3.roles) == 5

    with pytest.raises(KeyError):
        get_protocol("P8")


def test_protocol_runner_p1(simple_script, mock_provider):
    """Test ProtocolRunner execution for P1."""
    runner = ProtocolRunner(mock_provider)
    results = runner.run(simple_script, ProtocolLevel.P1)

    assert "coverage" in results
    assert "triage_decision" in results
    assert "combined_markdown" in results

    assert results["triage_decision"] == "Mocked protocol output content"
    assert "Mocked protocol output content" in results["combined_markdown"]
    assert "## Coverage Summary" in results["combined_markdown"]


def test_protocol_runner_p3(simple_script, mock_provider):
    """Test ProtocolRunner execution for P3."""
    runner = ProtocolRunner(mock_provider)
    results = runner.run(simple_script, ProtocolLevel.P3)

    assert "coverage" in results
    assert "structural" in results
    assert "character_atlas" in results
    assert "diagnostic" in results
    assert "revision_roadmap" in results
    assert "combined_markdown" in results

    assert "Test Script" in results["combined_markdown"]
    assert "## Coverage Summary" in results["combined_markdown"]
    assert "## Structural Architecture" in results["combined_markdown"]
    assert "## Character Atlas" in results["combined_markdown"]
    assert "## Diagnostic Report" in results["combined_markdown"]


def test_protocol_runner_normalizes_string_level(simple_script, mock_provider):
    """Lowercase string levels should execute the selected protocol, not an empty shell."""
    runner = ProtocolRunner(mock_provider)
    results = runner.run(simple_script, "p3")

    assert "coverage" in results
    assert "structural" in results
    assert "character_atlas" in results
    assert "diagnostic" in results
    assert "revision_roadmap" in results
    assert "combined_markdown" in results

"""Tests for Fountain script parsing."""

import pytest

from narratological.parsers.fountain import FountainParser, parse_fountain

FOUNTAIN_TEXT = """Title: Parser Fixture

INT. FARMHOUSE - DAY
John waits by the window.

JOHN
I heard the engine.

MARY (V.O.)
Then we still have time.

CUT TO:

.MONTAGE - THE ROAD
The truck rolls past empty fields.

DRIVER^
No turning back.
"""


def test_parse_fountain_text_extracts_scenes_and_characters():
    """Direct text input should become a Script with ordered scenes and characters."""
    script = parse_fountain(FOUNTAIN_TEXT)

    assert script.title == "Untitled Script"
    assert script.format == "Fountain"
    assert script.scene_count == 2
    assert [scene.slug for scene in script.scenes] == [
        "INT. FARMHOUSE - DAY",
        "MONTAGE - THE ROAD",
    ]
    assert script.scenes[0].characters_present == ["JOHN", "MARY"]
    assert script.scenes[0].summary.startswith("John waits by the window.")
    assert {character.name for character in script.characters} == {"DRIVER", "JOHN", "MARY"}


def test_parse_fountain_path_uses_file_stem_for_title(tmp_path):
    """Path input should be read from disk and derive a human title from the file name."""
    path = tmp_path / "sample_script.fountain"
    path.write_text(FOUNTAIN_TEXT, encoding="utf-8")

    script_from_path = parse_fountain(path)
    script_from_string_path = parse_fountain(str(path))

    assert script_from_path.title == "Sample Script"
    assert script_from_string_path.title == "Sample Script"
    assert script_from_path.scene_count == script_from_string_path.scene_count == 2


def test_parse_fountain_missing_path_raises_file_not_found(tmp_path):
    """Explicit Path input should fail clearly when the file does not exist."""
    missing = tmp_path / "missing.fountain"

    with pytest.raises(FileNotFoundError, match="File not found"):
        parse_fountain(missing)


def test_fountain_parser_can_be_reused_without_leaking_state():
    """A parser instance should not carry scenes or characters across parse calls."""
    parser = FountainParser()

    first_scenes, first_characters = parser.parse(FOUNTAIN_TEXT)
    second_scenes, second_characters = parser.parse("EXT. PORCH - NIGHT\nA porch light hums.")

    assert len(first_scenes) == 2
    assert {character.name for character in first_characters} == {"DRIVER", "JOHN", "MARY"}
    assert len(second_scenes) == 1
    assert second_scenes[0].slug == "EXT. PORCH - NIGHT"
    assert second_characters == []


def test_parse_fountain_long_non_path_string_is_treated_as_content():
    """Long script text should not be interpreted as a filesystem path."""
    long_text = "INT. ROOM - DAY\n" + ("A quiet room.\n" * 300)

    script = parse_fountain(long_text)

    assert script.scene_count == 1
    assert script.page_count > 1
    assert script.scenes[0].slug == "INT. ROOM - DAY"

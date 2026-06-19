"""Fountain script parser.

Parses .fountain files into Script models.
Adheres to Fountain 1.1 syntax spec.
"""

from __future__ import annotations

import re
from pathlib import Path

from narratological.models.analysis import Character, Scene, Script


class FountainParser:
    """State-machine parser for Fountain syntax."""

    def __init__(self) -> None:
        self._reset()

    def _reset(self) -> None:
        """Reset parser state before parsing a new document."""
        self.scenes: list[Scene] = []
        self.characters: set[str] = set()
        self._current_scene: Scene | None = None
        self._current_content: list[str] = []
        self._scene_characters: set[str] = set()

    def parse(self, text: str) -> tuple[list[Scene], list[Character]]:
        """Parse fountain text into scenes and characters."""
        self._reset()
        lines = text.splitlines()

        # Ensure we capture the final scene
        if lines and lines[-1].strip():
            lines.append("")

        for line in lines:
            line = line.rstrip()

            if self._is_scene_heading(line):
                self._finalize_current_scene()
                self._start_new_scene(line)
            elif self._is_character_cue(line):
                char_name = self._extract_character_name(line)
                self.characters.add(char_name)
                self._scene_characters.add(char_name)
                if self._current_scene:
                    self._current_content.append(line)
            else:
                if self._current_scene:
                    self._current_content.append(line)

        self._finalize_current_scene()

        # Create Character models
        char_models = [
            Character(name=name, role="character", description="Extracted from script")
            for name in sorted(self.characters)
        ]

        return self.scenes, char_models

    def _is_scene_heading(self, line: str) -> bool:
        """Check if line is a scene heading."""
        # Forced scene heading
        if line.startswith("."):
            return True

        # Standard scene headings
        # INT, EXT, EST, INT./EXT., INT/EXT, I/E
        heading_prefixes = (
            "INT ",
            "EXT ",
            "EST ",
            "INT.",
            "EXT.",
            "EST.",
            "INT./EXT.",
            "INT/EXT ",
            "I/E ",
            "I/E.",
        )
        return line.upper().startswith(heading_prefixes)

    def _is_character_cue(self, line: str) -> bool:
        """Check if line is a character cue.

        Fountain rules:
        - Uppercase
        - Not a scene heading
        - Preceded by empty line (not strictly enforced here for robustness)
        - Can contain (cont'd) or (V.O.)
        """
        if not line.isupper():
            return False

        # Ignore common transitions that might look like characters
        transitions = {"CUT TO:", "FADE OUT.", "SMASH CUT TO:", "FADE IN:", "THE END"}
        if line in transitions:
            return False

        # Has to look like a name
        # Allow @ symbol for forced character names
        if line.startswith("@"):
            return True

        return True

    def _extract_character_name(self, line: str) -> str:
        """Clean character name from cue."""
        if line.startswith("@"):
            name = line[1:]
        else:
            name = line

        # Remove parentheticals like (V.O.), (O.S.), (CONT'D)
        name = re.sub(r"\s*\(.*\)", "", name)
        # Remove caret for dual dialogue
        name = name.rstrip("^").strip()

        return name

    def _start_new_scene(self, heading: str) -> None:
        """Initialize a new scene."""
        clean_heading = heading.lstrip(".").strip()
        self._current_scene = Scene(
            number=len(self.scenes) + 1,
            slug=clean_heading,
            summary="",  # Will be generated later
            characters_present=[],  # Will be populated
        )
        self._current_content = []
        self._scene_characters = set()

    def _finalize_current_scene(self) -> None:
        """Save the current scene."""
        if self._current_scene:
            # Generate summary from content
            content_text = "\n".join(self._current_content).strip()
            summary = self._generate_summary(content_text)

            self._current_scene.summary = summary
            self._current_scene.characters_present = sorted(self._scene_characters)

            self.scenes.append(self._current_scene)

    def _generate_summary(self, content: str) -> str:
        """Generate a summary from the first few action lines."""
        lines = content.split("\n")
        action_lines = []

        for line in lines:
            if not line.strip():
                continue
            # Skip character cues and dialogue (heuristic)
            if self._is_character_cue(line):
                continue
            # Skip parentheticals
            if line.strip().startswith("("):
                continue

            action_lines.append(line.strip())
            if len(action_lines) >= 3:
                break

        summary = " ".join(action_lines)
        if len(summary) > 200:
            summary = summary[:197] + "..."

        return summary or "Scene action"


def parse_fountain(source: Path | str) -> Script:
    """Parse a .fountain file or direct text content into a Script model."""
    if isinstance(source, Path):
        if not source.exists():
            raise FileNotFoundError(f"File not found: {source}")
        text = source.read_text(encoding="utf-8")
        title = source.stem.replace("_", " ").title()
    else:
        # Check if source is a string representing a path that exists
        try:
            potential_path = Path(source)
            if len(source) < 260 and potential_path.exists() and potential_path.is_file():
                text = potential_path.read_text(encoding="utf-8")
                title = potential_path.stem.replace("_", " ").title()
            else:
                text = source
                title = "Untitled Script"
        except Exception:
            text = source
            title = "Untitled Script"

    parser = FountainParser()
    scenes, characters = parser.parse(text)

    # Estimate pages (Fountain: ~55 lines per page roughly)
    page_count = max(1, text.count("\n") // 55)

    return Script(
        title=title,
        format="Fountain",
        page_count=page_count,
        scene_count=len(scenes),
        scenes=scenes,
        characters=characters,
    )

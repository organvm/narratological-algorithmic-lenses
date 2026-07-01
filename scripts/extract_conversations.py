#!/usr/bin/env python3
"""Extract 27 conversation threads from Claude Desktop conversations.json export."""

import json
import re
from datetime import datetime
from pathlib import Path

CONVERSATIONS_JSON = Path("~/Workspace/intake/data-2026-02-16-00-20-00-batch-0000/conversations.json")
REPO_ROOT = Path("~/world/realm/create/org/liminal/repo/narratological-algorithmic-lenses")
OUTPUT_DIR = REPO_ROOT / "specs/00-chat-transcripts/desktop"
ARTIFACTS_DIR = OUTPUT_DIR / "artifacts"

# CT-ID → UUID mapping from manifest
CT_UUIDS = {
    "CT-001": "a31d8914-aacb-4a69-b8aa-4341532390d8",
    "CT-002": "a90dd864-6a46-455e-812f-f63fc402425f",
    "CT-003": "04db480d-969c-4194-9b7d-6d8360bddf5a",
    "CT-004": "1e323a77-3cca-42ec-b13b-f9d9f1472b40",
    "CT-005": "f2c43556-1781-41ce-beab-7a966df084bc",
    "CT-006": "eb967bd0-08fe-426c-96bc-3b1b6005ef3e",
    "CT-007": "76b614bf-5745-4a16-aa96-e182bcf75a1e",
    "CT-008": "ff7e1f3a-d051-47f2-9593-21b1923da9d5",
    "CT-009": "3c65d363-16db-4299-80ef-7053419c166f",
    "CT-010": "72c5caf7-f83e-486b-8614-a313aa232af6",
    "CT-011": "0f8f5311-ea85-4b93-bd05-94e1e38e8651",
    "CT-012": "50cf10b3-ea99-4725-843b-ce3f7cc2e095",
    "CT-013": "4322269d-4c9d-47aa-8ad6-3754a0b98bbb",
    "CT-014": "e1cd0d3b-e3ce-46df-8d35-1c2b31153a9f",
    "CT-015": "62b8433c-f529-4325-a7f1-00ab8494026f",
    "CT-016": "eb75fc65-ec3c-4fff-aa01-01b467bc4f47",
    "CT-017": "03cdab5a-46c8-4b3f-ba4c-4aa6c1228c00",
    "CT-018": "278248d2-9d64-47d5-a9f2-72da9f2a2971",
    "CT-019": "2a827cf1-5bbe-4234-b5f6-e86646c3a871",
    "CT-020": "fa97906a-7571-477a-9173-6083ee82b2b8",
    "CT-021": "beff0b1b-606f-4aa2-a85d-5ac1ddce5435",
    "CT-022": "0afc882c-22e5-4c9d-abb9-e3c1731ea49f",
    "CT-023": "d07d1fce-806f-445e-9093-5d5eaececd58",
    "CT-024": "e76c911d-9ed4-4f01-88c6-f865049b2444",
    "CT-025": "a72a4630-7655-4129-92ad-c8be69304e73",
    "CT-026": "c7a37811-618f-42c3-951a-0a7fa83adfef",
    "CT-027": "72996a9c-f6ab-4d51-bbd1-03267dfaa914",
}

# CT-ID → manifest metadata
CT_META = {
    "CT-001": {"title": "Building narratological algorithms from cinema and games", "tags": ["PLANNING", "STUDY_GUIDE", "MULTI-MEDIA"]},
    "CT-002": {"title": "Research roles and documents for artistic analysis", "tags": ["METHODOLOGY", "FEEDBACK_ROLES", "TEMPLATES"]},
    "CT-003": {"title": "Comprehensive script analysis and dramaturgical breakdown", "tags": ["SKILL_CREATION", "ANALYSIS", "DRAMATURGICAL"]},
    "CT-004": {"title": "First draft feedback on open view", "tags": ["CREATIVE_WORK", "FEEDBACK", "STRUCTURAL_ANALYSIS"]},
    "CT-005": {"title": "Attention economy across media forms", "tags": ["META_THEORY", "ATTENTION", "CROSS-MEDIA"]},
    "CT-006": {"title": "Tarantino's genre taxonomy and creative methodology", "tags": ["RESEARCH", "FILM", "GENRE", "TARANTINO"]},
    "CT-007": {"title": "Narratological algorithms from artistic principles", "tags": ["SKILL_CREATION", "METHODOLOGY", "CORE"]},
    "CT-008": {"title": "Bharata-Muni's narrative principles as algorithms", "tags": ["CLASSICAL", "INDIAN", "RASA", "NATYASASTRA"]},
    "CT-009": {"title": "Bharata-Muni's narrative principles as algorithms (extended)", "tags": ["CLASSICAL", "INDIAN", "PERFORMANCE", "NATYASASTRA"]},
    "CT-010": {"title": "Horace's poetic principles as narrative algorithms", "tags": ["CLASSICAL", "ROMAN", "CRAFT"]},
    "CT-011": {"title": "Plato's principles as narratological algorithms", "tags": ["CLASSICAL", "GREEK", "PHILOSOPHY", "MIMESIS"]},
    "CT-012": {"title": "Aristotle's poetics as narrative algorithms", "tags": ["CLASSICAL", "GREEK", "FOUNDATIONAL"]},
    "CT-013": {"title": "Kubrick's non-submersible narrative units", "tags": ["RESEARCH", "FILM", "KUBRICK", "ADAPTATION"]},
    "CT-014": {"title": "Narratological algorithms from layered obstacles", "tags": ["ALGO", "TELEVISION", "SCENE_DESIGN", "PWB"]},
    "CT-015": {"title": "South Park's narratological algorithms", "tags": ["ALGO", "COMEDY", "ANIMATION", "CAUSALITY"]},
    "CT-016": {"title": "David's comedic rules as narratological algorithms", "tags": ["ALGO", "COMEDY", "TELEVISION", "LARRY_DAVID"]},
    "CT-017": {"title": "McKee's narratological algorithms", "tags": ["ALGO", "SCREENWRITING", "MCKEE", "FOUNDATIONAL"]},
    "CT-018": {"title": "McKee's narrative principles formalized (OCR session)", "tags": ["SOURCE_EXTRACTION", "OCR", "MCKEE"]},
    "CT-019": {"title": "Scene complications as narrative protocol", "tags": ["RESEARCH", "INITIAL", "MULTI-TECHNIQUE"]},
    "CT-020": {"title": "Claude project manifest with annotated bibliography", "tags": ["MANIFEST", "DOCUMENTATION", "PROJECT_MANAGEMENT"]},
    "CT-021": {"title": "Designing multi-lens protocols for project review", "tags": ["PROTOCOL_DESIGN", "METHODOLOGY", "FRAMEWORK"]},
    "CT-022": {"title": "Applying analysis protocols to creative work", "tags": ["SKILL_CREATION", "PROTOCOL_IMPLEMENTATION", "ARCHITECTURE"]},
    "CT-023": {"title": "P7 comprehensive analysis of open view", "tags": ["CREATIVE_WORK", "P7_COMPREHENSIVE", "ANALYSIS", "OPEN_VIEW"]},
    "CT-024": {"title": "Family trauma and mythological adaptation", "tags": ["CREATIVE_WORK", "AUTOBIOGRAPHY", "MYTHOLOGY", "OPEN_VIEW", "EL_SERIES"]},
    "CT-025": {"title": "Enumerating fundamental narrative structures", "tags": ["RESEARCH", "NARRATIVE_THEORY", "ENUMERATION", "COMPUTATIONAL"]},
    "CT-026": {"title": "First manifest amendment session", "tags": ["MANIFEST", "DOCUMENTATION", "AMENDMENT"]},
    "CT-027": {"title": "Balancing novelty against comparative analysis", "tags": ["EPISTEMOLOGY", "CRITIQUE", "PROJECT_LIMITATIONS", "METHODOLOGY"]},
}

# Reverse UUID → CT-ID lookup
UUID_TO_CT = {v: k for k, v in CT_UUIDS.items()}


def slugify(text: str, max_len: int = 60) -> str:
    """Convert text to kebab-case slug."""
    text = text.lower()
    text = re.sub(r"[''']", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text


def extract_text_content(message: dict) -> str:
    """Extract text content from a message, skipping thinking blocks."""
    parts = []
    for block in message.get("content", []):
        if block.get("type") == "text":
            text = block.get("text", "")
            if text.strip():
                parts.append(text)
    # Fallback to the text field if content blocks are empty
    if not parts:
        text = message.get("text", "")
        if text.strip():
            parts.append(text)
    return "\n\n".join(parts)


def detect_artifacts(text: str, ct_id: str, msg_idx: int) -> list:
    """Detect substantial generated documents in assistant messages.

    Returns list of (title, content) tuples for extracted artifacts.
    """
    artifacts = []

    # Look for markdown documents with clear headers that are >2000 chars
    # Common patterns: "# Title\n\n..." at the start of a substantial block
    sections = re.split(r'\n(?=# [A-Z])', text)

    for section in sections:
        # Skip short sections
        if len(section) < 2000:
            continue

        # Check if this looks like a standalone document (starts with # heading)
        match = re.match(r'^# (.+?)(?:\n|$)', section)
        if match:
            title = match.group(1).strip()
            # Skip generic conversational headings
            skip_patterns = ["Summary", "Here's", "Let me", "I'll", "Based on"]
            if any(title.startswith(p) for p in skip_patterns):
                continue
            artifacts.append((title, section))

    return artifacts


def format_conversation(conv: dict, ct_id: str) -> tuple:
    """Format a conversation as markdown with YAML frontmatter.

    Returns (markdown_content, list_of_artifacts).
    """
    meta = CT_META.get(ct_id, {})
    title = meta.get("title", conv.get("name", "Untitled"))
    tags = meta.get("tags", [])

    messages = conv.get("chat_messages", [])

    # Build YAML frontmatter
    lines = ["---"]
    lines.append(f"ct_id: {ct_id}")
    lines.append(f"uuid: {conv['uuid']}")
    lines.append(f"title: \"{title}\"")
    lines.append(f"created_at: {conv.get('created_at', 'unknown')}")
    lines.append(f"updated_at: {conv.get('updated_at', 'unknown')}")
    lines.append(f"message_count: {len(messages)}")
    lines.append(f"tags: [{', '.join(tags)}]")
    lines.append("source: claude-desktop-export")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"**{ct_id}** | {len(messages)} messages | Source: Claude Desktop")
    lines.append("")
    lines.append("---")
    lines.append("")

    all_artifacts = []

    for i, msg in enumerate(messages):
        sender = msg.get("sender", "unknown")
        timestamp = msg.get("created_at", "")

        # Format sender label
        if sender == "human":
            label = "Human"
        elif sender == "assistant":
            label = "Assistant"
        else:
            label = sender.capitalize()

        text = extract_text_content(msg)
        if not text.strip():
            continue

        # Timestamp formatting
        ts_display = ""
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                ts_display = f" *({dt.strftime('%Y-%m-%d %H:%M UTC')})*"
            except (ValueError, TypeError):
                ts_display = f" *({timestamp})*"

        lines.append(f"## {label}{ts_display}")
        lines.append("")
        lines.append(text)
        lines.append("")
        lines.append("---")
        lines.append("")

        # Check for artifacts in assistant messages
        if sender == "assistant":
            artifacts = detect_artifacts(text, ct_id, i)
            for art_title, art_content in artifacts:
                all_artifacts.append({
                    "title": art_title,
                    "content": art_content,
                    "source_ct": ct_id,
                    "message_index": i,
                })

    return "\n".join(lines), all_artifacts


def main():
    print(f"Loading {CONVERSATIONS_JSON} ...")
    with open(CONVERSATIONS_JSON) as f:
        conversations = json.load(f)

    print(f"Loaded {len(conversations)} total conversations")

    # Build UUID lookup
    conv_by_uuid = {}
    for conv in conversations:
        conv_by_uuid[conv["uuid"]] = conv

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    extracted = 0
    total_artifacts = 0
    results = []

    for ct_id in sorted(CT_UUIDS.keys(), key=lambda x: int(x.split("-")[1])):
        uuid = CT_UUIDS[ct_id]
        conv = conv_by_uuid.get(uuid)

        if not conv:
            print(f"  MISSING: {ct_id} ({uuid})")
            continue

        meta = CT_META.get(ct_id, {})
        title = meta.get("title", conv.get("name", "untitled"))
        slug = slugify(title)
        filename = f"{ct_id}_{slug}.md"

        content, artifacts = format_conversation(conv, ct_id)

        dest = OUTPUT_DIR / filename
        dest.write_text(content)

        msg_count = len(conv.get("chat_messages", []))
        size_kb = len(content.encode("utf-8")) / 1024
        print(f"  {ct_id}: {title[:50]:<50s} ({msg_count} msgs, {size_kb:.1f}K)")

        # Write artifacts
        for art in artifacts:
            art_slug = slugify(art["title"], max_len=50)
            art_filename = f"{ct_id}_{art_slug}.md"
            art_path = ARTIFACTS_DIR / art_filename

            art_lines = [
                "---",
                f"source_thread: {ct_id}",
                f"source_message: {art['message_index']}",
                f"extracted_from: {filename}",
                "---",
                "",
                art["content"],
            ]
            art_path.write_text("\n".join(art_lines))
            total_artifacts += 1

        extracted += 1
        results.append({
            "ct_id": ct_id,
            "uuid": uuid,
            "title": title,
            "filename": filename,
            "message_count": msg_count,
            "size_kb": size_kb,
            "artifact_count": len(artifacts),
        })

    print(f"\nExtracted {extracted}/{len(CT_UUIDS)} conversations, {total_artifacts} artifacts")

    # Write extraction summary
    summary_path = OUTPUT_DIR / "EXTRACTION-SUMMARY.md"
    lines = ["# Conversation Thread Extraction Summary\n"]
    lines.append(f"Extracted: {datetime.now().isoformat()}\n")
    lines.append(f"Source: `{CONVERSATIONS_JSON}`\n")
    lines.append(f"Total conversations in export: {len(conversations)}\n")
    lines.append(f"Manifest threads extracted: {extracted}/{len(CT_UUIDS)}\n")
    lines.append(f"Artifacts extracted: {total_artifacts}\n")
    lines.append("")
    lines.append("| CT-ID | Title | Messages | Size | Artifacts | File |")
    lines.append("|-------|-------|----------|------|-----------|------|")
    for r in results:
        lines.append(
            f"| {r['ct_id']} | {r['title'][:40]} | {r['message_count']} | "
            f"{r['size_kb']:.0f}K | {r['artifact_count']} | `{r['filename']}` |"
        )
    lines.append("")
    summary_path.write_text("\n".join(lines))
    print(f"Wrote extraction summary to {summary_path}")


if __name__ == "__main__":
    main()

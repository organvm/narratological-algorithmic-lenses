#!/usr/bin/env python3
"""Extract 19 missing text docs from Claude Desktop projects.json export."""

import json
import sys
from pathlib import Path

PROJECTS_JSON = Path("~/Workspace/intake/data-2026-02-16-00-20-00-batch-0000/projects.json")
REPO_ROOT = Path("~/world/realm/create/org/liminal/repo/narratological-algorithmic-lenses")
PROJECT_UUID = "019be5ff-cb43-77b2-8078-ac2adff3a15d"

# Map: (doc_index, destination_path)
# Index is 0-based position in the project's docs array
EXTRACTIONS = [
    (15, "specs/05-secondary-sources/stanley-kubricks-narratological-philosophy.md"),
    (25, "specs/05-secondary-sources/attention-mechanics-meta-principles.md"),
    (35, "specs/10-project-manifests/narratological-project-manifest-v1.md"),
    (36, "specs/08-protocol-framework/analysis-protocols-framework.md"),
    (37, "specs/08-protocol-framework/protocol-specific-templates.md"),
    (38, "specs/08-protocol-framework/protocol-invocation-guide.md"),
    (39, "specs/08-protocol-framework/protocol-invocation-prompts.md"),
    (41, "specs/08-protocol-framework/quick-reference.md"),
    (42, "specs/08-protocol-framework/integration-guide.md"),
    (40, "specs/09-protocol-skills/creative-analysis/SKILL.md"),
    (43, "specs/09-protocol-skills/protocol-triage/SKILL.md"),
    (44, "specs/09-protocol-skills/protocol-structural/SKILL.md"),
    (45, "specs/09-protocol-skills/protocol-craft/SKILL.md"),
    (46, "specs/09-protocol-skills/protocol-scholarly/SKILL.md"),
    (47, "specs/09-protocol-skills/protocol-market/SKILL.md"),
    (48, "specs/09-protocol-skills/protocol-extraction/SKILL.md"),
    (49, "specs/09-protocol-skills/protocol-comprehensive/SKILL.md"),
    (50, "specs/05-secondary-sources/are-there-a-finite-number-of-stories.md"),
    (51, "specs/10-project-manifests/narratological-project-manifest-v3.md"),
]


def main():
    print(f"Loading {PROJECTS_JSON} ...")
    with open(PROJECTS_JSON) as f:
        projects = json.load(f)

    # Find the open-view project
    project = None
    for p in projects:
        if p.get("uuid") == PROJECT_UUID:
            project = p
            break

    if not project:
        print(f"ERROR: Project {PROJECT_UUID} not found!")
        sys.exit(1)

    docs = project["docs"]
    print(f"Found project '{project['name']}' with {len(docs)} docs")

    extracted = 0
    for idx, dest_rel in EXTRACTIONS:
        if idx >= len(docs):
            print(f"  SKIP: Index {idx} out of range (only {len(docs)} docs)")
            continue

        doc = docs[idx]
        content = doc.get("content", "")
        filename = doc.get("filename", f"doc_{idx}")

        dest = REPO_ROOT / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)

        size_kb = len(content.encode("utf-8")) / 1024
        print(f"  [{idx:2d}] {filename[:60]:<60s} → {dest_rel} ({size_kb:.1f}K)")
        extracted += 1

    print(f"\nExtracted {extracted}/{len(EXTRACTIONS)} documents.")

    # Also produce a full doc index for audit purposes
    audit_path = REPO_ROOT / "specs/10-project-manifests/project-docs-index.md"
    lines = ["# Open-View Project Document Index\n"]
    lines.append(f"Project UUID: `{PROJECT_UUID}`\n")
    lines.append(f"Total docs: {len(docs)}\n")
    lines.append("| Idx | Filename | Size | UUID |")
    lines.append("|-----|----------|------|------|")
    for i, doc in enumerate(docs):
        fn = doc.get("filename", "—")
        content = doc.get("content", "")
        size_kb = len(content.encode("utf-8")) / 1024
        uuid = doc.get("uuid", "—")
        lines.append(f"| {i} | {fn} | {size_kb:.1f}K | `{uuid}` |")
    lines.append("")
    audit_path.write_text("\n".join(lines))
    print(f"Wrote doc index to {audit_path}")


if __name__ == "__main__":
    main()

# Hall-Monitor Audit - 2026-06-07

## Scope Checked

- Repo: `~/Code/organvm/narratological-algorithmic-lenses`
- Origin: `[email redacted]:a-organvm/narratological-algorithmic-lenses.git`
- Gemini artifacts: `.gemini/plans`, `.gemini/handoffs`, `.gemini/worktrees`
- Antigravity artifacts: `~/.local/share/gemini/antigravity-cli`
- OpenCode artifacts: `.git/opencode`, `~/.local/share/opencode/log`, `~/.local/share/opencode/snapshot`
- IRF registry: `~/Code/organvm/organvm-corpvs-testamentvm/INST-INDEX-RERUM-FACIENDARUM.md`

## Findings

- CI workflow existed but was disabled on GitHub; local test proof was not enough.
- Advanced CodeQL workflow conflicted with GitHub default CodeQL setup and produced rejected analyses.
- `ProtocolRunner.run(script, "p3")` accepted the level via registry lookup but compared the original lowercase string later, returning only `combined_markdown`.
- Stale remote metadata named `organvm-i-theoria` or old workflow `ci-python.yml` while the actual remote is `a-organvm` and the workflow is `ci.yml`.
- Gemini/Antigravity local worktrees were ignored by git; Antigravity logs showed patch creation failures for `.gemini/worktrees/*` directories.
- The `milestone-4-cicd` worktree branch HEAD `32d237a` was not an ancestor of `main`; branch state is preserved at `origin/codex/preserve-milestone-4-cicd-2026-06-07`, and its dirty diff is preserved in `2026-06-07-milestone-4-cicd-worktree-preservation.patch`.
- OpenCode created session `ses_15dec3b44ffetRe5iBmgVtLVV2` and snapshots for this repo, but no repo-local OpenCode artifact is tracked.
- CI exposed FastMCP wrapper drift in `scripts/test_mcp_smoke.py`: one environment imported plain functions while another exposed `.fn`; the smoke script now supports both.

## External Index Sweep

- GitHub issues for this repo: none open at audit time.
- GitHub PRs for this repo: none open at audit time.
- Omega scorecard: no repo-local scorecard file found.
- SGO inquiry log: no repo-local `inquiry-log.yaml` found.
- Seed contract: updated for real org, workflow, protocol capability, and default CodeQL posture.
- CLAUDE/GEMINI context: narrow stale org repair applied; broad `organvm context sync --dry-run` would update 249 files, so write mode was not run from this repo.
- Concordance: no repo-local concordance file found.
- IRF stats at audit time: 969 total, 485 open, 484 completed, 12 P0, 146 P1.
- IRF: existing rows cover the active classes: IRF-SYS-156 for CI cascade, IRF-SYS-126 for local-only drift enforcement, IRF-SYS-247 for stale corpvs path/stub drift, and IRF-APP-059 for CI/CD workflow creation. No direct IRF mutation was made from this repo because the canonical corpvs checkout is dirty with unrelated corpus/session changes.

## Verification

- `uv run pytest packages/core/tests/test_protocols.py -q`: 4 passed.
- `uv run ruff check .`: passed.
- `uv run mypy .`: success on 77 source files.
- `uv run pytest`: 309 passed, 1 skipped.
- `uv run python scripts/test_api_smoke.py`: all API endpoints passed.
- `uv run python scripts/test_mcp_smoke.py`: 28 studies, 1 mimesis axiom, 4 MCP tools registered.
- CI rerun after MCP compatibility fix required: first enabled CI run reached MCP smoke and failed on direct `.fn` access.
- `npm run web:test`: 5 files passed, 12 tests passed.
- `npm run web:build`: Vite production build passed.
- `git diff --check`: passed.
- `gh workflow list`: `CI` is active after remote enable.

# Session Plan: Milestone 3 — Package Hardening

**Date:** 2026-06-06
**Phase:** BUILD/PROVE
**Goal:** Verify and smoke-test all system packages (CLI, API, Web, MCP, VS Code) to ensure robustness and stability, completing Milestone 3.

---

## 1. CLI End-to-End Verification
Smoke-test all main command groups using `specs/06-open-view-drafts/test_fountain.fountain` as the test subject:
- [ ] `validate` (compendium integrity and markdown-JSON synchronization)
- [ ] `study` (listing and detailing available narrative frameworks)
- [ ] `algorithm` (listing and running registered algorithms)
- [ ] `analyze` (running analyst role checks on the Fountain script)
- [ ] `diagnose` (running diagnostic tests like Causal Binding thresholds on the script)
- [ ] `generate` (generating beat maps and structural formats)

## 2. API Service Verification
- [ ] Spin up FastAPI server locally in the background using `uv run uvicorn narratological_api.main:app`
- [ ] Execute `curl` requests to verify key REST endpoints:
  - [ ] `/studies` or equivalent GET endpoint
  - [ ] `/analysis` trigger and status check
  - [ ] `/diagnostics` endpoint
- [ ] Properly clean up and terminate the background server process

## 3. Web Dashboard Verification
- [ ] Run `npm install` inside `packages/web/` (or the monorepo root)
- [ ] Verify `npm run web:build` (or `npm run build` in `packages/web`) compiles TypeScript/React code with zero errors
- [ ] Run `npm run web:test` (or `npm run test` in `packages/web`) to ensure all Vitest suites pass

## 4. MCP Server Verification
- [ ] Initialize the MCP server manually/via python module
- [ ] Verify tool discovery and check tool definitions
- [ ] Test calling a basic tool (e.g. study listing) through the server framework

## 5. VS Code Snippet Verification
- [ ] Inspect snippet definition files in `packages/vscode/` to ensure syntax formatting is correct and triggers are correctly mapped

## 6. Closing & Progress Tracking
- [ ] Document all results and findings
- [ ] Update `docs/plans/there+back-again.md` marking Milestone 3 as complete
- [ ] Commit any necessary fixes or configuration updates

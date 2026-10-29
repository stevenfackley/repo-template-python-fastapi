# Decisions

ADR log. Append-only.

## {{DATE}} — Initial stack: Python 3.11 + FastAPI + uv

**Status:** accepted
**Context:** Greenfield service under `repo-template-python-fastapi`. Async IO, quick iteration.
**Decision:** Python 3.11, FastAPI, Pydantic v2, ruff + mypy + pytest, uv for dep management.
**Consequences:** deps range-pinned in `pyproject.toml` (no `uv.lock` committed yet); pip forbidden in CI. No telemetry SDKs (CI-enforced).

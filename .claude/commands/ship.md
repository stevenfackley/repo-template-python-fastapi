---
description: Full pre-push gate.
---

Run in order, stop on first failure:

1. `uv run ruff check .`
2. `uv run ruff format --check .`
3. `uv run mypy src`
4. `uv run pytest`
5. `pwsh scripts/scan-secrets.ps1`
6. Print `git rev-parse --short HEAD` + `git status --short`.

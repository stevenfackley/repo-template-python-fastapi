# {{PROJECT_NAME}}

## Stack
{{FLAVOR}}. Python 3.11 + FastAPI + uv. See `docs/architecture/SDD.md`.

## Standard flow
analyze -> read docs/ -> read pyproject.toml -> plan -> work.

## Conventions
- Image tags: `sha-{SHORT_SHA}` (test), `prod-{SHA}` (prod).
- Release tags: `YYYYMMDD_{{PROJECT_NAME}}_Release`.
- Deps: `uv pip` over pip. Range-pinned (`>=`) in `pyproject.toml`; no `uv.lock` committed yet.
- Lint: `ruff check`, `ruff format --check`.
- Types: strict mypy.
- Tests: pytest + pytest-asyncio (unit + in-process integration) in `ci` on PR and main. Post-deploy smoke = the deploy workflows' `/health` check. No scheduled E2E integration workflow yet.
- Commits: Conventional Commits.

## Deploy target
{{DEPLOY_TARGET}}

## Commands
- `/ship` — full pre-push (lint + types + tests + secret-scan)
- `/deploy-test` — trigger test deploy
- `/add-adr` — new DECISIONS.md entry
- `/smoke` — run E2E smoke locally

## Do not
- Add static AWS keys. Use OIDC.
- Skip the secret-scan pre-commit hook.
- Bump major deps without an ADR.
- Add telemetry SDKs. Banned by CI.
- `print()` in production code. Use `logging`.

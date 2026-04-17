# {{PROJECT_NAME}} — dev cheat sheet

## Lint / test / run

```bash
uv pip install -e ".[dev]"
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run uvicorn app.main:app --reload --port 8080
```

## OpenAPI export

```bash
uv run python scripts/export-openapi.py   # writes docs/api/openapi.json
```

## Docker

```bash
docker compose up --build
docker compose -f docker-compose.yml -f docker-compose.prod.yml config
```

## CI ops

```bash
gh run list --status failure --limit 5
gh run view <RUN_ID> --log-failed
gh workflow run deploy-test.yml
```

## Tagging

- `sha-{SHORT_SHA}` — test
- `prod-{SHA}` — prod (immutable)
- `YYYYMMDD_{{PROJECT_NAME}}_Release` — release tag

# {{PROJECT_NAME}}

{{FLAVOR}} — Python 3.11 FastAPI service.

## Quick start

```bash
uv pip install -e ".[dev]"
uv run uvicorn app.main:app --reload --port 8080
curl http://localhost:8080/health
```

Full dev-env setup: see `C:\Users\steve\projects\DEV_SETUP_GUIDE.md`.

## Docker

```bash
docker compose up --build
```

## Deploy

Target: `{{DEPLOY_TARGET}}`.

## License

{{YEAR}} {{AUTHOR}}. MIT.

# Getting started with {{PROJECT_NAME}}

## Prerequisites
Docker Desktop, OR Python 3.11 + `uv`.

## Run (Docker)

```bash
docker compose up --build
curl http://localhost:8080/health
```

## Run (native)

```bash
uv pip install -e ".[dev]"
uv run uvicorn app.main:app --reload --port 8080
```

## Configuration
Copy `.env.example` → `.env`.

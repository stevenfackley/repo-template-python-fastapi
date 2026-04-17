# {{PROJECT_NAME}} — System Design Document

## Stack
Python 3.11, FastAPI, Pydantic v2, uv. Deploy target: {{DEPLOY_TARGET}}.

## Runtime topology
<!-- Services, network zones, external dependencies. -->

## Data
<!-- Stores, migrations. -->

## Object storage (opt-in)
S3-compatible via `src/app/storage.py` (boto3). Cloudflare R2 in prod, MinIO locally.
Env: `S3_ENDPOINT`, `S3_REGION=auto`, `S3_ACCESS_KEY_ID`, `S3_SECRET_ACCESS_KEY`, `S3_BUCKET`, `S3_FORCE_PATH_STYLE=true`, optional `S3_PUBLIC_BASE_URL`.
`get_s3()` / `get_bucket()` raise `RuntimeError` on first use when unconfigured — zero cost until used.

## Auth
<!-- Who calls this service, how they prove identity. -->

## Observability
Stdout JSON logs via `logging`. No Application Insights / Sentry / Datadog (CI-enforced).

## Failure modes
<!-- What happens when each dependency is down? -->

## Scaling
uvicorn workers × N; ASGI behind a reverse proxy.

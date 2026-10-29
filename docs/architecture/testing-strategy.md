# Testing strategy

## Unit
pytest, pure functions, no IO.

## Integration
`httpx.AsyncClient(ASGITransport(app))` — in-process, hits real routes + DI.

## E2E smoke
Curl against deployed container. Runs post-deploy: `deploy-test` / `deploy-prod` check `/health` via `deploy-ec2-ssh`. Locally: `/smoke`.

## E2E integration
Full scenarios. Not automated yet: no scheduled workflow exists. Add one before relying on it.

## Coverage
Target ~70% line on `src/`.

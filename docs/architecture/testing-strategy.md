# Testing strategy

## Unit
pytest, pure functions, no IO.

## Integration
`httpx.AsyncClient(ASGITransport(app))` — in-process, hits real routes + DI.

## E2E smoke
Curl against deployed container. Health + one happy path. Runs post-deploy.

## E2E integration
Full scenarios. Nightly schedule.

## Coverage
Target ~70% line on `src/`.

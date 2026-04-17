from __future__ import annotations

from httpx import AsyncClient


async def test_health_ok(client: AsyncClient) -> None:
    r = await client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["service"] == "{{PROJECT_NAME}}"


async def test_root_ok(client: AsyncClient) -> None:
    r = await client.get("/")
    assert r.status_code == 200

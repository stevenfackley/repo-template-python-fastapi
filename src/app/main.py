from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from app import __version__

app = FastAPI(title="{{PROJECT_NAME}}", version=__version__)


class Health(BaseModel):
    service: str
    status: str
    version: str


@app.get("/health", response_model=Health)
async def health() -> Health:
    return Health(service="{{PROJECT_NAME}}", status="ok", version=__version__)


@app.get("/")
async def root() -> dict[str, str]:
    return {"service": "{{PROJECT_NAME}}", "status": "ok"}

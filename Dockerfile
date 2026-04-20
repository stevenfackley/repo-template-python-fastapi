# Multi-stage Python build. Distroless runtime, non-root.

FROM python:3.14-slim AS build
WORKDIR /src
RUN pip install --no-cache-dir uv==0.5.*

COPY pyproject.toml ./
COPY src/ src/

RUN uv pip install --system --no-cache --target=/install .

FROM gcr.io/distroless/python3-debian12:nonroot AS runtime
WORKDIR /app

COPY --from=build /install /app
COPY --from=build /src/src /app/src

ENV PYTHONPATH=/app:/app/src \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER nonroot
EXPOSE 8080

ENTRYPOINT ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# syntax=docker/dockerfile:1
# Build context: the repository root (uv.lock lives there).
FROM python:3.13-slim AS build
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/opt/venv
WORKDIR /repo
COPY pyproject.toml uv.lock .python-version ./
COPY sdk/pyproject.toml sdk/pyproject.toml
COPY backend/models/ backend/models/
COPY backend/shared/ backend/shared/
COPY backend/services/platform/ backend/services/platform/
RUN uv sync --locked --no-dev --package platform --no-editable

FROM python:3.13-slim AS runtime
ENV PATH=/opt/venv/bin:$PATH \
    PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip uninstall -y pip \
    && useradd --system --uid 10001 --no-create-home simpleerp
COPY --from=build /opt/venv /opt/venv
WORKDIR /app
COPY backend/services/platform/conf/ conf/
COPY backend/shared/context/conf/catalogs/refusal_codes.yaml conf/catalogs/refusal_codes.yaml
RUN mkdir -p logs && chown simpleerp /app/logs
USER simpleerp
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/v1/health', timeout=3)"]
CMD ["uvicorn", "--factory", "erp_platform.api.app_factory:AppFactory.create", "--host", "0.0.0.0", "--port", "8000"]

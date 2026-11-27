from __future__ import annotations

import pytest
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.storage.context.request_context_store import RequestContextStore
from fastapi import FastAPI
from fastapi.testclient import TestClient

from tests.api.middleware.helpers import build_app, load_catalog


@pytest.fixture
def catalog() -> RefusalCatalog:
    return load_catalog()


@pytest.fixture
def app() -> FastAPI:
    return build_app()


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)


@pytest.fixture
def store() -> RequestContextStore:
    return RequestContextStore()

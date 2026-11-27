from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from erp_platform.api.app_factory import AppFactory
from erp_platform.service.contracts.contract_comparator import ContractComparator
from erp_platform.service.contracts.contract_service import ContractService
from erp_platform.storage.contracts.open_api_document_repository import OpenApiDocumentRepository
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import JsonValue


@pytest.fixture
def service_folder() -> Path:
    return Path(__file__).resolve().parents[2]


@pytest.fixture
def app(service_folder: Path, monkeypatch: pytest.MonkeyPatch) -> FastAPI:
    monkeypatch.chdir(service_folder)
    return AppFactory.create()


@pytest.fixture
def document(app: FastAPI) -> Dict[str, JsonValue]:
    return app.openapi()


@pytest.fixture
def contract_service() -> ContractService:
    return ContractService(OpenApiDocumentRepository(), ContractComparator())


@pytest.fixture
def committed_path(service_folder: Path) -> Path:
    return service_folder / "openapi.json"


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    headers = {"X-Company-Id": "C-12", "X-User-Id": "U-7", "Authorization": "Bearer s3cr3t-token-value"}
    return TestClient(app, headers=headers)

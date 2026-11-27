from __future__ import annotations

from typing import Dict

import pytest
from erp_platform.service.contracts.contract_comparator import ContractComparator
from erp_platform.service.contracts.contract_service import ContractService
from erp_platform.storage.contracts.open_api_document_repository import OpenApiDocumentRepository
from pydantic import JsonValue


@pytest.fixture
def generated() -> Dict[str, JsonValue]:
    return {
        "openapi": "3.1.0",
        "info": {"title": "Platform", "version": "1.0.0"},
        "paths": {"/v1/health": {"get": {"responses": {"200": {"description": "Ok"}}}}},
        "components": {
            "schemas": {
                "Health": {
                    "type": "object",
                    "properties": {"status": {"type": "string"}, "version": {"type": "string"}},
                },
            },
        },
    }


@pytest.fixture
def without_version_property() -> Dict[str, JsonValue]:
    return {
        "openapi": "3.1.0",
        "info": {"title": "Platform", "version": "1.0.0"},
        "paths": {"/v1/health": {"get": {"responses": {"200": {"description": "Ok"}}}}},
        "components": {
            "schemas": {
                "Health": {"type": "object", "properties": {"status": {"type": "string"}}},
            },
        },
    }


@pytest.fixture
def service() -> ContractService:
    return ContractService(OpenApiDocumentRepository(), ContractComparator())

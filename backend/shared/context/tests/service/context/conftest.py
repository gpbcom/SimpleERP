from __future__ import annotations

import pytest
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.storage.context.request_context_store import RequestContextStore


@pytest.fixture
def store() -> RequestContextStore:
    return RequestContextStore()


@pytest.fixture
def service(store: RequestContextStore) -> CompanyContextService:
    return CompanyContextService(store)

from __future__ import annotations

from typing import Iterator

import pytest
from erp_context.models.context.request_context import RequestContext
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.storage.context.request_context_store import RequestContextStore

from tests.api.rights.helpers import REQUEST_ID, a_user, load_catalog


@pytest.fixture
def catalog() -> RefusalCatalog:
    return load_catalog()


@pytest.fixture
def context_service() -> CompanyContextService:
    return CompanyContextService(RequestContextStore())


@pytest.fixture
def bound_context(context_service: CompanyContextService) -> Iterator[CompanyContextService]:
    token = context_service.bind(RequestContext(user=a_user(), request_id=REQUEST_ID))
    yield context_service
    context_service.release(token)

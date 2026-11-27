from __future__ import annotations

import logging
from pathlib import Path

import pytest
from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_models.ids.company_id import CompanyId


@pytest.fixture
def catalog() -> RefusalCatalog:
    path = Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "refusal_codes.yaml"
    return RefusalCatalog.load(path)


@pytest.fixture
def user() -> UserContext:
    return UserContext(user_id="user-7", company_id=CompanyId(value="C-1"))


@pytest.fixture
def record() -> RecordRef:
    return RecordRef(record_type="invoice", company_id=CompanyId(value="C-1"), record_id="rec-42")


@pytest.fixture
def other_company_record() -> RecordRef:
    return RecordRef(record_type="invoice", company_id=CompanyId(value="C-2"), record_id="rec-99")


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("tests.rights")

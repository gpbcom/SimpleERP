from __future__ import annotations

from typing import Dict

import pytest
from erp_context.models.context.exceptions import (
    SERecordRefInvalidCompanyId,
    SERecordRefInvalidRecordId,
    SERecordRefInvalidRecordType,
)
from erp_context.models.context.record_ref import RecordRef
from erp_models.ids.company_id import CompanyId
from pydantic import JsonValue, ValidationError


class TestRecordRef:
    def test_defaults(self) -> None:
        reference = RecordRef(record_type="customer", company_id=CompanyId(value="C-12"))
        assert reference.record_id is None
        with pytest.raises(ValidationError):
            RecordRef.model_validate({"company_id": CompanyId(value="C-12")})
        with pytest.raises(ValidationError):
            RecordRef.model_validate({"record_type": "customer"})

    def test_full_valid_construction(self) -> None:
        reference = RecordRef(record_type=" customer ", company_id=CompanyId(value="C-12"), record_id=" K-7 ")
        assert reference.record_type == "customer"
        assert reference.company_id == CompanyId(value="C-12")
        assert reference.record_id == "K-7"

    @pytest.mark.parametrize("name", ["record_id"])
    def test_none_becomes_the_default(self, name: str) -> None:
        reference = RecordRef.model_validate({"record_type": "customer", "company_id": {"value": "C-12"}, name: None})
        assert getattr(reference, name) is None

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("record_type", "", SERecordRefInvalidRecordType),
            ("record_type", "   ", SERecordRefInvalidRecordType),
            ("record_type", None, SERecordRefInvalidRecordType),
            ("record_type", 42, SERecordRefInvalidRecordType),
            ("record_type", True, SERecordRefInvalidRecordType),
            ("company_id", None, SERecordRefInvalidCompanyId),
            ("company_id", 42, SERecordRefInvalidCompanyId),
            ("company_id", True, SERecordRefInvalidCompanyId),
            ("record_id", "", SERecordRefInvalidRecordId),
            ("record_id", "   ", SERecordRefInvalidRecordId),
            ("record_id", 42, SERecordRefInvalidRecordId),
            ("record_id", True, SERecordRefInvalidRecordId),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"record_type": "customer", "company_id": {"value": "C-12"}, "record_id": "K-7"}
        data[name] = value
        with pytest.raises(error):
            RecordRef.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RecordRef.model_validate({"record_type": "customer", "company_id": {"value": "C-12"}, "unknown": 1})

    def test_round_trip(self) -> None:
        reference = RecordRef(record_type="customer", company_id=CompanyId(value="C-12"), record_id="K-7")
        assert RecordRef.model_validate(reference.model_dump()) == reference
        assert RecordRef.model_validate_json(reference.model_dump_json()) == reference

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        reference = RecordRef(record_type="customer", company_id=CompanyId(value="C-12"))
        with pytest.raises(ValidationError):
            reference.record_type = "supplier"

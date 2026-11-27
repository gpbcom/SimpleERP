from __future__ import annotations

import pytest
from erp_models.base.opaque_id import OpaqueId
from erp_models.ids.company_id import CompanyId
from erp_models.ids.exceptions import SECompanyIdInvalidValue, SEInvalidCompanyIdException
from erp_models.ids.record_id import RecordId
from pydantic import JsonValue, ValidationError


class TestCompanyId:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            CompanyId()  # type: ignore[call-arg]

    def test_full_valid_construction(self) -> None:
        company_id = CompanyId(value="  C-12  ")

        assert company_id.value == "C-12"
        assert isinstance(company_id, OpaqueId)
        assert CompanyId.INVALID_VALUE is SECompanyIdInvalidValue

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SECompanyIdInvalidValue):
            CompanyId(value=None)  # type: ignore[arg-type]

    @pytest.mark.parametrize("value", ["", "  ", True, 12, ["C-12"]])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SECompanyIdInvalidValue):
            CompanyId(value=value)  # type: ignore[arg-type]

    def test_the_value_exception_is_a_model_exception_and_not_a_value_error(self) -> None:
        assert issubclass(SECompanyIdInvalidValue, SEInvalidCompanyIdException)
        assert not issubclass(SECompanyIdInvalidValue, ValueError)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CompanyId(value="C-12", other="x")  # type: ignore[call-arg]

    def test_round_trip(self) -> None:
        company_id = CompanyId(value="C-12")

        assert company_id.model_dump(mode="json") == {"value": "C-12"}
        assert company_id.model_dump_json() == '{"value":"C-12"}'
        assert CompanyId.model_validate(company_id.model_dump(mode="json")) == company_id
        assert CompanyId.model_validate_json(company_id.model_dump_json()) == company_id

    def test_a_company_id_never_equals_a_record_id_of_the_same_text(self) -> None:
        assert CompanyId(value="C-12") != RecordId(value="C-12")

    def test_two_company_ids_with_the_same_text_are_equal_and_hash_alike(self) -> None:
        first = CompanyId(value="C-12")
        second = CompanyId(value="C-12")

        assert first == second
        assert hash(first) == hash(second)

    @pytest.mark.parametrize("text", ["C-12", "c-12", "COMPANY_9", "0042"])
    def test_the_text_is_kept_as_given(self, text: str) -> None:
        assert CompanyId(value=text).value == text

    def test_assignment_is_refused(self) -> None:
        company_id = CompanyId(value="C-12")

        with pytest.raises(ValidationError):
            company_id.value = "C-13"  # type: ignore[misc]

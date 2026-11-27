from __future__ import annotations

import pytest
from erp_models.base.opaque_id import OpaqueId
from erp_models.ids.exceptions import SEInvalidRecordIdException, SERecordIdInvalidValue
from erp_models.ids.record_id import RecordId
from pydantic import JsonValue, ValidationError


class TestRecordId:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            RecordId()  # type: ignore[call-arg]

    def test_full_valid_construction(self) -> None:
        record_id = RecordId(value="  R-7  ")

        assert record_id.value == "R-7"
        assert isinstance(record_id, OpaqueId)
        assert RecordId.INVALID_VALUE is SERecordIdInvalidValue

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SERecordIdInvalidValue):
            RecordId(value=None)  # type: ignore[arg-type]

    @pytest.mark.parametrize("value", ["", "  ", True, 12, ["C-12"]])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SERecordIdInvalidValue):
            RecordId(value=value)  # type: ignore[arg-type]

    def test_the_value_exception_is_a_model_exception_and_not_a_value_error(self) -> None:
        assert issubclass(SERecordIdInvalidValue, SEInvalidRecordIdException)
        assert not issubclass(SERecordIdInvalidValue, ValueError)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RecordId(value="R-7", other="x")  # type: ignore[call-arg]

    def test_round_trip(self) -> None:
        record_id = RecordId(value="C-12")

        assert record_id.model_dump(mode="json") == {"value": "C-12"}
        assert record_id.model_dump_json() == '{"value":"C-12"}'
        assert RecordId.model_validate(record_id.model_dump(mode="json")) == record_id
        assert RecordId.model_validate_json(record_id.model_dump_json()) == record_id

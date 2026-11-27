from __future__ import annotations

import pytest
from erp_models.base.exceptions import SEInvalidOpaqueIdException, SEOpaqueIdInvalidValue
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.base.opaque_id import OpaqueId
from pydantic import JsonValue, ValidationError


class TestOpaqueId:
    def test_configuration(self) -> None:
        assert issubclass(OpaqueId, FrozenErpModel)
        assert OpaqueId.INVALID_VALUE is SEOpaqueIdInvalidValue
        assert issubclass(SEOpaqueIdInvalidValue, SEInvalidOpaqueIdException)
        assert not issubclass(SEOpaqueIdInvalidValue, ValueError)

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            OpaqueId()

    def test_full_valid_construction(self) -> None:
        assert OpaqueId(value="C-12").value == "C-12"

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SEOpaqueIdInvalidValue):
            OpaqueId(value=None)

    @pytest.mark.parametrize("value", ["", "   ", True, 12, ["a"]])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEOpaqueIdInvalidValue):
            OpaqueId(value=value)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            OpaqueId(value="C-12", other="x")

    def test_round_trip(self) -> None:
        original = OpaqueId(value="C-12")
        assert OpaqueId.model_validate(original.model_dump(mode="json")) == original
        assert OpaqueId.model_validate_json(original.model_dump_json()) == original

    def test_the_text_is_stripped(self) -> None:
        assert OpaqueId(value=" C-12 ").value == "C-12"

    def test_ids_with_the_same_value_are_equal_and_hash_alike(self) -> None:
        assert OpaqueId(value="C-12") == OpaqueId(value=" C-12")
        assert hash(OpaqueId(value="C-12")) == hash(OpaqueId(value="C-12"))

    def test_assignment_is_refused(self) -> None:
        instance = OpaqueId(value="C-12")
        with pytest.raises(ValidationError):
            instance.value = "C-13"

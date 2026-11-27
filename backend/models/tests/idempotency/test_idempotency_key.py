from __future__ import annotations

import pytest
from erp_models.base.opaque_id import OpaqueId
from erp_models.idempotency.exceptions import SEIdempotencyKeyInvalidValue, SEInvalidIdempotencyKeyException
from erp_models.idempotency.idempotency_key import IdempotencyKey
from pydantic import JsonValue, ValidationError


class TestIdempotencyKey:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            IdempotencyKey.model_validate({})

    def test_full_valid_construction(self) -> None:
        key = IdempotencyKey(value="  k-1  ")
        assert key.value == "k-1"
        assert isinstance(key, OpaqueId)

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SEIdempotencyKeyInvalidValue):
            IdempotencyKey.model_validate({"value": None})

    @pytest.mark.parametrize("value", ["", "  ", True, 12, ["k"]])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEIdempotencyKeyInvalidValue):
            IdempotencyKey.model_validate({"value": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            IdempotencyKey.model_validate({"value": "k-1", "other": "x"})

    def test_round_trip(self) -> None:
        key = IdempotencyKey(value="k-1")
        assert IdempotencyKey.model_validate(key.model_dump(mode="json")) == key
        assert IdempotencyKey.model_validate_json(key.model_dump_json()) == key

    def test_the_invalid_value_exception_is_the_one_of_the_model(self) -> None:
        assert IdempotencyKey.INVALID_VALUE is SEIdempotencyKeyInvalidValue

    def test_the_exceptions_form_a_hierarchy_outside_value_error(self) -> None:
        assert issubclass(SEIdempotencyKeyInvalidValue, SEInvalidIdempotencyKeyException)
        assert not issubclass(SEInvalidIdempotencyKeyException, ValueError)
        assert not issubclass(SEIdempotencyKeyInvalidValue, ValueError)

    def test_a_write_repeated_with_its_key_carries_an_equal_key(self) -> None:
        first = IdempotencyKey(value="k-1")
        repeated = IdempotencyKey(value=" k-1 ")
        assert first == repeated
        assert hash(first) == hash(repeated)

    def test_the_keys_of_repeated_writes_make_one_key(self) -> None:
        keys = {IdempotencyKey(value="k-1"), IdempotencyKey(value=" k-1 "), IdempotencyKey(value="k-1")}
        assert len(keys) == 1

    def test_different_keys_are_kept_apart(self) -> None:
        keys = {IdempotencyKey(value="k-1"), IdempotencyKey(value="k-2")}
        assert len(keys) == 2

    def test_a_key_never_equals_an_opaque_id_with_the_same_text(self) -> None:
        assert IdempotencyKey(value="k-1") != OpaqueId(value="k-1")

    def test_assignment_is_refused(self) -> None:
        key = IdempotencyKey(value="k-1")
        with pytest.raises(ValidationError):
            key.value = "k-2"

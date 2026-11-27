from __future__ import annotations

import pytest
from erp_models.base.erp_model import ErpModel
from erp_models.base.frozen_erp_model import FrozenErpModel
from pydantic import Field, JsonValue, ValidationError, create_model


class TestFrozenErpModel:
    def sample(self) -> type[FrozenErpModel]:
        return create_model(
            "SampleModel",
            __base__=FrozenErpModel,
            name=(str, Field(default="a", description="A name.")),
        )

    def test_configuration(self) -> None:
        assert issubclass(FrozenErpModel, ErpModel)
        assert FrozenErpModel.model_config.get("extra") == "forbid"
        assert FrozenErpModel.model_config.get("frozen") is True

    def test_defaults(self) -> None:
        assert self.sample()().name == "a"

    def test_full_valid_construction(self) -> None:
        assert self.sample()(name="b").name == "b"

    def test_none_becomes_the_default(self) -> None:
        model = self.sample()
        assert model().name == "a"
        with pytest.raises(ValidationError):
            model(name=None)

    @pytest.mark.parametrize("value", [12, ["a"], {"a": 1}, True])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(ValidationError):
            self.sample()(name=value)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            self.sample()(name="b", other="c")
        with pytest.raises(ValidationError):
            FrozenErpModel(other="c")

    def test_round_trip(self) -> None:
        model = self.sample()
        original = model(name="b")
        assert model.model_validate(original.model_dump(mode="json")) == original
        assert model.model_validate_json(original.model_dump_json()) == original

    def test_assignment_is_refused(self) -> None:
        instance = self.sample()(name="b")
        with pytest.raises(ValidationError):
            instance.name = "c"

    def test_equal_instances_hash_alike(self) -> None:
        model = self.sample()
        assert hash(model(name="b")) == hash(model(name="b"))

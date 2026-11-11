from __future__ import annotations

from decimal import Decimal
from typing import Dict

import pytest
from pydantic import JsonValue

from ai_cost.models.pricing.exceptions import SEModelPriceInvalidPrice, SEModelPriceInvalidText
from ai_cost.models.pricing.model_price import ModelPrice


class TestModelPrice:
    def price_fields(self) -> Dict[str, JsonValue]:
        return {
            "name": "Claude Haiku 5.5",
            "match": "claude-haiku-5-5",
            "input_per_mtok": "0.10",
            "output_per_mtok": "0.50",
            "cache_write_5m_per_mtok": "0.125",
            "cache_write_1h_per_mtok": "0.20",
            "cache_read_per_mtok": "0.01",
        }

    def test_defaults(self) -> None:
        price = ModelPrice(name="x", match="x", input_per_mtok=Decimal("1"), output_per_mtok=Decimal("2"))
        assert (price.cache_write_5m_per_mtok, price.cache_write_1h_per_mtok, price.cache_read_per_mtok) == (
            Decimal("0"),
            Decimal("0"),
            Decimal("0"),
        )

    def test_full_valid_construction(self) -> None:
        price = ModelPrice.model_validate(self.price_fields())
        assert price.cache_write_5m_per_mtok == Decimal("0.125")
        assert price.match == "claude-haiku-5-5"

    @pytest.mark.parametrize("name", ["cache_write_5m_per_mtok", "cache_write_1h_per_mtok", "cache_read_per_mtok"])
    def test_none_becomes_the_default(self, name: str) -> None:
        fields = self.price_fields()
        fields[name] = None
        assert getattr(ModelPrice.model_validate(fields), name) == Decimal("0")

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("name", "", SEModelPriceInvalidText),
            ("match", None, SEModelPriceInvalidText),
            ("input_per_mtok", None, SEModelPriceInvalidPrice),
            ("output_per_mtok", "-1", SEModelPriceInvalidPrice),
            ("cache_read_per_mtok", True, SEModelPriceInvalidPrice),
            ("cache_write_1h_per_mtok", "cheap", SEModelPriceInvalidPrice),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = self.price_fields()
        fields[name] = value
        with pytest.raises(error):
            ModelPrice.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            ModelPrice.model_validate({**self.price_fields(), "cache_write_per_mtok": "1"})

    def test_round_trip(self) -> None:
        price = ModelPrice.model_validate(self.price_fields())
        assert ModelPrice.model_validate_json(price.model_dump_json()) == price

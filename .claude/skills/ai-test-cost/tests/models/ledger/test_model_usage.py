from __future__ import annotations

from decimal import Decimal

import pytest
from pydantic import JsonValue

from ai_cost.models.ledger.exceptions import SEModelUsageInvalidCostUsd, SEModelUsageInvalidTokens
from ai_cost.models.ledger.model_usage import ModelUsage
from tests.models.ledger.helpers import usage_fields


class TestModelUsage:
    def test_defaults(self) -> None:
        usage = ModelUsage()
        assert (usage.input_tokens, usage.output_tokens, usage.cost_usd) == (0, 0, Decimal("0"))

    def test_full_valid_construction(self) -> None:
        usage = ModelUsage.model_validate(usage_fields())
        assert usage.cache_write_1h_tokens == 5
        assert usage.cost_usd == Decimal("0.0123")

    @pytest.mark.parametrize(
        "name",
        [
            "input_tokens",
            "output_tokens",
            "cache_read_tokens",
            "cache_write_5m_tokens",
            "cache_write_1h_tokens",
            "cost_usd",
        ],
    )
    def test_none_becomes_the_default(self, name: str) -> None:
        fields = usage_fields()
        fields[name] = None
        assert getattr(ModelUsage.model_validate(fields), name) == 0

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("input_tokens", -1, SEModelUsageInvalidTokens),
            ("output_tokens", True, SEModelUsageInvalidTokens),
            ("cache_read_tokens", "many", SEModelUsageInvalidTokens),
            ("cache_write_5m_tokens", 1.5, SEModelUsageInvalidTokens),
            ("cost_usd", "-0.01", SEModelUsageInvalidCostUsd),
            ("cost_usd", "free", SEModelUsageInvalidCostUsd),
            ("cost_usd", False, SEModelUsageInvalidCostUsd),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = usage_fields()
        fields[name] = value
        with pytest.raises(error):
            ModelUsage.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            ModelUsage.model_validate({**usage_fields(), "calls": 3})

    def test_round_trip(self) -> None:
        usage = ModelUsage.model_validate(usage_fields())
        assert ModelUsage.model_validate_json(usage.model_dump_json()) == usage

    def test_the_cost_is_a_json_number(self) -> None:
        assert '"cost_usd":0.0123' in ModelUsage.model_validate(usage_fields()).model_dump_json()

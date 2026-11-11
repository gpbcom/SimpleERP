from __future__ import annotations

from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue

from ai_cost.models.pricing.exceptions import (
    SEPriceTableInvalidPrices,
    SEPriceTableInvalidReadOn,
    SEPriceTableInvalidSource,
    SEPriceTableUnreadable,
)
from ai_cost.models.pricing.price_table import PriceTable


class TestPriceTable:
    SKILL_DIR = Path(__file__).resolve().parents[3]

    def table_fields(self) -> Dict[str, JsonValue]:
        return {
            "source": "Anthropic pricing page",
            "read_on": "2026-11-10",
            "prices": [
                {"name": "Claude Opus 5.5", "match": "claude-opus-5-5", "input_per_mtok": 4, "output_per_mtok": 20}
            ],
        }

    def test_defaults(self) -> None:
        assert PriceTable.model_validate(self.table_fields()).prices[0].cache_read_per_mtok == Decimal("0")

    def test_full_valid_construction(self) -> None:
        table = PriceTable.model_validate(self.table_fields())
        assert table.read_on == date(2026, 11, 10)
        assert table.prices[0].output_per_mtok == Decimal("20")

    def test_none_becomes_the_default(self) -> None:
        fields = self.table_fields()
        fields["source"] = None
        with pytest.raises(SEPriceTableInvalidSource):
            PriceTable.model_validate(fields)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("source", " ", SEPriceTableInvalidSource),
            ("read_on", "last week", SEPriceTableInvalidReadOn),
            ("read_on", None, SEPriceTableInvalidReadOn),
            ("prices", [], SEPriceTableInvalidPrices),
            ("prices", "claude", SEPriceTableInvalidPrices),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = self.table_fields()
        fields[name] = value
        with pytest.raises(error):
            PriceTable.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            PriceTable.model_validate({**self.table_fields(), "unknown": {}})

    def test_round_trip(self) -> None:
        table = PriceTable.model_validate(self.table_fields())
        assert PriceTable.model_validate_json(table.model_dump_json()) == table

    def test_the_checked_in_prices_cover_the_current_models(self) -> None:
        table = PriceTable.load(self.SKILL_DIR / "conf" / "prices.yaml")
        assert [price.match for price in table.prices] == [
            "claude-fable-5-1",
            "claude-opus-5-5",
            "claude-sonnet-5-5",
            "claude-haiku-5-5",
        ]
        assert "https://platform.claude.com/docs/en/about-claude/pricing" in table.source
        assert table.read_on == date(2026, 11, 10)

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEPriceTableUnreadable):
            PriceTable.load(tmp_path / "missing.yaml")

from __future__ import annotations

from decimal import Decimal

import pytest

from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.service.pricing.price_book import PriceBook


class TestPriceBook:
    @pytest.mark.parametrize(
        ("model", "name"),
        [
            ("claude-haiku-5-5", "Claude Haiku 5.5"),
            ("claude-opus-5-5", "Claude Opus 5.5"),
            ("anthropic.claude-sonnet-5-5", "Claude Sonnet 5.5"),
            ("claude-fable-5-1", "Claude Fable 5.1"),
            ("claude-mystery-9", "Claude Fable 5.1"),
            ("unknown", "Claude Fable 5.1"),
        ],
    )
    def test_a_model_finds_its_price_and_an_unknown_one_the_most_expensive(
        self, prices: PriceBook, model: str, name: str
    ) -> None:
        assert prices.price_of(model).name == name

    def test_every_kind_of_token_is_priced_exactly(self, prices: PriceBook) -> None:
        million = 1_000_000
        usage = ModelUsage(
            input_tokens=million,
            output_tokens=million,
            cache_read_tokens=million,
            cache_write_5m_tokens=million,
            cache_write_1h_tokens=million,
        )
        priced = prices.priced("claude-haiku-5-5", usage)
        assert priced.cost_usd == Decimal("0.10") + Decimal("0.50") + Decimal("0.01") + Decimal("0.125") + Decimal(
            "0.20"
        )
        assert priced.input_tokens == million

    def test_a_small_cost_is_kept_to_the_millionth_of_a_dollar(self, prices: PriceBook) -> None:
        assert prices.priced("claude-opus-5-5", ModelUsage(input_tokens=3)).cost_usd == Decimal("0.000012")

    def test_the_source_names_the_page_and_its_date(self, prices: PriceBook) -> None:
        assert "https://platform.claude.com/docs/en/about-claude/pricing" in prices.source
        assert "2026-11-10" in prices.source

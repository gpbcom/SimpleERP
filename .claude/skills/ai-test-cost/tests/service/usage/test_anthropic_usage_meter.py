from __future__ import annotations

import logging
from datetime import UTC, datetime
from decimal import Decimal

import httpx
import pytest

from ai_cost.service.pricing.price_book import PriceBook
from ai_cost.service.usage.anthropic_usage_meter import AnthropicUsageMeter
from ai_cost.service.usage.exceptions import SEUsageMeasureFailedError
from ai_cost.storage.usage.anthropic_usage_client import AnthropicUsageClient
from tests.storage.usage.helpers import ADMIN_SECRET, usage_page, usage_result
from tests.storage.usage.usage_report_handler import UsageReportHandler


class TestAnthropicUsageMeter:
    START = datetime(2026, 11, 10, 9, 0, tzinfo=UTC)
    END = datetime(2026, 11, 10, 9, 5, tzinfo=UTC)

    def meter(self, handler: UsageReportHandler, prices: PriceBook, logger: logging.Logger) -> AnthropicUsageMeter:
        client = AnthropicUsageClient(None, logger, transport=httpx.MockTransport(handler))
        return AnthropicUsageMeter(client, prices, logger)

    def test_the_measure_prices_the_reported_tokens(
        self, monkeypatch: pytest.MonkeyPatch, prices: PriceBook, logger: logging.Logger
    ) -> None:
        monkeypatch.setenv("ANTHROPIC_ADMIN_KEY", ADMIN_SECRET)
        meter = self.meter(
            UsageReportHandler([usage_page([usage_result("claude-opus-5-5", 1000, 100)])]), prices, logger
        )
        usage = meter.measure(self.START, self.END)
        expected = (Decimal(1000) * 4 + Decimal(100) * 20 + Decimal(100) * 5) / 1_000_000
        assert usage["claude-opus-5-5"].cost_usd == expected
        assert (meter.measurable, meter.ready()) == (True, True)

    def test_the_meter_is_not_ready_without_the_admin_key(
        self, monkeypatch: pytest.MonkeyPatch, prices: PriceBook, logger: logging.Logger
    ) -> None:
        monkeypatch.delenv("ANTHROPIC_ADMIN_KEY", raising=False)
        meter = self.meter(UsageReportHandler([usage_page([])]), prices, logger)
        assert (meter.measurable, meter.ready()) == (True, False)
        with pytest.raises(SEUsageMeasureFailedError):
            meter.measure(self.START, self.END)

    def test_a_failed_report_is_a_failed_measure(
        self, monkeypatch: pytest.MonkeyPatch, prices: PriceBook, logger: logging.Logger
    ) -> None:
        monkeypatch.setenv("ANTHROPIC_ADMIN_KEY", ADMIN_SECRET)
        meter = self.meter(UsageReportHandler([{}], status_code=500), prices, logger)
        with pytest.raises(SEUsageMeasureFailedError):
            meter.measure(self.START, self.END)

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import Optional

import httpx
import pytest

from ai_cost.storage.usage.anthropic_usage_client import AnthropicUsageClient
from ai_cost.storage.usage.exceptions import SEAnthropicUsageRequestFailedError, SEAnthropicUsageUnavailableError
from tests.storage.usage.helpers import ADMIN_SECRET, usage_page, usage_result
from tests.storage.usage.usage_report_handler import UsageReportHandler


class TestAnthropicUsageClient:
    START = datetime(2026, 11, 10, 9, 0, 42, tzinfo=UTC)
    END = datetime(2026, 11, 10, 9, 3, 5, tzinfo=UTC)

    def client(
        self, handler: UsageReportHandler, logger: logging.Logger, api_key_id: Optional[str] = None
    ) -> AnthropicUsageClient:
        return AnthropicUsageClient(api_key_id, logger, transport=httpx.MockTransport(handler))

    def test_without_the_admin_key_the_report_is_unavailable(
        self, monkeypatch: pytest.MonkeyPatch, logger: logging.Logger
    ) -> None:
        monkeypatch.delenv("ANTHROPIC_ADMIN_KEY", raising=False)
        client = self.client(UsageReportHandler([usage_page([])]), logger)
        assert client.configured is False
        with pytest.raises(SEAnthropicUsageUnavailableError):
            client.usage(self.START, self.END)

    def test_the_request_follows_the_usage_report_contract(
        self, monkeypatch: pytest.MonkeyPatch, logger: logging.Logger
    ) -> None:
        monkeypatch.setenv("ANTHROPIC_ADMIN_KEY", ADMIN_SECRET)
        handler = UsageReportHandler([usage_page([])])
        self.client(handler, logger, api_key_id="apikey_01").usage(self.START, self.END)
        request = handler.requests[0]
        assert str(request.url).startswith("https://api.anthropic.com/v1/organizations/usage_report/messages?")
        assert request.headers["x-api-key"] == ADMIN_SECRET
        assert request.headers["anthropic-version"] == "2023-06-01"
        assert request.url.params.get_list("starting_at") == ["2026-11-10T09:00:00Z"]
        assert request.url.params.get_list("ending_at") == ["2026-11-10T09:04:00Z"]
        assert request.url.params.get_list("bucket_width") == ["1m"]
        assert request.url.params.get_list("group_by[]") == ["model"]
        assert request.url.params.get_list("api_key_ids[]") == ["apikey_01"]

    def test_the_whole_organisation_is_read_without_an_api_key_id(
        self, monkeypatch: pytest.MonkeyPatch, logger: logging.Logger
    ) -> None:
        monkeypatch.setenv("ANTHROPIC_ADMIN_KEY", ADMIN_SECRET)
        handler = UsageReportHandler([usage_page([])])
        self.client(handler, logger).usage(self.START, self.END)
        assert "api_key_ids[]" not in handler.requests[0].url.params

    def test_tokens_add_up_per_model_across_buckets_and_pages(
        self, monkeypatch: pytest.MonkeyPatch, logger: logging.Logger
    ) -> None:
        monkeypatch.setenv("ANTHROPIC_ADMIN_KEY", ADMIN_SECRET)
        handler = UsageReportHandler(
            [
                usage_page(
                    [usage_result("claude-haiku-5-5", 1000, 200), usage_result("claude-opus-5-5", 10, 5)], "page_2"
                ),
                usage_page([usage_result("claude-haiku-5-5", 500, 100, cache_read=40), usage_result(None, 1, 1)]),
            ]
        )
        usage = self.client(handler, logger).usage(self.START, self.END)
        assert handler.requests[1].url.params.get_list("page") == ["page_2"]
        haiku = usage["claude-haiku-5-5"]
        assert (haiku.input_tokens, haiku.output_tokens, haiku.cache_read_tokens, haiku.cache_write_5m_tokens) == (
            1500,
            300,
            40,
            200,
        )
        assert set(usage) == {"claude-haiku-5-5", "claude-opus-5-5", "unknown"}

    @pytest.mark.parametrize(
        "handler",
        [
            UsageReportHandler([{"type": "error", "error": {"type": "authentication_error"}}], status_code=401),
            UsageReportHandler([{"data": "nothing"}]),
            UsageReportHandler([{"data": [{"results": [{"model": "x", "output_tokens": "many"}]}]}]),
            UsageReportHandler([usage_page([])], failure=httpx.ConnectError("no route")),
        ],
        ids=["unauthorised", "no-buckets", "bad-tokens", "unreachable"],
    )
    def test_a_failed_request_is_reported_without_the_admin_key(
        self,
        monkeypatch: pytest.MonkeyPatch,
        logger: logging.Logger,
        caplog: pytest.LogCaptureFixture,
        handler: UsageReportHandler,
    ) -> None:
        monkeypatch.setenv("ANTHROPIC_ADMIN_KEY", ADMIN_SECRET)
        caplog.set_level(logging.DEBUG)
        with pytest.raises(SEAnthropicUsageRequestFailedError) as raised:
            self.client(handler, logger).usage(self.START, self.END)
        assert ADMIN_SECRET not in str(raised.value)
        assert ADMIN_SECRET not in caplog.text

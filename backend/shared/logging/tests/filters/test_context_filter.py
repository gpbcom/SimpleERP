from __future__ import annotations

import logging

import pytest
from erp_logging.context.log_context import LogContext
from erp_logging.filters.context_filter import ContextFilter
from erp_logging.models.exceptions import SELoggingConfigInvalidError


class TestContextFilter:
    def a_record(self) -> logging.LogRecord:
        return logging.LogRecord("test", logging.INFO, __file__, 1, "message", None, None)

    def test_the_record_carries_the_service_given(self) -> None:
        record = self.a_record()
        ContextFilter("customers").filter(record)
        assert record.service == "customers"

    def test_the_record_carries_the_bound_company_and_request(self) -> None:
        LogContext.bind("c-1", "r-1")
        record = self.a_record()
        ContextFilter("customers").filter(record)
        assert record.company == "c-1"
        assert record.request == "r-1"

    def test_unbound_values_are_written_as_a_dash(self) -> None:
        record = self.a_record()
        ContextFilter("customers").filter(record)
        assert record.company == ContextFilter.UNSET == "-"
        assert record.request == "-"

    def test_the_filter_always_returns_true(self) -> None:
        assert ContextFilter("customers").filter(self.a_record()) is True
        LogContext.bind("c-1", "r-1")
        assert ContextFilter("customers").filter(self.a_record()) is True

    @pytest.mark.parametrize("service", ["", "   "])
    def test_a_blank_service_is_refused(self, service: str) -> None:
        with pytest.raises(SELoggingConfigInvalidError):
            ContextFilter(service)

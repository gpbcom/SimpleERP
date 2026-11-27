from __future__ import annotations

import asyncio
from typing import Optional, Tuple

from erp_logging.context.log_context import LogContext


class TestLogContext:
    def test_both_values_are_none_by_default(self) -> None:
        assert LogContext.company() is None
        assert LogContext.request() is None

    def test_a_bound_company_and_request_are_read_back(self) -> None:
        LogContext.bind("company-1", "request-1")
        assert LogContext.company() == "company-1"
        assert LogContext.request() == "request-1"

    def test_clear_resets_both_values(self) -> None:
        LogContext.bind("company-1", "request-1")
        LogContext.clear()
        assert LogContext.company() is None
        assert LogContext.request() is None

    async def bind_and_read(self, company: str, request: str) -> Tuple[Optional[str], Optional[str]]:
        LogContext.bind(company, request)
        await asyncio.sleep(0)
        return LogContext.company(), LogContext.request()

    async def bind_in_child(self) -> None:
        LogContext.bind("child-company", "child-request")

    async def test_two_tasks_each_read_back_their_own_values(self) -> None:
        first, second = await asyncio.gather(
            self.bind_and_read("company-a", "request-a"),
            self.bind_and_read("company-b", "request-b"),
        )
        assert first == ("company-a", "request-a")
        assert second == ("company-b", "request-b")

    async def test_a_value_bound_in_a_task_does_not_leak_to_the_caller(self) -> None:
        await asyncio.create_task(self.bind_in_child())
        assert LogContext.company() is None
        assert LogContext.request() is None

from __future__ import annotations

import asyncio
import logging
from typing import Optional

import pytest
from erp_context.models.context.request_context import RequestContext
from erp_context.models.context.user_context import UserContext
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessNoCompanyError
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.storage.context.request_context_store import RequestContextStore
from erp_models.ids.company_id import CompanyId


class TestCompanyContextService:
    def a_context(self, company: str = "C-1") -> RequestContext:
        user = UserContext(user_id="U-1", company_id=CompanyId(value=company))
        return RequestContext(user=user, request_id="R-1")

    def test_a_bound_context_is_read_through_the_store_peek_and_current(
        self,
        store: RequestContextStore,
        service: CompanyContextService,
    ) -> None:
        context = self.a_context("C-1")
        token = service.bind(context)
        try:
            assert store.get() == context
            assert service.peek() == context
            assert service.current() == context
        finally:
            service.release(token)

    def test_nothing_is_bound_after_release(
        self,
        store: RequestContextStore,
        service: CompanyContextService,
    ) -> None:
        token = service.bind(self.a_context("C-1"))
        service.release(token)
        assert store.get() is None
        assert service.peek() is None

    def test_current_without_a_context_is_refused_as_no_company(self, service: CompanyContextService) -> None:
        with pytest.raises(SEAccessNoCompanyError) as raised:
            service.current()
        assert raised.value.reason == RefusalReason.NO_COMPANY

    def test_current_without_a_context_logs_a_warning_or_an_error(
        self, service: CompanyContextService, caplog: pytest.LogCaptureFixture
    ) -> None:
        with caplog.at_level(logging.DEBUG), pytest.raises(SEAccessNoCompanyError):
            service.current()
        assert any(record.levelno in (logging.WARNING, logging.ERROR) for record in caplog.records)

    async def bind_and_read(self, service: CompanyContextService, context: RequestContext) -> Optional[CompanyId]:
        service.bind(context)
        await asyncio.sleep(0)
        current = service.peek()
        return current.user.company_id if current else None

    async def test_two_tasks_that_bind_different_companies_each_see_their_own(
        self, service: CompanyContextService
    ) -> None:
        first, second = await asyncio.gather(
            asyncio.create_task(self.bind_and_read(service, self.a_context("C-1"))),
            asyncio.create_task(self.bind_and_read(service, self.a_context("C-2"))),
        )
        assert first == CompanyId(value="C-1")
        assert second == CompanyId(value="C-2")

    async def test_a_context_bound_in_a_task_does_not_leak_to_the_caller(self, service: CompanyContextService) -> None:
        await asyncio.create_task(self.bind_and_read(service, self.a_context("C-1")))
        assert service.peek() is None

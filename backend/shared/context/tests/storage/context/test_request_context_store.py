from __future__ import annotations

import asyncio
from typing import Optional

from erp_context.models.context.request_context import RequestContext
from erp_context.models.context.user_context import UserContext
from erp_context.storage.context.request_context_store import RequestContextStore
from erp_models.ids.company_id import CompanyId


class TestRequestContextStore:
    def a_context(self, company: str = "C-1") -> RequestContext:
        user = UserContext(user_id="U-1", company_id=CompanyId(value=company))
        return RequestContext(user=user, request_id="R-1")

    def test_nothing_is_bound_by_default(self) -> None:
        assert RequestContextStore().get() is None

    def test_a_bound_context_is_read_back(self) -> None:
        store = RequestContextStore()
        context = self.a_context()
        token = store.set(context)
        try:
            assert store.get() == context
        finally:
            store.reset(token)

    def test_reset_restores_what_was_bound_before(self) -> None:
        store = RequestContextStore()
        outer = store.set(self.a_context("C-1"))
        inner = store.set(self.a_context("C-2"))
        store.reset(inner)
        current = store.get()
        assert current is not None
        assert current.user.company_id == CompanyId(value="C-1")
        store.reset(outer)
        assert store.get() is None

    async def bind_and_read(self, store: RequestContextStore, company: str) -> Optional[CompanyId]:
        store.set(self.a_context(company))
        await asyncio.sleep(0)
        current = store.get()
        return current.user.company_id if current else None

    async def test_two_tasks_each_see_their_own_context(self) -> None:
        store = RequestContextStore()
        first, second = await asyncio.gather(
            asyncio.create_task(self.bind_and_read(store, "C-1")),
            asyncio.create_task(self.bind_and_read(store, "C-2")),
        )
        assert first == CompanyId(value="C-1")
        assert second == CompanyId(value="C-2")

    async def test_a_context_bound_in_a_task_does_not_leak_to_the_caller(self) -> None:
        store = RequestContextStore()
        await asyncio.create_task(self.bind_and_read(store, "C-1"))
        assert store.get() is None

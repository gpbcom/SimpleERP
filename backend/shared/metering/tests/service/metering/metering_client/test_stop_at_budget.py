from __future__ import annotations

import logging
from decimal import Decimal
from typing import Callable, List, Tuple

import httpx
import pytest
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.models.metering.exceptions import SEMeteringBudgetExhaustedError
from erp_metering.service.metering.metering_client import MeteringClient
from erp_metering.storage.events.usage_event_writer import UsageEventWriter
from erp_metering.storage.servers.metering_server_repository import MeteringServerRepository
from erp_models.events.event_envelope import EventEnvelope
from erp_models.money.money import Money
from erp_outbox.storage.outbox_store import OutboxStore

from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


class TestStopAtBudget:
    def make_client(self, metering_http: httpx.AsyncClient, outbox_writer: OutboxStore) -> MeteringClient:
        return MeteringClient(MeteringServerRepository(metering_http), UsageEventWriter(outbox_writer))

    async def work(self, awaited: List[str]) -> Tuple[str, Money]:
        awaited.append("work")
        return "quote sent", Money(amount=Decimal("9.50"), currency="EUR")

    async def test_a_call_without_legal_duty_is_refused_when_the_budget_is_spent(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("0")
        client = self.make_client(metering_http, outbox_writer)
        awaited: List[str] = []

        with pytest.raises(SEMeteringBudgetExhaustedError):
            await client.call(paid_call_factory(amount=Decimal("10.00")), lambda: self.work(awaited))

        assert awaited == []

    async def test_a_refused_call_only_reaches_the_budget_check(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("0")
        client = self.make_client(metering_http, outbox_writer)
        awaited: List[str] = []

        with pytest.raises(SEMeteringBudgetExhaustedError):
            await client.call(paid_call_factory(amount=Decimal("10.00")), lambda: self.work(awaited))

        assert metering_server.requests == [("POST", "/v1/budget-checks")]
        assert metering_server.reservations == {}
        assert metering_server.settlements == []

    async def test_a_refused_call_writes_no_usage_event(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("0")
        client = self.make_client(metering_http, outbox_writer)
        awaited: List[str] = []

        with pytest.raises(SEMeteringBudgetExhaustedError):
            await client.call(paid_call_factory(amount=Decimal("10.00")), lambda: self.work(awaited))

        assert outbox_events() == []

    async def test_a_call_with_a_legal_duty_goes_on_when_the_budget_is_spent(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("0")
        client = self.make_client(metering_http, outbox_writer)
        awaited: List[str] = []

        result = await client.call(
            paid_call_factory(amount=Decimal("10.00"), legal_duty=True), lambda: self.work(awaited)
        )

        assert result == "quote sent"
        assert awaited == ["work"]
        events = outbox_events()
        assert len(events) == 1
        assert UsageEvent.model_validate(events[0].payload).over_budget is True

    async def test_a_legal_duty_call_over_budget_is_reported_with_a_warning(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        metering_server.remaining = Decimal("0")
        client = self.make_client(metering_http, outbox_writer)
        awaited: List[str] = []

        with caplog.at_level(logging.DEBUG):
            await client.call(paid_call_factory(amount=Decimal("10.00"), legal_duty=True), lambda: self.work(awaited))

        messages = [record.getMessage().lower() for record in caplog.records if record.levelno == logging.WARNING]
        assert any("exhausted" in message and "legal duty" in message for message in messages)

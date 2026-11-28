from __future__ import annotations

import logging
from decimal import Decimal
from typing import Callable, List, Tuple

import httpx
import pytest
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.models.metering.exceptions import SEMeteringServerUnavailableError
from erp_metering.service.metering.metering_client import MeteringClient
from erp_metering.storage.events.usage_event_writer import UsageEventWriter
from erp_metering.storage.servers.metering_server_repository import MeteringServerRepository
from erp_models.events.event_envelope import EventEnvelope
from erp_models.money.money import Money
from erp_outbox.storage.outbox_store import OutboxStore

from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


class TestUnavailableServer:
    ACTUAL_COST: Decimal = Decimal("5.00")

    def client(self, metering_http: httpx.AsyncClient, outbox_writer: OutboxStore) -> MeteringClient:
        return MeteringClient(MeteringServerRepository(metering_http), UsageEventWriter(outbox_writer))

    async def work(self) -> Tuple[str, Money]:
        self.awaited += 1
        return "e-invoice sent", Money(amount=self.ACTUAL_COST, currency="EUR")

    async def test_a_call_without_legal_duty_is_refused(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.available = False
        self.awaited = 0

        with pytest.raises(SEMeteringServerUnavailableError):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(legal_duty=False), self.work)

    async def test_the_work_of_a_refused_call_is_never_awaited(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.available = False
        self.awaited = 0

        with pytest.raises(SEMeteringServerUnavailableError):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(legal_duty=False), self.work)

        assert self.awaited == 0

    async def test_a_call_with_legal_duty_returns_the_result_of_the_work(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.available = False
        self.awaited = 0

        result = await self.client(metering_http, outbox_writer).call(paid_call_factory(legal_duty=True), self.work)

        assert result == "e-invoice sent"
        assert self.awaited == 1

    async def test_a_call_with_legal_duty_writes_one_usage_event_without_reservation(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.available = False
        self.awaited = 0

        await self.client(metering_http, outbox_writer).call(paid_call_factory(legal_duty=True), self.work)

        events = outbox_events()
        assert len(events) == 1
        event = UsageEvent.model_validate(events[0].payload)
        assert event.reservation_id is None

    async def test_a_call_with_legal_duty_logs_a_warning(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        metering_server.available = False
        self.awaited = 0

        with caplog.at_level(logging.DEBUG):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(legal_duty=True), self.work)

        assert any(record.levelno == logging.WARNING for record in caplog.records)

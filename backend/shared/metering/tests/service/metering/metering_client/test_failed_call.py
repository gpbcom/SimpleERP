from __future__ import annotations

import logging
from decimal import Decimal
from typing import Callable, List, Tuple

import httpx
import pytest
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.service.metering.metering_client import MeteringClient
from erp_metering.storage.events.usage_event_writer import UsageEventWriter
from erp_metering.storage.servers.metering_server_repository import MeteringServerRepository
from erp_models.events.event_envelope import EventEnvelope
from erp_models.money.money import Money
from erp_outbox.storage.outbox_store import OutboxStore

from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


class TestFailedCall:
    ACTUAL_COST: Decimal = Decimal("8.40")

    def client(self, metering_http: httpx.AsyncClient, outbox_writer: OutboxStore) -> MeteringClient:
        return MeteringClient(MeteringServerRepository(metering_http), UsageEventWriter(outbox_writer))

    async def failing_work(self) -> Tuple[str, Money]:
        raise ValueError("the paid call broke")

    async def work_that_takes_the_server_down(self) -> Tuple[str, Money]:
        self.server.available = False
        return "payroll declared", Money(amount=self.ACTUAL_COST, currency="EUR")

    async def test_an_exception_of_the_work_is_re_raised_unchanged(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        with pytest.raises(ValueError, match="the paid call broke"):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(), self.failing_work)

    async def test_the_reservation_is_released_when_the_work_fails(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        with pytest.raises(ValueError, match="paid call broke"):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(), self.failing_work)

        assert len(metering_server.released) == 1
        assert metering_server.reservations == {}

    async def test_a_failed_work_is_not_settled_and_writes_no_usage_event(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        with pytest.raises(ValueError, match="paid call broke"):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(), self.failing_work)

        assert metering_server.settlements == []
        assert outbox_events() == []

    async def test_a_failed_work_logs_a_warning(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        metering_server.remaining = Decimal("100")

        with caplog.at_level(logging.DEBUG), pytest.raises(ValueError, match="paid call broke"):
            await self.client(metering_http, outbox_writer).call(paid_call_factory(), self.failing_work)

        assert any(record.levelno == logging.WARNING for record in caplog.records)

    async def test_the_result_is_returned_when_the_settlement_fails(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")
        self.server = metering_server

        result = await self.client(metering_http, outbox_writer).call(
            paid_call_factory(), self.work_that_takes_the_server_down
        )

        assert result == "payroll declared"
        assert metering_server.settlements == []

    async def test_a_failed_settlement_logs_a_warning(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        metering_server.remaining = Decimal("100")
        self.server = metering_server

        with caplog.at_level(logging.DEBUG):
            await self.client(metering_http, outbox_writer).call(
                paid_call_factory(), self.work_that_takes_the_server_down
            )

        assert any(record.levelno == logging.WARNING for record in caplog.records)

    async def test_a_failed_settlement_still_writes_one_usage_event_with_the_reservation_id(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")
        self.server = metering_server

        await self.client(metering_http, outbox_writer).call(paid_call_factory(), self.work_that_takes_the_server_down)

        events = outbox_events()
        assert len(events) == 1
        event = UsageEvent.model_validate(events[0].payload)
        assert event.reservation_id in metering_server.reservations

from __future__ import annotations

from decimal import Decimal
from typing import Callable, List, Tuple

import httpx
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.service.metering.metering_client import MeteringClient
from erp_metering.storage.events.usage_event_writer import UsageEventWriter
from erp_metering.storage.servers.metering_server_repository import MeteringServerRepository
from erp_models.events.event_envelope import EventEnvelope
from erp_models.money.money import Money
from erp_outbox.storage.outbox_store import OutboxStore

from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


class TestSettledCall:
    ACTUAL_COST: Decimal = Decimal("8.40")

    async def work(self) -> Tuple[str, Money]:
        return "invoice read", Money(amount=self.ACTUAL_COST, currency="EUR")

    async def run_call(
        self,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> str:
        client = MeteringClient(MeteringServerRepository(metering_http), UsageEventWriter(outbox_writer))
        return await client.call(paid_call_factory(amount=Decimal("10.00")), self.work)

    async def test_the_result_of_the_work_is_returned(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        result = await self.run_call(metering_http, outbox_writer, paid_call_factory)

        assert result == "invoice read"

    async def test_the_server_sees_the_check_the_reservation_and_the_settlement_in_order(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        await self.run_call(metering_http, outbox_writer, paid_call_factory)

        assert len(metering_server.settlements) == 1
        reservation_id = metering_server.settlements[0].reservation_id
        assert metering_server.requests == [
            ("POST", "/v1/budget-checks"),
            ("POST", "/v1/reservations"),
            ("POST", f"/v1/reservations/{reservation_id}/settlement"),
        ]

    async def test_the_settlement_carries_the_actual_cost(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        await self.run_call(metering_http, outbox_writer, paid_call_factory)

        assert metering_server.settlements[0].actual_cost == Money(amount=self.ACTUAL_COST, currency="EUR")

    async def test_one_usage_event_is_written_for_the_settled_call(
        self,
        metering_server: StandInMeteringServer,
        metering_http: httpx.AsyncClient,
        outbox_writer: OutboxStore,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100")

        await self.run_call(metering_http, outbox_writer, paid_call_factory)

        events = outbox_events()
        assert len(events) == 1
        assert events[0].event_type == "metering.usage"
        event = UsageEvent.model_validate(events[0].payload)
        assert event.reservation_id == metering_server.settlements[0].reservation_id
        assert event.actual_cost == Money(amount=self.ACTUAL_COST, currency="EUR")
        assert event.over_budget is False

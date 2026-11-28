from __future__ import annotations

from decimal import Decimal
from typing import Callable, List

from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.storage.events.usage_event_writer import UsageEventWriter
from erp_models.events.event_envelope import EventEnvelope
from erp_models.money.money import Money
from erp_models.times.utc_timestamp import UtcTimestamp


class TestUsageEventWriter:
    def a_usage_event(self, paid_call: PaidCall, reservation_id: str = "R-1") -> UsageEvent:
        return UsageEvent(
            call=paid_call,
            reservation_id=reservation_id,
            actual_cost=Money(amount=Decimal("9.50"), currency="EUR"),
            over_budget=False,
            settled_at=UtcTimestamp.now(),
        )

    async def test_one_write_gives_exactly_one_envelope_of_the_usage_type(
        self,
        outbox_writer: object,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        writer = UsageEventWriter(outbox_writer)

        await writer.write(self.a_usage_event(paid_call_factory()))

        events = outbox_events()
        assert len(events) == 1
        assert events[0].event_type == "metering.usage"
        assert events[0].event_type == UsageEvent.EVENT_TYPE

    async def test_the_payload_validates_back_into_an_equal_usage_event(
        self,
        outbox_writer: object,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        writer = UsageEventWriter(outbox_writer)
        event = self.a_usage_event(paid_call_factory(amount=Decimal("12.00"), legal_duty=True))

        await writer.write(event)

        assert UsageEvent.model_validate(outbox_events()[0].payload) == event

    async def test_two_writes_give_two_envelopes_with_distinct_identifiers(
        self,
        outbox_writer: object,
        outbox_events: Callable[[], List[EventEnvelope]],
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        writer = UsageEventWriter(outbox_writer)

        await writer.write(self.a_usage_event(paid_call_factory(), "R-1"))
        await writer.write(self.a_usage_event(paid_call_factory(), "R-2"))

        events = outbox_events()
        assert len(events) == 2
        assert events[0].event_id != events[1].event_id

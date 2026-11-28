from __future__ import annotations

from datetime import UTC, datetime
from typing import Dict

import pytest
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.exceptions import (
    SEInvalidUsageEventException,
    SEUsageEventInvalidActualCost,
    SEUsageEventInvalidCall,
    SEUsageEventInvalidOverBudget,
    SEUsageEventInvalidReservationId,
    SEUsageEventInvalidSettledAt,
)
from erp_metering.models.events.usage_event import UsageEvent
from erp_models.ids.company_id import CompanyId
from erp_models.money.money import Money
from erp_models.times.utc_timestamp import UtcTimestamp
from pydantic import JsonValue, ValidationError


class TestUsageEvent:
    def a_call(self) -> PaidCall:
        return PaidCall(
            company_id=CompanyId(value="C-12"),
            module="purchasing",
            feature="ocr",
            estimated_cost=Money(amount="1.50", currency="EUR"),
        )

    def a_settled_at(self) -> UtcTimestamp:
        return UtcTimestamp(instant=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC))

    def valid_data(self) -> Dict[str, JsonValue]:
        return {
            "call": self.a_call().model_dump(mode="json"),
            "actual_cost": {"amount": "1.20", "currency": "EUR"},
            "settled_at": self.a_settled_at().model_dump(mode="json"),
        }

    def test_defaults(self) -> None:
        event = UsageEvent(
            call=self.a_call(),
            actual_cost=Money(amount="1.20", currency="EUR"),
            settled_at=self.a_settled_at(),
        )

        assert event.reservation_id is None
        assert event.over_budget is False

    def test_the_event_type_is_metering_usage(self) -> None:
        assert UsageEvent.EVENT_TYPE == "metering.usage"

    def test_full_valid_construction(self) -> None:
        event = UsageEvent(
            call=self.a_call(),
            reservation_id="  R-1  ",
            actual_cost=Money(amount="1.20", currency="EUR"),
            over_budget=True,
            settled_at=self.a_settled_at(),
        )

        assert event.call == self.a_call()
        assert event.reservation_id == "R-1"
        assert event.actual_cost == Money(amount="1.20", currency="EUR")
        assert event.over_budget is True
        assert event.settled_at == self.a_settled_at()

    @pytest.mark.parametrize("name", ["reservation_id", "over_budget"])
    def test_none_becomes_the_default(self, name: str) -> None:
        data = self.valid_data()
        data[name] = None

        event = UsageEvent.model_validate(data)

        assert getattr(event, name) == UsageEvent.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("call", None, SEUsageEventInvalidCall),
            ("call", 12, SEUsageEventInvalidCall),
            ("call", True, SEUsageEventInvalidCall),
            ("call", "", SEUsageEventInvalidCall),
            ("call", [1, 2], SEUsageEventInvalidCall),
            ("reservation_id", 12, SEUsageEventInvalidReservationId),
            ("reservation_id", True, SEUsageEventInvalidReservationId),
            ("reservation_id", "", SEUsageEventInvalidReservationId),
            ("reservation_id", "   ", SEUsageEventInvalidReservationId),
            ("actual_cost", None, SEUsageEventInvalidActualCost),
            ("actual_cost", 12, SEUsageEventInvalidActualCost),
            ("actual_cost", True, SEUsageEventInvalidActualCost),
            ("actual_cost", "1.20", SEUsageEventInvalidActualCost),
            ("actual_cost", {"amount": "-0.01", "currency": "EUR"}, SEUsageEventInvalidActualCost),
            ("over_budget", "yes", SEUsageEventInvalidOverBudget),
            ("over_budget", 1, SEUsageEventInvalidOverBudget),
            ("over_budget", 0, SEUsageEventInvalidOverBudget),
            ("settled_at", None, SEUsageEventInvalidSettledAt),
            ("settled_at", 12, SEUsageEventInvalidSettledAt),
            ("settled_at", True, SEUsageEventInvalidSettledAt),
            ("settled_at", {"instant": "not a time"}, SEUsageEventInvalidSettledAt),
            ("settled_at", {"instant": "2026-01-02T03:04:05"}, SEUsageEventInvalidSettledAt),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data = self.valid_data()
        data[name] = value

        with pytest.raises(error):
            UsageEvent.model_validate(data)

    @pytest.mark.parametrize(
        "error",
        [
            SEUsageEventInvalidCall,
            SEUsageEventInvalidReservationId,
            SEUsageEventInvalidActualCost,
            SEUsageEventInvalidOverBudget,
            SEUsageEventInvalidSettledAt,
        ],
    )
    def test_every_field_exception_is_a_usage_event_exception(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidUsageEventException)

    def test_rejects_unknown_keys(self) -> None:
        data = self.valid_data()
        data["unknown"] = 1

        with pytest.raises(ValidationError):
            UsageEvent.model_validate(data)

    def test_assigning_a_field_of_a_built_event_is_refused(self) -> None:
        event = UsageEvent.model_validate(self.valid_data())

        with pytest.raises(ValidationError):
            event.over_budget = True  # type: ignore[misc]

    def test_round_trip(self) -> None:
        event = UsageEvent(
            call=self.a_call(),
            reservation_id="R-1",
            actual_cost=Money(amount="1.20", currency="EUR"),
            over_budget=True,
            settled_at=self.a_settled_at(),
        )

        assert UsageEvent.model_validate_json(event.model_dump_json()) == event

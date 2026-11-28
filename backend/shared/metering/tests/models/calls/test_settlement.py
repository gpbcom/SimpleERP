from __future__ import annotations

from decimal import Decimal

import pytest
from erp_metering.models.calls.exceptions import (
    SEInvalidSettlementException,
    SESettlementInvalidActualCost,
    SESettlementInvalidReservationId,
)
from erp_metering.models.calls.settlement import Settlement
from erp_models.money.money import Money
from pydantic import JsonValue, ValidationError


class TestSettlement:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            Settlement.model_validate({})

    def test_full_valid_construction(self) -> None:
        settlement = Settlement(reservation_id="  res-1  ", actual_cost=Money(amount="1.50", currency="EUR"))
        assert settlement.reservation_id == "res-1"
        assert settlement.actual_cost == Money(amount="1.50", currency="EUR")

    def test_a_zero_cost_is_accepted(self) -> None:
        settlement = Settlement(reservation_id="res-1", actual_cost=Money(amount="0", currency="EUR"))
        assert settlement.actual_cost.amount == Decimal("0")

    def test_none_is_refused_for_each_required_field(self) -> None:
        cost = {"amount": "1", "currency": "EUR"}
        with pytest.raises(SESettlementInvalidReservationId):
            Settlement.model_validate({"reservation_id": None, "actual_cost": cost})
        with pytest.raises(SESettlementInvalidActualCost):
            Settlement.model_validate({"reservation_id": "res-1", "actual_cost": None})

    @pytest.mark.parametrize("value", ["", "   ", True, 12, 1.5, ["res-1"], {"a": 1}])
    def test_rejects_bad_reservation_ids(self, value: JsonValue) -> None:
        with pytest.raises(SESettlementInvalidReservationId):
            Settlement.model_validate({"reservation_id": value, "actual_cost": {"amount": "1", "currency": "EUR"}})

    @pytest.mark.parametrize("amount", ["-0.01", "-1", "-1000"])
    def test_rejects_a_negative_actual_cost(self, amount: str) -> None:
        with pytest.raises(SESettlementInvalidActualCost):
            Settlement(reservation_id="res-1", actual_cost=Money(amount=amount, currency="EUR"))

    @pytest.mark.parametrize("value", ["1.50", 12, True, ["1"]])
    def test_rejects_an_actual_cost_that_is_not_money(self, value: JsonValue) -> None:
        with pytest.raises(SESettlementInvalidActualCost):
            Settlement.model_validate({"reservation_id": "res-1", "actual_cost": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Settlement.model_validate(
                {"reservation_id": "res-1", "actual_cost": {"amount": "1", "currency": "EUR"}, "other": "x"}
            )

    def test_round_trip(self) -> None:
        settlement = Settlement(reservation_id="res-1", actual_cost=Money(amount="2.25", currency="EUR"))
        assert Settlement.model_validate(settlement.model_dump(mode="json")) == settlement
        assert Settlement.model_validate_json(settlement.model_dump_json()) == settlement

    def test_the_field_exceptions_belong_to_the_model_hierarchy(self) -> None:
        assert issubclass(SESettlementInvalidReservationId, SEInvalidSettlementException)
        assert issubclass(SESettlementInvalidActualCost, SEInvalidSettlementException)

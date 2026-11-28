from __future__ import annotations

import logging
from decimal import Decimal
from typing import Awaitable, Callable, Dict

import httpx
import pytest
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.calls.settlement import Settlement
from erp_metering.models.metering.exceptions import (
    SEMeteringReservationRefusedError,
    SEMeteringServerUnavailableError,
)
from erp_metering.storage.servers.metering_server_repository import MeteringServerRepository
from erp_models.money.money import Money

from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


class TestMeteringServerRepository:
    @pytest.fixture
    def repository(self, metering_http: httpx.AsyncClient) -> MeteringServerRepository:
        return MeteringServerRepository(metering_http)

    async def test_a_call_within_the_remaining_budget_is_within_budget(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("100.00")
        check = await repository.check_budget(paid_call_factory(amount=Decimal("100.00")))
        assert check.within_budget is True
        assert metering_server.requests == [("POST", "/v1/budget-checks")]

    async def test_a_call_with_the_budget_spent_is_not_within_budget(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("0")
        check = await repository.check_budget(paid_call_factory(amount=Decimal("10.00")))
        assert check.within_budget is False

    async def test_a_reservation_returns_an_id_that_the_server_recorded(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("50.00")
        call = paid_call_factory(amount=Decimal("10.00"))
        reservation = await repository.reserve(call)
        assert reservation.reservation_id in metering_server.reservations
        assert metering_server.reservations[reservation.reservation_id] == call
        assert metering_server.requests == [("POST", "/v1/reservations")]

    async def test_a_reservation_over_budget_without_a_legal_duty_is_refused(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("5.00")
        with pytest.raises(SEMeteringReservationRefusedError):
            await repository.reserve(paid_call_factory(amount=Decimal("10.00")))
        assert metering_server.reservations == {}

    async def test_a_reservation_over_budget_with_a_legal_duty_succeeds(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("0")
        reservation = await repository.reserve(paid_call_factory(amount=Decimal("10.00"), legal_duty=True))
        assert reservation.reservation_id in metering_server.reservations

    async def test_a_settlement_is_recorded_by_the_server(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("50.00")
        reservation = await repository.reserve(paid_call_factory(amount=Decimal("10.00")))
        settlement = Settlement(
            reservation_id=reservation.reservation_id, actual_cost=Money(amount=Decimal("8.00"), currency="EUR")
        )
        settled = await repository.settle(settlement)
        assert settled == settlement
        assert metering_server.settlements == [settlement]

    async def test_a_settlement_of_an_unknown_reservation_is_unavailable(
        self, repository: MeteringServerRepository
    ) -> None:
        settlement = Settlement(reservation_id="unknown", actual_cost=Money(amount=Decimal("1.00"), currency="EUR"))
        with pytest.raises(SEMeteringServerUnavailableError):
            await repository.settle(settlement)

    async def test_a_release_of_an_unknown_reservation_is_unavailable(
        self, repository: MeteringServerRepository
    ) -> None:
        with pytest.raises(SEMeteringServerUnavailableError):
            await repository.release("unknown")

    async def test_a_release_is_recorded_by_the_server(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.remaining = Decimal("50.00")
        reservation = await repository.reserve(paid_call_factory(amount=Decimal("10.00")))
        await repository.release(reservation.reservation_id)
        assert metering_server.released == [reservation.reservation_id]

    @pytest.mark.parametrize("method", ["check_budget", "reserve", "settle", "release"])
    async def test_an_unavailable_server_makes_every_method_fail(
        self,
        method: str,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.available = False
        call = paid_call_factory()
        settlement = Settlement(reservation_id="r1", actual_cost=Money(amount=Decimal("1.00"), currency="EUR"))
        operations: Dict[str, Callable[[], Awaitable[object]]] = {
            "check_budget": lambda: repository.check_budget(call),
            "reserve": lambda: repository.reserve(call),
            "settle": lambda: repository.settle(settlement),
            "release": lambda: repository.release("r1"),
        }
        with pytest.raises(SEMeteringServerUnavailableError):
            await operations[method]()

    async def test_a_closed_server_makes_the_call_fail(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
    ) -> None:
        metering_server.close()
        with pytest.raises(SEMeteringServerUnavailableError):
            await repository.check_budget(paid_call_factory())

    async def test_a_failure_is_logged_as_a_warning_or_an_error(
        self,
        repository: MeteringServerRepository,
        metering_server: StandInMeteringServer,
        paid_call_factory: Callable[..., PaidCall],
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        metering_server.available = False
        with caplog.at_level(logging.DEBUG), pytest.raises(SEMeteringServerUnavailableError):
            await repository.check_budget(paid_call_factory())
        assert any(record.levelno >= logging.WARNING for record in caplog.records)

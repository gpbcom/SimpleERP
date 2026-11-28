from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Awaitable, Callable, Optional, Tuple

# First-party imports
from erp_models.money.money import Money
from erp_models.times.utc_timestamp import UtcTimestamp

from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.calls.settlement import Settlement
from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.models.metering.exceptions import (
    SEMeteringBudgetExhaustedError,
    SEMeteringReservationRefusedError,
    SEMeteringServerUnavailableError,
)
from erp_metering.storage.events.usage_event_writer import UsageEventWriter
from erp_metering.storage.servers.metering_server_repository import MeteringServerRepository


class MeteringClient:
    """The client every paid call goes through: check, reserve, call, settle, emit.

    Attributes:
        server (MeteringServerRepository): The metering server that holds the budget counters.
        events (UsageEventWriter): Where the usage event of each settled call is written.
        logger (Logger): Logger instance.

    Notes:
        - The flow is the budget check, the reservation, the call, the settlement and the usage event (TC-21).
        - **A call with a legal duty is never stopped by a budget or by an unreachable server** (BR-F22-06). It is
          flagged ``over_budget`` when the budget is spent, and it goes on without a reservation, and so without a
          settlement, when the server cannot be reached.
        - A call that fails releases its reservation and writes no usage event, because nothing was spent.
        - A usage event that cannot be written propagates, so that no paid call is left unrecorded.
    """

    def __init__(
        self,
        server: MeteringServerRepository,
        events: UsageEventWriter,
        logger: Optional[Logger] = None,
    ) -> None:
        """Keep the server and the event writer.

        Args:
            server (MeteringServerRepository): The metering server that holds the budget counters.
            events (UsageEventWriter): Where the usage events are written.
            logger (Optional[Logger]): Logger instance.
        """
        self.server = server
        self.events = events
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _stop_or_flag(self, paid_call: PaidCall, reason: str) -> None:
        """Stop a call that meets a spent budget, unless it is a legal duty.

        Args:
            paid_call (PaidCall): The call that was checked.
            reason (str): What the server said, in a few words.

        Raises:
            SEMeteringBudgetExhaustedError: When the call has no legal duty.
        """
        if paid_call.legal_duty:
            self.logger.warning(
                "Budget exhausted (%s) for a call of %s under a legal duty: it goes on.", reason, paid_call.module
            )
            return
        self.logger.error("Budget exhausted (%s) for a call of %s: it is stopped.", reason, paid_call.module)
        raise SEMeteringBudgetExhaustedError(
            f"The budget is spent for a call of {paid_call.module}. "  # noqa: E501
            "The call was not made."
        )

    async def _admit(self, paid_call: PaidCall) -> Tuple[Optional[str], bool]:
        """Check the budget and reserve the estimated cost.

        Args:
            paid_call (PaidCall): The call to admit.

        Returns:
            Tuple[Optional[str], bool]: The reservation id, ``None`` when there is none, and whether the call is over
                budget.

        Raises:
            SEMeteringBudgetExhaustedError: When the budget is spent and the call has no legal duty.
            SEMeteringServerUnavailableError: When the server fails and the call has no legal duty.
        """
        over_budget = False
        try:
            check = await self.server.check_budget(paid_call)
            if not check.within_budget:
                self._stop_or_flag(paid_call, "check")
                over_budget = True
            reservation = await self.server.reserve(paid_call)
        except SEMeteringReservationRefusedError:
            self._stop_or_flag(paid_call, "reservation refused")
            return None, True
        except SEMeteringServerUnavailableError:
            if not paid_call.legal_duty:
                raise
            self.logger.warning(
                "Metering server unavailable for a legal-duty call of %s: no reservation.", paid_call.module
            )
            return None, over_budget
        self.logger.debug("Admitted a call of %s.", paid_call.module)
        return reservation.reservation_id, over_budget

    async def _release(self, reservation_id: Optional[str]) -> None:
        """Release a reservation after a failed call, without ever raising.

        Args:
            reservation_id (Optional[str]): The reservation to release, if any.
        """
        if reservation_id is None:
            return
        try:
            await self.server.release(reservation_id)
        except SEMeteringServerUnavailableError:
            self.logger.warning("Reservation %s could not be released.", reservation_id)

    async def _settle(self, reservation_id: Optional[str], actual_cost: Money) -> None:
        """Settle a reservation with the real cost, without ever raising.

        Args:
            reservation_id (Optional[str]): The reservation to settle, if any.
            actual_cost (Money): What the call really cost.
        """
        if reservation_id is None:
            self.logger.debug("No reservation to settle.")
            return
        try:
            await self.server.settle(Settlement(reservation_id=reservation_id, actual_cost=actual_cost))
        except SEMeteringServerUnavailableError:
            self.logger.warning("Reservation %s could not be settled.", reservation_id)

    ############################
    # Publicly Exposed Methods #
    ############################

    async def call[T](self, paid_call: PaidCall, work: Callable[[], Awaitable[Tuple[T, Money]]]) -> T:
        """Make one paid call under the metering flow.

        Args:
            paid_call (PaidCall): The call, with its scope and its estimated cost.
            work (Callable[[], Awaitable[Tuple[T, Money]]]): The call itself, returning its result and its real cost.

        Returns:
            T: The result of the work.

        Raises:
            SEMeteringBudgetExhaustedError: When the budget is spent and the call has no legal duty.
            SEMeteringServerUnavailableError: When the server fails and the call has no legal duty.
            SEMeteringUsageEventNotWrittenError: When the usage event cannot be written.
        """
        reservation_id, over_budget = await self._admit(paid_call)
        try:
            result, actual_cost = await work()
        except Exception:
            await self._release(reservation_id)
            self.logger.warning("A paid call of %s failed: its reservation is released.", paid_call.module)
            raise
        await self._settle(reservation_id, actual_cost)
        await self.events.write(
            UsageEvent(
                call=paid_call,
                reservation_id=reservation_id,
                actual_cost=actual_cost,
                over_budget=over_budget,
                settled_at=UtcTimestamp.now(),
            )
        )
        self.logger.info("Settled a paid call of %s.", paid_call.module)
        return result

from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Optional, Set

# Third-party imports
import httpx
from erp_models.exceptions import SEInvalidModelException
from pydantic import ValidationError

from erp_metering.models.calls.budget_check import BudgetCheck
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.calls.reservation import Reservation
from erp_metering.models.calls.settlement import Settlement
from erp_metering.models.metering.exceptions import (
    SEMeteringReservationRefusedError,
    SEMeteringServerUnavailableError,
)


class MeteringServerRepository:
    """Reads and writes the budget counters of the metering server over its HTTP API.

    Attributes:
        BUDGET_CHECKS_PATH (str): The route of budget checks.
        RESERVATIONS_PATH (str): The route of reservations.
        CONFLICT_STATUS (int): The status that means a reservation is refused.
        http (httpx.AsyncClient): The client the caller owns, and closes.
        logger (Logger): Logger instance.

    Notes:
        - **A body that carries a cost is never logged in full**: only ids and outcomes are.
        - A transport error, an unexpected status or an answer that fails validation all raise
          ``SEMeteringServerUnavailableError``, so that the caller handles one failure.
    """

    BUDGET_CHECKS_PATH: ClassVar[str] = "/v1/budget-checks"
    RESERVATIONS_PATH: ClassVar[str] = "/v1/reservations"
    CONFLICT_STATUS: ClassVar[int] = 409

    def __init__(self, http: httpx.AsyncClient, logger: Optional[Logger] = None) -> None:
        """Create the repository.

        Args:
            http (httpx.AsyncClient): The client the caller owns, and closes.
            logger (Optional[Logger]): Logger instance.
        """
        self.http = http
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _unavailable(self, message: str, error: Optional[Exception] = None) -> SEMeteringServerUnavailableError:
        """Log an error and build the exception to raise.

        Args:
            message (str): The message of the exception.
            error (Optional[Exception]): The cause, logged by its type only.

        Returns:
            SEMeteringServerUnavailableError: The exception to raise.
        """
        self.logger.error("Metering server failure: %s (%s).", message, type(error).__name__ if error else "no cause")
        return SEMeteringServerUnavailableError(message)

    async def _send(self, method: str, path: str, expected: Set[int], content: Optional[str] = None) -> httpx.Response:
        """Send one request and check its status.

        Args:
            method (str): The HTTP method.
            path (str): The path of the route.
            expected (Set[int]): The statuses that are not a failure.
            content (Optional[str]): The JSON body, if any.

        Returns:
            httpx.Response: The answer.

        Raises:
            SEMeteringServerUnavailableError: When the call fails or the status is not expected.
        """
        self.logger.debug("Sending %s %s to the metering server.", method, path)
        try:
            response = await self.http.request(
                method, path, content=content, headers={"Content-Type": "application/json"} if content else None
            )
        except httpx.HTTPError as error:
            raise self._unavailable(f"The metering server cannot be reached for {method} {path}.", error) from error
        if response.status_code not in expected:
            raise self._unavailable(
                f"Unexpected status {response.status_code} "  # noqa: E501
                f"for {method} {path}."
            )
        return response

    ############################
    # Publicly Exposed Methods #
    ############################

    async def check_budget(self, paid_call: PaidCall) -> BudgetCheck:
        """Ask whether a paid call fits in its budgets.

        Args:
            paid_call (PaidCall): The call to check.

        Returns:
            BudgetCheck: The answer of the server.

        Raises:
            SEMeteringServerUnavailableError: When the server fails or answers something unusable.
        """
        response = await self._send("POST", self.BUDGET_CHECKS_PATH, {200}, paid_call.model_dump_json())
        try:
            check = BudgetCheck.model_validate_json(response.content)
        except (ValidationError, SEInvalidModelException) as error:
            raise self._unavailable("The budget check answer is invalid.", error) from error
        self.logger.info("Checked a budget: within_budget=%s.", check.within_budget)
        return check

    async def reserve(self, paid_call: PaidCall) -> Reservation:
        """Reserve the estimated cost of a paid call.

        Args:
            paid_call (PaidCall): The call to reserve.

        Returns:
            Reservation: The reservation granted.

        Raises:
            SEMeteringReservationRefusedError: When the server refuses with a 409.
            SEMeteringServerUnavailableError: When the server fails or answers something unusable.
        """
        response = await self._send(
            "POST", self.RESERVATIONS_PATH, {200, 201, self.CONFLICT_STATUS}, paid_call.model_dump_json()
        )
        if response.status_code == self.CONFLICT_STATUS:
            self.logger.error("The metering server refused a reservation.")
            raise SEMeteringReservationRefusedError(
                "The metering server refused the reservation. "  # noqa: E501
                "The budget is spent."
            )
        try:
            reservation = Reservation.model_validate_json(response.content)
        except (ValidationError, SEInvalidModelException) as error:
            raise self._unavailable("The reservation answer is invalid.", error) from error
        self.logger.info("Reserved %s.", reservation.reservation_id)
        return reservation

    async def settle(self, settlement: Settlement) -> Settlement:
        """Settle a reservation with the real cost of the call.

        Args:
            settlement (Settlement): The real cost and the reservation it settles.

        Returns:
            Settlement: The settlement as the server recorded it.

        Raises:
            SEMeteringServerUnavailableError: When the server fails or answers something unusable.
        """
        path = f"{self.RESERVATIONS_PATH}/{settlement.reservation_id}/settlement"
        response = await self._send("POST", path, {200}, settlement.model_dump_json())
        try:
            settled = Settlement.model_validate_json(response.content)
        except (ValidationError, SEInvalidModelException) as error:
            raise self._unavailable("The settlement answer is invalid.", error) from error
        self.logger.info("Settled %s.", settled.reservation_id)
        return settled

    async def release(self, reservation_id: str) -> None:
        """Release a reservation without settling it.

        Args:
            reservation_id (str): The reservation to release.

        Raises:
            SEMeteringServerUnavailableError: When the server fails or the reservation is unknown.
        """
        await self._send("DELETE", f"{self.RESERVATIONS_PATH}/{reservation_id}", {200, 204})
        self.logger.info("Released %s.", reservation_id)

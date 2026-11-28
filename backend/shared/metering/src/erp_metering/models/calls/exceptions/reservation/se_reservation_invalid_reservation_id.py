from __future__ import annotations

# First-party imports
from erp_metering.models.calls.exceptions.reservation.se_invalid_reservation_exception import (
    SEInvalidReservationException,
)


class SEReservationInvalidReservationId(SEInvalidReservationException):
    """Exception raised when an invalid ``reservation_id`` is provided."""

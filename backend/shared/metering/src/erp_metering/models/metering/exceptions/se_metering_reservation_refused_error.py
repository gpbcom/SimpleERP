from __future__ import annotations

from erp_metering.models.metering.exceptions.se_metering_error import SEMeteringError


class SEMeteringReservationRefusedError(SEMeteringError):
    """Raised when the metering server refuses a reservation."""

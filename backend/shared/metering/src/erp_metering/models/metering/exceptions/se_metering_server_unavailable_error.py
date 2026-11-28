from __future__ import annotations

from erp_metering.models.metering.exceptions.se_metering_error import SEMeteringError


class SEMeteringServerUnavailableError(SEMeteringError):
    """Raised when the metering server cannot be reached or gives an answer the client cannot use."""

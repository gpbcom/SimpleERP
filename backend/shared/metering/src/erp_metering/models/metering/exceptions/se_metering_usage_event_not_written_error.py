from __future__ import annotations

from erp_metering.models.metering.exceptions.se_metering_error import SEMeteringError


class SEMeteringUsageEventNotWrittenError(SEMeteringError):
    """Raised when a usage event cannot be written through the outbox."""

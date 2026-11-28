from __future__ import annotations

from erp_metering.models.metering.exceptions.se_metering_error import SEMeteringError


class SEMeteringBudgetExhaustedError(SEMeteringError):
    """Raised when a paid call without a legal duty meets an exhausted budget, before the call is made."""

from __future__ import annotations

# First-party imports
from erp_metering.models.events.exceptions.usage_event.se_invalid_usage_event_exception import (
    SEInvalidUsageEventException,
)


class SEUsageEventInvalidOverBudget(SEInvalidUsageEventException):
    """Exception raised when an invalid ``over_budget`` is provided."""

from __future__ import annotations

from ai_cost.service.usage.exceptions.se_usage_error import SEUsageError


class SEUsageMeasureFailedError(SEUsageError):
    """Raised when a run's cost cannot be measured."""

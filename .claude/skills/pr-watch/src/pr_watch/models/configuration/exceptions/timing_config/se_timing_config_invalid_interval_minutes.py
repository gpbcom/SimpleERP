from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_timing_config_exception import SEInvalidTimingConfigException


class SETimingConfigInvalidIntervalMinutes(SEInvalidTimingConfigException):
    """Exception raised when an invalid ``interval_minutes`` is provided."""

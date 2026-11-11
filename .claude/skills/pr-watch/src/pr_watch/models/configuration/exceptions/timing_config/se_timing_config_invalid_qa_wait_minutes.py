from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_timing_config_exception import SEInvalidTimingConfigException


class SETimingConfigInvalidQaWaitMinutes(SEInvalidTimingConfigException):
    """Exception raised when an invalid ``qa_wait_minutes`` is provided."""

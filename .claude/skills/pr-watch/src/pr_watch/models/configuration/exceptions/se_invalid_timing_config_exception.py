from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidTimingConfigException(SEPrWatchError):
    """Exception raised when an invalid TimingConfig is provided."""

from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidCheckRunException(SEPrWatchError):
    """Exception raised when an invalid CheckRun is provided."""

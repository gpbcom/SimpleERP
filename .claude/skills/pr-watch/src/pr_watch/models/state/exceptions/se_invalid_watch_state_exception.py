from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidWatchStateException(SEPrWatchError):
    """Exception raised when an invalid WatchState is provided."""

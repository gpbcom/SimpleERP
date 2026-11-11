from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidWatchHistoryException(SEPrWatchError):
    """Exception raised when an invalid WatchHistory is provided."""

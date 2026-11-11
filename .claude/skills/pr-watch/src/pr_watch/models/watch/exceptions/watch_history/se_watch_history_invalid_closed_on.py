from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_watch_history_exception import SEInvalidWatchHistoryException


class SEWatchHistoryInvalidClosedOn(SEInvalidWatchHistoryException):
    """Exception raised when an invalid ``closed_on`` is provided."""

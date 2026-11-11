from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_watch_history_exception import SEInvalidWatchHistoryException


class SEWatchHistoryInvalidRegisteredOn(SEInvalidWatchHistoryException):
    """Exception raised when an invalid ``registered_on`` is provided."""

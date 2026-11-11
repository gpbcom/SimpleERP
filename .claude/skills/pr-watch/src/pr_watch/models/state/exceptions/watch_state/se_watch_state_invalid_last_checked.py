from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_watch_state_exception import SEInvalidWatchStateException


class SEWatchStateInvalidLastChecked(SEInvalidWatchStateException):
    """Exception raised when an invalid ``last_checked`` is provided."""

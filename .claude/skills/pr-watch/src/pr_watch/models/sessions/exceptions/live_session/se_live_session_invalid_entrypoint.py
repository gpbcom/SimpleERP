from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_live_session_exception import SEInvalidLiveSessionException


class SELiveSessionInvalidEntrypoint(SEInvalidLiveSessionException):
    """Exception raised when an invalid ``entrypoint`` is provided."""

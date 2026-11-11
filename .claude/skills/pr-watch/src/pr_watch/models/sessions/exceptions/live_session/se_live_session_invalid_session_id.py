from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_live_session_exception import SEInvalidLiveSessionException


class SELiveSessionInvalidSessionId(SEInvalidLiveSessionException):
    """Exception raised when an invalid ``session_id`` is provided."""

from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_live_session_exception import SEInvalidLiveSessionException


class SELiveSessionInvalidCwd(SEInvalidLiveSessionException):
    """Exception raised when an invalid ``cwd`` is provided."""

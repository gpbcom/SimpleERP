from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_session_ref_exception import SEInvalidSessionRefException


class SESessionRefInvalidSessionId(SEInvalidSessionRefException):
    """Exception raised when an invalid ``session_id`` is provided."""

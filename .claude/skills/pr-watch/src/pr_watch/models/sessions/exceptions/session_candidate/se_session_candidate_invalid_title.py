from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_session_candidate_exception import (
    SEInvalidSessionCandidateException,
)


class SESessionCandidateInvalidTitle(SEInvalidSessionCandidateException):
    """Exception raised when an invalid ``title`` is provided."""

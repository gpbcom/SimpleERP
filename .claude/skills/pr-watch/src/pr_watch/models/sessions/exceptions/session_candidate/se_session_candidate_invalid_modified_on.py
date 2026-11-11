from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_session_candidate_exception import (
    SEInvalidSessionCandidateException,
)


class SESessionCandidateInvalidModifiedOn(SEInvalidSessionCandidateException):
    """Exception raised when an invalid ``modified_on`` is provided."""

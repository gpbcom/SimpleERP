from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_dispatch_outcome_exception import SEInvalidDispatchOutcomeException


class SEDispatchOutcomeInvalidOk(SEInvalidDispatchOutcomeException):
    """Exception raised when an invalid ``ok`` is provided."""

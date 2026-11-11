from __future__ import annotations

from pr_watch.models.events.exceptions.se_invalid_operation_exception import SEInvalidOperationException


class SEOperationInvalidLink(SEInvalidOperationException):
    """Exception raised when an invalid ``link`` is provided."""

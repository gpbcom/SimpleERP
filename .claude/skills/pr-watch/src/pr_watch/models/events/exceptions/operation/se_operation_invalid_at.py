from __future__ import annotations

from pr_watch.models.events.exceptions.se_invalid_operation_exception import SEInvalidOperationException


class SEOperationInvalidAt(SEInvalidOperationException):
    """Exception raised when an invalid ``at`` is provided."""

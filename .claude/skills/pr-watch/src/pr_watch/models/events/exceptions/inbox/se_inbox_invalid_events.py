from __future__ import annotations

from pr_watch.models.events.exceptions.se_invalid_inbox_exception import SEInvalidInboxException


class SEInboxInvalidEvents(SEInvalidInboxException):
    """Exception raised when an invalid ``events`` is provided."""

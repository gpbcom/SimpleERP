from __future__ import annotations

from pr_watch.models.events.exceptions.se_invalid_pr_event_exception import SEInvalidPrEventException


class SEPrEventInvalidId(SEInvalidPrEventException):
    """Exception raised when an invalid ``id`` is provided."""

from __future__ import annotations

from pr_watch.models.events.exceptions.se_invalid_pr_event_exception import SEInvalidPrEventException


class SEPrEventInvalidAckedOn(SEInvalidPrEventException):
    """Exception raised when an invalid ``acked_on`` is provided."""

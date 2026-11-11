from __future__ import annotations

from pr_watch.models.events.exceptions.se_invalid_event_detail_exception import SEInvalidEventDetailException


class SEEventDetailInvalidLink(SEInvalidEventDetailException):
    """Exception raised when an invalid ``link`` is provided."""

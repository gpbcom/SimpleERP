from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_ticket_watch_exception import SEInvalidTicketWatchException


class SETicketWatchInvalidKey(SEInvalidTicketWatchException):
    """Exception raised when an invalid ``key`` is provided."""

from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_ticket_watch_exception import SEInvalidTicketWatchException


class SETicketWatchInvalidHistory(SEInvalidTicketWatchException):
    """Exception raised when an invalid ``history`` is provided."""

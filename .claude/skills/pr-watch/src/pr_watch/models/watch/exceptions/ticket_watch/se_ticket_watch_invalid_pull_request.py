from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_ticket_watch_exception import SEInvalidTicketWatchException


class SETicketWatchInvalidPullRequest(SEInvalidTicketWatchException):
    """Exception raised when an invalid ``pull_request`` is provided."""

from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidTicketWatchException(SEPrWatchError):
    """Exception raised when an invalid TicketWatch is provided."""

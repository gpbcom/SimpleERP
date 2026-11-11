from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidInboxException(SEPrWatchError):
    """Exception raised when an invalid Inbox is provided."""

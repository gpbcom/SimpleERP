from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidSessionRefException(SEPrWatchError):
    """Exception raised when an invalid SessionRef is provided."""

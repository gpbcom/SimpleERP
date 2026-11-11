from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPrEventException(SEPrWatchError):
    """Exception raised when an invalid PrEvent is provided."""

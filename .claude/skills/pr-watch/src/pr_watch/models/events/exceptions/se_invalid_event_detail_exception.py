from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidEventDetailException(SEPrWatchError):
    """Exception raised when an invalid EventDetail is provided."""

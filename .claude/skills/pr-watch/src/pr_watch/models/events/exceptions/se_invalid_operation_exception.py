from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidOperationException(SEPrWatchError):
    """Exception raised when an invalid Operation is provided."""

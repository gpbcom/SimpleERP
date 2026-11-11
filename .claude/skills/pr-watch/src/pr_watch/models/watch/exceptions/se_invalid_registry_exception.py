from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidRegistryException(SEPrWatchError):
    """Exception raised when an invalid Registry is provided."""

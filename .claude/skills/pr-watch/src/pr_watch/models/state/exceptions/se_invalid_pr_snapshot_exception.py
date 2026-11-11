from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPrSnapshotException(SEPrWatchError):
    """Exception raised when an invalid PrSnapshot is provided."""

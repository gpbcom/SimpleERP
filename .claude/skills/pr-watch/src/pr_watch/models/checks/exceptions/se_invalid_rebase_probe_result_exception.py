from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidRebaseProbeResultException(SEPrWatchError):
    """Exception raised when an invalid RebaseProbeResult is provided."""

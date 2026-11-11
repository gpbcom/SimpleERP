from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidSessionCandidateException(SEPrWatchError):
    """Exception raised when an invalid SessionCandidate is provided."""

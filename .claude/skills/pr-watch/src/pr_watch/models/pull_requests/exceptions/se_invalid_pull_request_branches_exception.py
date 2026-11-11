from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPullRequestBranchesException(SEPrWatchError):
    """Exception raised when an invalid PullRequestBranches is provided."""

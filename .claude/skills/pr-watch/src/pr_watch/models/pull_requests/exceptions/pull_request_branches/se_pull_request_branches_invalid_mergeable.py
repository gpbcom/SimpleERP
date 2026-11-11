from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pull_request_branches_exception import (
    SEInvalidPullRequestBranchesException,
)


class SEPullRequestBranchesInvalidMergeable(SEInvalidPullRequestBranchesException):
    """Exception raised when an invalid ``mergeable`` is provided."""

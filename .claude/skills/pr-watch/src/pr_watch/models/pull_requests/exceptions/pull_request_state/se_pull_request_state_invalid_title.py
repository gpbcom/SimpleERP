from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pull_request_state_exception import (
    SEInvalidPullRequestStateException,
)


class SEPullRequestStateInvalidTitle(SEInvalidPullRequestStateException):
    """Exception raised when an invalid ``title`` is provided."""

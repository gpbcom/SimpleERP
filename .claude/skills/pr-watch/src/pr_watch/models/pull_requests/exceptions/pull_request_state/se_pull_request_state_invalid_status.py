from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pull_request_state_exception import (
    SEInvalidPullRequestStateException,
)


class SEPullRequestStateInvalidStatus(SEInvalidPullRequestStateException):
    """Exception raised when an invalid ``status`` is provided."""

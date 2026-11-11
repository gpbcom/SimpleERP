from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_unwatched_pull_request_exception import (
    SEInvalidUnwatchedPullRequestException,
)


class SEUnwatchedPullRequestInvalidNumber(SEInvalidUnwatchedPullRequestException):
    """Exception raised when an invalid ``number`` is provided."""

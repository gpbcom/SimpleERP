from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pull_request_timeline_exception import (
    SEInvalidPullRequestTimelineException,
)


class SEPullRequestTimelineInvalidMergeCommit(SEInvalidPullRequestTimelineException):
    """Exception raised when an invalid ``merge_commit`` is provided."""

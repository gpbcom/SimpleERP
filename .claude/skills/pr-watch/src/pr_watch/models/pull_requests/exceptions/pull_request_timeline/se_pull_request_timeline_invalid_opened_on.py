from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pull_request_timeline_exception import (
    SEInvalidPullRequestTimelineException,
)


class SEPullRequestTimelineInvalidOpenedOn(SEInvalidPullRequestTimelineException):
    """Exception raised when an invalid ``opened_on`` is provided."""

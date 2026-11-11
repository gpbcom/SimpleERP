from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pull_request_timeline_exception import (
    SEInvalidPullRequestTimelineException,
)


class SEPullRequestTimelineInvalidClosedOn(SEInvalidPullRequestTimelineException):
    """Exception raised when an invalid ``closed_on`` is provided."""

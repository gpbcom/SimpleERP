from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_pull_request_ref_exception import SEInvalidPullRequestRefException


class SEPullRequestRefInvalidNumber(SEInvalidPullRequestRefException):
    """Exception raised when an invalid ``number`` is provided."""

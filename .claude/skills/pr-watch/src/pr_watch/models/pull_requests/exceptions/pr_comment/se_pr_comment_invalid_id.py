from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pr_comment_exception import SEInvalidPrCommentException


class SEPrCommentInvalidId(SEInvalidPrCommentException):
    """Exception raised when an invalid ``id`` is provided."""

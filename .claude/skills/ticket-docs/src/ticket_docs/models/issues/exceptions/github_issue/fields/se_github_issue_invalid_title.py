from __future__ import annotations

from ticket_docs.models.issues.exceptions.github_issue.se_invalid_github_issue_exception import (
    SEInvalidGithubIssueException,
)


class SEGithubIssueInvalidTitle(SEInvalidGithubIssueException):
    """Exception raised when an invalid ``title`` is provided."""

from __future__ import annotations

from ticket_docs.models.issues.exceptions.github_issue.se_invalid_github_issue_exception import (
    SEInvalidGithubIssueException,
)


class SEGithubIssueInvalidSubIssues(SEInvalidGithubIssueException):
    """Exception raised when an invalid ``sub_issues`` is provided."""

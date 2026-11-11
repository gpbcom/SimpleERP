from __future__ import annotations

from ticket_docs.models.issues.exceptions.issue_rules.se_invalid_issue_rules_exception import (
    SEInvalidIssueRulesException,
)


class SEIssueRulesUnreadable(SEInvalidIssueRulesException):
    """Exception raised when the issue rules catalogue file cannot be read."""

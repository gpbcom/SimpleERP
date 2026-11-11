from __future__ import annotations

from ticket_docs.models.issues.exceptions.issue_rules.se_invalid_issue_rules_exception import (
    SEInvalidIssueRulesException,
)


class SEIssueRulesInconsistent(SEInvalidIssueRulesException):
    """Exception raised when the issue rules contradict each other."""

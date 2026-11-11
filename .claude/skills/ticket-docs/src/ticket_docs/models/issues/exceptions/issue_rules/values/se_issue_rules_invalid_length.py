from __future__ import annotations

from ticket_docs.models.issues.exceptions.issue_rules.se_invalid_issue_rules_exception import (
    SEInvalidIssueRulesException,
)


class SEIssueRulesInvalidLength(SEInvalidIssueRulesException):
    """Exception raised when an invalid ``title_max_length`` is provided."""

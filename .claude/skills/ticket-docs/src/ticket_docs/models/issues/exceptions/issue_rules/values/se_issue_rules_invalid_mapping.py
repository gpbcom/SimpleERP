from __future__ import annotations

from ticket_docs.models.issues.exceptions.issue_rules.se_invalid_issue_rules_exception import (
    SEInvalidIssueRulesException,
)


class SEIssueRulesInvalidMapping(SEInvalidIssueRulesException):
    """Exception raised when an invalid mapping of names to labels, kinds or options is provided."""

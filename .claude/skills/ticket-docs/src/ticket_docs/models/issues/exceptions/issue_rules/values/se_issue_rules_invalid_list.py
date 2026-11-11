from __future__ import annotations

from ticket_docs.models.issues.exceptions.issue_rules.se_invalid_issue_rules_exception import (
    SEInvalidIssueRulesException,
)


class SEIssueRulesInvalidList(SEInvalidIssueRulesException):
    """Exception raised when an invalid list of labels, sections, columns, prefixes or statuses is provided."""

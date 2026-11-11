from __future__ import annotations

from ticket_docs.models.issues.exceptions.issue_rules.se_invalid_issue_rules_exception import (
    SEInvalidIssueRulesException,
)


class SEIssueRulesInvalidReferenceKinds(SEInvalidIssueRulesException):
    """Exception raised when an invalid ``reference_kinds`` is provided."""

from __future__ import annotations

from project_docs.models.catalogs.exceptions.doc_map_rule.se_invalid_doc_map_rule_exception import (
    SEInvalidDocMapRuleException,
)


class SEDocMapRuleInvalidChapters(SEInvalidDocMapRuleException):
    """Exception raised when an invalid ``chapters`` is provided."""

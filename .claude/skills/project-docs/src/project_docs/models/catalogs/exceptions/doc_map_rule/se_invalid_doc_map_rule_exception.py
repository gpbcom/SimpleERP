from __future__ import annotations

from project_docs.models.exceptions import SEProjectDocsError


class SEInvalidDocMapRuleException(SEProjectDocsError):
    """Exception raised when an invalid DocMapRule is provided."""

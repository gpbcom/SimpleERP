from __future__ import annotations

from project_docs.models.exceptions import SEProjectDocsError


class SEInvalidDocMapException(SEProjectDocsError):
    """Exception raised when an invalid DocMap is provided."""

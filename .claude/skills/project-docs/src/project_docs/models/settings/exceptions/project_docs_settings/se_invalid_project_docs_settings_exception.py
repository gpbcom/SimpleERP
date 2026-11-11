from __future__ import annotations

from project_docs.models.exceptions import SEProjectDocsError


class SEInvalidProjectDocsSettingsException(SEProjectDocsError):
    """Exception raised when an invalid ProjectDocsSettings is provided."""

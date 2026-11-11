from __future__ import annotations

from project_docs.models.exceptions import SEProjectDocsError


class SEProjectDocsServiceError(SEProjectDocsError):
    """Base class for every error raised while mapping or checking the documentation."""

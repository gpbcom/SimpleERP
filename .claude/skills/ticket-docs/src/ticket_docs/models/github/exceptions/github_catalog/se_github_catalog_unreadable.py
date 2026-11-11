from __future__ import annotations

from ticket_docs.models.github.exceptions.github_catalog.se_invalid_github_catalog_exception import (
    SEInvalidGithubCatalogException,
)


class SEGithubCatalogUnreadable(SEInvalidGithubCatalogException):
    """Exception raised when the GitHub catalogue file cannot be read."""

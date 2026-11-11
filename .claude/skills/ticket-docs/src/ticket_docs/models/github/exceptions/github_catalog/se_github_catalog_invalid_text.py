from __future__ import annotations

from ticket_docs.models.github.exceptions.github_catalog.se_invalid_github_catalog_exception import (
    SEInvalidGithubCatalogException,
)


class SEGithubCatalogInvalidText(SEInvalidGithubCatalogException):
    """Exception raised when an invalid ``owner``, ``repository``, branch or ``evidence_release_prefix`` is provided."""

from __future__ import annotations

from project_docs.models.catalogs.exceptions.doc_map.se_invalid_doc_map_exception import SEInvalidDocMapException


class SEDocMapInvalidChapterPattern(SEInvalidDocMapException):
    """Exception raised when an invalid ``per_service`` or ``per_frontend`` is provided."""

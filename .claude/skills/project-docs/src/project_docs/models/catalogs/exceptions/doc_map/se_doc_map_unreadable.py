from __future__ import annotations

from project_docs.models.catalogs.exceptions.doc_map.se_invalid_doc_map_exception import SEInvalidDocMapException


class SEDocMapUnreadable(SEInvalidDocMapException):
    """Exception raised when the doc map file cannot be read or parsed."""

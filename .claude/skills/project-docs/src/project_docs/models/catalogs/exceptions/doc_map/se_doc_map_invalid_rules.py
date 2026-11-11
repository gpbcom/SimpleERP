from __future__ import annotations

from project_docs.models.catalogs.exceptions.doc_map.se_invalid_doc_map_exception import SEInvalidDocMapException


class SEDocMapInvalidRules(SEInvalidDocMapException):
    """Exception raised when an invalid ``rules`` is provided."""

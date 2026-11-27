from __future__ import annotations

from erp_platform.models.contracts.exceptions.document.se_open_api_document_error import SEOpenApiDocumentError


class SEOpenApiDocumentUnreadableError(SEOpenApiDocumentError):
    """Raised when an OpenAPI document cannot be read or is not a JSON object."""

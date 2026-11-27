from __future__ import annotations

from erp_models.paging.exceptions.se_invalid_cursor_page_exception import SEInvalidCursorPageException


class SECursorPageInvalidItems(SEInvalidCursorPageException):
    """Exception raised when an invalid ``items`` is provided."""

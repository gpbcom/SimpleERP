from __future__ import annotations

from erp_models.paging.exceptions.se_invalid_cursor_page_exception import SEInvalidCursorPageException


class SECursorPageInvalidNextCursor(SEInvalidCursorPageException):
    """Exception raised when an invalid ``next_cursor`` is provided."""

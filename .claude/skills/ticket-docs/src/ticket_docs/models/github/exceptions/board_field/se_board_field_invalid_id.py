from __future__ import annotations

from ticket_docs.models.github.exceptions.board_field.se_invalid_board_field_exception import (
    SEInvalidBoardFieldException,
)


class SEBoardFieldInvalidId(SEInvalidBoardFieldException):
    """Exception raised when an invalid ``id`` is provided."""

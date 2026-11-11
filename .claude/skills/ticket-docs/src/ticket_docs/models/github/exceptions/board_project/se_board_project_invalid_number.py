from __future__ import annotations

from ticket_docs.models.github.exceptions.board_project.se_invalid_board_project_exception import (
    SEInvalidBoardProjectException,
)


class SEBoardProjectInvalidNumber(SEInvalidBoardProjectException):
    """Exception raised when an invalid ``number`` is provided."""

from __future__ import annotations

from ticket_docs.models.github.exceptions.board_project.se_invalid_board_project_exception import (
    SEInvalidBoardProjectException,
)


class SEBoardProjectInvalidText(SEInvalidBoardProjectException):
    """Exception raised when an invalid ``url`` or ``id`` is provided."""

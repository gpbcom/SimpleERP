from __future__ import annotations

from harness_core.models.git.exceptions.se_invalid_file_change_exception import SEInvalidFileChangeException


class SEFileChangeInvalidPath(SEInvalidFileChangeException):
    """Exception raised when an invalid ``path`` is provided."""

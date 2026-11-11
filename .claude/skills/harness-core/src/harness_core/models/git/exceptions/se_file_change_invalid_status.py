from __future__ import annotations

from harness_core.models.git.exceptions.se_invalid_file_change_exception import SEInvalidFileChangeException


class SEFileChangeInvalidStatus(SEInvalidFileChangeException):
    """Exception raised when an invalid ``status`` is provided."""

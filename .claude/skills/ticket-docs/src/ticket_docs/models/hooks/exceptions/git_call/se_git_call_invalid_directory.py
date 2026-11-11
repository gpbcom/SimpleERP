from __future__ import annotations

from ticket_docs.models.hooks.exceptions.git_call.se_invalid_git_call_exception import SEInvalidGitCallException


class SEGitCallInvalidDirectory(SEInvalidGitCallException):
    """Exception raised when an invalid ``directory`` is provided."""

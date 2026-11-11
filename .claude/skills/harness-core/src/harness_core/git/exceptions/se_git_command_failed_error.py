from __future__ import annotations

from harness_core.git.exceptions.se_git_error import SEGitError


class SEGitCommandFailedError(SEGitError):
    """Raised when a git command exits with an error."""

from __future__ import annotations

from harness_core.github.exceptions.se_github_error import SEGithubError


class SEGithubTokenMissingError(SEGithubError):
    """Raised when no GitHub token can be found."""

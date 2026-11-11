from __future__ import annotations

from harness_core.github.exceptions.se_github_error import SEGithubError


class SEGithubRequestFailedError(SEGithubError):
    """Raised when GitHub cannot be reached or answers with an error."""

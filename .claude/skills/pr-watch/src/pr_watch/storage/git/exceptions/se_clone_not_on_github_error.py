from __future__ import annotations

from pr_watch.storage.git.exceptions.se_clone_error import SECloneError


class SECloneNotOnGithubError(SECloneError):
    """Raised when the clone's ``origin`` is not a GitHub repository."""

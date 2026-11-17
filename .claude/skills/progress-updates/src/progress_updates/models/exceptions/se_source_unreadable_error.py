from __future__ import annotations

from progress_updates.models.exceptions.se_progress_updates_error import SEProgressUpdatesError


class SESourceUnreadableError(SEProgressUpdatesError):
    """Raised when a source of tasks (a folder, ``ps``, ``gh``) cannot be read."""

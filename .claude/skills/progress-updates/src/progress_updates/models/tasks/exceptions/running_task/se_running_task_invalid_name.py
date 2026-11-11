from __future__ import annotations

from progress_updates.models.tasks.exceptions.running_task.se_invalid_running_task_exception import (
    SEInvalidRunningTaskException,
)


class SERunningTaskInvalidName(SEInvalidRunningTaskException):
    """Exception raised when an invalid ``name`` is provided."""

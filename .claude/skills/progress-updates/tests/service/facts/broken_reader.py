from __future__ import annotations

from typing import List

from progress_updates.models.enums import TaskSource
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.storage.task_reader import TaskReader


class BrokenReader(TaskReader):
    """A reader whose source cannot be read, as ``gh`` without a network."""

    def __init__(self) -> None:
        super().__init__(TaskSource.ACTIONS)

    def tasks(self) -> List[RunningTask]:
        raise SESourceUnreadableError("GitHub Actions cannot be read. The gh command failed.")

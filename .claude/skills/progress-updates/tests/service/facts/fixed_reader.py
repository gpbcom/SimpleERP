from __future__ import annotations

from typing import List

from progress_updates.models.enums import TaskSource
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.storage.task_reader import TaskReader


class FixedReader(TaskReader):
    """A reader returning the tasks it was given."""

    def __init__(self, tasks: List[RunningTask]) -> None:
        super().__init__(TaskSource.BACKGROUND)
        self.found = tasks

    def tasks(self) -> List[RunningTask]:
        return list(self.found)

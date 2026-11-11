from __future__ import annotations

from typing import List

from progress_updates.models.enums import TaskSource
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.storage.task_reader import TaskReader


class SequenceReader(TaskReader):
    """A reader whose tasks change at each read, then stay as the last ones."""

    def __init__(self, reads: List[List[RunningTask]]) -> None:
        super().__init__(TaskSource.BACKGROUND)
        self.reads = reads
        self.count = 0

    def tasks(self) -> List[RunningTask]:
        tasks = self.reads[min(self.count, len(self.reads) - 1)]
        self.count += 1
        return list(tasks)

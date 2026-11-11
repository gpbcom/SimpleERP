from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional, Set, Tuple

# First-party imports
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.storage.task_reader import TaskReader


class FactCollector:
    """Gathers the tasks of an update from every source, declared tasks first.

    Attributes:
        readers (List[TaskReader]): The sources.
        declared (List[RunningTask]): The tasks Claude declares, such as subagents.
        logger (Logger): Logger instance.

    Notes:
        **A source that cannot be read becomes a warning task**, so that the update says so and the other sources are
        still reported (CS-11).
    """

    def __init__(self, readers: List[TaskReader], declared: List[RunningTask], logger: Optional[Logger] = None) -> None:
        """Set the sources.

        Args:
            readers (List[TaskReader]): The sources.
            declared (List[RunningTask]): The tasks Claude declares.
            logger (Optional[Logger]): Logger instance.
        """
        self.readers = readers
        self.declared = declared
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def collect(self) -> List[RunningTask]:
        """Read every source.

        Returns:
            List[RunningTask]: The declared tasks, then each source's, each task once.
        """
        found: List[RunningTask] = []
        seen: Set[Tuple[TaskSource, str]] = set()
        for task in self.declared:
            if (task.source, task.name) not in seen:
                seen.add((task.source, task.name))
                found.append(task)
        for reader in self.readers:
            try:
                tasks = reader.tasks()
            except SESourceUnreadableError as error:
                self.logger.warning("The %s source was not read: %s.", reader.source.value, type(error).__name__)
                found.append(
                    RunningTask(
                        name=f"{reader.source.value} source",
                        source=reader.source,
                        state=TaskState.WARNING,
                        detail=f"not read: {error}",
                        done=None,
                        total=None,
                    )
                )
                continue
            for task in tasks:
                if (task.source, task.name) not in seen:
                    seen.add((task.source, task.name))
                    found.append(task)
        self.logger.info("Collected %d tasks from %d sources.", len(found), len(self.readers))
        return found

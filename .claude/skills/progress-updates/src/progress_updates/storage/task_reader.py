from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import ClassVar, List, Optional

# First-party imports
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.tasks.running_task import RunningTask


class TaskReader(ABC):
    """A source of the tasks an update reports.

    Attributes:
        ELLIPSIS (str): Marks a line that was cut.
        PASSED (str): The icon a recorded run that passed starts with.
        FAILED (str): The icon a recorded run that failed starts with.
        INVALID (str): The icon an invalid run starts with.
        source (TaskSource): Where the tasks are read.
        line_max_chars (int): Characters kept of an output line.
        logger (Logger): Logger instance.
    """

    ELLIPSIS: ClassVar[str] = "…"
    PASSED: ClassVar[str] = "✅"
    FAILED: ClassVar[str] = "❌"
    INVALID: ClassVar[str] = "⚠️"

    def __init__(self, source: TaskSource, line_max_chars: int = 160, logger: Optional[Logger] = None) -> None:
        """Set the source and the line length.

        Args:
            source (TaskSource): Where the tasks are read.
            line_max_chars (int): Characters kept of an output line.
            logger (Optional[Logger]): Logger instance.
        """
        self.source = source
        self.line_max_chars = line_max_chars
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _one_line(self, text: str) -> str:
        """Put a text on one line, cut to ``line_max_chars``.

        Args:
            text (str): The text.

        Returns:
            str: The text on one line, ending with an ellipsis when it was cut.
        """
        line = " ".join(text.split())
        if len(line) <= self.line_max_chars:
            return line
        return line[: self.line_max_chars - 1] + self.ELLIPSIS

    def _verdict(self, line: str) -> Optional[TaskState]:
        """Read the verdict a line starts with, as ``ticket-docs record-run`` writes it.

        Args:
            line (str): The line, such as ``✅ PASS 43/43``.

        Returns:
            Optional[TaskState]: Done, failed or warning, ``None`` when the line starts with no verdict.
        """
        icon = next((mark for mark in (self.PASSED, self.FAILED, self.INVALID) if line.startswith(mark)), "")
        match icon:
            case self.PASSED:
                return TaskState.DONE
            case self.FAILED:
                return TaskState.FAILED
            case self.INVALID:
                return TaskState.WARNING
            case _:
                return None

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def tasks(self) -> List[RunningTask]:
        """Read the tasks of the source.

        Returns:
            List[RunningTask]: The tasks found.

        Raises:
            SESourceUnreadableError: When the source cannot be read.
        """

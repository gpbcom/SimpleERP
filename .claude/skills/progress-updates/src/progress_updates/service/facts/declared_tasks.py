from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, List, Optional, Pattern

# First-party imports
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.tasks.exceptions import SEInvalidRunningTaskException
from progress_updates.models.tasks.running_task import RunningTask


class DeclaredTasks:
    """Reads the tasks Claude declares on the command line: ``name=state:detail [done/total]``.

    Attributes:
        DECLARATION (Pattern[str]): A declaration.
        COUNTS (Pattern[str]): The optional counts at the end of the detail.
        logger (Logger): Logger instance.

    Notes:
        A declaration that cannot be read becomes a warning task, so that the mistake shows in the update.
    """

    DECLARATION: ClassVar[Pattern[str]] = re.compile(r"^(?P<name>[^=]+)=(?P<state>[a-z]+)(?::(?P<detail>.*))?$", re.S)
    COUNTS: ClassVar[Pattern[str]] = re.compile(r"\s*\[(\d+)/(\d+)\]\s*$")

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _warning(self, text: str, name: str) -> RunningTask:
        """Turn a declaration that cannot be read into a warning task.

        Args:
            text (str): The declaration.
            name (str): The name read from it, empty when none was.

        Returns:
            RunningTask: A warning task quoting the declaration.
        """
        self.logger.warning("Bad task declaration: %r.", text)
        return RunningTask(
            name=name or text.strip() or "declared task",
            source=TaskSource.DECLARED,
            state=TaskState.WARNING,
            detail=f"bad declaration: {text!r}",
            done=None,
            total=None,
        )

    def _task(self, text: str) -> RunningTask:
        """Read one declaration.

        Args:
            text (str): The declaration.

        Returns:
            RunningTask: The task, or a warning task when the declaration cannot be read.
        """
        matched = self.DECLARATION.match(text.strip())
        if matched is None:
            return self._warning(text, "")
        detail = matched.group("detail") or ""
        counts = self.COUNTS.search(detail)
        try:
            return RunningTask.model_validate(
                {
                    "name": matched.group("name"),
                    "source": TaskSource.DECLARED.value,
                    "state": matched.group("state"),
                    "detail": self.COUNTS.sub("", detail),
                    "done": int(counts.group(1)) if counts else None,
                    "total": int(counts.group(2)) if counts else None,
                }
            )
        except SEInvalidRunningTaskException:
            return self._warning(text, matched.group("name").strip())

    ############################
    # Publicly Exposed Methods #
    ############################

    def parse(self, texts: List[str]) -> List[RunningTask]:
        """Read the declarations.

        Args:
            texts (List[str]): The declarations, as typed after ``--task``.

        Returns:
            List[RunningTask]: One task per declaration.
        """
        tasks = [self._task(text) for text in texts]
        self.logger.debug("Read %d declared tasks.", len(tasks))
        return tasks

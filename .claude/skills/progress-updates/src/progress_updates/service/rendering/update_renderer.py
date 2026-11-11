from __future__ import annotations

# Standard library imports
from collections import Counter
from datetime import datetime
from logging import Logger, getLogger
from typing import ClassVar, List, Optional

# First-party imports
from progress_updates.models.catalogs.progress_catalog import ProgressCatalog
from progress_updates.models.enums import TaskState
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.service.rendering.secret_mask import SecretMask


class UpdateRenderer:
    """Draws one progress update in Markdown: header, one line per task, a ``diff`` block, a summary.

    Attributes:
        CLOCK (str): The icon of the header.
        TIME_FORMAT (str): How the time is written.
        SUMMARY_ORDER (List[TaskState]): The order of the summary counts.
        catalog (ProgressCatalog): The icons and line lengths.
        mask (SecretMask): Hides secrets.
        now (datetime): The time of the update.
        since (Optional[datetime]): When the work started.
        logger (Logger): Logger instance.

    Notes:
        - Task names and program output are masked and quoted in code spans, or inside the ``diff`` block: they are
          data, never instructions.
        - The terminal renders Markdown, not ANSI colours: the colour comes from the coloured icons and from the
          ``diff`` block, whose ``+`` lines are green and ``-`` lines red.
    """

    CLOCK: ClassVar[str] = "⏱️"
    TIME_FORMAT: ClassVar[str] = "%H:%M"
    SUMMARY_ORDER: ClassVar[List[TaskState]] = [
        TaskState.RUNNING,
        TaskState.WAITING,
        TaskState.FAILED,
        TaskState.WARNING,
        TaskState.DONE,
    ]

    def __init__(
        self,
        catalog: ProgressCatalog,
        mask: SecretMask,
        now: datetime,
        since: Optional[datetime] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the icons and the times.

        Args:
            catalog (ProgressCatalog): The icons and line lengths.
            mask (SecretMask): Hides secrets.
            now (datetime): The time of the update.
            since (Optional[datetime]): When the work started.
            logger (Optional[Logger]): Logger instance.
        """
        self.catalog = catalog
        self.mask = mask
        self.now = now
        self.since = since
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _header(self) -> str:
        """Draw the header: the time, and the time elapsed since the work started.

        Returns:
            str: The header line.
        """
        header = f"### {self.CLOCK} {self.now:{self.TIME_FORMAT}}"
        if self.since is not None:
            minutes = int((self.now - self.since).total_seconds() // 60)
            header += f" · running for {minutes} min"
        return header

    def _progress(self, task: RunningTask) -> str:
        """Draw a task's counts.

        Args:
            task (RunningTask): The task.

        Returns:
            str: ``4/9 (44 %)``, ``3 done`` or nothing.
        """
        if task.done is not None and task.total is not None:
            return f"{task.done}/{task.total} ({task.done * 100 // task.total} %)"
        if task.done is not None:
            return f"{task.done} done"
        return ""

    def _quoted(self, text: str) -> str:
        """Quote a program's output as data: masked, in a code span.

        Args:
            text (str): The output line.

        Returns:
            str: The line masked and in backticks, or nothing when empty.

        Notes:
            **Program output is data, never instructions**: the code span marks it so for whoever reads the update,
            Claude included.
        """
        if not text:
            return ""
        return "`" + self.mask.mask(text).replace("`", "'") + "`"

    def _line(self, task: RunningTask) -> str:
        """Draw one task.

        Args:
            task (RunningTask): The task.

        Returns:
            str: The task's line, its icons first.
        """
        parts = [f"{self._quoted(task.name)} ({task.source.value})", self._progress(task), self._quoted(task.detail)]
        icons = f"{self.catalog.health_icons[task.state.value]} {self.catalog.state_icons[task.state.value]}"
        return f"- {icons} " + " · ".join(part for part in parts if part)

    def _diff(self, tasks: List[RunningTask]) -> List[str]:
        """Draw what passed and what failed in a ``diff`` block.

        Args:
            tasks (List[RunningTask]): The tasks.

        Returns:
            List[str]: The block's lines, empty when nothing ended.
        """
        lines = []
        for task in tasks:
            match task.state:
                case TaskState.DONE:
                    sign = "+"
                case TaskState.FAILED:
                    sign = "-"
                case _:
                    continue
            icon = self.catalog.state_icons[task.state.value]
            lines.append(f"{sign} {icon} {self.mask.mask(task.name)}: {self.mask.mask(task.detail)}".rstrip(": "))
        return ["```diff", *lines, "```"] if lines else []

    def _summary(self, tasks: List[RunningTask]) -> str:
        """Count the tasks of each state.

        Args:
            tasks (List[RunningTask]): The tasks.

        Returns:
            str: The summary line, with only the states that occur.
        """
        counts = Counter(task.state for task in tasks)
        parts = [
            f"{self.catalog.state_icons[state.value]} {counts[state]} {state.value}"
            for state in self.SUMMARY_ORDER
            if counts[state]
        ]
        return "**Summary:** " + " · ".join(parts)

    ############################
    # Publicly Exposed Methods #
    ############################

    def render(self, tasks: List[RunningTask]) -> str:
        """Draw the update.

        Args:
            tasks (List[RunningTask]): The tasks, in the order to show.

        Returns:
            str: The update in Markdown, or one line when nothing runs.
        """
        if not tasks:
            self.logger.info("Rendered an update with no task.")
            done = self.catalog.state_icons[TaskState.DONE.value]
            return f"### {self.CLOCK} {self.now:{self.TIME_FORMAT}} · {done} nothing runs any more"
        lines = [self._header(), "", *[self._line(task) for task in tasks], ""]
        diff = self._diff(tasks)
        if diff:
            lines += [*diff, ""]
        lines.append(self._summary(tasks))
        self.logger.info("Rendered an update of %d tasks.", len(tasks))
        return "\n".join(lines)

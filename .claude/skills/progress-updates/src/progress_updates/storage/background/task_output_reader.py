from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern

# First-party imports
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.models.watch.watch_marker import WatchMarker
from progress_updates.storage.task_reader import TaskReader


class TaskOutputReader(TaskReader):
    """Reads the commands Claude Code moved to the background, from their output files.

    Attributes:
        SUFFIX (str): The suffix of an output file.
        EXIT (Pattern[str]): The line Claude Code adds when the command ends.
        TRANSCRIPT_START (str): How a subagent's transcript starts: those are left to the declared tasks.
        KILLED (str): The line Claude Code adds when a task is stopped by hand.
        tasks_dir (Path): The session's task folder.
        since (Optional[datetime]): Finished tasks older than this are left out.

    Notes:
        A running command has no exit line yet. A subagent's output file is its JSON transcript, which says nothing
        an update can show: Claude declares subagents with ``--task``.
        - The watch's own output (the Monitor's task) is no task: every line of it ends with a watch marker.
        - A command that exits 0 keeps the verdict of its last line: ``ticket-docs record-run`` behind a pipe can
          print ``❌ FAIL`` and still exit 0.
    """

    SUFFIX: ClassVar[str] = ".output"
    EXIT: ClassVar[Pattern[str]] = re.compile(r"^\[exited with code (\d+)\]$")
    TRANSCRIPT_START: ClassVar[str] = "{"
    KILLED: ClassVar[str] = "[killed]"

    def __init__(
        self,
        tasks_dir: Path,
        line_max_chars: int,
        since: Optional[datetime] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the folder.

        Args:
            tasks_dir (Path): The session's task folder.
            line_max_chars (int): Characters kept of an output line.
            since (Optional[datetime]): Finished tasks older than this are left out.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(TaskSource.BACKGROUND, line_max_chars, logger)
        self.tasks_dir = tasks_dir
        self.since = since

    ############################
    # Internal Helpers Methods #
    ############################

    def _task(self, path: Path) -> Optional[RunningTask]:
        """Read one output file.

        Args:
            path (Path): The output file.

        Returns:
            Optional[RunningTask]: The task, ``None`` for a transcript or a finished task older than ``since``.
        """
        text = path.read_text(encoding="utf-8", errors="replace")
        if text.lstrip().startswith(self.TRANSCRIPT_START):
            self.logger.debug("%s is a transcript: left to the declared tasks.", path.name)
            return None
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        events = [line for line in lines if not self.EXIT.match(line) and line != self.KILLED]
        if events and all(any(marker.value in line for marker in WatchMarker) for line in events):
            self.logger.debug("%s is the watch's own output.", path.name)
            return None
        last = lines[-1] if lines else ""
        ended = self.EXIT.match(last)
        before = lines[-2] if len(lines) > 1 else ""
        if ended is None and last != self.KILLED:
            state, detail = TaskState.RUNNING, last
        else:
            if self.since and path.stat().st_mtime < self.since.timestamp():
                self.logger.debug("%s ended before the update's start.", path.name)
                return None
            if last == self.KILLED:
                state, detail = TaskState.WARNING, f"stopped: {before}"
            elif ended is not None and int(ended.group(1)) == 0:
                state, detail = self._verdict(before) or TaskState.DONE, before
            else:
                state, detail = TaskState.FAILED, before
        return RunningTask(
            name=path.stem, source=self.source, state=state, detail=self._one_line(detail), done=None, total=None
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def tasks(self) -> List[RunningTask]:
        """Read every background command of the session.

        Returns:
            List[RunningTask]: The running ones, and those that ended since ``since``.

        Raises:
            SESourceUnreadableError: When the folder does not exist.
        """
        if not self.tasks_dir.is_dir():
            self.logger.error("The task folder %s does not exist.", self.tasks_dir)
            raise SESourceUnreadableError(
                f"The task folder {self.tasks_dir} cannot be read. "  # noqa: E501
                "It does not exist."
            )
        found: List[RunningTask] = []
        for path in sorted(self.tasks_dir.glob(f"*{self.SUFFIX}")):
            try:
                task = self._task(path)
            except OSError as error:
                self.logger.warning("Could not read %s: %s.", path.name, type(error).__name__)
                continue
            if task is not None:
                found.append(task)
        self.logger.info("Read %d background tasks.", len(found))
        return found

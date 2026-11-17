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
from progress_updates.storage.task_reader import TaskReader


class EvidenceReader(TaskReader):
    """Reads the newest runs of a ticket's evidence folder, written by ``ticket-docs record-run``.

    Attributes:
        README (str): The file that holds a run's result.
        RESULT (Pattern[str]): The Result row of that file.
        EXPECTED_RED (str): What ``record-run --expect red`` writes on a TDD red run.
        AS_EXPECTED (str): What it adds when the run failed as expected.
        folder (Path): The ticket's ``tests-evidences`` folder.
        count (int): How many of the newest runs are read.
        since (Optional[datetime]): Runs older than this are left out.
    """

    README: ClassVar[str] = "README.md"
    RESULT: ClassVar[Pattern[str]] = re.compile(r"\*\*Result\*\*\s*\|\s*([^|\n]+)\|")
    EXPECTED_RED: ClassVar[str] = "expected red"
    AS_EXPECTED: ClassVar[str] = ", as expected"

    def __init__(
        self,
        folder: Path,
        count: int,
        line_max_chars: int,
        since: Optional[datetime] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the folder.

        Args:
            folder (Path): The ticket's ``tests-evidences`` folder.
            count (int): How many of the newest runs are read.
            line_max_chars (int): Characters kept of a result.
            since (Optional[datetime]): Runs older than this are left out.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(TaskSource.EVIDENCE, line_max_chars, logger)
        self.folder = folder
        self.count = count
        self.since = since

    ############################
    # Internal Helpers Methods #
    ############################

    def _state(self, result: str) -> TaskState:
        """Read a run's state from its result.

        Args:
            result (str): The Result cell, such as ``✅ PASS 43/43``.

        Returns:
            TaskState: Done, failed, warning, or running while the README is not written yet.

        Notes:
            A TDD red run is meant to fail: it is done when it failed as expected, and failed otherwise.
        """
        if self.EXPECTED_RED in result:
            return TaskState.DONE if self.AS_EXPECTED in result else TaskState.FAILED
        verdict = self._verdict(result)
        return verdict if verdict is not None else TaskState.RUNNING

    ############################
    # Publicly Exposed Methods #
    ############################

    def tasks(self) -> List[RunningTask]:
        """Read the newest runs.

        Returns:
            List[RunningTask]: One task per run, newest first.

        Raises:
            SESourceUnreadableError: When the folder does not exist.
        """
        if not self.folder.is_dir():
            self.logger.error("The evidence folder %s does not exist.", self.folder)
            raise SESourceUnreadableError(
                f"The evidence folder {self.folder} cannot be read. "  # noqa: E501
                "It does not exist."
            )
        runs = sorted((path for path in self.folder.iterdir() if path.is_dir()), key=lambda path: path.stat().st_mtime)
        found: List[RunningTask] = []
        for run in reversed(runs[-self.count :] if self.count else []):
            if self.since and run.stat().st_mtime < self.since.timestamp():
                continue
            readme = run / self.README
            matched = self.RESULT.search(readme.read_text(encoding="utf-8")) if readme.is_file() else None
            result = matched.group(1).strip() if matched else "being written"
            found.append(
                RunningTask(
                    name=run.name,
                    source=self.source,
                    state=self._state(result),
                    detail=self._one_line(result),
                    done=None,
                    total=None,
                )
            )
        self.logger.info("Read %d runs in %s.", len(found), self.folder)
        return found

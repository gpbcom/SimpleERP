from __future__ import annotations

# Standard library imports
import subprocess
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.storage.task_reader import TaskReader


class ProcessReader(TaskReader):
    """Reads the processes working in the repository, with ``ps``.

    Attributes:
        COMMAND (Tuple[str, ...]): The ``ps`` command: pid, elapsed seconds, command line.
        IGNORED (Tuple[str, ...]): Command lines left out: the progress tool itself.
        root (Path): The repository.
    """

    COMMAND: ClassVar[Tuple[str, ...]] = ("ps", "-eo", "pid=,etimes=,args=")
    IGNORED: ClassVar[Tuple[str, ...]] = ("progress-updates",)

    def __init__(self, root: Path, line_max_chars: int, logger: Optional[Logger] = None) -> None:
        """Set the repository.

        Args:
            root (Path): The repository.
            line_max_chars (int): Characters kept of a command line.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(TaskSource.PROCESS, line_max_chars, logger)
        self.root = root

    ############################
    # Publicly Exposed Methods #
    ############################

    def tasks(self) -> List[RunningTask]:
        """Read the processes whose command line names the repository.

        Returns:
            List[RunningTask]: One running task per process.

        Raises:
            SESourceUnreadableError: When ``ps`` cannot run or fails.
        """
        try:
            result = subprocess.run(list(self.COMMAND), capture_output=True, text=True, check=False)
        except OSError as error:
            self.logger.error("ps could not run: %s.", type(error).__name__)
            raise SESourceUnreadableError(
                "The processes cannot be read. "  # noqa: E501
                f"ps could not run: {type(error).__name__}."
            ) from error
        if result.returncode != 0:
            self.logger.error("ps failed with exit code %d.", result.returncode)
            raise SESourceUnreadableError(
                "The processes cannot be read. "  # noqa: E501
                f"ps exited with code {result.returncode}."
            )
        found: List[RunningTask] = []
        for line in result.stdout.splitlines():
            parts = line.split(None, 2)
            if len(parts) < 3 or str(self.root) not in parts[2] or any(word in parts[2] for word in self.IGNORED):
                continue
            minutes = int(parts[1]) // 60
            found.append(
                RunningTask(
                    name=self._one_line(parts[2].replace(str(self.root), ".")),
                    source=self.source,
                    state=TaskState.RUNNING,
                    detail=f"pid {parts[0]} · running for {minutes} min",
                    done=None,
                    total=None,
                )
            )
        self.logger.info("Found %d processes in %s.", len(found), self.root)
        return found

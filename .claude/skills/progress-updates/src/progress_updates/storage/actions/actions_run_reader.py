from __future__ import annotations

# Standard library imports
import json
import subprocess
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from progress_updates.models.enums import ActionsRunStatus, TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.storage.task_reader import TaskReader


class ActionsRunReader(TaskReader):
    """Reads the repository's GitHub Actions runs in progress or waiting, with ``gh``.

    Notes:
        **A run's title is left out**: it is free text that anyone opening a pull request writes, and an update is read
        by Claude, so it could carry instructions. Only the workflow's name, the run's id and its status are shown.

    Attributes:
        COMMAND (Tuple[str, ...]): The ``gh run list`` command.
        root (Path): The repository, where ``gh`` runs.
    """

    COMMAND: ClassVar[Tuple[str, ...]] = (
        "gh",
        "run",
        "list",
        "--limit",
        "20",
        "--json",
        "databaseId,workflowName,status",
    )

    def __init__(self, root: Path, line_max_chars: int, logger: Optional[Logger] = None) -> None:
        """Set the repository.

        Args:
            root (Path): The repository, where ``gh`` runs.
            line_max_chars (int): Characters kept of an output line.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(TaskSource.ACTIONS, line_max_chars, logger)
        self.root = root

    ############################
    # Internal Helpers Methods #
    ############################

    def _state(self, status: str) -> Optional[TaskState]:
        """Map a run's status to a task state.

        Args:
            status (str): The status ``gh`` gives.

        Returns:
            Optional[TaskState]: Running or waiting, ``None`` for a run that is over.
        """
        match status:
            case ActionsRunStatus.IN_PROGRESS:
                return TaskState.RUNNING
            case (
                ActionsRunStatus.QUEUED
                | ActionsRunStatus.WAITING
                | ActionsRunStatus.PENDING
                | ActionsRunStatus.REQUESTED
            ):
                return TaskState.WAITING
            case _:
                return None

    ############################
    # Publicly Exposed Methods #
    ############################

    def tasks(self) -> List[RunningTask]:
        """Read the runs that have not ended.

        Returns:
            List[RunningTask]: One task per run in progress or waiting.

        Raises:
            SESourceUnreadableError: When ``gh`` cannot run, fails, or prints something else than a list.
        """
        try:
            result = subprocess.run(list(self.COMMAND), cwd=self.root, capture_output=True, text=True, check=False)
            runs = json.loads(result.stdout) if result.returncode == 0 else None
        except (OSError, json.JSONDecodeError) as error:
            self.logger.error("gh run list could not be read: %s.", type(error).__name__)
            raise SESourceUnreadableError(
                "The GitHub Actions runs cannot be read. "  # noqa: E501
                f"gh run list failed: {type(error).__name__}."
            ) from error
        if not isinstance(runs, list):
            self.logger.error("gh run list failed with exit code %d.", result.returncode)
            raise SESourceUnreadableError(
                "The GitHub Actions runs cannot be read. "  # noqa: E501
                f"gh run list exited with code {result.returncode}."
            )
        found: List[RunningTask] = []
        for run in runs:
            state = self._state(str(run.get("status", "")))
            if state is None:
                continue
            found.append(
                RunningTask(
                    name=self._one_line(f"{run.get('workflowName', 'run')} #{run.get('databaseId', '?')}"),
                    source=self.source,
                    state=state,
                    detail=str(run.get("status", "")).replace("_", " "),
                    done=None,
                    total=None,
                )
            )
        self.logger.info("Found %d Actions runs not ended.", len(found))
        return found

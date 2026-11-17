from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class TaskSource(StrEnum):
    """Where a task an update reports was found.

    Attributes:
        BACKGROUND (str): A command Claude Code moved to the background (its output file).
        PROCESS (str): A process started under the repository.
        DECLARED (str): A task Claude declares, such as a subagent or a workflow.
        EVIDENCE (str): A run recorded in the ticket's evidence folders.
        ACTIONS (str): A GitHub Actions run in progress.
    """

    BACKGROUND = "background"
    PROCESS = "process"
    DECLARED = "declared"
    EVIDENCE = "evidence"
    ACTIONS = "actions"

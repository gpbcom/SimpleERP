from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ToolName(StrEnum):
    """The Claude Code tools whose calls can start long-running work.

    Attributes:
        BASH (str): A shell command, in the background when asked.
        AGENT (str): A subagent, in the background when asked.
        WORKFLOW (str): A workflow of subagents, always in the background.
    """

    BASH = "Bash"
    AGENT = "Agent"
    WORKFLOW = "Workflow"

from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Optional

# First-party imports
from progress_updates.models.enums import ToolName
from progress_updates.models.hooks.tool_call import ToolCall


class BackgroundReminder:
    """Reminds Claude to start the progress updates when work goes to the background.

    Attributes:
        COMMAND (str): The reminder after a background command.
        AGENT (str): The reminder after a background subagent or a workflow.
        logger (Logger): Logger instance.
    """

    COMMAND: ClassVar[str] = (
        "A command now runs in the background. The owner wants an update every 2 minutes until it ends "
        "(progress-updates skill): if no watch runs yet, start the Monitor tool on "
        "`progress-updates watch --every 120 --tasks-dir <this session's tasks folder>`, and on each of its events "
        "post the output of `progress-updates status`."
    )
    AGENT: ClassVar[str] = (
        "A subagent or a workflow now runs in the background. The owner wants an update every 2 minutes until it "
        'ends (progress-updates skill): declare it with `--task "<name>=running:<what it does>"` on '
        "`progress-updates watch --every 120` (Monitor tool) and on `progress-updates status`, post an update on each "
        "event, and stop the Monitor when it has ended."
    )

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def reminder(self, call: ToolCall) -> Optional[str]:
        """Build the reminder of a tool call.

        Args:
            call (ToolCall): The tool call the hook reports.

        Returns:
            Optional[str]: The reminder, ``None`` when the call starts nothing long.
        """
        match call.tool_name:
            case ToolName.BASH if call.background:
                self.logger.info("A background command: reminder given.")
                return self.COMMAND
            case ToolName.AGENT if call.background:
                self.logger.info("A background subagent: reminder given.")
                return self.AGENT
            case ToolName.WORKFLOW:
                self.logger.info("A workflow: reminder given.")
                return self.AGENT
            case _:
                self.logger.debug("%s in the foreground: no reminder.", call.tool_name)
                return None

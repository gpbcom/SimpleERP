from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import List, Optional, TextIO

# First-party imports
from ai_cost.api.cli.ai_cost_cli import AiCostCli
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from harness_core.terminal.human_confirmation import HumanConfirmation


class CommandFactory(ABC):
    """Builds the entry points of the guard.

    Attributes:
        logger (Logger): Logger instance.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def cli(
        self,
        arguments: List[str],
        stdin: TextIO,
        stdout: TextIO,
        stderr: TextIO,
        settings: Optional[GuardSettings] = None,
        environment: Optional[CallerEnvironment] = None,
        confirmation: Optional[HumanConfirmation] = None,
    ) -> AiCostCli:
        """Build the command line.

        Args:
            arguments (List[str]): The command line, without the program name.
            stdin (TextIO): Where the hook's input is read.
            stdout (TextIO): Where results go.
            stderr (TextIO): Where errors go.
            settings (Optional[GuardSettings]): The enforcing settings, read from the versioned file when ``None``.
            environment (Optional[CallerEnvironment]): The caller's values, read from the environment when ``None``.
            confirmation (Optional[HumanConfirmation]): The person's terminal, ``/dev/tty`` when ``None``.

        Returns:
            AiCostCli: The command line, not run yet.
        """

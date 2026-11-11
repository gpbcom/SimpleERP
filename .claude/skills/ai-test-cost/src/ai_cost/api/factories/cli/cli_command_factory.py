from __future__ import annotations

# Standard library imports
from logging import Logger
from pathlib import Path
from typing import List, Optional, TextIO

# First-party imports
from ai_cost.api.cli.ai_cost_cli import AiCostCli
from ai_cost.api.factories.command_factory import CommandFactory
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from harness_core.terminal.human_confirmation import HumanConfirmation


class CliCommandFactory(CommandFactory):
    """Builds the ``ai-cost`` command line.

    Attributes:
        settings_file (Path): The versioned settings file.
        logger (Logger): Logger instance.
    """

    def __init__(self, settings_file: Path, logger: Optional[Logger] = None) -> None:
        """Set the settings file.

        Args:
            settings_file (Path): The versioned settings file.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.settings_file = settings_file

    ############################
    # Publicly Exposed Methods #
    ############################

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
        self.logger.debug("Building the ai-cost command line.")
        terminal = confirmation if confirmation is not None else HumanConfirmation(logger=self.logger)
        return AiCostCli(
            arguments, self.settings_file, settings, environment, stdin, stdout, stderr, terminal, self.logger
        )

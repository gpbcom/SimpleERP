from __future__ import annotations

# Standard library imports
import subprocess
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from ticket_docs.models.evidence.command_outcome import CommandOutcome


class CommandRunner:
    """Runs a command and keeps everything it writes.

    Attributes:
        NOT_FOUND_EXIT_CODE (int): The exit code of a program that cannot be started, as a shell gives it.
        logger (Logger): Logger instance.

    Notes:
        The standard error is merged into the standard output, so that the kept output reads in the order it was
        written.
    """

    NOT_FOUND_EXIT_CODE: ClassVar[int] = 127

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def run(self, command: List[str], cwd: Path, stdin: str = "") -> CommandOutcome:
        """Run a command until it ends.

        Args:
            command (List[str]): The program and its arguments.
            cwd (Path): The folder it runs in.
            stdin (str): What the command reads on its standard input.

        Returns:
            CommandOutcome: Its exit code and output. A program that cannot be started exits 127.
        """
        self.logger.debug("Running %s in %s.", command[0] if command else "", cwd)
        try:
            done = subprocess.run(
                command,
                cwd=cwd,
                input=stdin,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                check=False,
            )
        except OSError as error:
            self.logger.warning("%s could not start: %s.", command[0] if command else "", type(error).__name__)
            return CommandOutcome(exit_code=self.NOT_FOUND_EXIT_CODE, output=f"{command[0]}: {error}\n")
        self.logger.info("%s ended with exit code %d.", command[0], done.returncode)
        return CommandOutcome(exit_code=done.returncode, output=done.stdout or "")

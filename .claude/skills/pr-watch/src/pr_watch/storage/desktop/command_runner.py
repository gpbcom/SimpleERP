from __future__ import annotations

# Standard library imports
import shutil
import subprocess
from logging import Logger, getLogger
from typing import ClassVar, List, Optional


class CommandRunner:
    """Starts the desktop programs and the Claude Code command line.

    Attributes:
        TIMEOUT_S (int): The longest a program may take.
        MESSAGE_LENGTH (int): The characters of a program's error kept in a failure.
        logger (Logger): Logger instance.

    Notes:
        A failure comes back as a value, never as an exception: the caller records it, and the next run tries again.
    """

    TIMEOUT_S: ClassVar[int] = 60
    MESSAGE_LENGTH: ClassVar[int] = 200

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _run(self, command: List[str]) -> subprocess.CompletedProcess[str]:
        """Run a program and wait for it.

        Args:
            command (List[str]): The program and its arguments.

        Returns:
            subprocess.CompletedProcess[str]: What it did.

        Raises:
            OSError: When the program cannot start.
            subprocess.SubprocessError: When it runs out of time.
        """
        self.logger.debug("Running %s.", command[0])
        return subprocess.run(command, capture_output=True, text=True, timeout=self.TIMEOUT_S, check=False)

    ############################
    # Publicly Exposed Methods #
    ############################

    def available(self, program: str) -> bool:
        """Tell whether a program can be started.

        Args:
            program (str): Its name on the ``PATH``, or its path.

        Returns:
            bool: ``True`` when it is found.
        """
        return shutil.which(program) is not None

    def failure_of(self, command: List[str]) -> Optional[str]:
        """Run a program and say how it failed.

        Args:
            command (List[str]): The program and its arguments.

        Returns:
            Optional[str]: Why it failed, ``None`` when it succeeded.
        """
        try:
            result = self._run(command)
        except (OSError, subprocess.SubprocessError) as error:
            self.logger.warning("%s could not run: %s.", command[0], type(error).__name__)
            return f"{command[0]}: {type(error).__name__}"
        if result.returncode:
            self.logger.warning("%s exited with code %d.", command[0], result.returncode)
            return f"{command[0]} exited {result.returncode}: {result.stderr.strip()[: self.MESSAGE_LENGTH]}"
        self.logger.info("Ran %s.", command[0])
        return None

    def output_of(self, command: List[str]) -> Optional[str]:
        """Run a program and give what it printed.

        Args:
            command (List[str]): The program and its arguments.

        Returns:
            Optional[str]: Its standard output, ``None`` when it failed.
        """
        try:
            result = self._run(command)
        except (OSError, subprocess.SubprocessError) as error:
            self.logger.warning("%s could not run: %s.", command[0], type(error).__name__)
            return None
        if result.returncode:
            self.logger.warning("%s exited with code %d.", command[0], result.returncode)
            return None
        return result.stdout

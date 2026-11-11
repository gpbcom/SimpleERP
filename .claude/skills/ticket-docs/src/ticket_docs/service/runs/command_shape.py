from __future__ import annotations

# Standard library imports
import shlex
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.shell.shell_command_splitter import ShellCommandSplitter


class CommandShape:
    """Reads what kind of test run a command is, and adds the options that keep its reports.

    Attributes:
        PYTEST (str): pytest's program name.
        PYTHON_PREFIX (str): The start of a Python interpreter's name, such as ``python3.13``.
        MODULE_OPTION (str): The option that runs a module with Python.
        UV (str): uv's program name.
        UV_RUN (str): uv's command that runs a program.
        NPX (str): npx's program name.
        PLAYWRIGHT (List[str]): Playwright's program and its test command, after ``npx``.
        FOLDER_MARK (str): How the README names the evidence folder in a command.
        logger (Logger): Logger instance.
        splitter (ShellCommandSplitter): Reads the variables set before the program, and ``env``.

    Notes:
        - A pytest run is ``pytest`` (any path), ``uv run [options] pytest`` or ``<python> [options] -m pytest``,
          after any ``env`` and ``NAME=value`` prefix.
        - The evidence folder's absolute path is replaced in the shown command, so that the README reads the same
          on every machine.
    """

    PYTEST: ClassVar[str] = "pytest"
    PYTHON_PREFIX: ClassVar[str] = "python"
    MODULE_OPTION: ClassVar[str] = "-m"
    UV: ClassVar[str] = "uv"
    UV_RUN: ClassVar[str] = "run"
    NPX: ClassVar[str] = "npx"
    PLAYWRIGHT: ClassVar[List[str]] = ["playwright", "test"]
    FOLDER_MARK: ClassVar[str] = "<this folder>"

    def __init__(self, logger: Optional[Logger] = None, splitter: Optional[ShellCommandSplitter] = None) -> None:
        """Set the logger and the reader of variable prefixes.

        Args:
            logger (Optional[Logger]): Logger instance.
            splitter (Optional[ShellCommandSplitter]): Reads the variables set before the program.
        """
        self.logger = logger if logger else getLogger(__name__)
        self.splitter = splitter if splitter else ShellCommandSplitter(self.logger)

    ############################
    # Internal Helpers Methods #
    ############################

    def _program(self, command: List[str]) -> List[str]:
        """Drop the ``env`` and ``NAME=value`` words before the program.

        Args:
            command (List[str]): The command.

        Returns:
            List[str]: The program and its arguments.
        """
        return self.splitter.assignments(command)[1]

    def _name(self, word: str) -> str:
        """Give a program's name without its folder.

        Args:
            word (str): The program as typed.

        Returns:
            str: Its name.
        """
        return word.rsplit("/", 1)[-1]

    ############################
    # Publicly Exposed Methods #
    ############################

    def is_pytest(self, command: List[str]) -> bool:
        """Tell whether a command runs pytest.

        Args:
            command (List[str]): The command.

        Returns:
            bool: ``True`` for pytest, ``uv run pytest`` and ``python -m pytest``.
        """
        words = self._program(command)
        if not words:
            return False
        program = self._name(words[0])
        if program == self.PYTEST:
            return True
        if program == self.UV and self.UV_RUN in words[1:2]:
            rest = [word for word in words[2:] if not word.startswith("-")]
            return bool(rest) and self._name(rest[0]) == self.PYTEST
        if program.startswith(self.PYTHON_PREFIX) and self.MODULE_OPTION in words:
            index = words.index(self.MODULE_OPTION)
            return words[index + 1 : index + 2] == [self.PYTEST]
        return False

    def is_playwright(self, command: List[str]) -> bool:
        """Tell whether a command runs Playwright's tests.

        Args:
            command (List[str]): The command.

        Returns:
            bool: ``True`` for ``npx playwright test``.
        """
        words = self._program(command)
        return bool(words) and self._name(words[0]) == self.NPX and words[1:3] == self.PLAYWRIGHT

    def with_reports(self, command: List[str], folder: Path) -> List[str]:
        """Add the options that write pytest's reports into the evidence folder.

        Args:
            command (List[str]): The command.
            folder (Path): The evidence folder.

        Returns:
            List[str]: The command with ``--junitxml``, ``--html`` and ``--self-contained-html`` for pytest, else
            the command as it is.
        """
        if not self.is_pytest(command):
            return list(command)
        self.logger.debug("pytest writes its reports into %s.", folder.name)
        return [*command, f"--junitxml={folder}/report.xml", f"--html={folder}/report.html", "--self-contained-html"]

    def display(self, command: List[str], folder: Path, relative_cwd: str) -> str:
        """Write a command the way the README shows it.

        Args:
            command (List[str]): The command as run.
            folder (Path): The evidence folder, hidden behind ``<this folder>``.
            relative_cwd (str): The folder it ran in, relative to the repository.

        Returns:
            str: ``cd <folder> && <command>``, quoted as a shell would need it.
        """
        return f"cd {relative_cwd} && {shlex.join(command).replace(str(folder), self.FOLDER_MARK)}"

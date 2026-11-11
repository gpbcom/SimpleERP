from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, FrozenSet, List, Optional

# First-party imports
from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from ticket_docs.models.hooks.git_call import GitCall


class GitInvocations:
    """Finds the git commands of a Bash command line, and the folder each one runs in.

    Attributes:
        GIT (str): git's program name.
        CD (str): The builtin that changes folder.
        DIRECTORY_OPTION (str): git's global option that runs it in another folder.
        VALUED_OPTIONS (FrozenSet[str]): git's global options followed by a value.
        splitter (ShellCommandSplitter): Splits the command line into simple commands.
        logger (Logger): Logger instance.

    Notes:
        - The words are read as the shell reads them, quotes and ``sh -c`` strings included, so ``echo git push``
          and a commit message that mentions ``git push`` are not git commands.
        - A ``cd`` changes the folder of the git commands after it, as in the shell.
    """

    GIT: ClassVar[str] = "git"
    CD: ClassVar[str] = "cd"
    DIRECTORY_OPTION: ClassVar[str] = "-C"
    VALUED_OPTIONS: ClassVar[FrozenSet[str]] = frozenset({"-C", "-c", "--git-dir", "--work-tree", "--namespace"})

    def __init__(self, splitter: ShellCommandSplitter, logger: Optional[Logger] = None) -> None:
        """Set the splitter.

        Args:
            splitter (ShellCommandSplitter): Splits the command line into simple commands.
            logger (Optional[Logger]): Logger instance.
        """
        self.splitter = splitter
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _call(self, words: List[str], directory: Path) -> Optional[GitCall]:
        """Read one git command.

        Args:
            words (List[str]): The words after ``git``.
            directory (Path): The folder the shell is in.

        Returns:
            Optional[GitCall]: The command, ``None`` when no git command follows the global options.
        """
        index = 0
        while index < len(words) and words[index].startswith("-"):
            option = words[index]
            if option in self.VALUED_OPTIONS and index + 1 < len(words):
                if option == self.DIRECTORY_OPTION:
                    directory = (directory / Path(words[index + 1]).expanduser()).resolve()
                index += 1
            index += 1
        if index >= len(words):
            return None
        return GitCall(subcommand=words[index], arguments=words[index + 1 :], directory=directory)

    ############################
    # Publicly Exposed Methods #
    ############################

    def calls(self, command: str, cwd: Path) -> List[GitCall]:
        """List the git commands of a command line.

        Args:
            command (str): The Bash command line.
            cwd (Path): The folder it starts in.

        Returns:
            List[GitCall]: Each git command, in order, with its folder.
        """
        directory = cwd.resolve()
        calls: List[GitCall] = []
        for words in self.splitter.commands(self.splitter.without_data(command)):
            program = self.splitter.assignments(words)[1]
            if not program:
                continue
            if program[0] == self.CD and len(program) > 1:
                directory = (directory / Path(program[1]).expanduser()).resolve()
            elif program[0].rsplit("/", 1)[-1] == self.GIT:
                call = self._call(program[1:], directory)
                if call is not None:
                    calls.append(call)
        self.logger.debug("Found %d git commands.", len(calls))
        return calls

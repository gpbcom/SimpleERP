from __future__ import annotations

# Standard library imports
import re
from datetime import datetime, timedelta
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern

# First-party imports
from harness_core.git.exceptions import SEGitError
from harness_core.git.git_repository import GitRepository
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEInvalidBranchNameException
from ticket_docs.service.hooks.git_invocations import GitInvocations
from ticket_docs.service.paths.tickets_root import TicketsRoot


class TimeReminder:
    """Decides whether a commit on a ticket branch needs a reminder to bring PROGRESS.md's times up to date.

    Attributes:
        COMMIT (str): git's commit command.
        PROGRESS (str): The progress file.
        TIMESTAMP (Pattern[str]): A clock reading, ``YYYY-MM-DD HH:MM``.
        RUNNING_ROW (Pattern[str]): A Status row whose step is running.
        TIMESTAMP_FORMAT (str): How a clock reading is written.
        STALE_AFTER (timedelta): How old the latest clock reading may be.
        invocations (GitInvocations): Finds the commits of the command line.
        roots (TicketsRoot): Finds the tickets folder.
        logger (Logger): Logger instance.

    Notes:
        The ticket is the one the branch names (``feature/GH-12-...``). Without a PROGRESS.md for it, nothing is said.
    """

    COMMIT: ClassVar[str] = "commit"
    PROGRESS: ClassVar[str] = "PROGRESS.md"
    TIMESTAMP: ClassVar[Pattern[str]] = re.compile(r"\b(20\d\d-\d\d-\d\d \d\d:\d\d)\b")
    RUNNING_ROW: ClassVar[Pattern[str]] = re.compile(r"^\|[^|\n]*\|\s*🔄", re.M)
    TIMESTAMP_FORMAT: ClassVar[str] = "%Y-%m-%d %H:%M"
    STALE_AFTER: ClassVar[timedelta] = timedelta(minutes=15)

    def __init__(self, invocations: GitInvocations, roots: TicketsRoot, logger: Optional[Logger] = None) -> None:
        """Set the readers.

        Args:
            invocations (GitInvocations): Finds the commits of the command line.
            roots (TicketsRoot): Finds the tickets folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.invocations = invocations
        self.roots = roots
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _progress(self, directory: Path) -> Optional[Path]:
        """Find the PROGRESS.md of the ticket a repository's branch names.

        Args:
            directory (Path): The folder the commit ran in.

        Returns:
            Optional[Path]: The file, ``None`` when the branch names no ticket or the ticket has no PROGRESS.md.
        """
        try:
            repository = GitRepository.discover(directory, self.logger)
            ticket = BranchName.parse(repository.current_branch() or "HEAD").ticket
        except (SEGitError, SEInvalidBranchNameException):
            return None
        if ticket is None:
            return None
        progress = self.roots.of(repository) / ticket / self.PROGRESS
        return progress if progress.is_file() else None

    def _problems(self, text: str) -> List[str]:
        """List what is not current in a PROGRESS.md.

        Args:
            text (str): The file's text.

        Returns:
            List[str]: The problems, empty when the time tracking is current.
        """
        problems: List[str] = []
        if not self.RUNNING_ROW.search(text):
            problems.append("no Status row is 🔄 (the step being worked on has no Started time)")
        stamps = [datetime.strptime(stamp, self.TIMESTAMP_FORMAT) for stamp in self.TIMESTAMP.findall(text)]
        if not stamps:
            problems.append("PROGRESS.md holds no `YYYY-MM-DD HH:MM` clock reading")
        elif datetime.now() - max(stamps) > self.STALE_AFTER:
            minutes = int(self.STALE_AFTER.total_seconds() // 60)
            problems.append(
                f"its latest clock reading is {max(stamps):{self.TIMESTAMP_FORMAT}}, more than {minutes} minutes ago"
            )
        return problems

    ############################
    # Publicly Exposed Methods #
    ############################

    def reminder(self, command: str, cwd: Path) -> Optional[str]:
        """Build the reminder, when a commit on a ticket branch left the times behind.

        Args:
            command (str): The Bash command line that ran.
            cwd (Path): The folder it ran in.

        Returns:
            Optional[str]: The reminder, ``None`` when none is needed.
        """
        commits = [call for call in self.invocations.calls(command, cwd) if call.subcommand == self.COMMIT]
        if not commits:
            return None
        progress = self._progress(commits[-1].directory)
        if progress is None:
            return None
        problems = self._problems(progress.read_text(encoding="utf-8"))
        if not problems:
            self.logger.debug("The times of %s are current.", progress.parent.name)
            return None
        self.logger.info("The times of %s are behind.", progress.parent.name)
        return (
            f"Time tracking of {progress.parent.name} is behind after this commit: {'; '.join(problems)}. "
            f"Before going on, run `date '+%F %H:%M'` and update {progress} as the ticket-docs skill "
            "(section 'Time spent') says: the running step's Started and Elapsed so far, its **Time** line "
            "(sub-step just finished, waits excluded), and the **Total time** line."
        )

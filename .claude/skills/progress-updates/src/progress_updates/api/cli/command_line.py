from __future__ import annotations

# Standard library imports
import argparse
from datetime import datetime
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from progress_updates.models.enums import ProgressCommand, TaskSource


class CommandLine:
    """The ``progress-updates`` command line.

    Attributes:
        DEFAULT_SOURCES (str): The sources read when none is named.
        CLOCK_FORMAT (str): A start time typed as ``HH:MM``, today.
        parser (argparse.ArgumentParser): The parser of every command.
    """

    DEFAULT_SOURCES: ClassVar[str] = "background,process,evidence,actions"
    CLOCK_FORMAT: ClassVar[str] = "%H:%M"

    def __init__(self) -> None:
        """Describe the commands."""
        self.parser = argparse.ArgumentParser(
            prog="progress-updates",
            description="Report long-running work every 2 minutes, colourised, exhaustive, with icons.",
        )
        commands = self.parser.add_subparsers(dest="command", required=True)
        status = commands.add_parser(ProgressCommand.STATUS.value, help="print one progress update")
        watch = commands.add_parser(
            ProgressCommand.WATCH.value,
            help="print one line every 2 minutes while something runs, for the Monitor tool",
        )
        commands.add_parser(ProgressCommand.HOOK.value, help="the PostToolUse hook: remind Claude to report progress")
        for command in (status, watch):
            command.add_argument(
                "--sources",
                type=self._sources,
                default=self._sources(self.DEFAULT_SOURCES),
                help=f"comma-separated sources, by default {self.DEFAULT_SOURCES}",
            )
            command.add_argument("--tasks-dir", type=Path, help="the session's background task folder")
            command.add_argument("--evidence", type=Path, help="the active ticket's tests-evidences folder")
            command.add_argument("--since", type=self._moment, help="when the work started: HH:MM today, or ISO")
            command.add_argument(
                "--task",
                action="append",
                default=[],
                help='a task Claude declares, such as "research agent=running:12 pages [12/30]"',
            )
        watch.add_argument("--every", type=int, help="seconds between two events, at least 120")
        watch.add_argument("--max-ticks", type=int, help="stop after this many events")

    ############################
    # Internal Helpers Methods #
    ############################

    def _sources(self, text: str) -> List[TaskSource]:
        """Read a comma-separated list of sources.

        Args:
            text (str): The list, such as ``background,actions``.

        Returns:
            List[TaskSource]: The sources.

        Raises:
            argparse.ArgumentTypeError: When a name is not a source.
        """
        names = [name.strip() for name in text.split(",") if name.strip()]
        known = [source.value for source in TaskSource if source is not TaskSource.DECLARED]
        unknown = [name for name in names if name not in known]
        if unknown:
            raise argparse.ArgumentTypeError(f"unknown sources {unknown}: choose among {known}")
        return [TaskSource(name) for name in names]

    def _moment(self, text: str) -> datetime:
        """Read a start time.

        Args:
            text (str): ``HH:MM`` for today, or an ISO date and time.

        Returns:
            datetime: The time.

        Raises:
            argparse.ArgumentTypeError: When the text is neither.
        """
        try:
            clock = datetime.strptime(text, self.CLOCK_FORMAT)
        except ValueError:
            clock = None
        if clock is not None:
            return datetime.now().replace(hour=clock.hour, minute=clock.minute, second=0, microsecond=0)
        try:
            return datetime.fromisoformat(text)
        except ValueError as error:
            raise argparse.ArgumentTypeError(f"not a time: {text!r} (HH:MM or ISO)") from error

    ############################
    # Publicly Exposed Methods #
    ############################

    def parse(self, arguments: Optional[List[str]]) -> argparse.Namespace:
        """Read a command line.

        Args:
            arguments (Optional[List[str]]): The arguments, by default the process's.

        Returns:
            argparse.Namespace: The options.
        """
        return self.parser.parse_args(arguments)

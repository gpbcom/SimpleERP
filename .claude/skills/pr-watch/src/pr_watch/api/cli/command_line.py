from __future__ import annotations

# Standard library imports
import argparse
from typing import List, Optional

# First-party imports
from pr_watch.models.enums import PrWatchCommand
from pr_watch.service.inbox.inbox_service import InboxService


class CommandLine:
    """The ``pr-watch`` command line.

    Attributes:
        parser (argparse.ArgumentParser): The parser of every command.
    """

    def __init__(self) -> None:
        """Describe the commands."""
        self.parser = argparse.ArgumentParser(
            prog="pr-watch",
            description="Watch a ticket's open pull request and bring its problems to the ticket's own session.",
        )
        commands = self.parser.add_subparsers(dest="command", required=True)
        commands.add_parser(
            PrWatchCommand.ONCE.value, help="check every watched pull request once (the timer's command)"
        )
        commands.add_parser(PrWatchCommand.RENDER.value, help="write the summary pages again")
        commands.add_parser(
            PrWatchCommand.STATUS.value, help="print the watched pull requests and their waiting events"
        )
        self._session_commands(commands)
        self._inbox_commands(commands)
        commands.add_parser(PrWatchCommand.HOOK_INBOX.value, help="UserPromptSubmit hook: hand a session its events")
        install = commands.add_parser(PrWatchCommand.INSTALL_UNITS.value, help="copy the systemd units")
        install.add_argument("--target", help="the folder of the user units, by default ~/.config/systemd/user")

    ############################
    # Internal Helpers Methods #
    ############################

    def _session_commands(self, commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
        """Describe the commands that link a ticket's pull request to a session.

        Args:
            commands (argparse._SubParsersAction[argparse.ArgumentParser]): The sub-commands.
        """
        register = commands.add_parser(
            PrWatchCommand.REGISTER.value, help="watch a ticket's pull request for a session"
        )
        register.add_argument("key", help="the ticket, such as GH-12")
        register.add_argument(
            "--link", action="append", default=[], help="a pull request link, by default PROGRESS.md's"
        )
        register.add_argument("--session", help="the owner session, by default the one this command runs in")
        register.add_argument("--no-session", action="store_true", help="watch with notifications only")
        backfill = commands.add_parser(PrWatchCommand.BACKFILL.value, help="propose a session for unwatched tickets")
        backfill.add_argument("--apply", action="store_true", help="register the proposed sessions")

    def _inbox_commands(self, commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
        """Describe the commands a ticket's session sends about its events.

        Args:
            commands (argparse._SubParsersAction[argparse.ArgumentParser]): The sub-commands.
        """
        show = commands.add_parser(PrWatchCommand.SHOW.value, help="print the waiting events of a ticket")
        show.add_argument("key")
        ack = commands.add_parser(PrWatchCommand.ACK.value, help="mark a ticket's events as taken by its session")
        ack.add_argument("key")
        ack.add_argument("event_ids", nargs="*", help="the events, by default every waiting one")
        log = commands.add_parser(PrWatchCommand.LOG.value, help="log an operation done in the ticket's session")
        log.add_argument("key")
        log.add_argument("kind", choices=[kind.value for kind in InboxService.SESSION_OPERATIONS])
        log.add_argument("detail")
        log.add_argument("--link", help="the commit, run or comment it refers to")
        log.add_argument("--pr", help="<owner>/<name>#<number> when the ticket has several pull requests")

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

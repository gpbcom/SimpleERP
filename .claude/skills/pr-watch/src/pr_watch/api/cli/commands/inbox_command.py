from __future__ import annotations

# Standard library imports
from datetime import datetime

# First-party imports
from pr_watch.api.cli.command import Command
from pr_watch.models.enums import OperationKind, PrWatchCommand


class InboxCommand(Command):
    """``pr-watch show``, ``ack`` and ``log``: what a ticket's session does with its events.

    Notes:
        ``ack`` and ``log`` change the state under its lock, then write the summary pages again.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _show(self) -> None:
        """Print the waiting events of a ticket."""
        inbox = self.services.inbox()
        pending = inbox.pending(self.options.key)
        for event in pending:
            print(inbox.describe(event))
        if not pending:
            print(f"No event of {self.options.key} is waiting.")

    def _ack(self) -> None:
        """Mark a ticket's events as taken, and write the pages again."""
        with self.services.lock():
            taken = self.services.inbox().ack(self.options.key, self.options.event_ids, datetime.now().astimezone())
            self.services.renderer().refresh()
        print(f"{len(taken)} events taken.")

    def _log(self) -> None:
        """Log an operation of a ticket's session, and write the pages again."""
        with self.services.lock():
            operation = self.services.inbox().log(
                self.options.key,
                OperationKind(self.options.kind),
                self.options.detail,
                self.options.link,
                self.options.pr,
                datetime.now().astimezone(),
            )
            self.services.renderer().refresh()
        print(f"Logged {operation.kind.value} on {operation.pr_id}.")

    def _perform(self) -> None:
        """Run ``show``, ``ack`` or ``log``."""
        match PrWatchCommand(self.options.command):
            case PrWatchCommand.SHOW:
                self._show()
            case PrWatchCommand.ACK:
                self._ack()
            case _:
                self._log()

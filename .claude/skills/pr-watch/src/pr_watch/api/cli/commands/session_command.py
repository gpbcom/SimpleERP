from __future__ import annotations

# Standard library imports
import os
from datetime import datetime
from typing import ClassVar, Optional

# First-party imports
from pr_watch.api.cli.command import Command
from pr_watch.models.enums import PrWatchCommand
from pr_watch.models.watch.session_ref import SessionRef
from pr_watch.service.exceptions import SENotInSessionError


class SessionCommand(Command):
    """``pr-watch register`` and ``pr-watch backfill``: link a ticket's pull request to its session.

    Attributes:
        SESSION_VARIABLE (str): The variable Claude Code exports to every command it runs.

    Notes:
        - ``register`` without ``--session`` watches for the session it runs in, from ``CLAUDE_CODE_SESSION_ID``.
        - ``backfill`` only proposes: ``--apply`` registers the proposals, on the person's go.
    """

    SESSION_VARIABLE: ClassVar[str] = "CLAUDE_CODE_SESSION_ID"

    ############################
    # Internal Helpers Methods #
    ############################

    def _owner(self) -> Optional[SessionRef]:
        """Find the session a registration is for.

        Returns:
            Optional[SessionRef]: The session, ``None`` with ``--no-session``.

        Raises:
            SENotInSessionError: When no session is given and the command does not run in one.
        """
        if self.options.no_session:
            return None
        session_id = self.options.session or os.environ.get(self.SESSION_VARIABLE, "").strip()
        if not session_id:
            self.logger.error("pr-watch register ran outside a Claude Code session.")
            raise SENotInSessionError(
                "This command does not run in a Claude Code session. "  # noqa: E501
                "Give --session <id>, or --no-session for notifications only."
            )
        return self.services.registration().session_for(session_id)

    def _register(self) -> None:
        """Register a ticket's pull request and write the pages again."""
        owner = self._owner()
        with self.services.lock():
            watches = self.services.registration().register(
                self.options.key, self.options.link, owner, datetime.now().astimezone()
            )
            self.services.renderer().refresh()
        for watch in watches:
            who = f"session {owner.session_id}" if owner else "no session (notifications only)"
            print(f"Watching {watch.id} ({watch.pull_request.url}) for {who}.")

    def _backfill(self) -> None:
        """Propose a session for every unwatched ticket, and register the proposals with ``--apply``."""
        registration = self.services.registration()
        with self.services.lock():
            proposals = registration.proposals()
            for key, link, candidates in proposals:
                chosen = candidates[0] if candidates else None
                said = f"session {chosen.session_id} ({chosen.title})" if chosen else "no session found"
                print(f"{key} {link}: {said}")
                for other in candidates[1:]:
                    print(f"    other candidate: {other.session_id} ({other.title})")
                if self.options.apply:
                    owner = registration.session_for(chosen.session_id, chosen.cwd) if chosen else None
                    registration.register(key, [link], owner, datetime.now().astimezone())
            if self.options.apply:
                self.services.renderer().refresh()
        if not self.options.apply:
            print("Nothing registered: run again with --apply to register these proposals.")

    def _perform(self) -> None:
        """Run ``register`` or ``backfill``."""
        match PrWatchCommand(self.options.command):
            case PrWatchCommand.REGISTER:
                self._register()
            case _:
                self._backfill()

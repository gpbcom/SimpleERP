from __future__ import annotations

# Standard library imports
import json
import sys
from logging import Logger, getLogger
from typing import ClassVar, Optional

# Third-party imports
from pydantic import JsonValue

# First-party imports
from harness_core.lifecycle.runnable import Runnable
from pr_watch.service.inbox.inbox_service import InboxService


class HookCommand(Runnable):
    """``pr-watch hook-inbox``: the ``UserPromptSubmit`` hook that hands a session the events of its tickets.

    Attributes:
        EVENT_NAME (str): The hook event Claude Code names in the answer.
        inbox (InboxService): Reads the registry and the inboxes.
        exit_code (int): Always 0, read after ``execute``.
        logger (Logger): Logger instance.

    Notes:
        - **The standard output is read by Claude Code as the hook's answer**: the command prints the hook JSON or
          nothing, and logs go to the log file only.
        - **It never fails a prompt**: any error is logged and the command exits 0 with no output.
        - It runs before every prompt, so it is not a ``Command``: it imports the inbox service only, never the
          GitHub client nor the other services, and answers well under half a second.
    """

    EVENT_NAME: ClassVar[str] = "UserPromptSubmit"

    def __init__(self, inbox: InboxService, logger: Optional[Logger] = None) -> None:
        """Set the inbox service.

        Args:
            inbox (InboxService): Reads the registry and the inboxes.
            logger (Optional[Logger]): Logger instance.
        """
        self.inbox = inbox
        self.exit_code = 0
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _answer(self) -> None:
        """Read the session from the hook's input and print its waiting events, if any."""
        payload: JsonValue = json.load(sys.stdin)
        session_id = payload.get("session_id") if isinstance(payload, dict) else None
        if not isinstance(session_id, str) or not session_id:
            self.logger.debug("The hook input names no session.")
            return
        context = self.inbox.hook_context(session_id)
        if context is None:
            return
        answer = {"hookSpecificOutput": {"hookEventName": self.EVENT_NAME, "additionalContext": context}}
        print(json.dumps(answer))
        self.logger.info("Handed the waiting events to session %s.", session_id[:8])

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Acquire nothing: the inbox service reads the files when asked."""

    def run(self) -> None:
        """Answer the hook, and stay silent on any error."""
        try:
            self._answer()
        except Exception as error:  # noqa: BLE001
            self.logger.warning("The prompt hook failed: %s.", type(error).__name__)
        self.exit_code = 0

    def close(self) -> None:
        """Release nothing."""

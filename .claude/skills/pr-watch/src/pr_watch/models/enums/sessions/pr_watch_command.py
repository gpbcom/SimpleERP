from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class PrWatchCommand(StrEnum):
    """The commands of the ``pr-watch`` command line.

    Attributes:
        ONCE: Check every watched pull request once.
        RENDER: Write the summary pages again.
        STATUS: Print the watched pull requests.
        REGISTER: Watch a ticket's pull request for a session.
        BACKFILL: Propose a session for every ticket whose pull request nobody watches.
        SHOW: Print the waiting events of a ticket.
        ACK: Mark a ticket's events as taken.
        LOG: Log an operation done in the ticket's session.
        HOOK_INBOX: Answer the ``UserPromptSubmit`` hook.
        INSTALL_UNITS: Copy the systemd units to the user's folder.
    """

    ONCE = "once"
    RENDER = "render"
    STATUS = "status"
    REGISTER = "register"
    BACKFILL = "backfill"
    SHOW = "show"
    ACK = "ack"
    LOG = "log"
    HOOK_INBOX = "hook-inbox"
    INSTALL_UNITS = "install-units"

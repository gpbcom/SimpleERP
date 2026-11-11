from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import PullRequestStatus
from pr_watch.models.validation.field_rules import FieldRules
from pr_watch.models.watch.exceptions import (
    SETicketWatchInvalidHistory,
    SETicketWatchInvalidKey,
    SETicketWatchInvalidPullRequest,
    SETicketWatchInvalidSession,
)
from pr_watch.models.watch.pull_request_ref import PullRequestRef
from pr_watch.models.watch.session_ref import SessionRef
from pr_watch.models.watch.watch_history import WatchHistory


class TicketWatch(BaseModel):
    """A watched pull request and the Claude Code session of its ticket.

    Attributes:
        key (str): The ticket.
        pull_request (PullRequestRef): The pull request.
        session (Optional[SessionRef]): The ticket's session, ``None`` for a watch that only notifies.
        history (WatchHistory): Where the pull request stands.

    Notes:
        A watch without a session only notifies: nobody's session is reopened for it.
    """

    model_config = ConfigDict(extra="forbid")

    key: str = Field(description="The ticket.", examples=["GH-12"])
    pull_request: PullRequestRef = Field(
        description="The pull request.",
        examples=[{"repository": "gpbcom/simple-erp", "number": 7, "root": "/home/me/simple-erp"}],
    )
    session: Optional[SessionRef] = Field(
        default=None,
        description="The ticket's session, ``None`` for a watch that only notifies.",
        examples=[{"session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314", "cwd": "/home/me/simple-erp"}],
    )
    history: WatchHistory = Field(
        description="Where the pull request stands.",
        examples=[{"status": "open", "registered_on": "2026-11-10T09:00:00+01:00"}],
    )

    @field_validator("key", mode="before")
    def validate_key(cls, value: JsonValue) -> JsonValue:
        """Validate ``key``.

        Args:
            value (JsonValue): The raw key.

        Returns:
            JsonValue: The key.

        Raises:
            SETicketWatchInvalidKey: When the value is not a ``GH-<n>`` key.
        """
        return FieldRules.ticket(value, SETicketWatchInvalidKey, "key")

    @field_validator("pull_request", mode="before")
    def validate_pull_request(cls, value: JsonValue) -> JsonValue:
        """Validate ``pull_request``.

        Args:
            value (JsonValue): The raw pull request.

        Returns:
            JsonValue: The pull request.

        Raises:
            SETicketWatchInvalidPullRequest: When the value is not a model or a mapping of its fields.
        """
        return FieldRules.nested(value, SETicketWatchInvalidPullRequest, "pull_request")

    @field_validator("session", mode="before")
    def validate_session(cls, value: JsonValue) -> JsonValue:
        """Validate ``session``.

        Args:
            value (JsonValue): The raw session, or ``None``.

        Returns:
            JsonValue: The session, or ``None``.

        Raises:
            SETicketWatchInvalidSession: When the value is not a model or a mapping of its fields.
        """
        if value is None:
            return None
        return FieldRules.nested(value, SETicketWatchInvalidSession, "session")

    @field_validator("history", mode="before")
    def validate_history(cls, value: JsonValue) -> JsonValue:
        """Validate ``history``.

        Args:
            value (JsonValue): The raw history.

        Returns:
            JsonValue: The history.

        Raises:
            SETicketWatchInvalidHistory: When the value is not a model or a mapping of its fields.
        """
        return FieldRules.nested(value, SETicketWatchInvalidHistory, "history")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def id(self) -> str:
        """The watch's identifier, ``<key>:<repository>#<number>``."""
        return f"{self.key}:{self.pull_request.label}"

    @property
    def is_open(self) -> bool:
        """Whether the pull request is still open."""
        return self.history.status == PullRequestStatus.OPEN

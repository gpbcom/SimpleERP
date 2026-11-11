from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.sessions.exceptions import (
    SESessionCandidateInvalidCwd,
    SESessionCandidateInvalidMentionsPr,
    SESessionCandidateInvalidModifiedOn,
    SESessionCandidateInvalidSessionId,
    SESessionCandidateInvalidTitle,
)
from pr_watch.models.validation.field_rules import FieldRules


class SessionCandidate(BaseModel):
    """A Claude Code session whose title names a ticket, a candidate to own its pull request.

    Attributes:
        session_id (str): The session.
        title (str): Its title.
        cwd (Optional[str]): The folder it ran in.
        modified_on (datetime): The last write to its transcript.
        mentions_pr (bool): Whether its transcript holds the pull request's link.
    """

    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(description="The session.", examples=["7a30c2c8-75fe-4e6a-8475-dc3d38910314"])
    title: str = Field(description="Its title.", examples=["GH-12 add customers"])
    cwd: Optional[str] = Field(default=None, description="The folder it ran in.", examples=["/home/me/simple-erp"])
    modified_on: datetime = Field(
        description="The last write to its transcript.", examples=["2026-11-10T08:00:00+01:00"]
    )
    mentions_pr: bool = Field(
        default=False, description="Whether its transcript holds the pull request's link.", examples=[True]
    )

    @field_validator("session_id", mode="before")
    def validate_session_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``session_id``.

        Args:
            value (JsonValue): The raw session id.

        Returns:
            JsonValue: The session id.

        Raises:
            SESessionCandidateInvalidSessionId: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SESessionCandidateInvalidSessionId, "session_id")

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw title.

        Returns:
            JsonValue: The title.

        Raises:
            SESessionCandidateInvalidTitle: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SESessionCandidateInvalidTitle, "title")

    @field_validator("cwd", mode="before")
    def validate_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cwd``.

        Args:
            value (JsonValue): The raw cwd, or ``None``.

        Returns:
            JsonValue: The cwd, or ``None``.

        Raises:
            SESessionCandidateInvalidCwd: When the value is not a path.
        """
        if value is None:
            return None
        return FieldRules.path(value, SESessionCandidateInvalidCwd, "cwd")

    @field_validator("modified_on", mode="before")
    def validate_modified_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``modified_on``.

        Args:
            value (JsonValue): The raw modified on.

        Returns:
            JsonValue: The modified on.

        Raises:
            SESessionCandidateInvalidModifiedOn: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SESessionCandidateInvalidModifiedOn, "modified_on")

    @field_validator("mentions_pr", mode="before")
    def validate_mentions_pr(cls, value: JsonValue) -> JsonValue:
        """Validate ``mentions_pr``.

        Args:
            value (JsonValue): The raw mentions pr, or ``None``.

        Returns:
            JsonValue: The mentions pr, or its default.

        Raises:
            SESessionCandidateInvalidMentionsPr: When the value is not a boolean.
        """
        if value is None:
            return cls.model_fields["mentions_pr"].get_default(call_default_factory=True)
        return FieldRules.flag(value, SESessionCandidateInvalidMentionsPr, "mentions_pr")

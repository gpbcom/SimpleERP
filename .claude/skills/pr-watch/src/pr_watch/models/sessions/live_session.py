from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import SessionEntrypoint
from pr_watch.models.sessions.exceptions import (
    SELiveSessionInvalidCwd,
    SELiveSessionInvalidEntrypoint,
    SELiveSessionInvalidPid,
    SELiveSessionInvalidSessionId,
    SELiveSessionInvalidStatus,
)
from pr_watch.models.validation.field_rules import FieldRules


class LiveSession(BaseModel):
    """A Claude Code session running now.

    Attributes:
        session_id (str): The session.
        pid (int): Its process.
        cwd (Optional[str]): The folder it runs in.
        entrypoint (Optional[str]): Where it runs, ``claude-vscode`` for the VS Code extension.
        status (Optional[str]): ``idle`` or ``busy``.
    """

    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(description="The session.", examples=["7a30c2c8-75fe-4e6a-8475-dc3d38910314"])
    pid: int = Field(description="Its process.", examples=[22839])
    cwd: Optional[str] = Field(default=None, description="The folder it runs in.", examples=["/home/me/simple-erp"])
    entrypoint: Optional[str] = Field(
        default=None,
        description="Where it runs, ``claude-vscode`` for the VS Code extension.",
        examples=["claude-vscode"],
    )
    status: Optional[str] = Field(default=None, description="``idle`` or ``busy``.", examples=["idle"])

    @field_validator("session_id", mode="before")
    def validate_session_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``session_id``.

        Args:
            value (JsonValue): The raw session id.

        Returns:
            JsonValue: The session id.

        Raises:
            SELiveSessionInvalidSessionId: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SELiveSessionInvalidSessionId, "session_id")

    @field_validator("pid", mode="before")
    def validate_pid(cls, value: JsonValue) -> JsonValue:
        """Validate ``pid``.

        Args:
            value (JsonValue): The raw pid.

        Returns:
            JsonValue: The pid.

        Raises:
            SELiveSessionInvalidPid: When the value is not an integer of zero or more.
        """
        return FieldRules.integer(value, SELiveSessionInvalidPid, "pid")

    @field_validator("cwd", mode="before")
    def validate_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cwd``.

        Args:
            value (JsonValue): The raw cwd, or ``None``.

        Returns:
            JsonValue: The cwd, or ``None``.

        Raises:
            SELiveSessionInvalidCwd: When the value is not a path.
        """
        if value is None:
            return None
        return FieldRules.path(value, SELiveSessionInvalidCwd, "cwd")

    @field_validator("entrypoint", mode="before")
    def validate_entrypoint(cls, value: JsonValue) -> JsonValue:
        """Validate ``entrypoint``.

        Args:
            value (JsonValue): The raw entrypoint, or ``None``.

        Returns:
            JsonValue: The entrypoint, or ``None``.

        Raises:
            SELiveSessionInvalidEntrypoint: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SELiveSessionInvalidEntrypoint, "entrypoint")

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw status, or ``None``.

        Returns:
            JsonValue: The status, or ``None``.

        Raises:
            SELiveSessionInvalidStatus: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SELiveSessionInvalidStatus, "status")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def in_vscode(self) -> bool:
        """Whether the session runs in the VS Code extension."""
        return self.entrypoint == SessionEntrypoint.VSCODE

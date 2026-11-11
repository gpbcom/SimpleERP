from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.validation.field_rules import FieldRules
from pr_watch.models.watch.exceptions import (
    SESessionRefInvalidCwd,
    SESessionRefInvalidSessionId,
)


class SessionRef(BaseModel):
    """The Claude Code session that owns a ticket's pull request.

    Attributes:
        session_id (str): The session.
        cwd (Optional[str]): The folder the session runs in, the one VS Code must have open.
    """

    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(description="The session.", examples=["7a30c2c8-75fe-4e6a-8475-dc3d38910314"])
    cwd: Optional[str] = Field(
        default=None,
        description="The folder the session runs in, the one VS Code must have open.",
        examples=["/home/me/simple-erp"],
    )

    @field_validator("session_id", mode="before")
    def validate_session_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``session_id``.

        Args:
            value (JsonValue): The raw session id.

        Returns:
            JsonValue: The session id.

        Raises:
            SESessionRefInvalidSessionId: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SESessionRefInvalidSessionId, "session_id")

    @field_validator("cwd", mode="before")
    def validate_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cwd``.

        Args:
            value (JsonValue): The raw cwd, or ``None``.

        Returns:
            JsonValue: The cwd, or ``None``.

        Raises:
            SESessionRefInvalidCwd: When the value is not a path.
        """
        if value is None:
            return None
        return FieldRules.path(value, SESessionRefInvalidCwd, "cwd")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def short(self) -> str:
        """The first eight characters of the session, as the summary page shows it."""
        return self.session_id[:8]

from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import DispatchAction
from pr_watch.models.sessions.exceptions import (
    SEDispatchOutcomeInvalidAction,
    SEDispatchOutcomeInvalidDetail,
    SEDispatchOutcomeInvalidOk,
)
from pr_watch.models.validation.field_rules import FieldRules


class DispatchOutcome(BaseModel):
    """How the events of a ticket were brought to its session.

    Attributes:
        action (DispatchAction): What was done.
        ok (bool): Whether every command it needed succeeded.
        detail (str): One line saying it, or why it failed.
    """

    model_config = ConfigDict(extra="forbid")

    action: DispatchAction = Field(description="What was done.", examples=["reopened_vscode"])
    ok: bool = Field(description="Whether every command it needed succeeded.", examples=[True])
    detail: str = Field(
        description="One line saying it, or why it failed.", examples=["session 7a30c2c8 opened in VS Code"]
    )

    @field_validator("action", mode="before")
    def validate_action(cls, value: JsonValue) -> JsonValue:
        """Validate ``action``.

        Args:
            value (JsonValue): The raw action.

        Returns:
            JsonValue: The action.

        Raises:
            SEDispatchOutcomeInvalidAction: When the value is not a ``DispatchAction``.
        """
        return FieldRules.member(value, SEDispatchOutcomeInvalidAction, "action", DispatchAction)

    @field_validator("ok", mode="before")
    def validate_ok(cls, value: JsonValue) -> JsonValue:
        """Validate ``ok``.

        Args:
            value (JsonValue): The raw ok.

        Returns:
            JsonValue: The ok.

        Raises:
            SEDispatchOutcomeInvalidOk: When the value is not a boolean.
        """
        return FieldRules.flag(value, SEDispatchOutcomeInvalidOk, "ok")

    @field_validator("detail", mode="before")
    def validate_detail(cls, value: JsonValue) -> JsonValue:
        """Validate ``detail``.

        Args:
            value (JsonValue): The raw detail.

        Returns:
            JsonValue: The detail.

        Raises:
            SEDispatchOutcomeInvalidDetail: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEDispatchOutcomeInvalidDetail, "detail")

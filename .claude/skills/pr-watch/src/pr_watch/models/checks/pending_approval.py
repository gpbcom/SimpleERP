from __future__ import annotations

# Standard library imports
from datetime import datetime

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.exceptions import (
    SEPendingApprovalInvalidEnvironment,
    SEPendingApprovalInvalidRunId,
    SEPendingApprovalInvalidWaitingSince,
)
from pr_watch.models.validation.field_rules import FieldRules


class PendingApproval(BaseModel):
    """A deployment that waits for its reviewer's approval.

    Attributes:
        run_id (int): The workflow run that waits.
        environment (str): The environment it waits for.
        waiting_since (datetime): When the wait started.
    """

    model_config = ConfigDict(extra="forbid")

    run_id: int = Field(description="The workflow run that waits.", examples=[601])
    environment: str = Field(description="The environment it waits for.", examples=["qa"])
    waiting_since: datetime = Field(description="When the wait started.", examples=["2026-11-10T09:00:00+01:00"])

    @field_validator("run_id", mode="before")
    def validate_run_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``run_id``.

        Args:
            value (JsonValue): The raw run id.

        Returns:
            JsonValue: The run id.

        Raises:
            SEPendingApprovalInvalidRunId: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEPendingApprovalInvalidRunId, "run_id")

    @field_validator("environment", mode="before")
    def validate_environment(cls, value: JsonValue) -> JsonValue:
        """Validate ``environment``.

        Args:
            value (JsonValue): The raw environment.

        Returns:
            JsonValue: The environment.

        Raises:
            SEPendingApprovalInvalidEnvironment: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPendingApprovalInvalidEnvironment, "environment")

    @field_validator("waiting_since", mode="before")
    def validate_waiting_since(cls, value: JsonValue) -> JsonValue:
        """Validate ``waiting_since``.

        Args:
            value (JsonValue): The raw waiting since.

        Returns:
            JsonValue: The waiting since.

        Raises:
            SEPendingApprovalInvalidWaitingSince: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEPendingApprovalInvalidWaitingSince, "waiting_since")

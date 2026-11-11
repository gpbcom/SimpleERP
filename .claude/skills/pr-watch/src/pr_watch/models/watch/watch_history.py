from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import PullRequestStatus
from pr_watch.models.validation.field_rules import FieldRules
from pr_watch.models.watch.exceptions import (
    SEWatchHistoryInvalidClosedOn,
    SEWatchHistoryInvalidOpenedOn,
    SEWatchHistoryInvalidRegisteredOn,
    SEWatchHistoryInvalidStatus,
)


class WatchHistory(BaseModel):
    """Where a watched pull request stands, and since when.

    Attributes:
        status (PullRequestStatus): Open, merged or closed without merge.
        registered_on (datetime): When the watch started.
        opened_on (Optional[datetime]): When the pull request was opened.
        closed_on (Optional[datetime]): When it was merged or closed.
    """

    model_config = ConfigDict(extra="forbid")

    status: PullRequestStatus = Field(
        default=PullRequestStatus.OPEN, description="Open, merged or closed without merge.", examples=["merged"]
    )
    registered_on: datetime = Field(description="When the watch started.", examples=["2026-11-10T09:00:00+01:00"])
    opened_on: Optional[datetime] = Field(
        default=None, description="When the pull request was opened.", examples=["2026-11-09T17:00:00+01:00"]
    )
    closed_on: Optional[datetime] = Field(
        default=None, description="When it was merged or closed.", examples=["2026-11-11T10:00:00+01:00"]
    )

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw status, or ``None``.

        Returns:
            JsonValue: The status, or its default.

        Raises:
            SEWatchHistoryInvalidStatus: When the value is not a ``PullRequestStatus``.
        """
        if value is None:
            return cls.model_fields["status"].get_default(call_default_factory=True)
        return FieldRules.member(value, SEWatchHistoryInvalidStatus, "status", PullRequestStatus)

    @field_validator("registered_on", mode="before")
    def validate_registered_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``registered_on``.

        Args:
            value (JsonValue): The raw registered on.

        Returns:
            JsonValue: The registered on.

        Raises:
            SEWatchHistoryInvalidRegisteredOn: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEWatchHistoryInvalidRegisteredOn, "registered_on")

    @field_validator("opened_on", mode="before")
    def validate_opened_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``opened_on``.

        Args:
            value (JsonValue): The raw opened on, or ``None``.

        Returns:
            JsonValue: The opened on, or ``None``.

        Raises:
            SEWatchHistoryInvalidOpenedOn: When the value is not a time with its time zone.
        """
        if value is None:
            return None
        return FieldRules.moment(value, SEWatchHistoryInvalidOpenedOn, "opened_on")

    @field_validator("closed_on", mode="before")
    def validate_closed_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``closed_on``.

        Args:
            value (JsonValue): The raw closed on, or ``None``.

        Returns:
            JsonValue: The closed on, or ``None``.

        Raises:
            SEWatchHistoryInvalidClosedOn: When the value is not a time with its time zone.
        """
        if value is None:
            return None
        return FieldRules.moment(value, SEWatchHistoryInvalidClosedOn, "closed_on")

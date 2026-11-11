from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import EventKind
from pr_watch.models.events.event_detail import EventDetail
from pr_watch.models.events.exceptions import (
    SEPrEventInvalidAckedOn,
    SEPrEventInvalidDetail,
    SEPrEventInvalidDetectedOn,
    SEPrEventInvalidId,
    SEPrEventInvalidKind,
)
from pr_watch.models.validation.field_rules import FieldRules


class PrEvent(BaseModel):
    """Something a pull request needs from its ticket's Claude Code session.

    Attributes:
        id (str): The event's identifier.
        kind (EventKind): What the pull request needs.
        detail (EventDetail): What the event says.
        detected_on (datetime): When the watcher saw it.
        acked_on (Optional[datetime]): When the session took it, ``None`` while it waits.

    Notes:
        The identifier is ``<watch id>|<what makes it unique>``, the same on every run that sees it again, so that an
        event enters the inbox once.
    """

    model_config = ConfigDict(extra="forbid")

    id: str = Field(description="The event's identifier.", examples=["GH-12:gpbcom/simple-erp#7|checks:668501e0d3a1"])
    kind: EventKind = Field(description="What the pull request needs.", examples=["checks_failed"])
    detail: EventDetail = Field(description="What the event says.", examples=[{"title": "2 checks failed on 668501e0"}])
    detected_on: datetime = Field(description="When the watcher saw it.", examples=["2026-11-10T09:10:00+01:00"])
    acked_on: Optional[datetime] = Field(
        default=None,
        description="When the session took it, ``None`` while it waits.",
        examples=["2026-11-10T09:30:00+01:00"],
    )

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``id``.

        Args:
            value (JsonValue): The raw id.

        Returns:
            JsonValue: The id.

        Raises:
            SEPrEventInvalidId: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPrEventInvalidId, "id")

    @field_validator("kind", mode="before")
    def validate_kind(cls, value: JsonValue) -> JsonValue:
        """Validate ``kind``.

        Args:
            value (JsonValue): The raw kind.

        Returns:
            JsonValue: The kind.

        Raises:
            SEPrEventInvalidKind: When the value is not a ``EventKind``.
        """
        return FieldRules.member(value, SEPrEventInvalidKind, "kind", EventKind)

    @field_validator("detail", mode="before")
    def validate_detail(cls, value: JsonValue) -> JsonValue:
        """Validate ``detail``.

        Args:
            value (JsonValue): The raw detail.

        Returns:
            JsonValue: The detail.

        Raises:
            SEPrEventInvalidDetail: When the value is not a model or a mapping of its fields.
        """
        return FieldRules.nested(value, SEPrEventInvalidDetail, "detail")

    @field_validator("detected_on", mode="before")
    def validate_detected_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``detected_on``.

        Args:
            value (JsonValue): The raw detected on.

        Returns:
            JsonValue: The detected on.

        Raises:
            SEPrEventInvalidDetectedOn: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEPrEventInvalidDetectedOn, "detected_on")

    @field_validator("acked_on", mode="before")
    def validate_acked_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``acked_on``.

        Args:
            value (JsonValue): The raw acked on, or ``None``.

        Returns:
            JsonValue: The acked on, or ``None``.

        Raises:
            SEPrEventInvalidAckedOn: When the value is not a time with its time zone.
        """
        if value is None:
            return None
        return FieldRules.moment(value, SEPrEventInvalidAckedOn, "acked_on")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def pr_id(self) -> str:
        """The identifier of the watch the event belongs to."""
        return self.id.split("|", 1)[0]

    @property
    def key(self) -> str:
        """The ticket the event belongs to."""
        return self.pr_id.split(":", 1)[0]

    @property
    def is_pending(self) -> bool:
        """Whether the session has not taken the event yet."""
        return self.acked_on is None

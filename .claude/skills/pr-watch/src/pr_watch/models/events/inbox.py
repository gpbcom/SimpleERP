from __future__ import annotations

# Standard library imports
from typing import List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.events.exceptions import (
    SEInboxInvalidEvents,
)
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.validation.field_rules import FieldRules


class Inbox(BaseModel):
    """The events of a ticket, waiting for its session or taken by it.

    Attributes:
        events (List[PrEvent]): Each event, oldest first.
    """

    model_config = ConfigDict(extra="forbid")

    events: List[PrEvent] = Field(default_factory=list, description="Each event, oldest first.", examples=[[]])

    @field_validator("events", mode="before")
    def validate_events(cls, value: JsonValue) -> JsonValue:
        """Validate ``events``.

        Args:
            value (JsonValue): The raw events, or ``None``.

        Returns:
            JsonValue: The events, or its default.

        Raises:
            SEInboxInvalidEvents: When the value is not a list.
        """
        if value is None:
            return cls.model_fields["events"].get_default(call_default_factory=True)
        return FieldRules.sequence(value, SEInboxInvalidEvents, "events")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def pending(self) -> List[PrEvent]:
        """The events the session has not taken yet, oldest first."""
        return [event for event in self.events if event.is_pending]

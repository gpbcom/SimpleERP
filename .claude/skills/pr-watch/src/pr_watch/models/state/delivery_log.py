from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Dict

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.state.exceptions import (
    SEDeliveryLogInvalidDispatched,
    SEDeliveryLogInvalidNotified,
)
from pr_watch.models.validation.field_rules import FieldRules


class DeliveryLog(BaseModel):
    """When the events reached their sessions, and when each ticket was last notified.

    Attributes:
        dispatched (Dict[str, datetime]): When each event reached its session, by event identifier.
        notified (Dict[str, datetime]): The last notification of each ticket.
    """

    model_config = ConfigDict(extra="forbid")

    dispatched: Dict[str, datetime] = Field(
        default_factory=dict,
        description="When each event reached its session, by event identifier.",
        examples=[{"GH-12:gpbcom/simple-erp#7|checks:668501e0d3a1": "2026-11-10T09:10:00+01:00"}],
    )
    notified: Dict[str, datetime] = Field(
        default_factory=dict,
        description="The last notification of each ticket.",
        examples=[{"GH-12": "2026-11-10T09:10:00+01:00"}],
    )

    @field_validator("dispatched", mode="before")
    def validate_dispatched(cls, value: JsonValue) -> JsonValue:
        """Validate ``dispatched``.

        Args:
            value (JsonValue): The raw dispatched, or ``None``.

        Returns:
            JsonValue: The dispatched, or its default.

        Raises:
            SEDeliveryLogInvalidDispatched: When the value is not a mapping keyed by strings.
        """
        if value is None:
            return cls.model_fields["dispatched"].get_default(call_default_factory=True)
        return FieldRules.mapping(value, SEDeliveryLogInvalidDispatched, "dispatched")

    @field_validator("notified", mode="before")
    def validate_notified(cls, value: JsonValue) -> JsonValue:
        """Validate ``notified``.

        Args:
            value (JsonValue): The raw notified, or ``None``.

        Returns:
            JsonValue: The notified, or its default.

        Raises:
            SEDeliveryLogInvalidNotified: When the value is not a mapping keyed by strings.
        """
        if value is None:
            return cls.model_fields["notified"].get_default(call_default_factory=True)
        return FieldRules.mapping(value, SEDeliveryLogInvalidNotified, "notified")

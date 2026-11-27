from __future__ import annotations

# Standard library imports
from typing import Dict, cast
from uuid import uuid4

# Third-party imports
from pydantic import Field, JsonValue, ValidationError, field_validator

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.events.exceptions import (
    SEEventEnvelopeInvalidCompanyId,
    SEEventEnvelopeInvalidEventId,
    SEEventEnvelopeInvalidEventType,
    SEEventEnvelopeInvalidOccurredAt,
    SEEventEnvelopeInvalidPayload,
)
from erp_models.ids.company_id import CompanyId
from erp_models.ids.exceptions import SECompanyIdInvalidValue, SERecordIdInvalidValue
from erp_models.ids.record_id import RecordId
from erp_models.times.exceptions import SEUtcTimestampInvalidInstant
from erp_models.times.utc_timestamp import UtcTimestamp


class EventEnvelope(FrozenErpModel):
    """The public contract of an event, what a service publishes through its outbox when something happened.

    Attributes:
        event_id (RecordId): The identifier of the event, a new one by default.
        event_type (str): The type of the event, a non-empty text such as ``audit.entry.appended``.
        company_id (CompanyId): The company the event belongs to.
        occurred_at (UtcTimestamp): When it happened, now in UTC by default.
        payload (Dict[str, JsonValue]): What happened, a JSON object, empty by default.

    Notes:
        - The model is frozen: an event that happened is never changed.
        - The model holds no more than the specifications fix. Routing, versioning and delivery belong to the
          services and to the event bus.
        - The payload is opaque here: its schema belongs to the event type, defined by the service that publishes it.
    """

    event_id: RecordId = Field(
        default_factory=lambda: RecordId(value=uuid4().hex), description="The identifier of the event."
    )
    event_type: str = Field(description="The type of the event, a non-empty text.")
    company_id: CompanyId = Field(description="The company the event belongs to.")
    occurred_at: UtcTimestamp = Field(default_factory=UtcTimestamp.now, description="When it happened, in UTC.")
    payload: Dict[str, JsonValue] = Field(default_factory=dict, description="What happened, a JSON object.")

    @field_validator("event_id", mode="before")
    def validate_event_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``event_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The identifier, or the default when None.

        Raises:
            SEEventEnvelopeInvalidEventId: When it is not a record identifier.
        """
        if value is None:
            return cls.model_fields["event_id"].get_default(call_default_factory=True)
        if isinstance(value, RecordId):
            return cast(JsonValue, value)
        if isinstance(value, dict):
            try:
                return cast(JsonValue, RecordId.model_validate(value))
            except (SERecordIdInvalidValue, ValidationError) as error:
                raise SEEventEnvelopeInvalidEventId(
                    f"Invalid event_id: {value!r}. "  # noqa: E501
                    "Must hold a non-empty text."
                ) from error
        raise SEEventEnvelopeInvalidEventId(
            f"Invalid event_id: {value!r}. "  # noqa: E501
            "Must be a record identifier."
        )

    @field_validator("event_type", mode="before")
    def validate_event_type(cls, value: JsonValue) -> JsonValue:
        """Validate ``event_type``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEEventEnvelopeInvalidEventType: When it is not a non-empty text.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEEventEnvelopeInvalidEventType(
                f"Invalid event_type: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("company_id", mode="before")
    def validate_company_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``company_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The company identifier.

        Raises:
            SEEventEnvelopeInvalidCompanyId: When it is not a company identifier.
        """
        if isinstance(value, CompanyId):
            return cast(JsonValue, value)
        if isinstance(value, dict):
            try:
                return cast(JsonValue, CompanyId.model_validate(value))
            except (SECompanyIdInvalidValue, ValidationError) as error:
                raise SEEventEnvelopeInvalidCompanyId(
                    f"Invalid company_id: {value!r}. "  # noqa: E501
                    "Must hold a non-empty text."
                ) from error
        raise SEEventEnvelopeInvalidCompanyId(
            f"Invalid company_id: {value!r}. "  # noqa: E501
            "Must be a company identifier."
        )

    @field_validator("occurred_at", mode="before")
    def validate_occurred_at(cls, value: JsonValue) -> JsonValue:
        """Validate ``occurred_at``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The timestamp, or the default when None.

        Raises:
            SEEventEnvelopeInvalidOccurredAt: When it is not a UTC timestamp.
        """
        if value is None:
            return cls.model_fields["occurred_at"].get_default(call_default_factory=True)
        if isinstance(value, UtcTimestamp):
            return cast(JsonValue, value)
        if isinstance(value, dict):
            try:
                return cast(JsonValue, UtcTimestamp.model_validate(value))
            except (SEUtcTimestampInvalidInstant, ValidationError) as error:
                raise SEEventEnvelopeInvalidOccurredAt(
                    f"Invalid occurred_at: {value!r}. "  # noqa: E501
                    "Must hold a timezone-aware instant."
                ) from error
        raise SEEventEnvelopeInvalidOccurredAt(
            f"Invalid occurred_at: {value!r}. "  # noqa: E501
            "Must be a UTC timestamp."
        )

    @field_validator("payload", mode="before")
    def validate_payload(cls, value: JsonValue) -> JsonValue:
        """Validate ``payload``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The object, or the default when None.

        Raises:
            SEEventEnvelopeInvalidPayload: When it is not an object.
        """
        if value is None:
            return cls.model_fields["payload"].get_default(call_default_factory=True)
        if not isinstance(value, dict):
            raise SEEventEnvelopeInvalidPayload(
                f"Invalid payload: {value!r}. "  # noqa: E501
                "Must be a JSON object."
            )
        return value

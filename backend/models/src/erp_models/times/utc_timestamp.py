from __future__ import annotations

# Standard library imports
from datetime import UTC, datetime
from typing import cast

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.times.exceptions import SEUtcTimestampInvalidInstant


class UtcTimestamp(FrozenErpModel):
    """An instant in time, always held in UTC.

    Attributes:
        instant (datetime): The instant, timezone-aware and converted to UTC.

    Notes:
        - Naive times are refused: without a zone, a time is not an instant.
        - Numbers are refused: the unit of an epoch (seconds or milliseconds) is ambiguous.
        - A text is read as an ISO 8601 instant, and ``Z`` is accepted as UTC.
    """

    instant: datetime = Field(description="The instant, a timezone-aware time converted to UTC.")

    @field_validator("instant", mode="before")
    def validate_instant(cls, value: JsonValue) -> JsonValue:
        """Validate ``instant``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The instant, converted to UTC.

        Raises:
            SEUtcTimestampInvalidInstant: When it is not an aware time or an ISO 8601 text of one.
        """
        parsed: object = value
        if isinstance(parsed, str):
            stripped = parsed.strip()
            if not stripped:
                raise SEUtcTimestampInvalidInstant(
                    f"Invalid instant: {value!r}. "  # noqa: E501
                    "Must be a non-empty ISO 8601 text."
                )
            try:
                parsed = datetime.fromisoformat(stripped)
            except ValueError as error:
                raise SEUtcTimestampInvalidInstant(
                    f"Invalid instant: {value!r}. "  # noqa: E501
                    "Must be an ISO 8601 text."
                ) from error
        if not isinstance(parsed, datetime):
            raise SEUtcTimestampInvalidInstant(
                f"Invalid instant: {value!r}. "  # noqa: E501
                "Must be a datetime or an ISO 8601 text."
            )
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise SEUtcTimestampInvalidInstant(
                f"Invalid instant: {value!r}. "  # noqa: E501
                "Must carry a timezone."
            )
        return cast(JsonValue, parsed.astimezone(UTC))

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def now(cls) -> UtcTimestamp:
        """Build the current instant.

        Returns:
            UtcTimestamp: The current time, in UTC.
        """
        return cls(instant=datetime.now(UTC))

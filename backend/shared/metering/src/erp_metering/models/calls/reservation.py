from __future__ import annotations

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_metering.models.calls.exceptions import SEReservationInvalidReservationId


class Reservation(FrozenErpModel):
    """The reservation of a paid call's estimated cost, granted by the metering server.

    Attributes:
        reservation_id (str): The identifier to give back when the call is settled.
    """

    reservation_id: str = Field(description="The identifier of the reservation, a non-empty text.")

    @field_validator("reservation_id", mode="before")
    def validate_reservation_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``reservation_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEReservationInvalidReservationId: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEReservationInvalidReservationId(
                f"Invalid reservation_id: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

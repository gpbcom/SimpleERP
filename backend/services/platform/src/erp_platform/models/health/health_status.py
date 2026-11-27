from __future__ import annotations

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_platform.models.health.enums import HealthState
from erp_platform.models.health.exceptions import SEHealthStatusInvalidStatus


class HealthStatus(FrozenErpModel):
    """The body of the health answer.

    Attributes:
        status (HealthState): The state of the service.
    """

    status: HealthState = Field(default=HealthState.OK, description="The state of the service.")

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The state, as text.

        Raises:
            SEHealthStatusInvalidStatus: When it is not the exact value of a ``HealthState``.
        """
        if value is None:
            return cls.model_fields["status"].get_default(call_default_factory=True)
        if not isinstance(value, str) or value not in {state.value for state in HealthState}:
            raise SEHealthStatusInvalidStatus(
                f"Invalid status: {value!r}. "  # noqa: E501
                "Must be one of the values of HealthState."
            )
        return str(value)

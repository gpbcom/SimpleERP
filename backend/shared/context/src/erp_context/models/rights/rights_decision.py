from __future__ import annotations

# Standard library imports
from typing import Optional

from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator, model_validator

# First-party imports
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.rights.exceptions import (
    SERightsDecisionInconsistent,
    SERightsDecisionInvalidAllowed,
    SERightsDecisionInvalidReason,
)


class RightsDecision(FrozenErpModel):
    """The answer of ``allowed(user, action, record)``.

    Attributes:
        allowed (bool): Whether the action is permitted.
        reason (Optional[RefusalReason]): Why it was refused, and ``None`` when it is permitted.

    Notes:
        A permitted decision never carries a reason, and a refused one always does.
    """

    allowed: bool = Field(description="Whether the action is permitted.")
    reason: Optional[RefusalReason] = Field(default=None, description="Why the action was refused, if it was.")

    @field_validator("allowed", mode="before")
    def validate_allowed(cls, value: JsonValue) -> JsonValue:
        """Validate ``allowed``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The boolean, unchanged.

        Raises:
            SERightsDecisionInvalidAllowed: When it is not a boolean.
        """
        if not isinstance(value, bool):
            raise SERightsDecisionInvalidAllowed(
                f"Invalid allowed: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value

    @field_validator("reason", mode="before")
    def validate_reason(cls, value: JsonValue) -> JsonValue:
        """Validate ``reason``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The reason, or ``None``.

        Raises:
            SERightsDecisionInvalidReason: When it is not a known refusal reason.
        """
        if value is None or isinstance(value, RefusalReason):
            return value
        if isinstance(value, bool) or not isinstance(value, str) or value not in set(RefusalReason):
            raise SERightsDecisionInvalidReason(
                f"Invalid reason: {value!r}. "  # noqa: E501
                f"Must be one of {sorted(item.value for item in RefusalReason)}."
            )
        return value

    @model_validator(mode="after")
    def validate_consistency(self) -> RightsDecision:
        """Check that ``allowed`` and ``reason`` agree.

        Returns:
            RightsDecision: The decision itself.

        Raises:
            SERightsDecisionInconsistent: When it is allowed with a reason, or refused without one.
        """
        if self.allowed and self.reason is not None:
            raise SERightsDecisionInconsistent(
                f"Invalid decision: allowed with reason {self.reason.value!r}. "  # noqa: E501
                "A permitted decision has no reason."
            )
        if not self.allowed and self.reason is None:
            raise SERightsDecisionInconsistent(
                "Invalid decision: refused without a reason. "  # noqa: E501
                "A refused decision needs a reason."
            )
        return self

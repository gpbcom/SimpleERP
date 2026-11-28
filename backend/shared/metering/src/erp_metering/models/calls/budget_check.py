from __future__ import annotations

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_metering.models.calls.exceptions import SEBudgetCheckInvalidWithinBudget


class BudgetCheck(FrozenErpModel):
    """The answer of the metering server to a budget check.

    Attributes:
        within_budget (bool): Whether the paid call fits in every budget that applies to it.

    Notes:
        - **The default is ``False``**, so that a missing answer stops the call rather than lets it through.
    """

    within_budget: bool = Field(default=False, description="Whether the paid call fits in its budgets.")

    @field_validator("within_budget", mode="before")
    def validate_within_budget(cls, value: JsonValue) -> JsonValue:
        """Validate ``within_budget``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The boolean, or ``False`` when it is ``None``.

        Raises:
            SEBudgetCheckInvalidWithinBudget: When it is not a boolean.
        """
        if value is None:
            return False
        if not isinstance(value, bool):
            raise SEBudgetCheckInvalidWithinBudget(
                f"Invalid within_budget: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value

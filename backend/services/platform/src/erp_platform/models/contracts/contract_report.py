from __future__ import annotations

# Standard library imports
from typing import List

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_platform.models.contracts.contract_change import ContractChange
from erp_platform.models.contracts.exceptions import (
    SEContractReportInvalidBreakingChanges,
    SEContractReportInvalidStale,
)


class ContractReport(FrozenErpModel):
    """The result of the contract check (REQ-T05-05).

    Attributes:
        stale (bool): Whether the committed document differs from the live one.
        breaking_changes (List[ContractChange]): The breaking changes found.
    """

    stale: bool = Field(default=False, description="Whether the committed document differs from the live one.")
    breaking_changes: List[ContractChange] = Field(default_factory=list, description="The breaking changes found.")

    @field_validator("stale", mode="before")
    def validate_stale(cls, value: JsonValue) -> JsonValue:
        """Validate ``stale``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The flag, unchanged.

        Raises:
            SEContractReportInvalidStale: When it is not a boolean.
        """
        if value is None:
            return cls.model_fields["stale"].get_default(call_default_factory=True)
        if not isinstance(value, bool):
            raise SEContractReportInvalidStale(
                f"Invalid stale: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value

    @field_validator("breaking_changes", mode="before")
    def validate_breaking_changes(cls, value: JsonValue) -> JsonValue:
        """Validate ``breaking_changes``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The list, unchanged.

        Raises:
            SEContractReportInvalidBreakingChanges: When it is not a list.
        """
        if value is None:
            return cls.model_fields["breaking_changes"].get_default(call_default_factory=True)
        if not isinstance(value, list):
            raise SEContractReportInvalidBreakingChanges(
                f"Invalid breaking_changes: {value!r}. "  # noqa: E501
                "Must be a list of contract changes."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def passed(self) -> bool:
        """Tell whether the check passed.

        Returns:
            bool: ``True`` when the document is not stale and holds no breaking change.
        """
        return not self.stale and not self.breaking_changes

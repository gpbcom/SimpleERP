from __future__ import annotations

# Standard library imports
from collections.abc import Mapping
from typing import List

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from pydantic import Field, JsonValue, field_validator, model_validator

# First-party imports
from erp_country_rules.models.exceptions import (
    SECountryRuleInvalidRule,
    SECountryRuleInvalidVersions,
    SECountryRuleOverlappingVersions,
)
from erp_country_rules.models.rules.rule_version import RuleVersion


class CountryRule(FrozenErpModel):
    """One rule of a country pack and its versions over time.

    Attributes:
        rule (str): The name of the rule, such as ``standard-rate``.
        versions (List[RuleVersion]): The versions of the rule, by ascending ``valid_from``, none overlapping.

    Notes:
        - Exactly one value is in force at a date, because the versions never overlap (REQ-T11-02).
        - A future-dated version applies from its ``valid_from``.
        - **An open-ended version can only be the last one.** Adjacent versions and gaps are allowed.
    """

    rule: str = Field(description="The name of the rule.")
    versions: List[RuleVersion] = Field(description="The versions of the rule, by ascending start, none overlapping.")

    ##############
    # Validators #
    ##############

    @field_validator("rule", mode="before")
    def validate_rule(cls, value: JsonValue) -> JsonValue:
        """Validate ``rule``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The stripped name.

        Raises:
            SECountryRuleInvalidRule: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SECountryRuleInvalidRule(
                f"Invalid rule: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("versions", mode="before")
    def validate_versions(cls, value: JsonValue) -> JsonValue:
        """Validate ``versions``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The same list, for each version to be validated by its own model.

        Raises:
            SECountryRuleInvalidVersions: When it is not a non-empty list of versions.
        """
        if not isinstance(value, list) or not value:
            raise SECountryRuleInvalidVersions(
                f"Invalid versions: {value!r}. "  # noqa: E501
                "Must be a non-empty list of versions."
            )
        for item in value:
            if not isinstance(item, (Mapping, RuleVersion)):
                raise SECountryRuleInvalidVersions(
                    f"Invalid versions: {value!r}. "  # noqa: E501
                    "Each version must be a mapping."
                )
        return value

    @model_validator(mode="after")
    def validate_periods(self) -> CountryRule:
        """Check that the versions are in ascending order and never overlap.

        Returns:
            CountryRule: The same rule.

        Raises:
            SECountryRuleOverlappingVersions: When a version starts before the previous one ends.
        """
        for previous, current in zip(self.versions, self.versions[1:], strict=False):
            if previous.valid_to is None or previous.valid_to >= current.valid_from:
                raise SECountryRuleOverlappingVersions(
                    f"Invalid versions: {current.valid_from.isoformat()!r}. "  # noqa: E501
                    "Must start after the previous version ends, in ascending order."
                )
        return self

from __future__ import annotations

# Standard library imports
import re
from collections.abc import Mapping
from typing import ClassVar, List, Pattern, Type

# Third-party imports
from erp_models.catalogs.yaml_catalog import YamlCatalog
from pydantic import ConfigDict, Field, JsonValue, field_validator, model_validator

# First-party imports
from erp_country_rules.models.exceptions import (
    SECountryPackInvalidCountry,
    SECountryPackInvalidRules,
    SECountryPackInvalidVersion,
    SECountryPackUnreadable,
)
from erp_country_rules.models.rules.country_rule import CountryRule


class CountryPack(YamlCatalog):
    """The catalogue of one country: its rules and their values over time.

    Attributes:
        UNREADABLE (Type[Exception]): The exception ``load`` raises when the file cannot be read.
        COUNTRY_PATTERN (Pattern[str]): The shape of a country code, two upper-case ASCII letters.
        model_config (ConfigDict): Refuses unknown keys and assignment, and validates the defaults.
        country (str): The country code, such as ``FR``.
        version (str): The version of the pack, such as ``2026.11``.
        rules (List[CountryRule]): The rules of the country, each name appearing once.

    Notes:
        - The signature of a pack is out of scope here (REQ-T11-01).
        - **A YAML number is refused as a version**, because ``2026.10`` would be read as ``2026.1``.
    """

    UNREADABLE: ClassVar[Type[Exception]] = SECountryPackUnreadable
    COUNTRY_PATTERN: ClassVar[Pattern[str]] = re.compile(r"[A-Z]{2}")

    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    country: str = Field(description="The country code, two upper-case letters.")
    version: str = Field(description="The version of the pack.")
    rules: List[CountryRule] = Field(description="The rules of the country, each name appearing once.")

    ##############
    # Validators #
    ##############

    @field_validator("country", mode="before")
    def validate_country(cls, value: JsonValue) -> JsonValue:
        """Validate ``country``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The stripped country code.

        Raises:
            SECountryPackInvalidCountry: When it is not two upper-case ASCII letters.
        """
        if not isinstance(value, str) or not cls.COUNTRY_PATTERN.fullmatch(value.strip()):
            raise SECountryPackInvalidCountry(
                f"Invalid country: {value!r}. "  # noqa: E501
                "Must be two upper-case ASCII letters."
            )
        return value.strip()

    @field_validator("version", mode="before")
    def validate_version(cls, value: JsonValue) -> JsonValue:
        """Validate ``version``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The stripped version.

        Raises:
            SECountryPackInvalidVersion: When it is not a non-empty text.
        """
        if not isinstance(value, str) or not value.strip():
            raise SECountryPackInvalidVersion(
                f"Invalid version: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("rules", mode="before")
    def validate_rules(cls, value: JsonValue) -> JsonValue:
        """Validate ``rules``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The same list, for each rule to be validated by its own model.

        Raises:
            SECountryPackInvalidRules: When it is not a non-empty list of rules.
        """
        if not isinstance(value, list) or not value:
            raise SECountryPackInvalidRules(
                f"Invalid rules: {value!r}. "  # noqa: E501
                "Must be a non-empty list of rules."
            )
        for item in value:
            if not isinstance(item, (Mapping, CountryRule)):
                raise SECountryPackInvalidRules(
                    f"Invalid rules: {value!r}. "  # noqa: E501
                    "Each rule must be a mapping."
                )
        return value

    @model_validator(mode="after")
    def validate_unique_rules(self) -> CountryPack:
        """Check that no two rules share a name.

        Returns:
            CountryPack: The same pack.

        Raises:
            SECountryPackInvalidRules: When a rule name appears twice.
        """
        names = [rule.rule for rule in self.rules]
        duplicates = sorted({name for name in names if names.count(name) > 1})
        if duplicates:
            raise SECountryPackInvalidRules(
                f"Invalid rules: {duplicates!r}. "  # noqa: E501
                "Each rule name must appear once."
            )
        return self

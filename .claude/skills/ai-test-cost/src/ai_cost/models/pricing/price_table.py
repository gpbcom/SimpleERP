from __future__ import annotations

# Standard library imports
from datetime import date
from typing import ClassVar, List

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from ai_cost.models.pricing.exceptions import (
    SEPriceTableInvalidPrices,
    SEPriceTableInvalidReadOn,
    SEPriceTableInvalidSource,
    SEPriceTableUnreadable,
)
from ai_cost.models.pricing.model_price import ModelPrice
from harness_core.models.catalogs.yaml_catalog import YamlCatalog


class PriceTable(YamlCatalog):
    """The prices of the Claude models, read from ``conf/prices.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the price file cannot be read.
        source (str): Where the prices come from.
        read_on (date): When they were read.
        prices (List[ModelPrice]): The price of each model, the first match wins.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEPriceTableUnreadable

    source: str = Field(
        description="Where the prices come from.",
        examples=["Anthropic pricing page, https://platform.claude.com/docs/en/about-claude/pricing"],
    )
    read_on: date = Field(description="When they were read.", examples=["2026-11-10"])
    prices: List[ModelPrice] = Field(description="The price of each model, the first match wins.", examples=[[]])

    @field_validator("source", mode="before")
    def validate_source(cls, value: JsonValue) -> JsonValue:
        """Validate ``source``.

        Args:
            value (JsonValue): The raw source.

        Returns:
            JsonValue: The source, stripped.

        Raises:
            SEPriceTableInvalidSource: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPriceTableInvalidSource(
                f"Invalid source: {value!r}. "  # noqa: E501
                "Must name where the prices come from."
            )
        return value.strip()

    @field_validator("read_on", mode="before")
    def validate_read_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``read_on``.

        Args:
            value (JsonValue): The raw date: a ``date`` read by YAML or an ISO 8601 string.

        Returns:
            JsonValue: The date in ISO 8601.

        Raises:
            SEPriceTableInvalidReadOn: When the value is not a date.
        """
        text = value.isoformat() if isinstance(value, date) else value
        if not isinstance(text, str):
            raise SEPriceTableInvalidReadOn(
                f"Invalid read_on: {value!r}. "  # noqa: E501
                "Must be a date such as 2026-11-10."
            )
        try:
            return date.fromisoformat(text).isoformat()
        except ValueError as error:
            raise SEPriceTableInvalidReadOn(
                f"Invalid read_on: {value!r}. "  # noqa: E501
                "Must be a date such as 2026-11-10."
            ) from error

    @field_validator("prices", mode="before")
    def validate_prices(cls, value: JsonValue) -> JsonValue:
        """Validate ``prices``.

        Args:
            value (JsonValue): The raw prices.

        Returns:
            JsonValue: The prices.

        Raises:
            SEPriceTableInvalidPrices: When the value is not a non-empty list.

        Notes:
            An empty table could not price an unknown model as the most expensive one, so it is refused.
        """
        if not isinstance(value, list) or not value:
            raise SEPriceTableInvalidPrices(
                f"Invalid prices: {value!r}. "  # noqa: E501
                "Must be a non-empty list of model prices."
            )
        return value

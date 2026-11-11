from __future__ import annotations

# Standard library imports
from decimal import Decimal, InvalidOperation

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, ValidationInfo, field_validator

# First-party imports
from ai_cost.models.pricing.exceptions import SEModelPriceInvalidPrice, SEModelPriceInvalidText


class ModelPrice(BaseModel):
    """What a million tokens of one model cost, in USD.

    Attributes:
        name (str): Name of the model.
        match (str): Text a model id contains for this price to apply.
        input_per_mtok (Decimal): Price of a million input tokens read without the cache.
        output_per_mtok (Decimal): Price of a million output tokens.
        cache_write_5m_per_mtok (Decimal): Price of a million tokens written to the 5-minute cache.
        cache_write_1h_per_mtok (Decimal): Price of a million tokens written to the 1-hour cache.
        cache_read_per_mtok (Decimal): Price of a million tokens read from the cache.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(description="Name of the model.", examples=["Claude Haiku 5.5"])
    match: str = Field(description="Text a model id contains for this price to apply.", examples=["claude-haiku-5-5"])
    input_per_mtok: Decimal = Field(
        description="Price of a million input tokens read without the cache.", examples=["0.10"]
    )
    output_per_mtok: Decimal = Field(description="Price of a million output tokens.", examples=["0.50"])
    cache_write_5m_per_mtok: Decimal = Field(
        default=Decimal("0"), description="Price of a million tokens written to the 5-minute cache.", examples=["0.125"]
    )
    cache_write_1h_per_mtok: Decimal = Field(
        default=Decimal("0"), description="Price of a million tokens written to the 1-hour cache.", examples=["0.20"]
    )
    cache_read_per_mtok: Decimal = Field(
        default=Decimal("0"), description="Price of a million tokens read from the cache.", examples=["0.01"]
    )

    @field_validator("name", "match", mode="before")
    def validate_text(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``name`` and ``match``.

        Args:
            value (JsonValue): The raw text.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEModelPriceInvalidText: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEModelPriceInvalidText(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator(
        "input_per_mtok",
        "output_per_mtok",
        "cache_write_5m_per_mtok",
        "cache_write_1h_per_mtok",
        "cache_read_per_mtok",
        mode="before",
    )
    def validate_price(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate the prices.

        Args:
            value (JsonValue): The raw price: a number or a decimal string.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The price as a decimal string, or the default for an optional price left out.

        Raises:
            SEModelPriceInvalidPrice: When a required price is missing, or a price is not zero or more.
        """
        field = info.field_name or ""
        if value is None and not cls.model_fields[field].is_required():
            return "0"
        if value is None or isinstance(value, bool):
            raise SEModelPriceInvalidPrice(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a price in USD."
            )
        try:
            price = Decimal(str(value))
        except InvalidOperation as error:
            raise SEModelPriceInvalidPrice(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a price in USD."
            ) from error
        if not price.is_finite() or price < 0:
            raise SEModelPriceInvalidPrice(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be zero or more."
            )
        return str(price)

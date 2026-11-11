from __future__ import annotations

# Standard library imports
from decimal import Decimal, InvalidOperation

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, ValidationInfo, field_serializer, field_validator

# First-party imports
from ai_cost.models.ledger.exceptions import SEModelUsageInvalidCostUsd, SEModelUsageInvalidTokens


class ModelUsage(BaseModel):
    """The tokens a run used on one model, and what they cost.

    Attributes:
        input_tokens (int): Input tokens read without the prompt cache.
        output_tokens (int): Output tokens.
        cache_read_tokens (int): Input tokens read from the prompt cache.
        cache_write_5m_tokens (int): Input tokens written to the 5-minute prompt cache.
        cache_write_1h_tokens (int): Input tokens written to the 1-hour prompt cache.
        cost_usd (Decimal): What these tokens cost, in USD.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    input_tokens: int = Field(default=0, description="Input tokens read without the prompt cache.", examples=[24456])
    output_tokens: int = Field(default=0, description="Output tokens.", examples=[11328])
    cache_read_tokens: int = Field(default=0, description="Input tokens read from the prompt cache.", examples=[0])
    cache_write_5m_tokens: int = Field(
        default=0, description="Input tokens written to the 5-minute prompt cache.", examples=[19942]
    )
    cache_write_1h_tokens: int = Field(
        default=0, description="Input tokens written to the 1-hour prompt cache.", examples=[0]
    )
    cost_usd: Decimal = Field(default=Decimal("0"), description="What these tokens cost, in USD.", examples=["0.0892"])

    @field_validator(
        "input_tokens",
        "output_tokens",
        "cache_read_tokens",
        "cache_write_5m_tokens",
        "cache_write_1h_tokens",
        mode="before",
    )
    def validate_tokens(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate the token counts.

        Args:
            value (JsonValue): The raw count.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The count, or the default for ``None``.

        Raises:
            SEModelUsageInvalidTokens: When the count is not a whole number of zero or more.
        """
        if value is None:
            return 0
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise SEModelUsageInvalidTokens(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                "Must be a whole number of zero or more."
            )
        return value

    @field_validator("cost_usd", mode="before")
    def validate_cost_usd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cost_usd``.

        Args:
            value (JsonValue): The raw cost: a number or a decimal string.

        Returns:
            JsonValue: The cost as a decimal string, or the default for ``None``.

        Raises:
            SEModelUsageInvalidCostUsd: When the cost is not an amount of zero or more.

        Notes:
            The amount goes through ``str`` so that a float read from JSON becomes the decimal it was written as.
        """
        if value is None:
            return "0"
        if isinstance(value, bool):
            raise SEModelUsageInvalidCostUsd(
                f"Invalid cost_usd: {value!r}. "  # noqa: E501
                "Must be an amount in USD."
            )
        try:
            amount = Decimal(str(value))
        except InvalidOperation as error:
            raise SEModelUsageInvalidCostUsd(
                f"Invalid cost_usd: {value!r}. "  # noqa: E501
                "Must be an amount in USD."
            ) from error
        if not amount.is_finite() or amount < 0:
            raise SEModelUsageInvalidCostUsd(
                f"Invalid cost_usd: {value!r}. "  # noqa: E501
                "Must be zero or more."
            )
        return str(amount)

    @field_serializer("cost_usd", when_used="json")
    def serialize_cost_usd(self, value: Decimal) -> float:
        """Write ``cost_usd`` as a JSON number.

        Args:
            value (Decimal): The cost.

        Returns:
            float: The same amount, a number for the tools that read the ledger.
        """
        return float(value)

from __future__ import annotations

# Standard library imports
from datetime import datetime
from decimal import Decimal, InvalidOperation
from enum import StrEnum
from typing import ClassVar, Dict, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, ValidationInfo, field_serializer, field_validator

# First-party imports
from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.ledger.exceptions import (
    SECostRunInvalidAmount,
    SECostRunInvalidChoice,
    SECostRunInvalidExitCode,
    SECostRunInvalidMoment,
    SECostRunInvalidSettled,
    SECostRunInvalidText,
    SECostRunInvalidUsage,
)
from ai_cost.models.ledger.model_usage import ModelUsage


class CostRun(BaseModel):
    """One paid AI test run of a ticket, or one cost charged to it by hand.

    Attributes:
        CHOICES (Dict[str, type[StrEnum]]): The enum each choice field takes its value from.
        id (str): Identifier of the run.
        label (str): What the run tests.
        command (str): The command run.
        started_on (datetime): When it started, or was refused.
        finished_on (Optional[datetime]): When it ended, ``None`` while it runs.
        estimate_usd (Decimal): What the run was expected to cost, in USD.
        cost_usd (Decimal): What it cost so far, in USD.
        status (RunStatus): Where the run stands.
        source (CostSource): Where its cost comes from.
        usage (Dict[str, ModelUsage]): The tokens and cost of each model.
        settled (bool): Whether the cost is final.
        exit_code (Optional[int]): Exit code of the command.
        note (Optional[str]): Why it was refused or stopped, or where a charged figure comes from.
    """

    CHOICES: ClassVar[Dict[str, type[StrEnum]]] = {"status": RunStatus, "source": CostSource}

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(description="Identifier of the run.", examples=["20261110-091502-3fa2c1"])
    label: str = Field(description="What the run tests.", examples=["invoice summary on Haiku"])
    command: str = Field(description="The command run.", examples=["uv run pytest tests -m llm"])
    started_on: datetime = Field(description="When it started, or was refused.", examples=["2026-11-10T09:15:02+01:00"])
    finished_on: Optional[datetime] = Field(
        default=None, description="When it ended, None while it runs.", examples=["2026-11-10T09:19:40+01:00"]
    )
    estimate_usd: Decimal = Field(description="What the run was expected to cost, in USD.", examples=["0.50"])
    cost_usd: Decimal = Field(default=Decimal("0"), description="What it cost so far, in USD.", examples=["0.0068"])
    status: RunStatus = Field(description="Where the run stands.", examples=["done"])
    source: CostSource = Field(description="Where its cost comes from.", examples=["usage_report"])
    usage: Dict[str, ModelUsage] = Field(
        default_factory=dict, description="The tokens and cost of each model.", examples=[{}]
    )
    settled: bool = Field(default=False, description="Whether the cost is final.", examples=[True])
    exit_code: Optional[int] = Field(default=None, description="Exit code of the command.", examples=[0])
    note: Optional[str] = Field(
        default=None,
        description="Why it was refused or stopped, or where a charged figure comes from.",
        examples=["estimate $5.00 above the $3.20 left"],
    )

    @field_validator("id", "label", "command", "note", mode="before")
    def validate_text(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``id``, ``label``, ``command`` and ``note``.

        Args:
            value (JsonValue): The raw text.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The text, stripped, or ``None`` for an optional field left out.

        Raises:
            SECostRunInvalidText: When the text is missing where it is required, or is not a non-empty string.
        """
        field = info.field_name or ""
        if value is None and not cls.model_fields[field].is_required():
            return None
        if not isinstance(value, str) or not value.strip():
            raise SECostRunInvalidText(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("started_on", "finished_on", mode="before")
    def validate_moment(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``started_on`` and ``finished_on``.

        Args:
            value (JsonValue): The raw moment: a ``datetime`` or an ISO 8601 string.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The moment in ISO 8601, or ``None`` for ``finished_on`` left out.

        Raises:
            SECostRunInvalidMoment: When the moment is missing where it is required, unreadable, or has no time zone.
        """
        field = info.field_name or ""
        if value is None and not cls.model_fields[field].is_required():
            return None
        text = value.isoformat() if isinstance(value, datetime) else value
        if not isinstance(text, str):
            raise SECostRunInvalidMoment(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be an ISO 8601 date and time with its time zone."
            )
        try:
            moment = datetime.fromisoformat(text)
        except ValueError as error:
            raise SECostRunInvalidMoment(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be an ISO 8601 date and time with its time zone."
            ) from error
        if moment.tzinfo is None:
            raise SECostRunInvalidMoment(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must carry its time zone."
            )
        return moment.isoformat()

    @field_validator("estimate_usd", "cost_usd", mode="before")
    def validate_amount(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``estimate_usd`` and ``cost_usd``.

        Args:
            value (JsonValue): The raw amount: a number or a decimal string.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The amount as a decimal string, or the default for ``cost_usd`` left out.

        Raises:
            SECostRunInvalidAmount: When the amount is missing where it is required, or is not zero or more.
        """
        field = info.field_name or ""
        if value is None and not cls.model_fields[field].is_required():
            return "0"
        if value is None or isinstance(value, bool):
            raise SECostRunInvalidAmount(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be an amount in USD."
            )
        try:
            amount = Decimal(str(value))
        except InvalidOperation as error:
            raise SECostRunInvalidAmount(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be an amount in USD."
            ) from error
        if not amount.is_finite() or amount < 0:
            raise SECostRunInvalidAmount(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be zero or more."
            )
        return str(amount)

    @field_validator("status", "source", mode="before")
    def validate_choice(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``status`` and ``source``.

        Args:
            value (JsonValue): The raw value.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The value.

        Raises:
            SECostRunInvalidChoice: When the value is not a member of the field's enum.
        """
        field = info.field_name or ""
        allowed = [member.value for member in cls.CHOICES[field]]
        if value not in allowed:
            raise SECostRunInvalidChoice(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                f"Must be one of {allowed}."
            )
        return value

    @field_validator("usage", mode="before")
    def validate_usage(cls, value: JsonValue) -> JsonValue:
        """Validate ``usage``.

        Args:
            value (JsonValue): The raw usage: a mapping of model ids to token counts.

        Returns:
            JsonValue: The mapping, or the default for ``None``.

        Raises:
            SECostRunInvalidUsage: When the value is not a mapping.
        """
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise SECostRunInvalidUsage(
                f"Invalid usage: {value!r}. "  # noqa: E501
                "Must map each model id to its tokens."
            )
        return value

    @field_validator("settled", mode="before")
    def validate_settled(cls, value: JsonValue) -> JsonValue:
        """Validate ``settled``.

        Args:
            value (JsonValue): The raw flag.

        Returns:
            JsonValue: The flag, or the default for ``None``.

        Raises:
            SECostRunInvalidSettled: When the value is not a boolean.
        """
        if value is None:
            return False
        if not isinstance(value, bool):
            raise SECostRunInvalidSettled(
                f"Invalid settled: {value!r}. "  # noqa: E501
                "Must be true or false."
            )
        return value

    @field_validator("exit_code", mode="before")
    def validate_exit_code(cls, value: JsonValue) -> JsonValue:
        """Validate ``exit_code``.

        Args:
            value (JsonValue): The raw exit code.

        Returns:
            JsonValue: The exit code, or ``None``.

        Raises:
            SECostRunInvalidExitCode: When the value is not a whole number.
        """
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, int):
            raise SECostRunInvalidExitCode(
                f"Invalid exit_code: {value!r}. "  # noqa: E501
                "Must be a whole number."
            )
        return value

    @field_serializer("estimate_usd", "cost_usd", when_used="json")
    def serialize_amount(self, value: Decimal) -> float:
        """Write an amount as a JSON number.

        Args:
            value (Decimal): The amount.

        Returns:
            float: The same amount, a number for the tools that read the ledger.
        """
        return float(value)

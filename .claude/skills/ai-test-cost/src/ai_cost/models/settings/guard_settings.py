from __future__ import annotations

# Standard library imports
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import ClassVar, Dict, FrozenSet, Optional, Tuple

# Third-party imports
from pydantic import Field, JsonValue, ValidationInfo, field_validator

# First-party imports
from ai_cost.models.enums import UsageSource
from ai_cost.models.settings.exceptions import (
    SEGuardSettingsInvalidNumber,
    SEGuardSettingsInvalidPath,
    SEGuardSettingsInvalidUsageSource,
    SEGuardSettingsUnreadable,
)
from harness_core.models.catalogs.yaml_catalog import YamlCatalog


class GuardSettings(YamlCatalog):
    """The settings that enforce the cap of the paid AI tests, read from the versioned ``conf/settings.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the settings file cannot be read.
        SKILL_DIR (Path): The skill's folder, from which a relative path is read.
        DEFAULT_CAP_USD_MIN (Decimal): The lowest cap.
        KILL_RATIO_MIN (Decimal): The lowest kill ratio.
        KILL_RATIO_MAX (Decimal): The highest kill ratio.
        POLL_INTERVAL_S_MIN (int): The shortest time between two measures.
        SETTLE_S_MIN (int): The shortest settling delay.
        MAX_UNMEASURED_MIN (int): The fewest failed measures that stop a run.
        BOUNDS (Dict[str, Tuple[Decimal, Optional[Decimal]]]): The bounds of each number field.
        WHOLE_NUMBERS (FrozenSet[str]): The number fields that are whole numbers.
        state_dir (Path): Folder of the ledgers, one per ticket, and of the log file.
        prices_file (Path): The price of each model.
        paid_commands_file (Path): The commands that call a paid AI.
        cost_template_file (Path): The layout of a ticket's ``COST.md``.
        default_cap_usd (Decimal): The cap of a ticket's paid AI tests, all runs together, in USD.
        kill_ratio (Decimal): The share of the cap at which a running test is killed.
        poll_interval_s (int): Seconds between two measures of a running test.
        settle_s (int): Seconds after a run ends before its measured cost is final.
        max_unmeasured (int): Measures in a row that may fail before a running test is stopped.
        usage_source (UsageSource): How a run's cost is measured.

    Notes:
        - **None of these settings is read from the environment.** A command could otherwise loosen the guard by
          exporting a variable, so changing one is a reviewed change of the versioned file. Tests pass their own
          values to the constructor.
        - ``kill_ratio`` stays below 1 because the usage report arrives a few minutes late.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEGuardSettingsUnreadable
    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]
    DEFAULT_CAP_USD_MIN: ClassVar[Decimal] = Decimal("0.01")
    KILL_RATIO_MIN: ClassVar[Decimal] = Decimal("0.01")
    KILL_RATIO_MAX: ClassVar[Decimal] = Decimal("1")
    POLL_INTERVAL_S_MIN: ClassVar[int] = 1
    SETTLE_S_MIN: ClassVar[int] = 0
    MAX_UNMEASURED_MIN: ClassVar[int] = 1
    BOUNDS: ClassVar[Dict[str, Tuple[Decimal, Optional[Decimal]]]] = {
        "default_cap_usd": (DEFAULT_CAP_USD_MIN, None),
        "kill_ratio": (KILL_RATIO_MIN, KILL_RATIO_MAX),
        "poll_interval_s": (Decimal(POLL_INTERVAL_S_MIN), None),
        "settle_s": (Decimal(SETTLE_S_MIN), None),
        "max_unmeasured": (Decimal(MAX_UNMEASURED_MIN), None),
    }
    WHOLE_NUMBERS: ClassVar[FrozenSet[str]] = frozenset({"poll_interval_s", "settle_s", "max_unmeasured"})

    state_dir: Path = Field(
        description="Folder of the ledgers, one per ticket, and of the log file.",
        examples=["~/.local/state/ai-test-cost"],
    )
    prices_file: Path = Field(description="The price of each model.", examples=["conf/prices.yaml"])
    paid_commands_file: Path = Field(
        description="The commands that call a paid AI.", examples=["conf/paid-commands.yaml"]
    )
    cost_template_file: Path = Field(description="The layout of a ticket's COST.md.", examples=["templates/COST.md"])
    default_cap_usd: Decimal = Field(
        description="The cap of a ticket's paid AI tests, all runs together, in USD.", examples=["20"]
    )
    kill_ratio: Decimal = Field(description="The share of the cap at which a running test is killed.", examples=["0.9"])
    poll_interval_s: int = Field(description="Seconds between two measures of a running test.", examples=[60])
    settle_s: int = Field(description="Seconds after a run ends before its measured cost is final.", examples=[300])
    max_unmeasured: int = Field(
        description="Measures in a row that may fail before a running test is stopped.", examples=[3]
    )
    usage_source: UsageSource = Field(description="How a run's cost is measured.", examples=["anthropic"])

    @field_validator("state_dir", "prices_file", "paid_commands_file", "cost_template_file", mode="before")
    def validate_path(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate the paths.

        Args:
            value (JsonValue): The raw path: a ``Path`` or a string, relative to the skill's folder or absolute.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The absolute path, ``~`` expanded, as a string.

        Raises:
            SEGuardSettingsInvalidPath: When the value is not a non-empty path.
        """
        text = str(value) if isinstance(value, Path) else value
        if not isinstance(text, str) or not text.strip():
            raise SEGuardSettingsInvalidPath(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                "Must be a non-empty path."
            )
        path = Path(text.strip()).expanduser()
        return str(path if path.is_absolute() else cls.SKILL_DIR / path)

    @field_validator("default_cap_usd", "kill_ratio", "poll_interval_s", "settle_s", "max_unmeasured", mode="before")
    def validate_number(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate the numbers.

        Args:
            value (JsonValue): The raw number: a number or a numeric string.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The number as a string.

        Raises:
            SEGuardSettingsInvalidNumber: When the value is not a number within the field's bounds, or not a whole
                number where one is expected.
        """
        field = info.field_name or ""
        if value is None or isinstance(value, bool):
            raise SEGuardSettingsInvalidNumber(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a number."
            )
        try:
            number = Decimal(str(value))
        except InvalidOperation as error:
            raise SEGuardSettingsInvalidNumber(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a number."
            ) from error
        low, high = cls.BOUNDS[field]
        whole = field in cls.WHOLE_NUMBERS
        if not number.is_finite() or (whole and number != number.to_integral_value()):
            raise SEGuardSettingsInvalidNumber(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a whole number."
            )
        if number < low or (high is not None and number > high):
            raise SEGuardSettingsInvalidNumber(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                f"Must be at least {low}{f' and at most {high}' if high is not None else ''}."
            )
        return str(int(number)) if whole else str(number)

    @field_validator("usage_source", mode="before")
    def validate_usage_source(cls, value: JsonValue) -> JsonValue:
        """Validate ``usage_source``.

        Args:
            value (JsonValue): The raw source.

        Returns:
            JsonValue: The source.

        Raises:
            SEGuardSettingsInvalidUsageSource: When the value is not a ``UsageSource``.
        """
        allowed = [source.value for source in UsageSource]
        if value not in allowed:
            raise SEGuardSettingsInvalidUsageSource(
                f"Invalid usage_source: {value!r}. "  # noqa: E501
                f"Must be one of {allowed}."
            )
        return value

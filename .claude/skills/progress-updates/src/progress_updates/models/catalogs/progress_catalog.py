from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict

# Third-party imports
from pydantic import Field, JsonValue, ValidationInfo, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from progress_updates.models.catalogs.exceptions import (
    SEProgressCatalogInvalidEvidenceMax,
    SEProgressCatalogInvalidHealthIcons,
    SEProgressCatalogInvalidIntervalS,
    SEProgressCatalogInvalidLineMaxChars,
    SEProgressCatalogInvalidStateIcons,
    SEProgressCatalogUnreadable,
)
from progress_updates.models.enums import TaskState


class ProgressCatalog(YamlCatalog):
    """How progress updates are paced and drawn (``conf/progress-updates.yaml``).

    Attributes:
        UNREADABLE (type[Exception]): Raised when the file cannot be read.
        INTERVAL_S_MIN (int): The shortest interval: 2 minutes, as the owner asked.
        INTERVAL_S_MAX (int): The longest interval.
        LINE_MAX_CHARS_MIN (int): The shortest output line kept.
        LINE_MAX_CHARS_MAX (int): The longest output line kept.
        EVIDENCE_MAX_MIN (int): The fewest evidence folders shown.
        EVIDENCE_MAX_MAX (int): The most evidence folders shown.
        interval_s (int): Seconds between two updates.
        line_max_chars (int): Characters kept of a task's last output line.
        evidence_max (int): How many of the newest evidence folders an update shows.
        state_icons (Dict[str, str]): The icon of each task state.
        health_icons (Dict[str, str]): The coloured health dot of each task state.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEProgressCatalogUnreadable
    INTERVAL_S_MIN: ClassVar[int] = 120
    INTERVAL_S_MAX: ClassVar[int] = 3600
    LINE_MAX_CHARS_MIN: ClassVar[int] = 40
    LINE_MAX_CHARS_MAX: ClassVar[int] = 400
    EVIDENCE_MAX_MIN: ClassVar[int] = 0
    EVIDENCE_MAX_MAX: ClassVar[int] = 20

    interval_s: int = Field(default=120, description="Seconds between two updates.", examples=[120])
    line_max_chars: int = Field(default=160, description="Characters kept of a last output line.", examples=[160])
    evidence_max: int = Field(default=5, description="Newest evidence folders shown.", examples=[5])
    state_icons: Dict[str, str] = Field(description="The icon of each task state.", examples=[{"done": "✅"}])
    health_icons: Dict[str, str] = Field(description="The health dot of each task state.", examples=[{"done": "🟢"}])

    @field_validator("interval_s", mode="before")
    def validate_interval_s(cls, value: JsonValue) -> JsonValue:
        """Validate ``interval_s``.

        Args:
            value (JsonValue): The raw interval.

        Returns:
            JsonValue: The interval, or the default when ``None``.

        Raises:
            SEProgressCatalogInvalidIntervalS: When the value is not a whole number in the bounds.
        """
        if value is None:
            return cls.model_fields["interval_s"].get_default(call_default_factory=True)
        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or not (cls.INTERVAL_S_MIN <= value <= cls.INTERVAL_S_MAX)
        ):
            raise SEProgressCatalogInvalidIntervalS(
                f"Invalid interval_s: {value!r}. "  # noqa: E501
                f"Must be a whole number in [{cls.INTERVAL_S_MIN}, {cls.INTERVAL_S_MAX}]."
            )
        return value

    @field_validator("line_max_chars", mode="before")
    def validate_line_max_chars(cls, value: JsonValue) -> JsonValue:
        """Validate ``line_max_chars``.

        Args:
            value (JsonValue): The raw length.

        Returns:
            JsonValue: The length, or the default when ``None``.

        Raises:
            SEProgressCatalogInvalidLineMaxChars: When the value is not a whole number in the bounds.
        """
        if value is None:
            return cls.model_fields["line_max_chars"].get_default(call_default_factory=True)
        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or not (cls.LINE_MAX_CHARS_MIN <= value <= cls.LINE_MAX_CHARS_MAX)
        ):
            raise SEProgressCatalogInvalidLineMaxChars(
                f"Invalid line_max_chars: {value!r}. "  # noqa: E501
                f"Must be a whole number in [{cls.LINE_MAX_CHARS_MIN}, {cls.LINE_MAX_CHARS_MAX}]."
            )
        return value

    @field_validator("evidence_max", mode="before")
    def validate_evidence_max(cls, value: JsonValue) -> JsonValue:
        """Validate ``evidence_max``.

        Args:
            value (JsonValue): The raw count.

        Returns:
            JsonValue: The count, or the default when ``None``.

        Raises:
            SEProgressCatalogInvalidEvidenceMax: When the value is not a whole number in the bounds.
        """
        if value is None:
            return cls.model_fields["evidence_max"].get_default(call_default_factory=True)
        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or not (cls.EVIDENCE_MAX_MIN <= value <= cls.EVIDENCE_MAX_MAX)
        ):
            raise SEProgressCatalogInvalidEvidenceMax(
                f"Invalid evidence_max: {value!r}. "  # noqa: E501
                f"Must be a whole number in [{cls.EVIDENCE_MAX_MIN}, {cls.EVIDENCE_MAX_MAX}]."
            )
        return value

    @field_validator("state_icons", "health_icons", mode="before")
    def validate_icons(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``state_icons`` and ``health_icons``.

        Args:
            value (JsonValue): The raw mapping of state to icon.
            info (ValidationInfo): Pydantic's validation information, which names the field.

        Returns:
            JsonValue: The mapping, its icons stripped.

        Raises:
            SEProgressCatalogInvalidStateIcons: When ``state_icons`` does not give one icon to each state.
            SEProgressCatalogInvalidHealthIcons: When ``health_icons`` does not give one icon to each state.
        """
        field = info.field_name
        error = SEProgressCatalogInvalidStateIcons if field == "state_icons" else SEProgressCatalogInvalidHealthIcons
        states = sorted(state.value for state in TaskState)
        if (
            not isinstance(value, dict)
            or sorted(value) != states
            or not all(isinstance(icon, str) and icon.strip() for icon in value.values())
        ):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                f"Must give one non-empty icon to each of {states}."
            )
        return {state: str(icon).strip() for state, icon in value.items()}

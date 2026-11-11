from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict, List

# Third-party imports
from pydantic import Field, JsonValue, ValidationInfo, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from project_docs.models.catalogs.doc_map_rule import DocMapRule
from project_docs.models.catalogs.exceptions import (
    SEDocMapInvalidAlways,
    SEDocMapInvalidChapterPattern,
    SEDocMapInvalidRules,
    SEDocMapUnreadable,
)


class DocMap(YamlCatalog):
    """Which project documentation chapters a changed path concerns, read from ``conf/doc-map.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): The exception raised when the file cannot be read.
        PLACEHOLDERS (Dict[str, str]): The placeholder each chapter pattern must hold.
        rules (List[DocMapRule]): The rules, the first matching one applying to a path.
        always (List[str]): The chapters of a path that matches no rule.
        per_service (str): The chapter every service must have, with ``{service}``.
        per_frontend (str): The chapter every front end must have, with ``{frontend}``.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEDocMapUnreadable
    PLACEHOLDERS: ClassVar[Dict[str, str]] = {"per_service": "{service}", "per_frontend": "{frontend}"}

    rules: List[DocMapRule] = Field(
        description="The rules, the first matching one applying to a path.",
        examples=[[{"paths": ["conf/*"], "chapters": ["docs/technical/configuration.md"]}]],
    )
    always: List[str] = Field(
        default_factory=list, description="The chapters of a path that matches no rule.", examples=[["README.md"]]
    )
    per_service: str = Field(
        description="The chapter every service must have.", examples=["docs/technical/services/{service}.md"]
    )
    per_frontend: str = Field(
        description="The chapter every front end must have.", examples=["docs/technical/frontends/{frontend}.md"]
    )

    @field_validator("rules", mode="before")
    def validate_rules(cls, value: JsonValue) -> JsonValue:
        """Validate ``rules``.

        Args:
            value (JsonValue): The raw rules.

        Returns:
            JsonValue: The rules, each validated by ``DocMapRule``.

        Raises:
            SEDocMapInvalidRules: When the value is not a non-empty list.
        """
        if not isinstance(value, list) or not value:
            raise SEDocMapInvalidRules(
                f"Invalid rules: {value!r}. "  # noqa: E501
                "Must be a non-empty list of rules."
            )
        return value

    @field_validator("always", mode="before")
    def validate_always(cls, value: JsonValue) -> JsonValue:
        """Validate ``always``.

        Args:
            value (JsonValue): The raw chapters, or ``None``.

        Returns:
            JsonValue: The chapters, stripped, or an empty list.

        Raises:
            SEDocMapInvalidAlways: When the value is not a list of non-empty strings.
        """
        if value is None:
            return []
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise SEDocMapInvalidAlways(
                f"Invalid always: {value!r}. "  # noqa: E501
                "Must be a list of non-empty chapter paths."
            )
        return [item.strip() for item in value if isinstance(item, str)]

    @field_validator("per_service", "per_frontend", mode="before")
    def validate_chapter_pattern(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate ``per_service`` and ``per_frontend``.

        Args:
            value (JsonValue): The raw chapter pattern.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The chapter pattern, stripped.

        Raises:
            SEDocMapInvalidChapterPattern: When the value is not a string holding the field's placeholder.
        """
        placeholder = cls.PLACEHOLDERS[str(info.field_name)]
        if not isinstance(value, str) or placeholder not in value:
            raise SEDocMapInvalidChapterPattern(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                f"Must be a chapter path holding {placeholder}."
            )
        return value.strip()

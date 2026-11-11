from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Dict, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from harness_core.models.branches.branch_kind import BranchKind
from harness_core.models.branches.exceptions import (
    SEBranchNameInvalidKind,
    SEBranchNameInvalidTicket,
    SEBranchNameInvalidValue,
    SEBranchNameInvalidVersion,
)


class BranchName(BaseModel):
    """A branch name read with the GitFlow conventions of GIT-8.

    Attributes:
        PATTERNS (Dict[BranchKind, re.Pattern[str]]): The full shape of each GitFlow prefix.
        TICKET_PATTERN (re.Pattern[str]): A ticket key, ``GH-<issue number>``.
        VERSION_PATTERN (re.Pattern[str]): A semantic version, ``x.y.z``.
        value (str): The branch name as git shows it.
        kind (BranchKind): Its GitFlow role.
        ticket (Optional[str]): The ticket key it carries, if any.
        version (Optional[str]): The version it carries, if any.

    Notes:
        - A name that starts with a GitFlow prefix but misses its shape is refused, so that a branch never escapes the
          harness's checks by a typo.
        - Any other name is ``OTHER``: Dependabot and similar tools make their own branches.
    """

    PATTERNS: ClassVar[Dict[BranchKind, re.Pattern[str]]] = {
        BranchKind.FEATURE: re.compile(r"^feature/(?P<ticket>GH-\d+)-[a-z0-9]+(?:-[a-z0-9]+)*$"),
        BranchKind.BUGFIX: re.compile(r"^bugfix/(?P<ticket>GH-\d+)-[a-z0-9]+(?:-[a-z0-9]+)*$"),
        BranchKind.RELEASE: re.compile(r"^release/(?P<version>\d+\.\d+\.\d+)$"),
        BranchKind.HOTFIX: re.compile(
            r"^hotfix/(?P<version>\d+\.\d+\.\d+)-(?P<ticket>GH-\d+)-[a-z0-9]+(?:-[a-z0-9]+)*$"
        ),
    }
    TICKET_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^GH-\d+$")
    VERSION_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^\d+\.\d+\.\d+$")

    model_config = ConfigDict(extra="forbid", frozen=True)

    value: str = Field(description="The branch name as git shows it.", examples=["feature/GH-12-add-customers"])
    kind: BranchKind = Field(description="Its GitFlow role.", examples=["feature"])
    ticket: Optional[str] = Field(default=None, description="The ticket key it carries.", examples=["GH-12"])
    version: Optional[str] = Field(default=None, description="The version it carries.", examples=["1.4.0"])

    @field_validator("value", mode="before")
    def validate_value(cls, value: JsonValue) -> JsonValue:
        """Validate ``value``.

        Args:
            value (JsonValue): The raw branch name.

        Returns:
            JsonValue: The branch name, stripped.

        Raises:
            SEBranchNameInvalidValue: When the name is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEBranchNameInvalidValue(
                f"Invalid value: {value!r}. "  # noqa: E501
                "Must be a non-empty branch name."
            )
        return value.strip()

    @field_validator("kind", mode="before")
    def validate_kind(cls, value: JsonValue) -> JsonValue:
        """Validate ``kind``.

        Args:
            value (JsonValue): The raw kind.

        Returns:
            JsonValue: The kind.

        Raises:
            SEBranchNameInvalidKind: When the value is not a ``BranchKind``.
        """
        if value not in {kind.value for kind in BranchKind}:
            raise SEBranchNameInvalidKind(
                f"Invalid kind: {value!r}. "  # noqa: E501
                f"Must be one of {[kind.value for kind in BranchKind]}."
            )
        return value

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket key, or ``None``.

        Returns:
            JsonValue: The ticket key, or ``None``.

        Raises:
            SEBranchNameInvalidTicket: When the value is not ``GH-<n>``.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not cls.TICKET_PATTERN.match(value):
            raise SEBranchNameInvalidTicket(
                f"Invalid ticket: {value!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        return value

    @field_validator("version", mode="before")
    def validate_version(cls, value: JsonValue) -> JsonValue:
        """Validate ``version``.

        Args:
            value (JsonValue): The raw version, or ``None``.

        Returns:
            JsonValue: The version, or ``None``.

        Raises:
            SEBranchNameInvalidVersion: When the value is not ``x.y.z``.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not cls.VERSION_PATTERN.match(value):
            raise SEBranchNameInvalidVersion(
                f"Invalid version: {value!r}. "  # noqa: E501
                "Must look like 1.4.0."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def parse(cls, value: str) -> BranchName:
        """Read a branch name.

        Args:
            value (str): The branch name.

        Returns:
            BranchName: The name, its kind, and the ticket and version it carries.

        Raises:
            SEBranchNameInvalidValue: When a GitFlow prefix is used without its full shape.
        """
        name = value.strip()
        if name in {BranchKind.MASTER.value, BranchKind.DEVELOP.value}:
            return cls(value=name, kind=name)
        for kind, pattern in cls.PATTERNS.items():
            if name.startswith(f"{kind.value}/"):
                match = pattern.match(name)
                if match is None:
                    raise SEBranchNameInvalidValue(
                        f"Invalid value: {name!r}. "  # noqa: E501
                        f"A {kind.value} branch must match {pattern.pattern}."
                    )
                groups = match.groupdict()
                return cls(value=name, kind=kind, ticket=groups.get("ticket"), version=groups.get("version"))
        return cls(value=name, kind=BranchKind.OTHER)

    @property
    def carries_ticket_work(self) -> bool:
        """Whether code for a ticket is written on this branch."""
        return self.ticket is not None and self.kind in {BranchKind.FEATURE, BranchKind.BUGFIX, BranchKind.HOTFIX}

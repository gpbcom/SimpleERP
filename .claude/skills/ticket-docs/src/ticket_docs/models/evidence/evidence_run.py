from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from typing import ClassVar, Dict, Optional, Pattern

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.enums import RunKind, RunPlace
from ticket_docs.models.evidence.exceptions import (
    SEEvidenceRunInvalidCommit,
    SEEvidenceRunInvalidDate,
    SEEvidenceRunInvalidDirty,
    SEEvidenceRunInvalidFolder,
    SEEvidenceRunInvalidKind,
    SEEvidenceRunInvalidText,
    SEEvidenceRunInvalidWhere,
)


class EvidenceRun(BaseModel):
    """One evidence folder, read from its ``README.md``.

    Attributes:
        ROW (Pattern[str]): A ``| **Label** | value |`` row of the README's table.
        COMMIT_CELL (Pattern[str]): The Commit cell: the hash, the branch and an optional note.
        FOLDER_NAME (Pattern[str]): An evidence folder name, ``<where>-<YYYY-MM-DD>-<check>``.
        COMMIT_PATTERN (Pattern[str]): A full commit hash.
        COUNTS (Pattern[str]): The ``passed/total`` counts of a result.
        DATE_FORMAT (str): How the README writes the date.
        DIRTY_NOTE (str): The note of a run made with uncommitted changes.
        INVALID_ICON (str): The icon of an invalid run.
        PASS_ICON (str): The icon of a passed run.
        EXPECTED_RED (str): The mark of a run expected to fail.
        AS_EXPECTED (str): The mark of a red run that did fail.
        folder (str): The folder's name.
        what (Optional[str]): What the run proves.
        command (Optional[str]): The command, as the README shows it.
        commit (Optional[str]): The full hash of the commit it ran on.
        branch (Optional[str]): The branch it ran on.
        dirty (bool): Whether the working tree had uncommitted changes.
        kind (Optional[RunKind]): What it tested.
        where (Optional[RunPlace]): Where it ran.
        date (Optional[datetime]): When it started, to the minute.
        result (Optional[str]): The verdict line.

    Notes:
        - ``from_readme`` reads the README of ``ticket-docs record-run`` and of the bootstrap recorder alike: a missing
          row stays ``None``, so that ``check`` can name it, and a row whose value is wrong raises.
        - A pipe inside a cell is escaped with a backslash, and read back as a plain pipe.
    """

    ROW: ClassVar[Pattern[str]] = re.compile(r"^\|\s*\*\*(?P<label>[^*|]+)\*\*\s*\|\s*(?P<value>.*?)\s*\|\s*$", re.M)
    COMMIT_CELL: ClassVar[Pattern[str]] = re.compile(
        r"^`(?P<commit>[^`]*)`(?:\s+on\s+`(?P<branch>[^`]*)`)?(?P<rest>.*)$"
    )
    FOLDER_NAME: ClassVar[Pattern[str]] = re.compile(r"^(?P<where>[a-z]+)-(?P<date>\d{4}-\d{2}-\d{2})-(?P<check>.+)$")
    COMMIT_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^[0-9a-f]{40}$")
    COUNTS: ClassVar[Pattern[str]] = re.compile(r"\b\d+/\d+\b")
    DATE_FORMAT: ClassVar[str] = "%Y-%m-%d %H:%M"
    DIRTY_NOTE: ClassVar[str] = "working tree has uncommitted changes"
    INVALID_ICON: ClassVar[str] = "⚠️"
    PASS_ICON: ClassVar[str] = "✅"
    EXPECTED_RED: ClassVar[str] = "expected red"
    AS_EXPECTED: ClassVar[str] = "as expected"

    model_config = ConfigDict(extra="forbid", frozen=True)

    folder: str = Field(description="The folder's name.", examples=["local-2026-11-10-tdd-red-storage"])
    what: Optional[str] = Field(default=None, description="What the run proves.", examples=["The storage tests"])
    command: Optional[str] = Field(default=None, description="The command, as the README shows it.")
    commit: Optional[str] = Field(default=None, description="The full hash of the commit it ran on.")
    branch: Optional[str] = Field(default=None, description="The branch it ran on.", examples=["feature/GH-1-x"])
    dirty: bool = Field(default=False, description="Whether the working tree had uncommitted changes.")
    kind: Optional[RunKind] = Field(default=None, description="What it tested.", examples=["unit"])
    where: Optional[RunPlace] = Field(default=None, description="Where it ran.", examples=["local"])
    date: Optional[datetime] = Field(default=None, description="When it started, to the minute.")
    result: Optional[str] = Field(default=None, description="The verdict line.", examples=["✅ PASS 3/3"])

    @field_validator("folder", mode="before")
    def validate_folder(cls, value: JsonValue) -> JsonValue:
        """Validate ``folder``.

        Args:
            value (JsonValue): The raw folder name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEEvidenceRunInvalidFolder: When the name is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEEvidenceRunInvalidFolder(
                f"Invalid folder: {value!r}. "  # noqa: E501
                "Must be a non-empty folder name."
            )
        return value.strip()

    @field_validator("what", "command", "branch", "result", mode="before")
    def validate_text(cls, value: JsonValue) -> JsonValue:
        """Validate ``what``, ``command``, ``branch`` and ``result``.

        Args:
            value (JsonValue): The raw text, or ``None``.

        Returns:
            JsonValue: The text, stripped, or ``None``.

        Raises:
            SEEvidenceRunInvalidText: When the value is not a non-empty string.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SEEvidenceRunInvalidText(
                f"Invalid text: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("commit", mode="before")
    def validate_commit(cls, value: JsonValue) -> JsonValue:
        """Validate ``commit``.

        Args:
            value (JsonValue): The raw commit hash, or ``None``.

        Returns:
            JsonValue: The hash in lower case, or ``None``.

        Raises:
            SEEvidenceRunInvalidCommit: When the value is not a full 40-character hash.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not cls.COMMIT_PATTERN.match(value.strip().lower()):
            raise SEEvidenceRunInvalidCommit(
                f"Invalid commit: {value!r}. "  # noqa: E501
                "Must be a full 40-character commit hash."
            )
        return value.strip().lower()

    @field_validator("dirty", mode="before")
    def validate_dirty(cls, value: JsonValue) -> JsonValue:
        """Validate ``dirty``.

        Args:
            value (JsonValue): The raw flag, or ``None``.

        Returns:
            JsonValue: The flag, ``False`` for ``None``.

        Raises:
            SEEvidenceRunInvalidDirty: When the value is not a boolean.
        """
        if value is None:
            return False
        if not isinstance(value, bool):
            raise SEEvidenceRunInvalidDirty(
                f"Invalid dirty: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value

    @field_validator("kind", mode="before")
    def validate_kind(cls, value: JsonValue) -> JsonValue:
        """Validate ``kind``.

        Args:
            value (JsonValue): The raw kind, or ``None``.

        Returns:
            JsonValue: The kind, or ``None``.

        Raises:
            SEEvidenceRunInvalidKind: When the value is not a ``RunKind``.
        """
        if value is None:
            return None
        if value not in {kind.value for kind in RunKind}:
            raise SEEvidenceRunInvalidKind(
                f"Invalid kind: {value!r}. "  # noqa: E501
                f"Must be one of {[kind.value for kind in RunKind]}."
            )
        return value

    @field_validator("where", mode="before")
    def validate_where(cls, value: JsonValue) -> JsonValue:
        """Validate ``where``.

        Args:
            value (JsonValue): The raw place, or ``None``.

        Returns:
            JsonValue: The place, or ``None``.

        Raises:
            SEEvidenceRunInvalidWhere: When the value is not a ``RunPlace``.
        """
        if value is None:
            return None
        if value not in {place.value for place in RunPlace}:
            raise SEEvidenceRunInvalidWhere(
                f"Invalid where: {value!r}. "  # noqa: E501
                f"Must be one of {[place.value for place in RunPlace]}."
            )
        return value

    @field_validator("date", mode="before")
    def validate_date(cls, value: JsonValue) -> JsonValue:
        """Validate ``date``.

        Args:
            value (JsonValue): The raw date, ``YYYY-MM-DD HH:MM``, a ``datetime``, or ``None``.

        Returns:
            JsonValue: The date as ISO text, or ``None``.

        Raises:
            SEEvidenceRunInvalidDate: When the value is not a date to the minute.
        """
        if value is None or isinstance(value, datetime):
            return value
        if isinstance(value, str):
            for reader in (cls.DATE_FORMAT, None):
                try:
                    moment = datetime.strptime(value.strip(), reader) if reader else datetime.fromisoformat(value)
                except ValueError:
                    continue
                return moment.isoformat()
        raise SEEvidenceRunInvalidDate(
            f"Invalid date: {value!r}. "  # noqa: E501
            "Must be written YYYY-MM-DD HH:MM."
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def from_readme(cls, folder: str, text: str) -> EvidenceRun:
        """Read an evidence folder's README.

        Args:
            folder (str): The folder's name.
            text (str): The README's text.

        Returns:
            EvidenceRun: The run. A row the README does not have stays ``None``.

        Raises:
            SEInvalidEvidenceRunException: A subclass, when a row holds a value that is not valid.
        """
        rows: Dict[str, str] = {}
        for match in cls.ROW.finditer(text):
            rows.setdefault(match.group("label").strip().lower(), match.group("value").replace("\\|", "|"))
        fields: Dict[str, JsonValue] = {"folder": folder}
        for label in ("what", "kind", "where", "date", "result"):
            fields[label] = rows.get(label)
        command = rows.get("command")
        fields["command"] = (
            command[1:-1] if command and len(command) > 1 and command[0] == command[-1] == "`" else command
        )
        commit = cls.COMMIT_CELL.match(rows.get("commit", ""))
        if commit is not None:
            fields["commit"] = commit.group("commit")
            fields["branch"] = commit.group("branch")
            fields["dirty"] = cls.DIRTY_NOTE in commit.group("rest")
        elif "commit" in rows:
            fields["commit"] = rows["commit"]
        return cls.model_validate(fields)

    @property
    def check(self) -> str:
        """The check's name: the folder name without its place and date."""
        match = self.FOLDER_NAME.match(self.folder)
        return match.group("check") if match else self.folder

    @property
    def icon(self) -> str:
        """The result's icon, empty when there is no result."""
        return self.result.split()[0] if self.result else ""

    @property
    def counts(self) -> Optional[str]:
        """The result's ``passed/total`` counts, when it has them."""
        match = self.COUNTS.search(self.result or "")
        return match.group(0) if match else None

    @property
    def passed(self) -> bool:
        """Whether the run passed."""
        return self.icon == self.PASS_ICON

    @property
    def invalid(self) -> bool:
        """Whether the run is invalid, such as an environment failure."""
        return self.icon == self.INVALID_ICON

    @property
    def expected_red(self) -> bool:
        """Whether the run was expected to fail and did."""
        result = self.result or ""
        return self.EXPECTED_RED in result and self.AS_EXPECTED in result

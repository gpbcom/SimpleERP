from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar, Dict, List

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from ticket_docs.models.checks.exceptions import (
    SEFolderRulesInvalidHeadings,
    SEFolderRulesInvalidList,
    SEFolderRulesInvalidMinutes,
    SEFolderRulesUnreadable,
)


class FolderRules(YamlCatalog):
    """What a ticket folder must hold: ``conf/folder-rules.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the file cannot be read.
        SQUASH_PERMIT_MINUTES_MIN (int): The shortest lifetime of a squash permit, in minutes.
        SQUASH_PERMIT_MINUTES_MAX (int): The longest lifetime of a squash permit, in minutes.
        SKILL_DIR (Path): The ticket-docs skill folder, which holds ``conf/``.
        required_files (List[str]): The files and folders every ticket folder holds.
        handover_files (List[str]): The files required, and linkable, once the ticket is handed over.
        headings (Dict[str, List[str]]): The headings each file keeps from its template.
        placeholders (List[str]): The template placeholders never left in a file.
        finished_files (List[str]): The files that keep no template slot once the ticket is handed over.
        status_icons (List[str]): The icons a status cell starts with.
        stage_icons (List[str]): The first icons of the Stage validation rows.
        result_sections (List[str]): The sections whose ✅ cells are test results.
        run_steps (List[str]): The words that make a Status step a test run.
        production_paths (List[str]): The production code, folders ending with a slash.
        test_paths (List[str]): The test files: folders ending with a slash, file name patterns otherwise.
        marker_files (List[str]): The file names that are never production code, such as ``__init__.py``.
        commit_options (List[str]): The long options of ``git commit``, without dashes, a value-taking one ending
            with ``=``. ``git-gate`` reads an abbreviated option against them (TEST-7).
        squash_permit_minutes (int): How long a squash permit of ``ticket-docs allow-squash`` counts (GIT-4).
        guard_state_folders (List[str]): The folders of the guards' state, which no Claude tool may write
            (``~`` for the home folder).
    """

    UNREADABLE: ClassVar[type[Exception]] = SEFolderRulesUnreadable
    SQUASH_PERMIT_MINUTES_MIN: ClassVar[int] = 1
    SQUASH_PERMIT_MINUTES_MAX: ClassVar[int] = 240
    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]

    required_files: List[str] = Field(description="The files and folders every ticket folder holds.")
    handover_files: List[str] = Field(
        default_factory=list, description="The files required, and linkable, once the ticket is handed over."
    )
    headings: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="The headings each file keeps from its template.",
        examples=[{"PLAN.md": ["## Files modified"]}],
    )
    placeholders: List[str] = Field(description="The template placeholders never left in a file.")
    finished_files: List[str] = Field(description="The files that keep no template slot once handed over.")
    status_icons: List[str] = Field(description="The icons a status cell starts with.", examples=[["✅", "⬜"]])
    stage_icons: List[str] = Field(description="The first icons of the Stage validation rows.")
    result_sections: List[str] = Field(description="The sections whose ✅ cells are test results.")
    run_steps: List[str] = Field(description="The words that make a Status step a test run.")
    production_paths: List[str] = Field(description="The production code, folders ending with a slash.")
    test_paths: List[str] = Field(description="The test files: folders ending with a slash, else file names.")
    marker_files: List[str] = Field(
        default_factory=list,
        description="The file names that are never production code, such as package markers.",
        examples=[["__init__.py"]],
    )
    commit_options: List[str] = Field(
        default_factory=list,
        description="The long options of git commit, without dashes, a value-taking one ending with =.",
        examples=[["all", "message="]],
    )
    guard_state_folders: List[str] = Field(
        default_factory=list,
        description="The folders of the guards' state, which no Claude tool may write.",
        examples=[["~/.local/state/ai-test-cost"]],
    )
    squash_permit_minutes: int = Field(
        default=30, description="How long a squash permit counts, in minutes.", examples=[30]
    )

    @field_validator(
        "required_files",
        "handover_files",
        "placeholders",
        "finished_files",
        "status_icons",
        "stage_icons",
        "result_sections",
        "run_steps",
        "production_paths",
        "test_paths",
        "marker_files",
        "commit_options",
        "guard_state_folders",
        mode="before",
    )
    def validate_list(cls, value: JsonValue) -> JsonValue:
        """Validate the lists of names, icons and paths.

        Args:
            value (JsonValue): The raw list, or ``None``.

        Returns:
            JsonValue: The list, empty for ``None``.

        Raises:
            SEFolderRulesInvalidList: When the value is not a list of non-empty strings.
        """
        if value is None:
            return []
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise SEFolderRulesInvalidList(
                f"Invalid list: {value!r}. "  # noqa: E501
                "Must be a list of non-empty strings."
            )
        return value

    @field_validator("squash_permit_minutes", mode="before")
    def validate_squash_permit_minutes(cls, value: JsonValue) -> JsonValue:
        """Validate ``squash_permit_minutes``.

        Args:
            value (JsonValue): The raw lifetime, or ``None``.

        Returns:
            JsonValue: The lifetime, the default for ``None``.

        Raises:
            SEFolderRulesInvalidMinutes: When the value is not a whole number of minutes in the bounds.
        """
        if value is None:
            return cls.model_fields["squash_permit_minutes"].get_default(call_default_factory=True)
        if isinstance(value, bool) or not isinstance(value, int):
            raise SEFolderRulesInvalidMinutes(
                f"Invalid squash_permit_minutes: {value!r}. "  # noqa: E501
                "Must be a whole number of minutes."
            )
        if not cls.SQUASH_PERMIT_MINUTES_MIN <= value <= cls.SQUASH_PERMIT_MINUTES_MAX:
            raise SEFolderRulesInvalidMinutes(
                f"Invalid squash_permit_minutes: {value}. "  # noqa: E501
                f"Must be in [{cls.SQUASH_PERMIT_MINUTES_MIN}, {cls.SQUASH_PERMIT_MINUTES_MAX}]."
            )
        return value

    @field_validator("headings", mode="before")
    def validate_headings(cls, value: JsonValue) -> JsonValue:
        """Validate ``headings``.

        Args:
            value (JsonValue): The raw headings by file, or ``None``.

        Returns:
            JsonValue: The headings, empty for ``None``.

        Raises:
            SEFolderRulesInvalidHeadings: When the value does not map file names to lists of non-empty headings.
        """
        if value is None:
            return {}
        if not isinstance(value, dict) or not all(
            isinstance(headings, list) and all(isinstance(heading, str) and heading.strip() for heading in headings)
            for headings in value.values()
        ):
            raise SEFolderRulesInvalidHeadings(
                f"Invalid headings: {value!r}. "  # noqa: E501
                "Must map each file name to the list of its headings."
            )
        return value

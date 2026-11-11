from __future__ import annotations

# Standard library imports
import re
from pathlib import Path
from typing import ClassVar, Dict, List, Optional, Pattern, Tuple

# Third-party imports
from pydantic import Field, JsonValue, ValidationInfo, field_validator, model_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from ticket_docs.models.issues.exceptions import (
    SEIssueRulesInconsistent,
    SEIssueRulesInvalidFamilies,
    SEIssueRulesInvalidLength,
    SEIssueRulesInvalidList,
    SEIssueRulesInvalidMapping,
    SEIssueRulesInvalidPattern,
    SEIssueRulesInvalidReferenceKinds,
    SEIssueRulesInvalidText,
    SEIssueRulesUnreadable,
)
from ticket_docs.models.issues.reference_kind import ReferenceKind


class IssueRules(YamlCatalog):
    """How features and tickets are written on GitHub (rule GIT-10): ``conf/issue-rules.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the file cannot be read.
        SKILL_DIR (Path): The ticket-docs skill folder, which holds ``conf/``.
        REPOSITORY_SLOT (str): The slot of ``owner/name`` in the link templates and patterns.
        PATTERN_GROUPS (Dict[str, Tuple[str, ...]]): The named groups each regular expression must define.
        TITLE_MAX_LENGTH_MIN (int): The shortest title limit accepted.
        TITLE_MAX_LENGTH_MAX (int): The longest title limit accepted.
        feature_label (str): The label of a feature.
        families (Dict[str, List[str]]): The component labels each feature family allows (the family matrix).
        components (List[str]): The component labels, one per ticket.
        title_pattern (str): A ticket title, its ``label`` group being the component.
        title_max_length (int): The longest ticket title, in characters.
        ticket_sections (List[str]): The level-2 sections of a ticket's body, in order.
        feature_sections (List[str]): The level-2 sections of a feature's body, in order.
        implementation_bullets (List[str]): The bold bullets of a ticket's Implementation section.
        acceptance_pattern (str): One acceptance criterion line, its ``id`` group being ``AC<n>``.
        tests_columns (List[str]): The columns of the Tests table.
        references_columns (List[str]): The columns of the References table.
        reference_kinds (Dict[str, ReferenceKind]): The kinds of reference, by name.
        required_reference_kinds (Dict[str, str]): The kind of reference each component needs at least one of.
        permalink (str): The template of a permalink, with ``{repository}``, ``{sha}`` and ``{path}``.
        permalink_pattern (str): A permalink, with the groups ``sha`` and ``path``.
        repository_link_pattern (str): Any link to a file or folder of the repository, pinned or not.
        pinned_prefixes (List[str]): The relative links ``pin-links`` turns into permalinks.
        type_labels (Dict[str, str]): The label of each ticket type.
        type_kinds (Dict[str, str]): The board Kind of each ticket type.
        default_type (str): The type of a ticket when none is given.
        priority_labels (Dict[str, str]): The label of each priority.
        priority_options (Dict[str, str]): The board Priority of each priority.
        default_priority (str): The priority when none is given.
        feature_kind (str): The board Kind of a feature.
        new_issue_statuses (List[str]): The board statuses a new issue may start in, the first by default.
        comment_marker (str): The first line of the issues workflow's comment.
        empty_form_answer (str): What an issue form writes for a field left empty.

    Notes:
        - **The family matrix is the heart of GIT-10**: a feature carries exactly one family label, and each of its
          tickets carries exactly one component label that the family allows.
        - ``HARNESS`` and ``SPECS`` are both a family and a component: an issue is a feature by its
          ``feature_label``, never by them.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEIssueRulesUnreadable
    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]
    REPOSITORY_SLOT: ClassVar[str] = "{repository}"
    PATTERN_GROUPS: ClassVar[Dict[str, Tuple[str, ...]]] = {
        "title_pattern": ("label",),
        "acceptance_pattern": ("id",),
        "permalink_pattern": ("sha", "path"),
        "repository_link_pattern": (),
    }
    TITLE_MAX_LENGTH_MIN: ClassVar[int] = 20
    TITLE_MAX_LENGTH_MAX: ClassVar[int] = 256

    feature_label: str = Field(description="The label of a feature.", examples=["feature"])
    families: Dict[str, List[str]] = Field(
        description="The component labels each feature family allows.", examples=[{"PRODUCT": ["BACKEND"]}]
    )
    components: List[str] = Field(description="The component labels, one per ticket.", examples=[["BACKEND"]])
    title_pattern: str = Field(description="A ticket title, its label group being the component.")
    title_max_length: int = Field(default=79, description="The longest ticket title, in characters.", examples=[79])
    ticket_sections: List[str] = Field(description="The level-2 sections of a ticket's body, in order.")
    feature_sections: List[str] = Field(description="The level-2 sections of a feature's body, in order.")
    implementation_bullets: List[str] = Field(description="The bold bullets of a ticket's Implementation section.")
    acceptance_pattern: str = Field(description="One acceptance criterion line, its id group being AC<n>.")
    tests_columns: List[str] = Field(description="The columns of the Tests table.")
    references_columns: List[str] = Field(description="The columns of the References table.")
    reference_kinds: Dict[str, ReferenceKind] = Field(description="The kinds of reference, by name.")
    required_reference_kinds: Dict[str, str] = Field(
        description="The kind of reference each component needs at least one of.", examples=[{"BACKEND": "spec"}]
    )
    permalink: str = Field(description="The template of a permalink, with {repository}, {sha} and {path}.")
    permalink_pattern: str = Field(description="A permalink, with the groups sha and path.")
    repository_link_pattern: str = Field(description="Any link to a file or folder of the repository.")
    pinned_prefixes: List[str] = Field(description="The relative links pin-links turns into permalinks.")
    type_labels: Dict[str, str] = Field(description="The label of each ticket type.")
    type_kinds: Dict[str, str] = Field(description="The board Kind of each ticket type.")
    default_type: str = Field(description="The type of a ticket when none is given.", examples=["feature"])
    priority_labels: Dict[str, str] = Field(description="The label of each priority.")
    priority_options: Dict[str, str] = Field(description="The board Priority of each priority.")
    default_priority: str = Field(description="The priority when none is given.", examples=["medium"])
    feature_kind: str = Field(description="The board Kind of a feature.", examples=["Feature"])
    new_issue_statuses: List[str] = Field(description="The board statuses a new issue may start in.")
    comment_marker: str = Field(description="The first line of the issues workflow's comment.")
    empty_form_answer: str = Field(description="What an issue form writes for a field left empty.")

    @field_validator(
        "feature_label",
        "permalink",
        "default_type",
        "default_priority",
        "feature_kind",
        "comment_marker",
        "empty_form_answer",
        mode="before",
    )
    def validate_text(cls, value: JsonValue) -> JsonValue:
        """Validate the label, the link template, the defaults, the Kind, the marker and the empty answer.

        Args:
            value (JsonValue): The raw text.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEIssueRulesInvalidText: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEIssueRulesInvalidText(
                f"Invalid text: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator(
        "components",
        "ticket_sections",
        "feature_sections",
        "implementation_bullets",
        "tests_columns",
        "references_columns",
        "pinned_prefixes",
        "new_issue_statuses",
        mode="before",
    )
    def validate_list(cls, value: JsonValue) -> JsonValue:
        """Validate the lists of labels, sections, bullets, columns, prefixes and statuses.

        Args:
            value (JsonValue): The raw list.

        Returns:
            JsonValue: The list.

        Raises:
            SEIssueRulesInvalidList: When the value is not a non-empty list of non-empty strings.
        """
        if (
            not isinstance(value, list)
            or not value
            or not all(isinstance(item, str) and item.strip() for item in value)
        ):
            raise SEIssueRulesInvalidList(
                f"Invalid list: {value!r}. "  # noqa: E501
                "Must be a non-empty list of non-empty strings."
            )
        return value

    @field_validator(
        "title_pattern", "acceptance_pattern", "permalink_pattern", "repository_link_pattern", mode="before"
    )
    def validate_pattern(cls, value: JsonValue, info: ValidationInfo) -> JsonValue:
        """Validate the regular expressions.

        Args:
            value (JsonValue): The raw regular expression.
            info (ValidationInfo): Which field is validated.

        Returns:
            JsonValue: The regular expression.

        Raises:
            SEIssueRulesInvalidPattern: When the value does not compile, once ``{repository}`` is filled in, or lacks
                one of the named groups its field needs.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEIssueRulesInvalidPattern(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                "Must be a non-empty regular expression."
            )
        try:
            compiled = re.compile(value.replace(cls.REPOSITORY_SLOT, re.escape("owner/name")))
        except re.error as error:
            raise SEIssueRulesInvalidPattern(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                f"It does not compile: {error}."
            ) from error
        missing = [group for group in cls.PATTERN_GROUPS[str(info.field_name)] if group not in compiled.groupindex]
        if missing:
            raise SEIssueRulesInvalidPattern(
                f"Invalid {info.field_name}: {value!r}. "  # noqa: E501
                f"Must define the named groups {', '.join(missing)}."
            )
        return value

    @field_validator("title_max_length", mode="before")
    def validate_title_max_length(cls, value: JsonValue) -> JsonValue:
        """Validate ``title_max_length``.

        Args:
            value (JsonValue): The raw length, or ``None``.

        Returns:
            JsonValue: The length, the default for ``None``.

        Raises:
            SEIssueRulesInvalidLength: When the value is not a whole number in the bounds.
        """
        if value is None:
            return cls.model_fields["title_max_length"].get_default(call_default_factory=True)
        if isinstance(value, bool) or not isinstance(value, int):
            raise SEIssueRulesInvalidLength(
                f"Invalid title_max_length: {value!r}. "  # noqa: E501
                "Must be a whole number of characters."
            )
        if not cls.TITLE_MAX_LENGTH_MIN <= value <= cls.TITLE_MAX_LENGTH_MAX:
            raise SEIssueRulesInvalidLength(
                f"Invalid title_max_length: {value}. "  # noqa: E501
                f"Must be in [{cls.TITLE_MAX_LENGTH_MIN}, {cls.TITLE_MAX_LENGTH_MAX}]."
            )
        return value

    @field_validator("families", mode="before")
    def validate_families(cls, value: JsonValue) -> JsonValue:
        """Validate ``families``.

        Args:
            value (JsonValue): The raw matrix.

        Returns:
            JsonValue: The matrix.

        Raises:
            SEIssueRulesInvalidFamilies: When the value is not a non-empty mapping of family labels to non-empty lists
                of component labels.
        """
        if (
            not isinstance(value, dict)
            or not value
            or not all(
                isinstance(components, list)
                and components
                and all(isinstance(component, str) and component.strip() for component in components)
                for components in value.values()
            )
        ):
            raise SEIssueRulesInvalidFamilies(
                f"Invalid families: {value!r}. "  # noqa: E501
                "Must map each family label to the non-empty list of the component labels it allows."
            )
        return value

    @field_validator(
        "required_reference_kinds", "type_labels", "type_kinds", "priority_labels", "priority_options", mode="before"
    )
    def validate_mapping(cls, value: JsonValue) -> JsonValue:
        """Validate the mappings of names to kinds, labels and board options.

        Args:
            value (JsonValue): The raw mapping.

        Returns:
            JsonValue: The mapping.

        Raises:
            SEIssueRulesInvalidMapping: When the value is not a non-empty mapping of names to non-empty strings.
        """
        if (
            not isinstance(value, dict)
            or not value
            or not all(isinstance(item, str) and item.strip() for item in value.values())
        ):
            raise SEIssueRulesInvalidMapping(
                f"Invalid mapping: {value!r}. "  # noqa: E501
                "Must map each name to a non-empty string."
            )
        return value

    @field_validator("reference_kinds", mode="before")
    def validate_reference_kinds(cls, value: JsonValue) -> JsonValue:
        """Validate ``reference_kinds``.

        Args:
            value (JsonValue): The raw kinds.

        Returns:
            JsonValue: The kinds.

        Raises:
            SEIssueRulesInvalidReferenceKinds: When the value is not a non-empty mapping of names to kinds.
        """
        if (
            not isinstance(value, dict)
            or not value
            or not all(isinstance(item, (dict, ReferenceKind)) for item in value.values())
        ):
            raise SEIssueRulesInvalidReferenceKinds(
                f"Invalid reference_kinds: {value!r}. "  # noqa: E501
                "Must map each kind name to its paths and patterns."
            )
        return value

    @model_validator(mode="after")
    def validate_consistency(self) -> IssueRules:
        """Check that the rules agree with each other.

        Returns:
            IssueRules: The rules.

        Raises:
            SEIssueRulesInconsistent: When a family allows an unknown component, a component has no required kind or
                an unknown one, the types or the priorities differ between their labels and their board options, or
                a default is not one of them.
        """
        unknown = sorted({item for items in self.families.values() for item in items} - set(self.components))
        if unknown:
            raise SEIssueRulesInconsistent(
                f"The families allow unknown components: {', '.join(unknown)}. "  # noqa: E501
                "Every component of a family must be in components."
            )
        if set(self.required_reference_kinds) != set(self.components) or not set(
            self.required_reference_kinds.values()
        ) <= set(self.reference_kinds):
            raise SEIssueRulesInconsistent(
                f"Invalid required_reference_kinds: {self.required_reference_kinds!r}. "  # noqa: E501
                "Must give every component one of the reference kinds."
            )
        if set(self.type_labels) != set(self.type_kinds) or self.default_type not in self.type_labels:
            raise SEIssueRulesInconsistent(
                f"The types differ: {sorted(self.type_labels)} against {sorted(self.type_kinds)}. "  # noqa: E501
                "type_labels and type_kinds must name the same types, default_type among them."
            )
        if set(self.priority_labels) != set(self.priority_options) or self.default_priority not in self.priority_labels:
            raise SEIssueRulesInconsistent(
                f"The priorities differ: {sorted(self.priority_labels)} against {sorted(self.priority_options)}. "  # noqa: E501
                "priority_labels and priority_options must name the same priorities, default_priority among them."
            )
        return self

    ############################
    # Publicly Exposed Methods #
    ############################

    def families_of(self, labels: List[str]) -> List[str]:
        """Give the family labels among an issue's labels.

        Args:
            labels (List[str]): The issue's labels.

        Returns:
            List[str]: Its family labels, in the issue's order.
        """
        return [label for label in labels if label in self.families]

    def components_of(self, labels: List[str]) -> List[str]:
        """Give the component labels among an issue's labels.

        Args:
            labels (List[str]): The issue's labels.

        Returns:
            List[str]: Its component labels, in the issue's order.
        """
        return [label for label in labels if label in self.components]

    def allows(self, family: str, component: str) -> bool:
        """Tell whether a feature family holds tickets of a component.

        Args:
            family (str): The family label.
            component (str): The component label.

        Returns:
            bool: ``True`` when the matrix allows it.
        """
        return component in self.families.get(family, [])

    def kind_of(self, path: str) -> Optional[str]:
        """Give the kind of reference a repository path is.

        Args:
            path (str): The path, relative to the repository root.

        Returns:
            Optional[str]: The kind's name, ``None`` when no kind covers the path.
        """
        return next((name for name, kind in self.reference_kinds.items() if kind.covers(path)), None)

    def permalink_of(self, repository: str, sha: str, path: str) -> str:
        """Build the permalink of a path at a commit.

        Args:
            repository (str): The repository, ``owner/name``.
            sha (str): The full commit hash.
            path (str): The path, relative to the repository root.

        Returns:
            str: The permalink.
        """
        return self.permalink.format(repository=repository, sha=sha, path=path)

    def permalink_regex(self, repository: str) -> Pattern[str]:
        """Give the regular expression of a permalink into one repository.

        Args:
            repository (str): The repository, ``owner/name``.

        Returns:
            Pattern[str]: The compiled pattern, with the groups ``sha`` and ``path``.
        """
        return re.compile(self.permalink_pattern.replace(self.REPOSITORY_SLOT, re.escape(repository)))

    def repository_link_regex(self, repository: str) -> Pattern[str]:
        """Give the regular expression of any link to a file or folder of one repository.

        Args:
            repository (str): The repository, ``owner/name``.

        Returns:
            Pattern[str]: The compiled pattern.
        """
        return re.compile(self.repository_link_pattern.replace(self.REPOSITORY_SLOT, re.escape(repository)))

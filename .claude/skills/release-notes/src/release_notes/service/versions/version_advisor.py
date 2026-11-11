from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional, Tuple

# First-party imports
from harness_core.git.git_repository import GitRepository
from release_notes.models.enums import VersionBump
from release_notes.models.fragments.changelog_fragment import ChangelogFragment
from release_notes.models.versions.exceptions import SEInvalidSemanticVersionException
from release_notes.models.versions.semantic_version import SemanticVersion
from release_notes.service.exceptions import SEFragmentsRefusedError
from release_notes.service.fragments.fragment_reader import FragmentReader


class VersionAdvisor:
    """Suggests the next version from the last version tag and the changelog fragments.

    Attributes:
        TAG_PATTERN (str): The ``git tag --list`` pattern of version tags.
        TAG_PREFIX (str): What a version tag starts with.
        RANKS (Dict[VersionBump, int]): How bumps compare, the highest one winning.
        BREAKING (str): The label of a fragment that starts with the breaking marker.
        repository (GitRepository): The repository, read for its tags.
        reader (FragmentReader): Reads the fragments and their types.
        logger (Logger): Logger instance.

    Notes:
        - The base is the highest ``v<x.y.z>`` tag, or ``0.0.0`` when there is none. Other tags are ignored.
        - A fragment bumps what its type bumps, and a fragment that starts with the breaking marker bumps major.
        - **While the major version is 0, a major bump bumps the minor version instead**: in semver 0.x anything may
          change, and ``1.0.0`` is the owner's decision, never a fragment's.
    """

    TAG_PATTERN: ClassVar[str] = "v*"
    TAG_PREFIX: ClassVar[str] = "v"
    RANKS: ClassVar[Dict[VersionBump, int]] = {VersionBump.PATCH: 0, VersionBump.MINOR: 1, VersionBump.MAJOR: 2}
    BREAKING: ClassVar[str] = "breaking"

    def __init__(self, repository: GitRepository, reader: FragmentReader, logger: Optional[Logger] = None) -> None:
        """Set the repository and the fragment reader.

        Args:
            repository (GitRepository): The repository, read for its tags.
            reader (FragmentReader): Reads the fragments and their types.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.reader = reader
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _last_tag(self) -> Optional[SemanticVersion]:
        """Find the highest version tag.

        Returns:
            Optional[SemanticVersion]: Its version, or ``None`` when no tag is ``v<x.y.z>``.
        """
        versions: List[SemanticVersion] = []
        for tag in self.repository.tags(self.TAG_PATTERN):
            try:
                versions.append(SemanticVersion.parse(tag.removeprefix(self.TAG_PREFIX)))
            except SEInvalidSemanticVersionException:
                self.logger.debug("The tag %s is not a version tag.", tag)
        return max(versions, key=lambda version: version.key) if versions else None

    def _bump(self, fragment: ChangelogFragment) -> Tuple[VersionBump, str]:
        """Give what one fragment bumps.

        Args:
            fragment (ChangelogFragment): The fragment.

        Returns:
            Tuple[VersionBump, str]: The bump, and its label in the reason.
        """
        if fragment.starts_with(self.reader.catalog.breaking_marker):
            return VersionBump.MAJOR, self.BREAKING
        kind = self.reader.catalog.named(fragment.type_name)
        bump = kind.bump if kind is not None else VersionBump.PATCH
        return bump, bump.value

    ############################
    # Publicly Exposed Methods #
    ############################

    def fragments(self) -> List[ChangelogFragment]:
        """Read the fragments a release would use.

        Returns:
            List[ChangelogFragment]: The fragments, by file name.

        Raises:
            SEFragmentsRefusedError: When there is no fragment, or one of them is invalid.
        """
        fragments, problems = self.reader.read_all()
        if problems:
            self.logger.error("%d fragments are invalid.", len(problems))
            raise SEFragmentsRefusedError(
                "Some changelog fragments are invalid. "  # noqa: E501
                f"Fix them first: {' '.join(problems)}"
            )
        if not fragments:
            self.logger.error("changelog.d holds no fragment.")
            raise SEFragmentsRefusedError(f"No fragment in {self.reader.FOLDER}/: nothing to release.")
        return fragments

    def suggest(self) -> Tuple[SemanticVersion, str]:
        """Suggest the next version.

        Returns:
            Tuple[SemanticVersion, str]: The version, and the reason in one sentence or two.

        Raises:
            SEFragmentsRefusedError: When there is no fragment, or one of them is invalid.
        """
        fragments = self.fragments()
        tagged = self._last_tag()
        base = tagged if tagged is not None else SemanticVersion()
        labelled = [(fragment, *self._bump(fragment)) for fragment in fragments]
        bump = max((item[1] for item in labelled), key=lambda found: self.RANKS[found])
        origin = f"{self.TAG_PREFIX}{base}" if tagged is not None else f"{base} (no v<x.y.z> tag yet)"
        details = ", ".join(f"{fragment.file_name} ({label})" for fragment, _, label in labelled)
        reason = f"{bump.value} bump from {origin}: {details}."
        applied = bump
        if bump == VersionBump.MAJOR and base.major == 0:
            applied = VersionBump.MINOR
            reason += " While the major version is 0, a major bump bumps the minor version instead (semver 0.x)."
        version = base.bumped(applied)
        self.logger.info("Suggested %s from %s and %d fragments.", version, origin, len(fragments))
        return version, reason

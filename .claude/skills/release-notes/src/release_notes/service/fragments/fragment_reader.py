from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.fragments.changelog_fragment import ChangelogFragment
from release_notes.storage.files.text_files import TextFiles


class FragmentReader:
    """Reads the changelog fragments of ``changelog.d/`` and says what is wrong with each one.

    Attributes:
        FOLDER (str): The fragments' folder.
        README (str): The folder's README, which is not a fragment.
        NAME_PATTERN (re.Pattern[str]): A fragment's file name, ``GH-<n>.<type>.md``.
        files (TextFiles): The repository's files.
        catalog (ChangelogTypeCatalog): The fragment types.
        logger (Logger): Logger instance.

    Notes:
        A problem is returned as a line for the person rather than raised, so that one run lists them all.
    """

    FOLDER: ClassVar[str] = "changelog.d"
    README: ClassVar[str] = "README.md"
    NAME_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^(?P<ticket>GH-\d+)\.(?P<type>[^.]+)\.md$")

    def __init__(self, files: TextFiles, catalog: ChangelogTypeCatalog, logger: Optional[Logger] = None) -> None:
        """Set the files and the types.

        Args:
            files (TextFiles): The repository's files.
            catalog (ChangelogTypeCatalog): The fragment types.
            logger (Optional[Logger]): Logger instance.
        """
        self.files = files
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def names(self) -> List[str]:
        """List the files of ``changelog.d/`` other than its README.

        Returns:
            List[str]: The file names, sorted.
        """
        return [name for name in self.files.names(self.FOLDER) if name != self.README]

    def path(self, name: str) -> str:
        """Give a fragment's path relative to the repository root.

        Args:
            name (str): The file name.

        Returns:
            str: The path, such as ``changelog.d/GH-12.added.md``.
        """
        return f"{self.FOLDER}/{name}"

    def read(self, name: str) -> Tuple[Optional[ChangelogFragment], List[str]]:
        """Read one fragment.

        Args:
            name (str): The file name in ``changelog.d/``.

        Returns:
            Tuple[Optional[ChangelogFragment], List[str]]: The fragment and no problem, or no fragment and its
            problem.
        """
        path = self.path(name)
        match = self.NAME_PATTERN.match(name)
        if match is None:
            return None, [f"{path}: not a fragment name, expected GH-<n>.<type>.md."]
        if self.catalog.named(match.group("type")) is None:
            return None, [
                f"{path}: unknown type {match.group('type')}, expected one of {', '.join(self.catalog.names())}."
            ]
        lines = [line.strip() for line in self.files.read(path).splitlines() if line.strip()]
        if not ChangelogFragment.LINES_MIN <= len(lines) <= ChangelogFragment.LINES_MAX:
            return None, [
                f"{path}: {len(lines)} non-empty lines, expected {ChangelogFragment.LINES_MIN} to"
                f" {ChangelogFragment.LINES_MAX}."
            ]
        self.logger.debug("Read the fragment %s.", name)
        return ChangelogFragment(ticket=match.group("ticket"), type_name=match.group("type"), lines=lines), []

    def read_all(self) -> Tuple[List[ChangelogFragment], List[str]]:
        """Read every fragment.

        Returns:
            Tuple[List[ChangelogFragment], List[str]]: The valid fragments, by file name, and the problems of the
            others.
        """
        fragments: List[ChangelogFragment] = []
        problems: List[str] = []
        for name in self.names():
            fragment, found = self.read(name)
            problems.extend(found)
            if fragment is not None:
                fragments.append(fragment)
        self.logger.info("Read %d fragments, %d with a problem.", len(fragments), len(problems))
        return fragments, problems

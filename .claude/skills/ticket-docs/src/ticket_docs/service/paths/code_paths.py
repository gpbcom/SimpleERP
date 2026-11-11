from __future__ import annotations

# Standard library imports
from fnmatch import fnmatch
from logging import Logger, getLogger
from typing import ClassVar, Dict, FrozenSet, Iterable, List, Optional

# First-party imports
from harness_core.models.git.change_status import ChangeStatus
from ticket_docs.models.checks.folder_rules import FolderRules


class CodePaths:
    """Tells production code and tests apart, by their path in the repository.

    Attributes:
        FOLDER_MARK (str): The end of a pattern that names a folder.
        NEW (FrozenSet[ChangeStatus]): The statuses of a file that did not exist before.
        rules (FolderRules): The production and test patterns.
        logger (Logger): Logger instance.

    Notes:
        - A folder pattern (``services/*/src/``) matches every path under it, from the repository root. Another
          pattern (``test_*.py``) matches the file name.
        - **A test inside a production folder is a test**, such as ``packages/x/tests/test_y.py``.
        - A package marker (``marker_files``, ``__init__.py``) is never production code: ``AGENT.md`` keeps them to
          imports and ``__all__``, and a tests-only commit needs them for its tests to be collected (TEST-7).
    """

    FOLDER_MARK: ClassVar[str] = "/"
    NEW: ClassVar[FrozenSet[ChangeStatus]] = frozenset({ChangeStatus.ADDED, ChangeStatus.UNTRACKED})

    def __init__(self, rules: FolderRules, logger: Optional[Logger] = None) -> None:
        """Set the patterns.

        Args:
            rules (FolderRules): The production and test patterns.
            logger (Optional[Logger]): Logger instance.
        """
        self.rules = rules
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _matches(self, path: str, patterns: List[str]) -> bool:
        """Tell whether a path matches one of the patterns.

        Args:
            path (str): The path, relative to the repository root.
            patterns (List[str]): The patterns.

        Returns:
            bool: ``True`` when one matches.
        """
        name = path.rsplit("/", 1)[-1]
        return any(
            fnmatch(path, f"{pattern}*") if pattern.endswith(self.FOLDER_MARK) else fnmatch(name, pattern)
            for pattern in patterns
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def is_test(self, path: str) -> bool:
        """Tell whether a path is a test file.

        Args:
            path (str): The path, relative to the repository root.

        Returns:
            bool: ``True`` for a test.
        """
        return self._matches(path, self.rules.test_paths)

    def is_production(self, path: str) -> bool:
        """Tell whether a path is production code.

        Args:
            path (str): The path, relative to the repository root.

        Returns:
            bool: ``True`` for production code that is not a test.
        """
        if path.rsplit("/", 1)[-1] in self.rules.marker_files:
            self.logger.debug("%s is a package marker, not production code.", path)
            return False
        return self._matches(path, self.rules.production_paths) and not self.is_test(path)

    def production(self, paths: Iterable[str]) -> List[str]:
        """Pick out the production code of a list of paths.

        Args:
            paths (Iterable[str]): The paths, relative to the repository root.

        Returns:
            List[str]: The production paths, sorted.
        """
        return sorted(path for path in paths if self.is_production(path))

    def new_tests(self, changes: Dict[str, ChangeStatus]) -> List[str]:
        """Pick out the test files a change adds.

        Args:
            changes (Dict[str, ChangeStatus]): How each path changed.

        Returns:
            List[str]: The added or untracked test paths, sorted.
        """
        return sorted(path for path, status in changes.items() if status in self.NEW and self.is_test(path))

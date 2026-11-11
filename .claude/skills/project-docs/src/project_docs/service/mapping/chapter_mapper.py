from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional

# First-party imports
from project_docs.models.catalogs.doc_map import DocMap


class ChapterMapper:
    """Maps changed paths to the documentation chapters they concern, with the doc map's rules.

    Attributes:
        TOKEN_PATTERN (re.Pattern[str]): A placeholder, a ``*`` or a ``?`` in a glob.
        doc_map (DocMap): The rules.
        compiled (List[Tuple[List[re.Pattern[str]], List[str]]]): Each rule's globs as regular expressions, and its
            chapters.
        logger (Logger): Logger instance.

    Notes:
        - The globs follow ``fnmatch`` on the whole path: ``*`` crosses ``/``, ``?`` is one character, and every
          other character, ``[`` included, is literal.
        - ``{service}`` or ``{frontend}`` matches one folder name, which replaces the same placeholder in the
          chapters.
        - **The first matching rule wins**, so a specific rule sits above a general one. A path no rule matches
          takes the ``always`` chapters, and a rule with no chapter means no documentation impact.
    """

    TOKEN_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"\{(?P<name>[a-z_]+)\}|(?P<star>\*)|(?P<one>\?)")

    def __init__(self, doc_map: DocMap, logger: Optional[Logger] = None) -> None:
        """Compile the rules.

        Args:
            doc_map (DocMap): The rules.
            logger (Optional[Logger]): Logger instance.
        """
        self.doc_map = doc_map
        self.logger = logger if logger else getLogger(__name__)
        self.compiled = [([self._regex(glob) for glob in rule.paths], rule.chapters) for rule in doc_map.rules]

    ############################
    # Internal Helpers Methods #
    ############################

    def _regex(self, glob: str) -> re.Pattern[str]:
        """Turn a glob into a regular expression on the whole path.

        Args:
            glob (str): The glob, such as ``services/{service}/src/*/api/*``.

        Returns:
            re.Pattern[str]: The expression, each placeholder a named group.
        """
        parts: List[str] = []
        position = 0
        for match in self.TOKEN_PATTERN.finditer(glob):
            parts.append(re.escape(glob[position : match.start()]))
            if match.group("name"):
                parts.append(f"(?P<{match.group('name')}>[^/]+)")
            elif match.group("star"):
                parts.append(".*")
            else:
                parts.append(".")
            position = match.end()
        parts.append(re.escape(glob[position:]))
        return re.compile("".join(parts) + r"\Z", re.DOTALL)

    ############################
    # Publicly Exposed Methods #
    ############################

    def chapters(self, path: str) -> List[str]:
        """Give the chapters one path concerns.

        Args:
            path (str): The path relative to the repository root.

        Returns:
            List[str]: The chapters of the first rule that matches, placeholders filled, or the ``always`` chapters.
        """
        for patterns, chapters in self.compiled:
            for pattern in patterns:
                match = pattern.match(path)
                if match:
                    filled = []
                    for chapter in chapters:
                        for name, value in match.groupdict().items():
                            chapter = chapter.replace(f"{{{name}}}", value)
                        filled.append(chapter)
                    return filled
        return list(self.doc_map.always)

    def map(self, paths: List[str]) -> Dict[str, List[str]]:
        """Gather the paths under each chapter they concern.

        Args:
            paths (List[str]): The changed paths.

        Returns:
            Dict[str, List[str]]: Each chapter, sorted, with its paths, sorted.
        """
        mapping: Dict[str, List[str]] = {}
        for path in sorted(set(paths)):
            for chapter in self.chapters(path):
                mapping.setdefault(chapter, []).append(path)
        self.logger.info("%d changed paths concern %d chapters.", len(set(paths)), len(mapping))
        return {chapter: mapping[chapter] for chapter in sorted(mapping)}

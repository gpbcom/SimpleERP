from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, Tuple


class DocumentFiles:
    """Reads the project documentation and the folders it describes, in one repository.

    Attributes:
        README (str): The root README, a document of its own.
        FOLDERS (Tuple[str, ...]): The documentation folders, read recursively.
        root (Path): The repository's top-level folder.
        logger (Logger): Logger instance.

    Notes:
        - Paths go in and out relative to the repository root, with forward slashes, as git and the doc map write
          them.
        - The folders are DOC-2's: ``docs/specs/`` is input and ticket folders are not project documentation, so
          neither is read.
    """

    README: ClassVar[str] = "README.md"
    FOLDERS: ClassVar[Tuple[str, ...]] = ("docs/functional", "docs/technical")

    def __init__(self, root: Path, logger: Optional[Logger] = None) -> None:
        """Set the repository.

        Args:
            root (Path): The repository's top-level folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.root = root
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def documents(self) -> List[str]:
        """List the project documentation.

        Returns:
            List[str]: ``README.md`` when it exists, then every Markdown file of the documentation folders, sorted.
        """
        found = [self.README] if self.exists(self.README) else []
        for folder in self.FOLDERS:
            found.extend(sorted(path.relative_to(self.root).as_posix() for path in (self.root / folder).rglob("*.md")))
        self.logger.debug("Found %d documents.", len(found))
        return found

    def exists(self, path: str) -> bool:
        """Tell whether a file or folder exists.

        Args:
            path (str): The path relative to the repository root.

        Returns:
            bool: ``True`` when it exists.
        """
        return (self.root / path).exists()

    def read(self, path: str) -> str:
        """Read a text file.

        Args:
            path (str): The path relative to the repository root.

        Returns:
            str: The text, empty when the file does not exist or cannot be read.
        """
        try:
            return (self.root / path).read_text(encoding="utf-8")
        except FileNotFoundError:
            self.logger.debug("%s does not exist.", path)
            return ""
        except (OSError, UnicodeDecodeError) as error:
            self.logger.warning("%s cannot be read: %s.", path, type(error).__name__)
            return ""

    def folders(self, parent: str) -> List[str]:
        """List the sub-folders of a folder, such as the services.

        Args:
            parent (str): The folder relative to the repository root, such as ``services``.

        Returns:
            List[str]: The names of its visible sub-folders, sorted, none when it does not exist.
        """
        folder = self.root / parent
        if not folder.is_dir():
            return []
        return sorted(item.name for item in folder.iterdir() if item.is_dir() and not item.name.startswith("."))

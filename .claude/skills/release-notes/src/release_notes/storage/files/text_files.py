from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional


class TextFiles:
    """Reads and writes the text files of one folder, such as the repository's CHANGELOG.md and fragments.

    Attributes:
        root (Path): The folder the paths are relative to.
        logger (Logger): Logger instance.

    Notes:
        Paths go in relative to the root, with forward slashes. Deleting a file leaves its ``git rm`` to the person
        or the skill, so the deletion is staged with the rest of the release commit.
    """

    def __init__(self, root: Path, logger: Optional[Logger] = None) -> None:
        """Set the folder.

        Args:
            root (Path): The folder the paths are relative to.
            logger (Optional[Logger]): Logger instance.
        """
        self.root = root
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def exists(self, path: str) -> bool:
        """Tell whether a file exists.

        Args:
            path (str): The path relative to the root.

        Returns:
            bool: ``True`` when it exists.
        """
        return (self.root / path).is_file()

    def read(self, path: str) -> str:
        """Read a text file.

        Args:
            path (str): The path relative to the root.

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

    def write(self, path: str, text: str) -> None:
        """Write a text file, replacing it.

        Args:
            path (str): The path relative to the root.
            text (str): The text.
        """
        (self.root / path).write_text(text, encoding="utf-8")
        self.logger.info("Wrote %s.", path)

    def delete(self, path: str) -> None:
        """Delete a file.

        Args:
            path (str): The path relative to the root.
        """
        (self.root / path).unlink()
        self.logger.info("Deleted %s.", path)

    def names(self, folder: str) -> List[str]:
        """List the files of a folder.

        Args:
            folder (str): The folder relative to the root.

        Returns:
            List[str]: The file names, sorted, none when the folder does not exist.
        """
        directory = self.root / folder
        if not directory.is_dir():
            return []
        return sorted(item.name for item in directory.iterdir() if item.is_file())

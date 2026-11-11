from __future__ import annotations

# Standard library imports
import os
import tempfile
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional


class TextFiles:
    """Reads and writes the watcher's text files.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - **A file is replaced at once** (a temporary file in the same folder, then ``os.replace``), so that a reader
          never sees half of one: the timer run and the commands a session sends share the files.
        - The parent folders are created when a file is written.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def read(self, path: Path) -> Optional[str]:
        """Read a text file.

        Args:
            path (Path): The file.

        Returns:
            Optional[str]: Its content, ``None`` when it does not exist.
        """
        if not path.exists():
            self.logger.debug("%s does not exist yet.", path)
            return None
        return path.read_text(encoding="utf-8")

    def write(self, path: Path, content: str) -> None:
        """Replace a text file at once.

        Args:
            path (Path): The file.
            content (str): Its new content.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
        os.replace(temporary, path)
        self.logger.debug("Wrote %s (%d characters).", path, len(content))

    def append_line(self, path: Path, line: str) -> None:
        """Add one line at the end of a text file.

        Args:
            path (Path): The file.
            line (str): The line, without its end of line.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")

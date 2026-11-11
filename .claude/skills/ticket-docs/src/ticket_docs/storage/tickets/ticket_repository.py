from __future__ import annotations

# Standard library imports
import shutil
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional


class TicketRepository:
    """The ticket folders under ``docs/tickets/``, and their index.

    Attributes:
        INDEX (str): The index of every run of every ticket, at the root.
        ARCHIVE_FORMAT (str): The archive format of a ticket folder.
        root (Path): The ``docs/tickets`` folder.
        logger (Logger): Logger instance.
    """

    INDEX: ClassVar[str] = "README.md"
    ARCHIVE_FORMAT: ClassVar[str] = "zip"

    def __init__(self, root: Path, logger: Optional[Logger] = None) -> None:
        """Set the tickets folder.

        Args:
            root (Path): The ``docs/tickets`` folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.root = root
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def folder(self, key: str) -> Path:
        """Give a ticket's folder.

        Args:
            key (str): The ticket.

        Returns:
            Path: ``<root>/<key>``, which may not exist.
        """
        return self.root / key

    def exists(self, key: str) -> bool:
        """Tell whether a ticket has a folder.

        Args:
            key (str): The ticket.

        Returns:
            bool: ``True`` when its folder exists.
        """
        return self.folder(key).is_dir()

    def read(self, key: str, relative: str) -> Optional[str]:
        """Read a file of a ticket folder.

        Args:
            key (str): The ticket.
            relative (str): The file's path inside the folder.

        Returns:
            Optional[str]: The text, ``None`` when the file does not exist.
        """
        path = self.folder(key) / relative
        if not path.is_file():
            self.logger.debug("%s has no %s.", key, relative)
            return None
        return path.read_text(encoding="utf-8")

    def markdown(self, key: str) -> List[Path]:
        """List every Markdown file of a ticket folder, sub-folders included.

        Args:
            key (str): The ticket.

        Returns:
            List[Path]: The files, sorted.
        """
        return sorted(self.folder(key).rglob("*.md"))

    def index(self) -> Optional[str]:
        """Read the index of every run.

        Returns:
            Optional[str]: Its text, ``None`` when it has not been written.
        """
        path = self.root / self.INDEX
        return path.read_text(encoding="utf-8") if path.is_file() else None

    def write_index(self, text: str, output: Optional[Path] = None) -> Path:
        """Write the index of every run.

        Args:
            text (str): The index.
            output (Optional[Path]): Where to write it, the root's ``README.md`` when ``None``.

        Returns:
            Path: The file written.
        """
        path = output if output else self.root / self.INDEX
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.logger.info("Wrote the evidence index %s.", path)
        return path

    def archive(self, key: str, destination: Path) -> Path:
        """Zip a ticket folder, its files under ``<key>/``.

        Args:
            key (str): The ticket.
            destination (Path): The zip file to write.

        Returns:
            Path: The zip file.
        """
        destination.parent.mkdir(parents=True, exist_ok=True)
        base = destination.with_suffix("")
        written = shutil.make_archive(str(base), self.ARCHIVE_FORMAT, root_dir=self.root, base_dir=key)
        self.logger.info("Zipped %s into %s.", key, written)
        return Path(written)

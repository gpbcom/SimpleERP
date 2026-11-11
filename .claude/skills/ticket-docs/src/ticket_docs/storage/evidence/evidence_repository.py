from __future__ import annotations

# Standard library imports
import re
import shutil
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern

# First-party imports
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.storage.evidence.exceptions import SEEvidenceReadmeMissingError


class EvidenceRepository:
    """The evidence folders of every ticket, under ``docs/tickets/<KEY>/tests-evidences/``.

    Attributes:
        TICKET_FOLDER (Pattern[str]): A ticket folder's name, ``GH-<n>``.
        EVIDENCE_DIR (str): The evidence folder of a ticket.
        README (str): The file that describes a run.
        root (Path): The ``docs/tickets`` folder.
        logger (Logger): Logger instance.

    Notes:
        - **A folder is never overwritten**: a second run of the same check on the same day gets ``-2``, then ``-3``.
        - A run folder is named ``<where>-<YYYY-MM-DD>-<check>``. Other folders, such as ``history/``, are not runs.
    """

    TICKET_FOLDER: ClassVar[Pattern[str]] = re.compile(r"^GH-\d+$")
    EVIDENCE_DIR: ClassVar[str] = "tests-evidences"
    README: ClassVar[str] = "README.md"

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

    def tickets(self) -> List[str]:
        """List the tickets that have a folder.

        Returns:
            List[str]: The ticket keys, sorted.
        """
        if not self.root.is_dir():
            return []
        return sorted(
            path.name for path in self.root.iterdir() if path.is_dir() and self.TICKET_FOLDER.match(path.name)
        )

    def evidence_dir(self, ticket: str) -> Path:
        """Give a ticket's evidence folder.

        Args:
            ticket (str): The ticket.

        Returns:
            Path: ``<root>/<ticket>/tests-evidences``, which may not exist.
        """
        return self.root / ticket / self.EVIDENCE_DIR

    def folders(self, ticket: str) -> List[Path]:
        """List a ticket's run folders.

        Args:
            ticket (str): The ticket.

        Returns:
            List[Path]: The folders named like a run, sorted by name.
        """
        evidence = self.evidence_dir(ticket)
        if not evidence.is_dir():
            return []
        folders = [path for path in evidence.iterdir() if path.is_dir() and EvidenceRun.FOLDER_NAME.match(path.name)]
        self.logger.debug("Found %d run folders for %s.", len(folders), ticket)
        return sorted(folders)

    def read(self, folder: Path) -> EvidenceRun:
        """Read a run folder's README.

        Args:
            folder (Path): The run folder.

        Returns:
            EvidenceRun: The run.

        Raises:
            SEEvidenceReadmeMissingError: When the folder has no README.
        """
        readme = folder / self.README
        if not readme.is_file():
            self.logger.error("%s has no %s.", folder.name, self.README)
            raise SEEvidenceReadmeMissingError(f"The evidence folder {folder.name} has no {self.README}.")
        return EvidenceRun.from_readme(folder.name, readme.read_text(encoding="utf-8"))

    def create(self, ticket: str, name: str) -> Path:
        """Create a new run folder, with a suffix when the name is taken.

        Args:
            ticket (str): The ticket.
            name (str): The folder's name, ``<where>-<YYYY-MM-DD>-<check>``.

        Returns:
            Path: The new, empty folder.
        """
        evidence = self.evidence_dir(ticket)
        folder = evidence / name
        suffix = 2
        while folder.exists():
            folder = evidence / f"{name}-{suffix}"
            suffix += 1
        folder.mkdir(parents=True)
        self.logger.info("Created the evidence folder %s.", folder)
        return folder

    def write(self, folder: Path, name: str, text: str) -> Path:
        """Write a text file in a run folder.

        Args:
            folder (Path): The run folder.
            name (str): The file's name.
            text (str): Its content.

        Returns:
            Path: The file.
        """
        path = folder / name
        path.write_text(text, encoding="utf-8")
        self.logger.debug("Wrote %s in %s.", name, folder.name)
        return path

    def copy_in(self, source: Path, folder: Path, name: str) -> bool:
        """Copy a report file or folder into a run folder.

        Args:
            source (Path): The report, a file or a folder.
            folder (Path): The run folder.
            name (str): Its name in the run folder.

        Returns:
            bool: ``True`` when it was copied, ``False`` when it does not exist.
        """
        target = folder / name
        if source.is_dir():
            shutil.copytree(source, target, dirs_exist_ok=True)
        elif source.is_file():
            shutil.copy2(source, target)
        else:
            self.logger.debug("Nothing to copy at %s.", source)
            return False
        self.logger.info("Copied %s into %s.", source.name, folder.name)
        return True

    def files(self, folder: Path) -> List[str]:
        """List what a run folder holds, folders ending with a slash.

        Args:
            folder (Path): The run folder.

        Returns:
            List[str]: The names, sorted.
        """
        return sorted(f"{path.name}/" if path.is_dir() else path.name for path in folder.iterdir())

    def large_files(self, ticket: str, limit_bytes: int) -> List[Path]:
        """Find the files of a ticket's evidence over a size.

        Args:
            ticket (str): The ticket.
            limit_bytes (int): The largest size allowed.

        Returns:
            List[Path]: The files over it, sorted.
        """
        evidence = self.evidence_dir(ticket)
        if not evidence.is_dir():
            return []
        large = sorted(path for path in evidence.rglob("*") if path.is_file() and path.stat().st_size > limit_bytes)
        if large:
            self.logger.warning("%d evidence files of %s are over %d bytes.", len(large), ticket, limit_bytes)
        return large

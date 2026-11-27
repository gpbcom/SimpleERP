from __future__ import annotations

# Standard library imports
import os
import subprocess
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from erp_testing.models.postgres.exceptions import SEPostgresBinariesNotFoundError
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig


class PostgresBinaries:
    """Finds the folder that holds the PostgreSQL server binaries.

    Attributes:
        NAMES (Tuple[str, ...]): The binaries a folder must hold to be accepted.
        PG_CONFIG_TIMEOUT_S (float): How long ``pg_config`` may run, in seconds.
        config (PostgresServerConfig): The settings, whose ``search_dirs`` are searched first.
        logger (Logger): Logger instance.

    Notes:
        - The search order is each of ``search_dirs`` (itself, then its ``<version>/bin`` children, newest version
          first), then ``PATH``, then ``pg_config --bindir``.
        - **A folder missing any one of the binaries is skipped**, so a partial installation is never used.
    """

    NAMES: ClassVar[Tuple[str, ...]] = ("initdb", "pg_ctl", "pg_isready", "psql")
    PG_CONFIG_TIMEOUT_S: ClassVar[float] = 10.0

    def __init__(self, config: PostgresServerConfig, logger: Optional[Logger] = None) -> None:
        """Create the finder.

        Args:
            config (PostgresServerConfig): The settings to read the search folders from.
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        self.config = config
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _is_complete(self, folder: Path) -> bool:
        """Tell whether a folder holds all the binaries.

        Args:
            folder (Path): The folder to inspect.

        Returns:
            bool: ``True`` when each binary is an executable file of the folder.
        """
        for name in self.NAMES:
            path = folder / name
            if not path.is_file() or not os.access(path, os.X_OK):
                self.logger.debug("Folder %s lacks %s.", folder, name)
                return False
        return True

    def _version_key(self, folder: Path) -> Tuple[int, int, str]:
        """Build the sort key of a version folder, so that the newest sorts last.

        Args:
            folder (Path): A child of a search folder.

        Returns:
            Tuple[int, int, str]: Numeric names rank above others, then by number, then by name.
        """
        name = folder.name
        digits = name.split(".")[0]
        if digits.isdigit():
            return (1, int(digits), name)
        return (0, 0, name)

    def _candidates_of(self, search_dir: str) -> List[Path]:
        """List the folders to inspect for one search folder, in order.

        Args:
            search_dir (str): One entry of ``search_dirs``.

        Returns:
            List[Path]: The folder itself, then the ``<version>/bin`` children, newest version first.
        """
        root = Path(search_dir)
        candidates: List[Path] = [root]
        if root.is_dir():
            versions = sorted((child for child in root.iterdir() if child.is_dir()), key=self._version_key)
            candidates.extend(child / "bin" for child in reversed(versions))
        return candidates

    def _from_pg_config(self) -> Optional[Path]:
        """Ask ``pg_config`` where the binaries are.

        Returns:
            Optional[Path]: The folder it reports, or ``None`` when ``pg_config`` is missing or fails.
        """
        try:
            result = subprocess.run(
                ["pg_config", "--bindir"],
                capture_output=True,
                check=False,
                encoding="utf-8",
                timeout=self.PG_CONFIG_TIMEOUT_S,
            )
        except (OSError, subprocess.SubprocessError) as error:
            self.logger.debug("pg_config is not usable: %s.", type(error).__name__)
            return None
        if result.returncode != 0 or not result.stdout.strip():
            self.logger.debug("pg_config reported no folder.")
            return None
        return Path(result.stdout.strip())

    ############################
    # Publicly Exposed Methods #
    ############################

    def find(self) -> Path:
        """Find the folder that holds ``initdb``, ``pg_ctl``, ``pg_isready`` and ``psql``.

        Returns:
            Path: The first complete folder found.

        Raises:
            SEPostgresBinariesNotFoundError: If no searched place holds all the binaries.
        """
        candidates: List[Path] = []
        for search_dir in self.config.search_dirs:
            candidates.extend(self._candidates_of(search_dir))
        candidates.extend(Path(entry) for entry in os.environ.get("PATH", "").split(os.pathsep) if entry)
        for candidate in candidates:
            if self._is_complete(candidate):
                self.logger.info("Found the PostgreSQL binaries in %s.", candidate)
                return candidate
        reported = self._from_pg_config()
        if reported is not None and self._is_complete(reported):
            self.logger.info("Found the PostgreSQL binaries in %s.", reported)
            return reported
        self.logger.error("No PostgreSQL binaries were found in %d places.", len(candidates))
        raise SEPostgresBinariesNotFoundError(
            f"No folder holds {', '.join(self.NAMES)}. "  # noqa: E501
            f"Searched {self.config.search_dirs!r}, PATH and pg_config."
        )

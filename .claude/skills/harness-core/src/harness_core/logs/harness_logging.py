from __future__ import annotations

# Standard library imports
from logging import DEBUG, Formatter, Logger, getLogger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import ClassVar, Optional


class HarnessLogging:
    """Where the harness tools write their logs.

    Attributes:
        FORMAT (str): The layout of a log line.
        MAX_BYTES (int): The size at which a log file rotates.
        BACKUP_COUNT (int): How many rotated files are kept.
        tool (str): The tool's name, which names its log file.
        state_dir (Path): The folder of the log files.

    Notes:
        - **A hook's standard output is read by Claude Code as its answer**, so the tools log to a file and never to
          the console.
        - The default folder is ``~/.local/state/claude-harness``.
    """

    FORMAT: ClassVar[str] = "%(asctime)s %(levelname)s %(name)s %(message)s"
    MAX_BYTES: ClassVar[int] = 1_000_000
    BACKUP_COUNT: ClassVar[int] = 3

    def __init__(self, tool: str, state_dir: Optional[Path] = None) -> None:
        """Set the tool and its log folder.

        Args:
            tool (str): The tool's name, such as ``ticket-docs``.
            state_dir (Optional[Path]): The folder of the log files.
        """
        self.tool = tool
        self.state_dir = state_dir if state_dir else Path.home() / ".local" / "state" / "claude-harness"

    ############################
    # Publicly Exposed Methods #
    ############################

    def logger(self, name: str) -> Logger:
        """Give a logger that writes to the tool's file only.

        Args:
            name (str): The logger's name, usually the module's.

        Returns:
            Logger: The logger, with one rotating file handler.
        """
        logger = getLogger(f"{self.tool}.{name}")
        if not logger.handlers:
            self.state_dir.mkdir(parents=True, exist_ok=True)
            handler = RotatingFileHandler(
                self.state_dir / f"{self.tool}.log",
                maxBytes=self.MAX_BYTES,
                backupCount=self.BACKUP_COUNT,
                encoding="utf-8",
            )
            handler.setFormatter(Formatter(self.FORMAT))
            logger.addHandler(handler)
            logger.setLevel(DEBUG)
            logger.propagate = False
        return logger

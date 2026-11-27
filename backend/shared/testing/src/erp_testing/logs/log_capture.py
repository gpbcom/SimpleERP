from __future__ import annotations

# Standard library imports
import logging
from logging import Logger, LogRecord
from types import TracebackType
from typing import List, Optional, Type


class LogCapture(logging.Handler):
    """Collect the log records of one logger, so that a test can assert on them.

    Attributes:
        records (List[LogRecord]): The records captured so far, in the order they were emitted.
        logger_name (Optional[str]): The name of the captured logger, or ``None`` for the root logger.
        level (int): The lowest level captured.
        previous_level (Optional[int]): The logger's own level before ``attach``, or ``None`` when not attached.
        target (Optional[Logger]): The logger the handler is attached to, or ``None`` when detached.

    Notes:
        - This class is a data holder that runs for every log event, so it does not log itself, as AGENT.md
          "Logging" allows. A log call here would also feed back into its own records.
        - **The logger's level is lowered while attached and restored by ``detach``**, so a capture never changes the
          level a test sees afterwards.
    """

    def __init__(self, logger_name: Optional[str] = None, level: int = logging.DEBUG) -> None:
        """Create a capture, not yet attached.

        Args:
            logger_name (Optional[str]): The logger to capture, or ``None`` for the root logger.
            level (int): The lowest level to capture.
        """
        super().__init__(level)
        self.records: List[LogRecord] = []
        self.logger_name = logger_name
        self.previous_level: Optional[int] = None
        self.target: Optional[Logger] = None

    ############################
    # Publicly Exposed Methods #
    ############################

    def emit(self, record: LogRecord) -> None:
        """Keep one record.

        Args:
            record (LogRecord): The record to keep.
        """
        self.records.append(record)

    def attach(self) -> None:
        """Add the handler to the logger, and lower the logger's level if it would drop records."""
        if self.target is not None:
            return
        logger = logging.getLogger(self.logger_name)
        self.previous_level = logger.level
        if logger.getEffectiveLevel() > self.level:
            logger.setLevel(self.level)
        logger.addHandler(self)
        self.target = logger

    def detach(self) -> None:
        """Remove the handler from the logger and restore the logger's level."""
        if self.target is None:
            return
        self.target.removeHandler(self)
        if self.previous_level is not None:
            self.target.setLevel(self.previous_level)
        self.target = None
        self.previous_level = None

    def messages(self, level: Optional[int] = None) -> List[str]:
        """Return the formatted messages captured.

        Args:
            level (Optional[int]): Keep only the records of exactly this level, or all of them when ``None``.

        Returns:
            List[str]: The messages, with their lazy arguments applied.
        """
        return [record.getMessage() for record in self.records if level is None or record.levelno == level]

    def contains(self, text: str, level: Optional[int] = None) -> bool:
        """Tell whether a captured message contains a text.

        Args:
            text (str): The text to look for.
            level (Optional[int]): Look only at the records of exactly this level, or at all of them when ``None``.

        Returns:
            bool: ``True`` when a message contains the text.
        """
        return any(text in message for message in self.messages(level))

    def clear(self) -> None:
        """Forget every record captured so far."""
        self.records.clear()

    def __enter__(self) -> LogCapture:
        """Attach the handler.

        Returns:
            LogCapture: This capture.
        """
        self.attach()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Detach the handler, whether or not the block failed.

        Args:
            exc_type (Optional[Type[BaseException]]): The exception type, if any.
            exc_value (Optional[BaseException]): The exception, if any.
            traceback (Optional[TracebackType]): The traceback, if any.
        """
        self.detach()

from __future__ import annotations

# Standard library imports
import json
import logging
from datetime import UTC, datetime
from typing import ClassVar, Dict, Tuple


class JsonLinesFormatter(logging.Formatter):
    """Format each log record as one JSON object on one line, for collection.

    Attributes:
        FIELDS (Tuple[str, ...]): The keys written for every record, in order.
        UNSET (str): The value of a tag the record does not carry.

    Notes:
        - ``json.dumps`` escapes every newline, so the output is always one line.
        - **Only the keys of ``FIELDS`` are written**, so an extra such as a ``_key`` entry never leaks (D240).
        - The tags ``service``, ``company`` and ``request`` are read from the record and default to ``UNSET``.
        - It stays silent because it runs for every event.
    """

    FIELDS: ClassVar[Tuple[str, ...]] = ("time", "level", "logger", "message", "service", "company", "request")
    UNSET: ClassVar[str] = "-"

    ############################
    # Publicly Exposed Methods #
    ############################

    def format(self, record: logging.LogRecord) -> str:
        """Format one record as a JSON line.

        Args:
            record (logging.LogRecord): The record to format.

        Returns:
            str: One JSON object, with no line break.
        """
        created = datetime.fromtimestamp(record.created, tz=UTC)
        data: Dict[str, str] = {
            "time": created.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        for name in self.FIELDS[4:]:
            data[name] = str(getattr(record, name, self.UNSET))
        if record.exc_info:
            data["exception"] = self.formatException(record.exc_info)
        return json.dumps(data, ensure_ascii=False)

from __future__ import annotations

# Standard library imports
import logging
from typing import ClassVar, Optional

# First-party imports
from erp_logging.context.log_context import LogContext
from erp_logging.models.exceptions import SELoggingConfigInvalidError


class ContextFilter(logging.Filter):
    """Tag every log record with the service, the company and the request.

    Attributes:
        UNSET (str): The value written when the company or the request is not bound.
        service (str): The name of the service that writes the records.
        logger (logging.Logger): Logger instance.

    Notes:
        - **The filter is attached to the handlers, not to the loggers**, so that every propagated record is tagged,
          including those of child loggers and of third-party libraries.
        - The company is an opaque id and is written as given.
        - ``filter`` is silent because it runs for every event.
    """

    UNSET: ClassVar[str] = "-"

    def __init__(self, service: str, logger: Optional[logging.Logger] = None) -> None:
        """Create the filter.

        Args:
            service (str): The name of the service.
            logger (Optional[logging.Logger]): Logger instance.

        Raises:
            SELoggingConfigInvalidError: If the service is blank.
        """
        super().__init__()
        self.logger = logger if logger else logging.getLogger(__name__)
        stripped = service.strip() if isinstance(service, str) else ""
        if not stripped:
            self.logger.error("The context filter received a blank service.")
            raise SELoggingConfigInvalidError(
                f"Invalid service: {service!r}. "  # noqa: E501
                "Must not be blank."
            )
        self.service = stripped

    ############################
    # Publicly Exposed Methods #
    ############################

    def filter(self, record: logging.LogRecord) -> bool:
        """Tag one record.

        Args:
            record (logging.LogRecord): The record to tag.

        Returns:
            bool: Always ``True``, so that no record is dropped.
        """
        record.service = self.service
        record.company = LogContext.company() or self.UNSET
        record.request = LogContext.request() or self.UNSET
        return True

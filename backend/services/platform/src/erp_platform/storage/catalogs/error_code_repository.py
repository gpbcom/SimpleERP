from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional

# First-party imports
from erp_models.errors.catalogs.error_catalog import ErrorCatalog
from erp_models.errors.catalogs.exceptions import SEInvalidErrorCatalogException

# Third-party imports
from pydantic import ValidationError

from erp_platform.storage.catalogs.exceptions import SEErrorCodeCatalogUnreadableError


class ErrorCodeRepository:
    """Read the platform's error code catalogue from its YAML file.

    Attributes:
        path (Path): The catalogue file, ``conf/catalogs/error_codes.yaml``.
        logger (Logger): Logger instance.

    Notes:
        - Storage reads data and nothing else: the catalogue is validated by ``ErrorCatalog``.
        - The messages never quote the content of the file.
    """

    def __init__(self, path: Path, logger: Optional[Logger] = None) -> None:
        """Initialise the repository.

        Args:
            path (Path): The catalogue file to read.
            logger (Optional[Logger]): Logger instance.
        """
        self.path = path
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def load(self) -> ErrorCatalog:
        """Load the error code catalogue.

        Returns:
            ErrorCatalog: The validated catalogue.

        Raises:
            SEErrorCodeCatalogUnreadableError: When the file cannot be read or is not a valid catalogue.
        """
        self.logger.debug("Loading the error code catalogue from %s.", self.path)
        try:
            catalog = ErrorCatalog.load(self.path)
        except (SEInvalidErrorCatalogException, ValidationError) as error:
            self.logger.error("Cannot load the error code catalogue %s: %s.", self.path, type(error).__name__)
            raise SEErrorCodeCatalogUnreadableError(
                f"Unreadable error code catalogue: {self.path}. "  # noqa: E501
                f"It could not be loaded ({type(error).__name__})."
            ) from error
        self.logger.info("Loaded %d error codes from %s.", len(catalog.codes), self.path)
        return catalog

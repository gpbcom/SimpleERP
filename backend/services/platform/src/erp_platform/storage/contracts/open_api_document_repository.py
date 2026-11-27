from __future__ import annotations

# Standard library imports
import json
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict, Optional

# Third-party imports
from pydantic import JsonValue

# First-party imports
from erp_platform.models.contracts.exceptions import SEOpenApiDocumentUnreadableError


class OpenApiDocumentRepository:
    """Read an OpenAPI document from a JSON file.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - Storage reads data and nothing else: it compares nothing and applies no rule.
        - **There is no ``write``**: ``.github/scripts/export_openapi.py`` writes the committed document.
        - The messages never quote the content of the file.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Initialise the repository.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def read(self, path: Path) -> Dict[str, JsonValue]:
        """Read one OpenAPI document.

        Args:
            path (Path): The JSON file to read.

        Returns:
            Dict[str, JsonValue]: The document, with the key order of the file.

        Raises:
            SEOpenApiDocumentUnreadableError: When the file is missing, is not UTF-8 JSON or is not an object.
        """
        self.logger.debug("Reading the OpenAPI document %s.", path)
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            self.logger.error("Cannot read the OpenAPI document %s: %s.", path, type(error).__name__)
            raise SEOpenApiDocumentUnreadableError(
                f"Unreadable OpenAPI document: {path}. "  # noqa: E501
                f"It could not be read as JSON ({type(error).__name__})."
            ) from error
        if not isinstance(document, dict):
            self.logger.error("The OpenAPI document %s is not a JSON object.", path)
            raise SEOpenApiDocumentUnreadableError(
                f"Unreadable OpenAPI document: {path}. "  # noqa: E501
                "Its top level must be a JSON object."
            )
        self.logger.info("Read the OpenAPI document %s.", path)
        return document

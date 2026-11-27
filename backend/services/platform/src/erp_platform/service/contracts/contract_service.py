from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict, List, Optional

# Third-party imports
from pydantic import JsonValue

# First-party imports
from erp_platform.models.contracts.contract_change import ContractChange
from erp_platform.models.contracts.contract_report import ContractReport
from erp_platform.service.contracts.contract_comparator import ContractComparator
from erp_platform.storage.contracts.open_api_document_repository import OpenApiDocumentRepository


class ContractService:
    """Check the committed OpenAPI document against the live one (REQ-T05-05).

    Attributes:
        repository (OpenApiDocumentRepository): Where the documents are read.
        comparator (ContractComparator): Finds the breaking changes between two documents.
        logger (Logger): Logger instance.

    Notes:
        - **There is no ``export``**: ``.github/scripts/export_openapi.py`` writes the committed document.
        - A document is stale when it differs from the live one by JSON equality, so formatting never matters.
    """

    def __init__(
        self,
        repository: OpenApiDocumentRepository,
        comparator: ContractComparator,
        logger: Optional[Logger] = None,
    ) -> None:
        """Create the service.

        Args:
            repository (OpenApiDocumentRepository): Where the documents are read.
            comparator (ContractComparator): Finds the breaking changes between two documents.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.comparator = comparator
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def check(
        self,
        generated: Dict[str, JsonValue],
        document_path: Path,
        baseline_path: Optional[Path],
    ) -> ContractReport:
        """Check the committed document against the live one and the baseline.

        Args:
            generated (Dict[str, JsonValue]): The document the application generates now.
            document_path (Path): The committed document.
            baseline_path (Optional[Path]): The baseline to look for breaking changes against, if any.

        Returns:
            ContractReport: Whether the document is stale, and the breaking changes found.

        Raises:
            SEOpenApiDocumentUnreadableError: When the committed document or the baseline cannot be read.
        """
        committed = self.repository.read(document_path)
        stale = committed != generated
        breaking_changes: List[ContractChange] = []
        if baseline_path is None:
            self.logger.debug("No baseline given, so no breaking change is looked for.")
        else:
            baseline = self.repository.read(baseline_path)
            breaking_changes = self.comparator.compare(baseline, committed)
        if stale:
            self.logger.warning("The committed OpenAPI document %s is stale.", document_path)
        if breaking_changes:
            self.logger.warning("Found %d breaking changes against the baseline.", len(breaking_changes))
        self.logger.info(
            "Contract check: the document is %s, with %d breaking changes.",
            "stale" if stale else "up to date",
            len(breaking_changes),
        )
        return ContractReport(stale=stale, breaking_changes=breaking_changes)

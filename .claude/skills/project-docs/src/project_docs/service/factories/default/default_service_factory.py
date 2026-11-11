from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from project_docs.models.catalogs.doc_map import DocMap
from project_docs.models.settings.project_docs_settings import ProjectDocsSettings
from project_docs.service.checks.coverage_check import CoverageCheck
from project_docs.service.checks.links.index_check import IndexCheck
from project_docs.service.checks.links.link_check import LinkCheck
from project_docs.service.checks.mermaid_check import MermaidCheck
from project_docs.service.checks.stamp_check import StampCheck
from project_docs.service.documentation.documentation_service import DocumentationService
from project_docs.service.factories.service_factory import ServiceFactory
from project_docs.service.mapping.chapter_mapper import ChapterMapper
from project_docs.service.tickets.ticket_check import TicketCheck
from project_docs.storage.files.document_files import DocumentFiles
from project_docs.storage.mermaid.mermaid_renderer import MermaidRenderer


class DefaultServiceFactory(ServiceFactory):
    """Builds the real services, on the repository that holds the caller's folder.

    Attributes:
        settings (ProjectDocsSettings): Where the tool reads.
        doc_map (DocMap): The doc map.
        logger (Logger): Logger instance.
    """

    def __init__(self, settings: ProjectDocsSettings, doc_map: DocMap, logger: Optional[Logger] = None) -> None:
        """Set the settings and the doc map.

        Args:
            settings (ProjectDocsSettings): Where the tool reads.
            doc_map (DocMap): The doc map.
            logger (Optional[Logger]): Logger instance.
        """
        self.settings = settings
        self.doc_map = doc_map
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def documentation(self) -> DocumentationService:
        """Build the documentation service of the caller's repository.

        Returns:
            DocumentationService: The service.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """
        repository = GitRepository.discover(self.settings.caller_cwd, self.logger)
        self.logger.debug("The repository is %s.", repository.root)
        files = DocumentFiles(repository.root, self.logger)
        checks = [
            IndexCheck(files, self.logger),
            LinkCheck(files, self.logger),
            CoverageCheck(files, self.doc_map, self.logger),
            StampCheck(files, self.logger),
            MermaidCheck(files, MermaidRenderer(self.logger), self.logger),
        ]
        return DocumentationService(
            repository, ChapterMapper(self.doc_map, self.logger), checks, TicketCheck(files, self.logger), self.logger
        )

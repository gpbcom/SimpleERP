from __future__ import annotations

import logging
from pathlib import Path

import pytest

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


@pytest.fixture
def rules() -> FolderRules:
    return FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml")


@pytest.fixture
def catalog() -> GithubCatalog:
    return GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")


@pytest.fixture
def tables(logger: logging.Logger) -> MarkdownTables:
    return MarkdownTables(logger)


@pytest.fixture
def ticket(tickets: Path) -> TicketBuilder:
    builder = TicketBuilder(tickets)
    builder.minimal()
    return builder


@pytest.fixture
def folder(tickets: Path, ticket: TicketBuilder, tables: MarkdownTables, logger: logging.Logger) -> TicketFolder:
    return TicketFolder(
        ticket.key, TicketRepository(tickets, logger), EvidenceRepository(tickets, logger), tables, logger
    )

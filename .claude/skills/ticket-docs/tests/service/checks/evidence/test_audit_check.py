from __future__ import annotations

import logging

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.service.checks.evidence.audit_check import AuditCheck
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestAuditCheck:
    HANDED_OVER = "| 2 — Final acceptance run and hand-over | ✅ Done | 2026-11-10 10:00 | 2026-11-10 11:00 | 1h00 |"
    HANDOVER_ROW = "| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |"
    REPORT = (
        "# 🔬 GH-7 — Requirements audit\n\n## 🧭 Verdict at a glance\n\nAC1 holds.\n\n## 🧪 What was run\n\nx\n\n"
        "## 🚩 4. Findings\n\nNone.\n\n## 🧱 Limits of this audit\n\nNone.\n"
    )

    def test_before_the_hand_over_no_audit_is_needed(
        self, folder: TicketFolder, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert AuditCheck(tables, logger).problems(folder) == []

    def test_a_handed_over_ticket_needs_its_audit(
        self, folder: TicketFolder, ticket: TicketBuilder, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        assert AuditCheck(tables, logger).problems(folder) == [
            "GH-7/tests-evidences: handed over without a requirements audit "
            "(dev-<date>-requirements-audit/REPORT.md, ticket-docs skill)"
        ]

    def test_the_latest_audit_covers_every_criterion_and_section(
        self, folder: TicketFolder, ticket: TicketBuilder, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        ticket.edit("TICKET.md", "- AC1: a customer is stored.\n", "- AC1: a customer is stored.\n- AC2: listed.\n")
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        old = builder.folder("dev-2026-11-09-requirements-audit")
        (old / "REPORT.md").write_text("# old\n", encoding="utf-8")
        audit = builder.folder("dev-2026-11-10-requirements-audit")
        (audit / "REPORT.md").write_text(self.REPORT.replace("## 🧱 Limits of this audit", "## Other") + "<slot>\n")
        assert AuditCheck(tables, logger).problems(folder) == [
            "GH-7/tests-evidences/dev-2026-11-10-requirements-audit/REPORT.md: section 'Limits' missing",
            "GH-7/tests-evidences/dev-2026-11-10-requirements-audit/REPORT.md: acceptance criteria of TICKET.md "
            "not audited: AC2",
            "GH-7/tests-evidences/dev-2026-11-10-requirements-audit/REPORT.md: template slots left: <slot>",
        ]
        (audit / "REPORT.md").write_text(self.REPORT.replace("AC1 holds.", "AC1 and AC2 hold."), encoding="utf-8")
        assert AuditCheck(tables, logger).problems(folder) == []

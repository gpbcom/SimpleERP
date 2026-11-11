from __future__ import annotations

import logging

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.models.catalogs.doc_map import DocMap
from project_docs.service.checks.coverage_check import CoverageCheck
from project_docs.storage.files.document_files import DocumentFiles
from tests.helpers import STAMP


class TestCoverageCheck:
    def check(self, sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger) -> CoverageCheck:
        return CoverageCheck(DocumentFiles(sandbox.root, logger), doc_map, logger)

    def test_no_service_and_no_front_end_need_no_chapter(
        self, sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger
    ) -> None:
        assert self.check(sandbox, doc_map, logger).problems() == []

    def test_each_service_and_front_end_without_its_chapter_is_reported(
        self, sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger
    ) -> None:
        sandbox.write("services/billing/Dockerfile", "FROM x\n")
        sandbox.write("services/stock/Dockerfile", "FROM x\n")
        sandbox.write("frontends/web/Dockerfile", "FROM x\n")
        sandbox.write("docs/technical/services/stock.md", f"# Stock\n\n{STAMP}\n")
        assert self.check(sandbox, doc_map, logger).problems() == [
            "services/billing/: no chapter docs/technical/services/billing.md.",
            "frontends/web/: no chapter docs/technical/frontends/web.md.",
        ]

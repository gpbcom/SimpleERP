from __future__ import annotations

import logging

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.service.checks.stamp_check import StampCheck
from project_docs.storage.files.document_files import DocumentFiles
from tests.helpers import EM_DASH


class TestStampCheck:
    def check(self, sandbox: GitSandbox, logger: logging.Logger) -> StampCheck:
        return StampCheck(DocumentFiles(sandbox.root, logger), logger)

    def test_a_complete_documentation_has_no_problem(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        assert self.check(sandbox, logger).problems() == []

    @pytest.mark.parametrize(
        "line",
        ["", "Last reviewed: 2026-11-10", "Last reviewed: 10/11/2026 (GH-1)", "Last reviewed: 2026-11-10 (#1)"],
    )
    def test_a_chapter_without_its_stamp_is_reported(
        self, sandbox: GitSandbox, logger: logging.Logger, line: str
    ) -> None:
        sandbox.write("docs/technical/api.md", f"# API\n\n{line}\n")
        assert self.check(sandbox, logger).problems() == [
            'docs/technical/api.md: no "Last reviewed: YYYY-MM-DD (GH-<n>)" line.'
        ]

    def test_an_impossible_date_is_reported(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write("README.md", "# simple-erp\n\nLast reviewed: 2026-13-40 (GH-1)\n")
        assert self.check(sandbox, logger).problems() == [
            "README.md: invalid date 2026-13-40 in its Last reviewed line."
        ]

    def test_every_em_dash_is_reported_with_its_line(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write(
            "docs/functional/capabilities.md",
            f"# Capabilities {EM_DASH} all\n\nNone {EM_DASH} yet.\n\nLast reviewed: 2026-11-10 (GH-1)\n",
        )
        assert self.check(sandbox, logger).problems() == [
            "docs/functional/capabilities.md:1: em dash.",
            "docs/functional/capabilities.md:3: em dash.",
        ]

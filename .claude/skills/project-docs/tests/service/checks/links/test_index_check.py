from __future__ import annotations

import logging

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.service.checks.links.index_check import IndexCheck
from project_docs.storage.files.document_files import DocumentFiles
from tests.helpers import STAMP


class TestIndexCheck:
    def check(self, sandbox: GitSandbox, logger: logging.Logger) -> IndexCheck:
        return IndexCheck(DocumentFiles(sandbox.root, logger), logger)

    def test_a_complete_documentation_has_no_problem(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        assert self.check(sandbox, logger).problems() == []

    def test_a_chapter_its_folder_readme_does_not_link_is_reported(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write("docs/technical/operations.md", f"# Operations\n\n{STAMP}\n")
        assert self.check(sandbox, logger).problems() == [
            "docs/technical/operations.md: not linked from docs/technical/README.md."
        ]

    def test_a_nested_chapter_is_linked_from_the_nearest_readme(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write("docs/technical/services/billing.md", f"# Billing\n\n{STAMP}\n")
        sandbox.write("docs/technical/frontends/web.md", f"# Web\n\n{STAMP}\n")
        sandbox.write("docs/technical/frontends/README.md", f"# Front ends\n\n[Web](web.md)\n\n{STAMP}\n")
        assert self.check(sandbox, logger).problems() == [
            "docs/technical/frontends/README.md: not linked from docs/technical/README.md.",
            "docs/technical/services/billing.md: not linked from docs/technical/README.md.",
        ]
        readme = (sandbox.root / "docs/technical/README.md").read_text(encoding="utf-8")
        sandbox.write(
            "docs/technical/README.md",
            readme.replace(STAMP, f"[Billing](services/billing.md) [Front ends](frontends/README.md)\n\n{STAMP}"),
        )
        assert self.check(sandbox, logger).problems() == []

    def test_a_missing_folder_readme_is_reported(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        (sandbox.root / "docs/functional/README.md").unlink()
        assert self.check(sandbox, logger).problems() == [
            "docs/functional/README.md: missing.",
            "docs/functional/capabilities.md: not linked from docs/functional/README.md.",
        ]

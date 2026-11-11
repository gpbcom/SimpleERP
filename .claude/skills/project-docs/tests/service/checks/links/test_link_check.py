from __future__ import annotations

import logging

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.service.checks.links.link_check import LinkCheck
from project_docs.storage.files.document_files import DocumentFiles
from tests.helpers import STAMP


class TestLinkCheck:
    def check(self, sandbox: GitSandbox, logger: logging.Logger) -> LinkCheck:
        return LinkCheck(DocumentFiles(sandbox.root, logger), logger)

    def test_a_complete_documentation_has_no_problem(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        assert self.check(sandbox, logger).problems() == []

    def test_a_relative_link_to_nothing_is_reported_with_its_line(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write(
            "docs/technical/api.md", f"# API\n\nSee [nothing](nowhere.md#x) and [up](../../../out.md).\n\n{STAMP}\n"
        )
        assert self.check(sandbox, logger).problems() == [
            "docs/technical/api.md:3: broken link to nowhere.md#x.",
            "docs/technical/api.md:3: broken link to ../../../out.md.",
        ]

    def test_external_links_anchors_folders_and_root_links_are_accepted(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write("AGENT.md", "# Rules\n")
        sandbox.write("docs/specs/READ.md", "specs\n")
        sandbox.write(
            "docs/technical/api.md",
            "# API\n\n[web](https://example.com/x.md) [mail](mailto:a@example.com) [top](#api) "
            "[specs](../specs/) [rules](/AGENT.md) [spaced](<../specs/READ.md>) "
            f"[coded](%2E%2E/specs/READ.md)\n\n{STAMP}\n",
        )
        assert self.check(sandbox, logger).problems() == []

    def test_the_root_readme_is_checked_too(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write("README.md", f"# simple-erp\n\n[Changelog](CHANGELOG.md)\n\n{STAMP}\n")
        assert self.check(sandbox, logger).problems() == ["README.md:3: broken link to CHANGELOG.md."]

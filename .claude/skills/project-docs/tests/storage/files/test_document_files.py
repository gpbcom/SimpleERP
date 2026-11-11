from __future__ import annotations

import logging

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.storage.files.document_files import DocumentFiles


class TestDocumentFiles:
    def test_documents_are_the_readme_then_every_markdown_file_of_the_two_folders(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write("docs/technical/services/billing.md", "x\n")
        sandbox.write("docs/technical/notes.txt", "x\n")
        sandbox.write("docs/specs/READ.md", "x\n")
        assert DocumentFiles(sandbox.root, logger).documents() == [
            "README.md",
            "docs/functional/README.md",
            "docs/functional/capabilities.md",
            "docs/technical/README.md",
            "docs/technical/api.md",
            "docs/technical/architecture.md",
            "docs/technical/development-process.md",
            "docs/technical/services/billing.md",
        ]

    def test_a_missing_readme_or_folder_is_left_out(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        (sandbox.root / "README.md").unlink()
        files = DocumentFiles(sandbox.root, logger)
        assert "README.md" not in files.documents()
        assert not files.exists("README.md")
        assert files.exists("docs/technical/api.md")

    def test_read_gives_the_text_and_an_empty_one_for_a_missing_file(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        files = DocumentFiles(sandbox.root, logger)
        assert files.read("docs/technical/api.md").startswith("# API")
        assert files.read("docs/tickets/GH-7/PROGRESS.md") == ""

    def test_folders_list_the_sub_folders_of_a_parent(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write("services/billing/Dockerfile", "FROM x\n")
        sandbox.write("services/stock/pyproject.toml", "\n")
        sandbox.write("services/.hidden/x", "\n")
        sandbox.write("services/README.md", "\n")
        files = DocumentFiles(sandbox.root, logger)
        assert files.folders("services") == ["billing", "stock"]
        assert files.folders("frontends") == []

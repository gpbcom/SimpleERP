from __future__ import annotations

import logging

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.service.exceptions import SEProjectDocsServiceError, SETicketKeyInvalidError
from project_docs.service.tickets.ticket_check import TicketCheck
from project_docs.storage.files.document_files import DocumentFiles


class TestTicketCheck:
    PROGRESS = "docs/tickets/GH-7/PROGRESS.md"
    MAPPING = {"README.md": ["LICENSE"], "docs/technical/api.md": ["src/api/a.py", "src/api/b.py"]}

    def progress(self, rows: str) -> str:
        return (
            "# GH-7 progress\n\n## Documentation\n\n| Chapter | Status | What changed |\n|---|---|---|\n"
            f"{rows}\n## Release note\n\n| Item | Status | Detail |\n|---|---|---|\n"
            "| docs/technical/api.md | ✅ | no doc impact: in the wrong section |\n"
        )

    def check(self, sandbox: GitSandbox, logger: logging.Logger) -> TicketCheck:
        return TicketCheck(DocumentFiles(sandbox.root, logger), logger)

    def test_chapters_changed_in_the_branch_need_nothing_else(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        changed = ["LICENSE", "README.md", "docs/technical/api.md", "src/api/a.py", "src/api/b.py"]
        assert self.check(sandbox, logger).unhandled("GH-7", self.MAPPING, changed) == []

    def test_a_chapter_neither_changed_nor_waived_is_reported(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write(
            self.PROGRESS, self.progress("| `docs/technical/README.md` | ✅ | no doc impact: nothing to add |\n")
        )
        assert self.check(sandbox, logger).unhandled(
            "GH-7", self.MAPPING, ["LICENSE", "src/api/a.py", "src/api/b.py"]
        ) == [
            "README.md: concerned by LICENSE but neither changed in the branch nor waived with"
            ' "no doc impact:" in docs/tickets/GH-7/PROGRESS.md.',
            "docs/technical/api.md: concerned by src/api/a.py, src/api/b.py but neither changed in the branch nor"
            ' waived with "no doc impact:" in docs/tickets/GH-7/PROGRESS.md.',
        ]

    def test_a_documentation_row_with_no_doc_impact_waives_its_chapter(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        sandbox.write(
            self.PROGRESS,
            self.progress(
                "| `README.md` | ✅ | no doc impact: no command changed |\n"
                "| docs/technical/api.md | ✅ | Updated the routes |\n"
            ),
        )
        problems = self.check(sandbox, logger).unhandled("GH-7", self.MAPPING, ["LICENSE", "src/api/a.py"])
        assert len(problems) == 1
        assert problems[0].startswith("docs/technical/api.md: concerned by src/api/a.py, src/api/b.py")

    @pytest.mark.parametrize("key", ["7", "gh-7", "GH-", "GH-7/../x"])
    def test_a_bad_ticket_key_is_refused(self, sandbox: GitSandbox, logger: logging.Logger, key: str) -> None:
        with pytest.raises(SETicketKeyInvalidError):
            self.check(sandbox, logger).unhandled(key, self.MAPPING, [])
        assert issubclass(SETicketKeyInvalidError, SEProjectDocsServiceError)

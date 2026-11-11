from __future__ import annotations

import logging

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.models.catalogs.doc_map import DocMap
from project_docs.models.settings.project_docs_settings import ProjectDocsSettings
from project_docs.service.documentation.documentation_service import DocumentationService
from project_docs.service.factories.default.default_service_factory import DefaultServiceFactory
from tests.helpers import EM_DASH, STAMP


class TestCheck:
    def service(self, sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger) -> DocumentationService:
        return DefaultServiceFactory(ProjectDocsSettings(caller_cwd=sandbox.root), doc_map, logger).documentation()

    def test_a_complete_documentation_has_no_problem(
        self, caller_in_sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger
    ) -> None:
        assert self.service(caller_in_sandbox, doc_map, logger).check(None, "develop") == []

    def test_every_check_reports_its_problems(
        self, caller_in_sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger
    ) -> None:
        caller_in_sandbox.write("docs/technical/operations.md", f"# Operations {EM_DASH} x\n\n[x](gone.md)\n")
        caller_in_sandbox.write("services/billing/Dockerfile", "FROM x\n")
        assert self.service(caller_in_sandbox, doc_map, logger).check(None, "develop") == [
            "docs/technical/operations.md: not linked from docs/technical/README.md.",
            "docs/technical/operations.md:3: broken link to gone.md.",
            "services/billing/: no chapter docs/technical/services/billing.md.",
            'docs/technical/operations.md: no "Last reviewed: YYYY-MM-DD (GH-<n>)" line.',
            "docs/technical/operations.md:1: em dash.",
        ]

    def test_with_a_ticket_each_chapter_the_branch_concerns_is_changed_or_waived(
        self, caller_in_sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger
    ) -> None:
        caller_in_sandbox.commit("code", {"src/api/routes.py": "x\n"})
        service = self.service(caller_in_sandbox, doc_map, logger)
        assert [problem.split(":")[0] for problem in service.check("GH-7", "develop")] == [
            "README.md",
            "docs/technical/api.md",
        ]
        api = (caller_in_sandbox.root / "docs/technical/api.md").read_text(encoding="utf-8")
        caller_in_sandbox.write("docs/technical/api.md", api.replace(STAMP, f"The routes.\n\n{STAMP}"))
        caller_in_sandbox.write(
            "docs/tickets/GH-7/PROGRESS.md",
            "## Documentation\n\n| Chapter | Status | What changed |\n|---|---|---|\n"
            "| README.md | ✅ | no doc impact: no command changed |\n",
        )
        assert service.check("GH-7", "develop") == []

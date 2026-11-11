from __future__ import annotations

import logging

import pytest

from harness_core.git.exceptions import SEGitCommandFailedError
from harness_core.testing.git_sandbox import GitSandbox
from project_docs.models.catalogs.doc_map import DocMap
from project_docs.models.settings.project_docs_settings import ProjectDocsSettings
from project_docs.service.factories.default.default_service_factory import DefaultServiceFactory


class TestMap:
    def test_the_branch_commits_and_the_uncommitted_changes_are_mapped(
        self, sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger
    ) -> None:
        sandbox.commit("api", {"src/api/cli/main.py": "x = 1\n"})
        sandbox.write("conf/app.yaml", "a: 1\n")
        sandbox.write("CHANGELOG.md", "# Changelog\n")
        service = DefaultServiceFactory(ProjectDocsSettings(caller_cwd=sandbox.root), doc_map, logger).documentation()
        assert service.changed_paths("develop") == ["CHANGELOG.md", "conf/app.yaml", "src/api/cli/main.py"]
        assert service.map("develop") == {
            "README.md": ["src/api/cli/main.py"],
            "docs/technical/api.md": ["src/api/cli/main.py"],
            "docs/technical/configuration.md": ["conf/app.yaml"],
        }

    def test_an_unknown_base_is_reported(self, sandbox: GitSandbox, doc_map: DocMap, logger: logging.Logger) -> None:
        service = DefaultServiceFactory(ProjectDocsSettings(caller_cwd=sandbox.root), doc_map, logger).documentation()
        with pytest.raises(SEGitCommandFailedError):
            service.map("origin/nowhere")

from __future__ import annotations

import logging

import pytest

from harness_core.models.git.change_status import ChangeStatus
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.paths.code_paths import CodePaths


class TestCodePaths:
    @pytest.fixture
    def paths(self, logger: logging.Logger) -> CodePaths:
        return CodePaths(FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml"), logger)

    @pytest.mark.parametrize(
        ("path", "production", "test"),
        [
            ("src/api/cli/main.py", True, False),
            ("services/customers/src/customers/service/x.py", True, False),
            ("frontends/web/src/App.vue", True, False),
            ("packages/lifecycle/runnable.py", True, False),
            (".claude/skills/ticket-docs/src/ticket_docs/x.py", True, False),
            ("tests/conventions/test_layers.py", False, True),
            (".claude/skills/ticket-docs/tests/models/test_x.py", False, True),
            ("services/customers/tests/test_api.py", False, True),
            ("frontends/web/e2e/login.spec.ts", False, True),
            ("packages/lifecycle/tests/test_runnable.py", False, True),
            ("README.md", False, False),
            (".claude/skills/cve-scan/src/cve_scan/__init__.py", False, False),
            ("src/models/customers/exceptions/__init__.py", False, False),
            (".claude/skills/ticket-docs/pyproject.toml", False, False),
            ("docs/technical/README.md", False, False),
        ],
    )
    def test_production_code_and_tests_are_told_apart(
        self, paths: CodePaths, path: str, production: bool, test: bool
    ) -> None:
        assert (paths.is_production(path), paths.is_test(path)) == (production, test)

    def test_the_production_files_of_a_list_are_picked_out_and_sorted(self, paths: CodePaths) -> None:
        files = ["tests/test_a.py", "src/b.py", "README.md", "src/a.py", "src/models/__init__.py"]
        assert paths.production(files) == ["src/a.py", "src/b.py"]

    def test_the_new_test_files_are_the_added_or_untracked_ones(self, paths: CodePaths) -> None:
        changes = {
            "tests/test_b.py": ChangeStatus.UNTRACKED,
            "tests/test_a.py": ChangeStatus.ADDED,
            "tests/test_c.py": ChangeStatus.MODIFIED,
            "tests/test_d.py": ChangeStatus.DELETED,
            "src/a.py": ChangeStatus.ADDED,
        }
        assert paths.new_tests(changes) == ["tests/test_a.py", "tests/test_b.py"]

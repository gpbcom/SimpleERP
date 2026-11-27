from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import List

# Third-party imports
import pytest

# First-party imports
from tests.harness.check_touched.helpers import add_worktree, git, make_repo, repo_root, run_hook

CATALOGUE_RELATIVE = ".claude/hooks/layer-checks.json"


class TestCheckTouchedLayout:
    def dry_run(self, tmp_path: Path, created: List[str], present: List[str]) -> List[str]:
        catalogue = (repo_root() / CATALOGUE_RELATIVE).read_text(encoding="utf-8")
        tmp_path.mkdir(parents=True, exist_ok=True)
        main = make_repo(tmp_path, catalogue)
        worker = add_worktree(main, tmp_path)
        for relative in created:
            path = worker / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("x = 1\n", encoding="utf-8")
        for relative in present:
            (worker / relative).mkdir(parents=True, exist_ok=True)
        return run_hook(worker, "--dry-run").stdout.splitlines()

    def test_a_service_change_lists_ruff_mypy_and_the_tests_that_mirror_it(self, tmp_path: Path) -> None:
        source = "backend/services/sales/src/erp_sales/service/quotes/quote_service.py"
        before = self.dry_run(tmp_path / "a", [source], [])
        assert any(line.endswith(f"uv run ruff check {source}") for line in before)
        assert any(line.endswith(f"uv run ruff format --check {source}") for line in before)
        assert any(line.endswith("uv run mypy backend/services/sales/src") for line in before)
        assert not any("pytest" in line for line in before)
        after = self.dry_run(tmp_path / "b", [source], ["backend/services/sales/tests/service/quotes"])
        assert any(line.endswith("uv run pytest backend/services/sales/tests/service/quotes -n 2") for line in after)

    @pytest.mark.parametrize(
        ("source", "package", "tests"),
        [
            ("backend/models/src/erp_models/sales/quote.py", "backend/models", "backend/models/tests/sales"),
            (
                "backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py",
                "backend/shared/lifecycle",
                "backend/shared/lifecycle/tests/runnables",
            ),
            ("plugins/shopify/src/erp_shopify/service/sync.py", "plugins/shopify", "plugins/shopify/tests/service"),
            ("sdk/src/erp_sdk/cli/main.py", "sdk", "sdk/tests/cli"),
        ],
    )
    def test_every_package_kind_lists_its_mypy_and_its_mirrored_tests(
        self, tmp_path: Path, source: str, package: str, tests: str
    ) -> None:
        lines = self.dry_run(tmp_path, [source], [tests])
        assert any(line.endswith(f"uv run mypy {package}/src") for line in lines)
        assert any(line.endswith(f"uv run pytest {tests} -n 2") for line in lines)

    @pytest.mark.parametrize(
        "test_file",
        ["backend/services/sales/tests/service/quotes/test_quote_service.py", "tests/conventions/test_layers.py"],
    )
    def test_a_change_only_under_tests_lists_ruff_but_no_pytest(self, tmp_path: Path, test_file: str) -> None:
        lines = self.dry_run(tmp_path, [test_file], [])
        assert any(line.endswith(f"uv run ruff check {test_file}") for line in lines)
        assert not any("pytest" in line for line in lines)
        assert not any("mypy" in line for line in lines)

    def test_a_harness_script_is_linted(self, tmp_path: Path) -> None:
        lines = self.dry_run(tmp_path, [".claude/scripts/tickets/checks.py"], ["tests/harness/checks"])
        assert any(line.endswith("uv run ruff check .claude/scripts/tickets/checks.py") for line in lines)
        assert any(line.endswith("uv run pytest tests/harness/checks -n 2") for line in lines)

    @pytest.mark.parametrize("app", ["frontend/backoffice", "frontend/portals/customer", "frontend/packages/ui"])
    def test_a_front_end_change_lists_its_pnpm_checks(self, tmp_path: Path, app: str) -> None:
        lines = self.dry_run(tmp_path, [f"{app}/src/a.ts", f"{app}/package.json"], [])
        for kind in ("lint", "typecheck", "test"):
            assert any(line.endswith(f"pnpm --filter ./{app} run --if-present {kind}") for line in lines)

    def test_a_playwright_change_lists_lint_and_typecheck_but_not_the_unit_tests(self, tmp_path: Path) -> None:
        app = "frontend/backoffice"
        main = make_repo(tmp_path, (repo_root() / CATALOGUE_RELATIVE).read_text(encoding="utf-8"))
        (main / app).mkdir(parents=True)
        (main / app / "package.json").write_text("{}", encoding="utf-8")
        git(main, "add", "-A")
        git(main, "commit", "-m", "the app")
        worker = add_worktree(main, tmp_path)
        (worker / app / "e2e").mkdir()
        (worker / app / "e2e" / "quotes.spec.ts").write_text("", encoding="utf-8")
        lines = run_hook(worker, "--dry-run").stdout.splitlines()
        assert any(line.endswith(f"pnpm --filter ./{app} run --if-present typecheck") for line in lines)
        assert not any(line.endswith("run --if-present test") for line in lines)

    def test_an_infra_change_lists_the_terraform_format_check(self, tmp_path: Path) -> None:
        lines = self.dry_run(tmp_path, ["infra/terraform/ovhcloud/main.tf"], [])
        assert any("terraform fmt -check -recursive infra/terraform/ovhcloud" in line for line in lines)

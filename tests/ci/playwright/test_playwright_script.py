from __future__ import annotations

from pathlib import Path

from tests.ci.playwright.helpers import make_project, playwright_calls, run_script


class TestPlaywrightScript:
    def test_a_front_end_with_a_config_runs_playwright_with_it(self, tmp_path: Path) -> None:
        make_project(tmp_path, "frontend/backoffice", config=True)
        result = run_script(tmp_path)
        assert result.returncode == 0
        assert playwright_calls(tmp_path) == ["frontend/backoffice|--config e2e/playwright.config.ts"]

    def test_the_config_comes_before_the_extra_arguments(self, tmp_path: Path) -> None:
        make_project(tmp_path, "frontend/backoffice", config=True)
        run_script(tmp_path, "--grep", "@smoke")
        assert playwright_calls(tmp_path) == ["frontend/backoffice|--config e2e/playwright.config.ts --grep @smoke"]

    def test_extra_arguments_reach_playwright_unchanged(self, tmp_path: Path) -> None:
        make_project(tmp_path, "frontend/backoffice")
        run_script(tmp_path, "--grep", "@smoke")
        assert playwright_calls(tmp_path) == ["frontend/backoffice|--grep @smoke"]

    def test_a_front_end_without_a_config_gets_no_config_option(self, tmp_path: Path) -> None:
        make_project(tmp_path, "frontend/backoffice")
        run_script(tmp_path)
        assert playwright_calls(tmp_path) == ["frontend/backoffice|"]

    def test_a_portal_is_run_too(self, tmp_path: Path) -> None:
        make_project(tmp_path, "frontend/backoffice")
        make_project(tmp_path, "frontend/portals/customer")
        run_script(tmp_path)
        assert sorted(playwright_calls(tmp_path)) == ["frontend/backoffice|", "frontend/portals/customer|"]

    def test_one_failing_front_end_fails_the_script_and_the_others_still_run(self, tmp_path: Path) -> None:
        make_project(tmp_path, "frontend/backoffice", failing=True)
        make_project(tmp_path, "frontend/portals/customer")
        result = run_script(tmp_path)
        assert result.returncode == 1
        assert "frontend/portals/customer|" in playwright_calls(tmp_path)

    def test_without_an_e2e_folder_the_script_succeeds_and_says_playwright_is_not_applicable(
        self, tmp_path: Path
    ) -> None:
        (tmp_path / "frontend" / "backoffice").mkdir(parents=True)
        result = run_script(tmp_path)
        assert result.returncode == 0
        assert "not applicable" in result.stdout
        assert playwright_calls(tmp_path) == []

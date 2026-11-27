from __future__ import annotations

# Standard library imports
import json
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import (
    BACKOFFICE,
    CUSTOMER_PORTAL,
    IMAGES_KEY,
    KEYS,
    PACKAGES_KEY,
    REPOSITORY_KEY,
    SALES,
    SERVICES_KEY,
    STOCK,
    TYPESCRIPT_KEY,
    compact,
    detect,
    nothing,
    outputs,
    run_detector,
    write_repo,
)


class TestDetectChanges:
    def test_the_output_is_five_lines_in_the_contract_order(self, tmp_path: Path) -> None:
        write_repo(tmp_path)
        result = run_detector(tmp_path, [f"{SALES}/x.py"])
        assert [line.split("=", 1)[0] for line in result.stdout.splitlines()] == KEYS
        values = outputs(result)
        for key in (SERVICES_KEY, PACKAGES_KEY, TYPESCRIPT_KEY, IMAGES_KEY):
            assert isinstance(json.loads(values[key]), list)
        assert values[REPOSITORY_KEY] in {"true", "false"}

    def test_no_changed_path_selects_nothing(self, tmp_path: Path) -> None:
        assert detect(tmp_path, []) == nothing()

    def test_a_change_to_one_service_selects_only_that_service_and_its_image(self, tmp_path: Path) -> None:
        changed = [
            f"{SALES}/src/sales/service/quotes/quote_service.py",
            f"{SALES}/conf/app.yaml",
            f"{SALES}/Dockerfile",
        ]
        assert detect(tmp_path, changed) == {
            **nothing(),
            SERVICES_KEY: compact([SALES]),
            IMAGES_KEY: compact([{"folder": SALES, "name": "sales"}]),
        }

    def test_two_services_are_selected_sorted_and_once_each(self, tmp_path: Path) -> None:
        changed = [f"{STOCK}/a.py", f"{SALES}/a.py", f"{STOCK}/b.py"]
        assert detect(tmp_path, changed)[SERVICES_KEY] == compact([SALES, STOCK])

    def test_a_service_without_a_dockerfile_builds_no_image(self, tmp_path: Path) -> None:
        values = detect(tmp_path, [f"{STOCK}/tests/test_x.py"])
        assert values[SERVICES_KEY] == compact([STOCK])
        assert values[IMAGES_KEY] == "[]"

    @pytest.mark.parametrize(
        "path",
        [
            "backend/services/gone/x.py",
            "backend/services/_template/x.py",
            "backend/services/.hidden/x.py",
            "backend/services/README.md",
            "frontend/mobile/src/main.ts",
        ],
    )
    def test_a_folder_that_is_not_a_project_selects_nothing(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path]) == nothing()

    @pytest.mark.parametrize(
        ("path", "package"),
        [("plugins/hello/src/hello/plugin.py", "plugins/hello"), ("sdk/src/erp_sdk/cli.py", "sdk")],
    )
    def test_a_plugin_or_the_sdk_selects_only_its_own_package(self, tmp_path: Path, path: str, package: str) -> None:
        assert detect(tmp_path, [path]) == {**nothing(), PACKAGES_KEY: compact([package])}

    def test_a_front_end_app_selects_its_project_and_its_image(self, tmp_path: Path) -> None:
        assert detect(tmp_path, [f"{BACKOFFICE}/src/main.ts"]) == {
            **nothing(),
            TYPESCRIPT_KEY: compact([BACKOFFICE]),
            IMAGES_KEY: compact([{"folder": BACKOFFICE, "name": "backoffice"}]),
        }

    def test_a_portal_image_is_named_after_the_portal(self, tmp_path: Path) -> None:
        values = detect(tmp_path, [f"{CUSTOMER_PORTAL}/src/App.vue"])
        assert values[TYPESCRIPT_KEY] == compact([CUSTOMER_PORTAL])
        assert values[IMAGES_KEY] == compact([{"folder": CUSTOMER_PORTAL, "name": "portal-customer"}])

    @pytest.mark.parametrize("path", ["tests/conventions/x.py", ".claude/hooks/x.py", ".githooks/pre-push"])
    def test_tests_and_harness_set_only_the_repository_flag(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path]) == {**nothing(), REPOSITORY_KEY: "true"}

    @pytest.mark.parametrize(
        "path", [".github/workflows/gitflow.yml", ".github/workflows/stage.yml", ".github/dependabot.yml"]
    )
    def test_a_workflow_that_is_not_reused_runs_only_the_repository_tests(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path]) == {**nothing(), REPOSITORY_KEY: "true"}

    @pytest.mark.parametrize(
        "path",
        [
            "docs/specs/02-functional/f06-customers-and-sales/README.md",
            "README.md",
            "AGENT.md",
            "infra/terraform/modules/network/main.tf",
            "packs/countries/fr/vat.yaml",
        ],
    )
    def test_unrelated_paths_select_nothing(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path]) == nothing()

    def test_blank_lines_and_surrounding_spaces_are_ignored(self, tmp_path: Path) -> None:
        values = detect(tmp_path, ["", f"  {STOCK}/x.py  ", "   ", ""])
        assert values == {**nothing(), SERVICES_KEY: compact([STOCK])}

    def test_an_unknown_argument_exits_with_two_and_a_usage_line(self, tmp_path: Path) -> None:
        write_repo(tmp_path)
        result = run_detector(tmp_path, [], "--bogus")
        assert result.returncode == 2
        assert "usage" in result.stderr.lower()

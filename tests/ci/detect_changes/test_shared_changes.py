from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import (
    ALL_TYPESCRIPT,
    BACKOFFICE,
    CUSTOMER_PORTAL,
    IMAGES_KEY,
    SALES,
    SERVICES_KEY,
    TYPESCRIPT_KEY,
    compact,
    detect,
    everything,
    nothing,
    outputs,
    run_detector,
)


class TestSharedChanges:
    @pytest.mark.parametrize(
        "path",
        [
            "backend/models/src/erp_models/customers/customer.py",
            "backend/shared/logging/src/erp_logging/setup.py",
            "uv.lock",
            "pyproject.toml",
            ".python-version",
            "pnpm-lock.yaml",
            "package.json",
            "pnpm-workspace.yaml",
            "compose.e2e.yaml",
            ".dockerignore",
            ".github/scripts/detect_changes.py",
            ".github/workflows/ci.yml",
            ".github/workflows/python.yml",
            ".github/workflows/typescript.yml",
            ".github/workflows/images.yml",
        ],
    )
    def test_a_shared_path_alone_runs_everything(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path]) == everything()

    def test_all_runs_everything_with_empty_stdin(self, tmp_path: Path) -> None:
        assert detect(tmp_path, [], "--all") == everything()

    def test_a_shared_path_with_a_service_path_lists_each_service_once(self, tmp_path: Path) -> None:
        assert detect(tmp_path, ["uv.lock", f"{SALES}/x.py"]) == everything()

    def test_a_service_manifest_is_not_the_root_manifest(self, tmp_path: Path) -> None:
        assert detect(tmp_path, [f"{SALES}/pyproject.toml"])[SERVICES_KEY] == compact([SALES])

    def test_a_shared_front_end_package_selects_every_front_end_and_its_images(self, tmp_path: Path) -> None:
        values = detect(tmp_path, ["frontend/packages/ui/src/Button.vue"])
        assert values == {
            **nothing(),
            TYPESCRIPT_KEY: compact(sorted(ALL_TYPESCRIPT)),
            IMAGES_KEY: compact(
                [{"folder": BACKOFFICE, "name": "backoffice"}, {"folder": CUSTOMER_PORTAL, "name": "portal-customer"}]
            ),
        }

    def test_a_repository_without_any_project_gives_empty_lists_and_runs_the_repository_tests(
        self, tmp_path: Path
    ) -> None:
        result = run_detector(tmp_path, [], "--all")
        assert result.returncode == 0, result.stderr
        assert outputs(result) == {**nothing(), "repository": "true"}

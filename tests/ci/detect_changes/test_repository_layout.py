from __future__ import annotations

# Standard library imports
import json
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import (
    IMAGES_KEY,
    PACKAGES_KEY,
    TYPESCRIPT_KEY,
    compact,
    nothing,
    outputs,
    run_detector,
)


class TestRepositoryLayout:
    ROOT = Path(__file__).resolve().parents[3]

    def test_the_python_workspace_members_are_listed_as_packages(self) -> None:
        result = run_detector(self.ROOT, [], "--all")
        assert result.returncode == 0, result.stderr
        packages = json.loads(outputs(result)[PACKAGES_KEY])
        assert {"backend/models", "sdk"} <= set(packages)

    def test_a_change_to_the_sdk_selects_only_the_sdk(self) -> None:
        result = run_detector(self.ROOT, ["sdk/README.md"])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == {**nothing(), PACKAGES_KEY: compact(["sdk"])}

    def test_the_front_end_apps_are_listed_as_typescript_projects(self) -> None:
        result = run_detector(self.ROOT, [], "--all")
        assert result.returncode == 0, result.stderr
        values = outputs(result)
        assert {"frontend/backoffice", "frontend/mobile"} <= set(json.loads(values[TYPESCRIPT_KEY]))
        folders = [image["folder"] for image in json.loads(values[IMAGES_KEY])]
        assert "frontend/backoffice" not in folders
        assert "frontend/mobile" not in folders

    def test_a_change_to_a_front_end_app_selects_only_that_app(self) -> None:
        result = run_detector(self.ROOT, ["frontend/mobile/README.md"])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == {**nothing(), TYPESCRIPT_KEY: compact(["frontend/mobile"])}

    @pytest.mark.parametrize(
        "path",
        [
            "infra/compose/README.md",
            "infra/helm/README.md",
            "infra/terraform/README.md",
            "packs/countries/README.md",
            "packs/sectors/README.md",
            "backend/services/README.md",
            "plugins/README.md",
        ],
    )
    def test_a_readme_of_a_folder_without_a_project_selects_nothing(self, path: str) -> None:
        result = run_detector(self.ROOT, [path])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == nothing()

    def test_a_change_to_the_shared_front_end_packages_selects_every_front_end(self) -> None:
        result = run_detector(self.ROOT, ["frontend/packages/README.md"])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == {**nothing(), TYPESCRIPT_KEY: compact(["frontend/backoffice", "frontend/mobile"])}

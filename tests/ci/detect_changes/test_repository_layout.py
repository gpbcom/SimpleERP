from __future__ import annotations

# Standard library imports
import json
import subprocess
from typing import Dict, List

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
from tests.ci.detect_changes.repository_layout.helpers import (
    LAYOUT_ROOT,
    folders_with_a_project,
    folders_without_a_project,
    readme_selection,
)


class TestRepositoryLayout:
    ROOT = LAYOUT_ROOT

    def selected(self, result: subprocess.CompletedProcess[str], expected: Dict[str, str]) -> Dict[str, str]:
        values = outputs(result)
        return {key: values[key] for key in expected}

    def front_end_projects(self) -> List[str]:
        frontend = self.ROOT / "frontend"
        found = [
            package.parent.relative_to(self.ROOT).as_posix()
            for pattern in ("*/package.json", "portals/*/package.json", "packages/*/package.json")
            for package in frontend.glob(pattern)
        ]
        return sorted(found)

    def front_ends_with_an_image(self) -> List[str]:
        """Return the front ends that hold a Dockerfile, which the detector lists as images."""
        return [folder for folder in self.front_end_projects() if (self.ROOT / folder / "Dockerfile").is_file()]

    def test_the_python_workspace_members_are_listed_as_packages(self) -> None:
        result = run_detector(self.ROOT, [], "--all")
        assert result.returncode == 0, result.stderr
        packages = json.loads(outputs(result)[PACKAGES_KEY])
        assert {"backend/models", "sdk"} <= set(packages)

    def test_the_front_end_apps_are_listed_as_typescript_projects(self) -> None:
        result = run_detector(self.ROOT, [], "--all")
        assert result.returncode == 0, result.stderr
        values = outputs(result)
        assert {"frontend/backoffice", "frontend/mobile"} <= set(json.loads(values[TYPESCRIPT_KEY]))
        folders = {image["folder"] for image in json.loads(values[IMAGES_KEY])}
        front_ends = {"frontend/backoffice", "frontend/mobile"}
        assert folders & front_ends == set(self.front_ends_with_an_image()) & front_ends

    @pytest.mark.parametrize("folder", folders_without_a_project(LAYOUT_ROOT))
    def test_a_readme_of_a_folder_without_a_project_selects_nothing(self, folder: str) -> None:
        result = run_detector(self.ROOT, [f"{folder}/README.md"])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == nothing()

    @pytest.mark.parametrize("folder", folders_with_a_project(LAYOUT_ROOT))
    def test_a_readme_of_a_folder_with_a_project_selects_what_its_markers_make_it(self, folder: str) -> None:
        result = run_detector(self.ROOT, [f"{folder}/README.md"])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == readme_selection(self.ROOT, folder)

    def test_a_change_to_the_shared_front_end_packages_selects_every_front_end(self) -> None:
        result = run_detector(self.ROOT, ["frontend/packages/README.md"])
        assert result.returncode == 0, result.stderr
        expected = {TYPESCRIPT_KEY: compact(self.front_end_projects())}
        assert self.selected(result, expected) == expected
        images = {image["folder"] for image in json.loads(outputs(result)[IMAGES_KEY])}
        assert images == set(self.front_ends_with_an_image())

"""The layout test, run on a fixture repository where a folder gains a marker, still passes.

Each time a ticket filled the layout, a hand-written case of ``test_repository_layout.py`` broke: a front end with an
image (T0.17), ``infra/helm`` once it held ``Chart.yaml`` (T0.19). This test copies the layout test, its helpers and the
detector into a fixture repository, adds a marker to one folder and runs the layout test there: its expectations must
follow the files.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Dict, List

import pytest

from tests.ci.detect_changes.repository_layout.helpers import LAYOUT_ROOT


class TestLayoutFollowsTheFiles:
    LAYOUT_TEST = "tests/ci/detect_changes/test_repository_layout.py"
    WITHOUT = "test_a_readme_of_a_folder_without_a_project_selects_nothing"
    WITH = "test_a_readme_of_a_folder_with_a_project_selects_what_its_markers_make_it"
    COPIED = [
        ".github/scripts/detect_changes.py",
        "tests/ci/detect_changes/helpers.py",
        "tests/ci/detect_changes/test_repository_layout.py",
        "tests/ci/detect_changes/repository_layout/helpers.py",
    ]
    LAYOUT: Dict[str, str] = {
        "backend/models/pyproject.toml": "[project]\nname = 'erp-models'\n",
        "backend/services/README.md": "Services.\n",
        "backend/services/platform/pyproject.toml": "[project]\nname = 'platform'\n",
        "backend/services/platform/Dockerfile": "FROM scratch\n",
        "sdk/pyproject.toml": "[project]\nname = 'erp-sdk'\n",
        "plugins/README.md": "Plugins.\n",
        "frontend/backoffice/package.json": "{}\n",
        "frontend/backoffice/Dockerfile": "FROM scratch\n",
        "frontend/mobile/package.json": "{}\n",
        "frontend/packages/ui/package.json": "{}\n",
        "infra/compose/compose.yaml": "services: {}\n",
        "infra/helm/README.md": "Helm.\n",
        "infra/terraform/README.md": "Terraform.\n",
        "packs/countries/README.md": "Countries.\n",
        "packs/sectors/README.md": "Sectors.\n",
        "bruno/platform/bruno.json": "{}\n",
    }

    def collected(self, root: Path) -> List[str]:
        result = self.run_layout_test(root, "--collect-only")
        assert result.returncode == 0, result.stdout + result.stderr
        return [line.rsplit("::", 1)[-1] for line in result.stdout.splitlines() if "::" in line]

    def write(self, root: Path, files: Dict[str, str]) -> None:
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def fixture_repository(self, root: Path, gained: Dict[str, str]) -> None:
        self.write(root, {path: (LAYOUT_ROOT / path).read_text(encoding="utf-8") for path in self.COPIED})
        self.write(root, {**self.LAYOUT, **gained})
        (root / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")

    def run_layout_test(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-p", "no:xdist", *args, self.LAYOUT_TEST],
            cwd=root,
            env={"PATH": "/usr/bin:/bin", "PYTHONPATH": str(root), "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            check=False,
        )

    @pytest.mark.parametrize(
        "gained",
        [
            {},
            {"infra/helm/Chart.yaml": "apiVersion: v2\nname: simpleerp\nversion: 0.1.0\n"},
            {"frontend/mobile/Dockerfile": "FROM scratch\n"},
            {"plugins/hello/pyproject.toml": "[project]\nname = 'hello'\n"},
            {
                "frontend/portals/customer/package.json": "{}\n",
                "frontend/portals/customer/Dockerfile": "FROM scratch\n",
            },
            {"backend/services/stock/pyproject.toml": "[project]\nname = 'stock'\n"},
        ],
        ids=["as-laid-out", "helm-gains-a-chart", "mobile-gains-an-image", "a-plugin", "a-portal", "a-service"],
    )
    def test_the_layout_test_passes_when_a_folder_gains_a_marker(self, tmp_path: Path, gained: Dict[str, str]) -> None:
        self.fixture_repository(tmp_path, gained)
        result = self.run_layout_test(tmp_path)
        assert result.returncode == 0, result.stdout + result.stderr

    def test_a_folder_that_gains_a_marker_moves_from_nothing_to_its_selection(self, tmp_path: Path) -> None:
        self.fixture_repository(tmp_path, {})
        before = self.collected(tmp_path)
        self.write(tmp_path, {"infra/helm/Chart.yaml": "apiVersion: v2\nname: simpleerp\nversion: 0.1.0\n"})
        after = self.collected(tmp_path)
        assert f"{self.WITHOUT}[infra/helm]" in before
        assert f"{self.WITH}[infra/helm]" not in before
        assert f"{self.WITHOUT}[infra/helm]" not in after
        assert f"{self.WITH}[infra/helm]" in after

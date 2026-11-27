from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import ClassVar, Dict, List

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[3]
HELM = ROOT / "infra" / "helm"
CHARTS = HELM / "charts"
CHART_NAMES = ["platform", "backoffice"]


class TestCharts:
    CHART_FILES: ClassVar[List[str]] = [
        "Chart.yaml",
        "values.yaml",
        ".helmignore",
        "templates/_helpers.tpl",
        "templates/deployment.yaml",
        "templates/service.yaml",
    ]

    def load(self, path: Path) -> Dict[str, object]:
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def chart_folders(self) -> List[str]:
        if not CHARTS.is_dir():
            return []
        return sorted(path.parent.name for path in CHARTS.glob("*/Chart.yaml"))

    def images(self) -> List[Dict[str, str]]:
        result = subprocess.run(
            [sys.executable, str(ROOT / ".github" / "scripts" / "detect_changes.py"), "--all", "--root", str(ROOT)],
            capture_output=True,
            text=True,
            check=True,
            input="",
            encoding="utf-8",
        )
        line = next(line for line in result.stdout.splitlines() if line.startswith("images="))
        return json.loads(line.split("=", 1)[1])

    def test_the_umbrella_chart_has_the_expected_fields(self) -> None:
        chart = self.load(HELM / "Chart.yaml")
        assert chart["apiVersion"] == "v2"
        assert chart["name"] == "simpleerp"
        assert chart["type"] == "application"
        assert chart["version"] == "0.1.0"
        assert chart["appVersion"] == "0.1.0"

    def test_the_umbrella_depends_on_every_chart_folder(self) -> None:
        chart = self.load(HELM / "Chart.yaml")
        names = sorted(str(dependency["name"]) for dependency in chart["dependencies"])  # type: ignore[attr-defined]
        assert names == self.chart_folders()
        assert set(CHART_NAMES) <= set(names)

    @pytest.mark.parametrize("name", CHART_NAMES)
    def test_each_dependency_is_enabled_by_its_own_condition(self, name: str) -> None:
        chart = self.load(HELM / "Chart.yaml")
        dependencies = {str(item["name"]): item for item in chart["dependencies"]}  # type: ignore[attr-defined]
        assert dependencies[name]["condition"] == f"{name}.enabled"
        assert dependencies[name]["version"] == "0.1.0"

    @pytest.mark.parametrize("name", CHART_NAMES)
    def test_a_chart_is_named_after_its_folder(self, name: str) -> None:
        chart = self.load(CHARTS / name / "Chart.yaml")
        assert chart["name"] == name
        assert chart["apiVersion"] == "v2"
        assert chart["type"] == "application"
        assert chart["version"] == "0.1.0"
        assert chart["appVersion"] == "0.1.0"

    @pytest.mark.parametrize("name", CHART_NAMES)
    def test_a_chart_has_its_required_files(self, name: str) -> None:
        missing = [file for file in self.CHART_FILES if not (CHARTS / name / file).is_file()]
        assert missing == []

    @pytest.mark.parametrize("name", CHART_NAMES)
    def test_a_chart_matches_an_image_with_a_dockerfile(self, name: str) -> None:
        images = {image["name"]: image["folder"] for image in self.images()}
        assert name in images
        assert (ROOT / images[name] / "Dockerfile").is_file()
        assert (CHARTS / name / "Chart.yaml").is_file()

    def test_every_chart_folder_matches_an_image(self) -> None:
        image_names = {image["name"] for image in self.images()}
        assert set(self.chart_folders()) <= image_names
        assert self.chart_folders() != []

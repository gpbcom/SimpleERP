from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from xml.etree import ElementTree

import pytest

REPOSITORY = Path(__file__).resolve().parents[3]
SCRIPT = REPOSITORY / ".github" / "scripts" / "check_helm.sh"
HELM_ROOT = REPOSITORY / "infra" / "helm"
TAG = "abc1234"
NEEDS_TOOLS = pytest.mark.skipif(
    shutil.which("helm") is None or shutil.which("kubeconform") is None,
    reason="helm and kubeconform are not on the PATH.",
)


class TestCheckHelm:
    def run_script(
        self, arguments: List[str], env: Optional[Dict[str, str]] = None
    ) -> subprocess.CompletedProcess[str]:
        bash = shutil.which("bash")
        assert bash is not None
        return subprocess.run(
            [bash, str(SCRIPT), *arguments],
            capture_output=True,
            text=True,
            check=False,
            env=env if env is not None else dict(os.environ),
            cwd=REPOSITORY,
        )

    def copy_chart(self, tmp_path: Path) -> Path:
        root = tmp_path / "helm"
        shutil.copytree(HELM_ROOT, root)
        return root

    def first_deployment(self, root: Path) -> Path:
        templates = sorted(root.glob("templates/*.yaml")) + sorted(root.glob("charts/*/templates/*.yaml"))
        deployments = [path for path in templates if "kind: Deployment" in path.read_text(encoding="utf-8")]
        assert deployments, "The chart holds no Deployment template."
        return deployments[0]

    @pytest.mark.parametrize("arguments", [[], ["one"], ["one", "two"], ["a", "b", "c", "d"]])
    def test_a_wrong_argument_count_exits_2_with_the_usage_line(self, arguments: List[str]) -> None:
        result = self.run_script(arguments)
        assert result.returncode == 2
        assert result.stderr.startswith("usage:")

    def test_a_missing_helm_exits_1_and_is_named(self, tmp_path: Path) -> None:
        bin_dir = tmp_path / "bin"
        bin_dir.mkdir()
        bash = shutil.which("bash")
        assert bash is not None
        (bin_dir / "bash").symlink_to(bash)
        result = self.run_script([str(HELM_ROOT), TAG, str(tmp_path / "reports")], env={"PATH": str(bin_dir)})
        assert result.returncode == 1
        assert "helm" in result.stderr

    @NEEDS_TOOLS
    def test_the_real_chart_passes_and_writes_a_junit_report(self, tmp_path: Path) -> None:
        reports = tmp_path / "reports"
        result = self.run_script([str(HELM_ROOT), TAG, str(reports)])
        assert result.returncode == 0, result.stderr
        root = ElementTree.parse(reports / "helm.xml").getroot()
        assert root.tag in {"testsuites", "testsuite"}

    @NEEDS_TOOLS
    def test_a_broken_template_fails(self, tmp_path: Path) -> None:
        root = self.copy_chart(tmp_path)
        template = self.first_deployment(root)
        template.write_text(
            template.read_text(encoding="utf-8") + '\n{{ include "missing.helper" . }}\n', encoding="utf-8"
        )
        result = self.run_script([str(root), TAG, str(tmp_path / "reports")])
        assert result.returncode != 0

    @NEEDS_TOOLS
    def test_an_unknown_field_in_the_deployment_spec_fails_the_strict_schema_check(self, tmp_path: Path) -> None:
        root = self.copy_chart(tmp_path)
        template = self.first_deployment(root)
        text = template.read_text(encoding="utf-8")
        assert "\nspec:\n" in text
        template.write_text(text.replace("\nspec:\n", "\nspec:\n  unknownField: true\n", 1), encoding="utf-8")
        result = self.run_script([str(root), TAG, str(tmp_path / "reports")])
        assert result.returncode != 0

from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import (
    HELM_KEY,
    REPOSITORY_KEY,
    SALES,
    detect,
    nothing,
    outputs,
    run_detector,
    write_repo,
)


class TestHelmChanges:
    HELM_PATHS = ["infra/helm/charts/platform/templates/deployment.yaml", "infra/helm/values.yaml"]

    @pytest.mark.parametrize("path", HELM_PATHS)
    def test_a_change_under_infra_helm_selects_the_helm_check_and_the_repository_tests(
        self, tmp_path: Path, path: str
    ) -> None:
        assert detect(tmp_path, [path]) == {**nothing(), HELM_KEY: "true", REPOSITORY_KEY: "true"}

    @pytest.mark.parametrize("path", HELM_PATHS)
    def test_without_the_umbrella_chart_the_helm_check_is_not_selected(self, tmp_path: Path, path: str) -> None:
        write_repo(tmp_path)
        (tmp_path / "infra/helm/Chart.yaml").unlink()
        result = run_detector(tmp_path, [path])
        assert result.returncode == 0, result.stderr
        assert outputs(result) == nothing()

    @pytest.mark.parametrize("path", ["infra/terraform/ovhcloud/main.tf", f"{SALES}/src/sales/x.py"])
    def test_a_change_outside_infra_helm_keeps_the_helm_check_off(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path])[HELM_KEY] == "false"

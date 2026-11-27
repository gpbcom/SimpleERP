from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import List

# First-party imports
from tests.harness.checks.helpers import call

CHANGED = ["infra/helm/charts/sales/templates/deployment.yaml"]


def helm_run(root: Path, changed: List[str], installed: bool) -> List[List[str]]:
    setup = (
        f"checks.ROOT = Path({str(root)!r}); commands = []\n"
        "checks.run = lambda command, cwd=None, env=None: (commands.append(command) or (0, ''))\n"
        f"checks.shutil.which = lambda name: {'/usr/bin/helm' if installed else None!r}\n"
        f"c = checks.Checks('T9.03', Path({str(root)!r}))\n"
        f"checks.helm_checks(c, {changed!r})"
    )
    value = call("[commands, c.not_applicable]", setup)
    assert isinstance(value, list)
    return value


def charts(root: Path) -> Path:
    for chart in ("infra/helm", "infra/helm/charts/sales"):
        (root / chart).mkdir(parents=True, exist_ok=True)
        (root / chart / "Chart.yaml").write_text("name: x\n", encoding="utf-8")
    return root


class TestChecksHelm:
    def test_a_changed_chart_is_linted_at_its_nearest_chart_folder(self, tmp_path: Path) -> None:
        commands, _ = helm_run(charts(tmp_path), CHANGED, True)
        assert commands == [["helm", "lint", "infra/helm/charts/sales"]]

    def test_a_changed_chart_without_helm_on_the_path_is_not_applicable(self, tmp_path: Path) -> None:
        commands, skipped = helm_run(charts(tmp_path), CHANGED, False)
        assert commands == []
        assert skipped == ["helm lint: helm is not installed on the PATH"]

    def test_no_chart_change_runs_nothing(self, tmp_path: Path) -> None:
        commands, skipped = helm_run(charts(tmp_path), ["infra/terraform/main.tf"], True)
        assert commands == []
        assert skipped == ["helm lint: no Helm chart change"]

from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import List

# First-party imports
from tests.harness.checks.helpers import call

CHANGED = ["frontend/backoffice/src/main.ts"]


def front_end_run(root: Path, changed: List[str]) -> List[List[str]]:
    setup = (
        f"checks.ROOT = Path({str(root)!r}); commands = []\n"
        "checks.run = lambda command, cwd=None, env=None: (commands.append(command) or (0, ''))\n"
        f"c = checks.Checks('T9.03', Path({str(root)!r}))\n"
        f"checks.typescript_checks(c, {changed!r})"
    )
    value = call("[commands, c.not_applicable]", setup)
    assert isinstance(value, list)
    return value


def write(root: Path, *names: str) -> Path:
    for name in names:
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text("{}", encoding="utf-8")
    return root


class TestChecksFrontEnd:
    def test_no_front_end_change_runs_nothing(self, tmp_path: Path) -> None:
        commands, skipped = front_end_run(tmp_path, ["backend/services/sales/src/erp_sales/a.py"])
        assert commands == []
        assert skipped == ["typescript: no front-end change"]

    def test_a_front_end_change_without_a_pnpm_workspace_is_not_applicable(self, tmp_path: Path) -> None:
        commands, skipped = front_end_run(tmp_path, CHANGED)
        assert commands == []
        assert any("no pnpm workspace" in entry for entry in skipped)

    def test_a_workspace_without_a_package_only_installs(self, tmp_path: Path) -> None:
        commands, skipped = front_end_run(write(tmp_path, "package.json", "pnpm-workspace.yaml"), CHANGED)
        assert commands == [["pnpm", "install", "--frozen-lockfile"]]
        assert len(skipped) == 3

    def test_every_front_end_package_kind_is_a_workspace_package(self, tmp_path: Path) -> None:
        for package in (
            "frontend/backoffice/package.json",
            "frontend/portals/customer/package.json",
            "frontend/packages/ui/package.json",
        ):
            root = write(tmp_path / package.split("/")[1], "pnpm-workspace.yaml", package)
            commands, _ = front_end_run(root, CHANGED)
            assert ["pnpm", "-r", "--if-present", "typecheck"] in commands

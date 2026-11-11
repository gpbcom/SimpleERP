from __future__ import annotations

import shutil
from pathlib import Path

from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.service.setup.unit_installer import UnitInstaller
from pr_watch.storage.files.text_files import TextFiles
from tests.stand_ins.git_sandbox import GitSandbox


class TestUnitInstaller:
    def test_the_units_run_the_skill_of_the_main_working_tree(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path)
        clone = sandbox.build(conflict=False)
        sandbox.git(clone, "worktree", "add", "-q", str(tmp_path / "tree"), "HEAD")
        skill = tmp_path / "tree" / ".claude" / "skills" / "pr-watch"
        shutil.copytree(WatchSettings().units_dir, skill / "systemd")
        written = UnitInstaller(skill / "systemd", skill, TextFiles()).install(tmp_path / "units")
        assert [path.name for path in written] == ["claude-pr-watch.service", "claude-pr-watch.timer"]
        service = written[0].read_text(encoding="utf-8")
        main_skill = clone.resolve() / ".claude" / "skills" / "pr-watch"
        assert f"ExecStart={main_skill}/bin/pr-watch once" in service
        assert f"WorkingDirectory={clone.resolve()}" in service
        assert "OnCalendar=Mon..Fri *-*-* 08..19:00/10:00" in written[1].read_text(encoding="utf-8")

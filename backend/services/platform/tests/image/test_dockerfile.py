from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pytest


class TestDockerfile:
    DOCKERFILE: ClassVar[Path] = Path(__file__).resolve().parents[2] / "Dockerfile"

    def runtime_stage(self) -> str:
        text = self.DOCKERFILE.read_text(encoding="utf-8")
        return text.rsplit("FROM ", 1)[1]

    def test_the_runtime_stage_upgrades_packages_after_updating_the_index(self) -> None:
        stage = self.runtime_stage()

        assert "apt-get update" in stage
        assert "apt-get upgrade" in stage
        assert stage.index("apt-get update") < stage.index("apt-get upgrade")

    def test_the_runtime_stage_removes_the_apt_lists(self) -> None:
        assert "/var/lib/apt/lists/*" in self.runtime_stage()

    def test_the_runtime_stage_uninstalls_pip(self) -> None:
        assert "pip uninstall -y pip" in self.runtime_stage()

    @pytest.mark.parametrize("command", ["apt-get upgrade", "/var/lib/apt/lists/*", "pip uninstall -y pip"])
    def test_the_runtime_stage_does_it_before_switching_user(self, command: str) -> None:
        stage = self.runtime_stage()

        assert command in stage
        assert "USER " in stage
        assert stage.index(command) < stage.index("USER ")

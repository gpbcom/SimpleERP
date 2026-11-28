from __future__ import annotations

from pathlib import Path
from typing import List

import pytest

from tests.infra.compose.helpers import COMPOSE_DIR, docker_calls, profile_settings, run_script, stand_in_machine


class TestInstall:
    def compose_calls(self, folder: Path) -> List[List[str]]:
        return [argv for argv in docker_calls(folder) if "compose" in argv]

    def files_of(self, argv: List[str]) -> List[Path]:
        return [Path(argv[i + 1]).resolve() for i, word in enumerate(argv) if word == "-f"]

    def up_calls(self, folder: Path) -> List[List[str]]:
        return [argv for argv in self.compose_calls(folder) if "up" in argv]

    def test_a_machine_under_the_budget_installs(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path)

        result = run_script("install.sh", [], env)

        assert result.returncode == 0, result.stderr
        ups = self.up_calls(tmp_path)
        assert len(ups) == 1
        up = ups[0]
        overlay = (COMPOSE_DIR / profile_settings()["LAPTOP_COMPOSE_FILE"]).resolve()
        base = (COMPOSE_DIR / "compose.yaml").resolve()
        assert overlay.exists()
        assert base.exists()
        for call in self.compose_calls(tmp_path):
            assert self.files_of(call) == [base, overlay]
        assert "--detach" in up
        assert "--wait" in up
        assert "Installed the laptop profile with the AI off." in result.stdout

    @pytest.mark.parametrize("args", [[], ["--ai", "off"]])
    def test_with_the_ai_off_milvus_is_not_installed(self, tmp_path: Path, args: List[str]) -> None:
        env = stand_in_machine(tmp_path)

        result = run_script("install.sh", args, env)

        assert result.returncode == 0, result.stderr
        up = self.up_calls(tmp_path)[0]
        assert "--profile" not in up
        assert "ai" not in up

    def test_with_the_ai_on_the_ai_profile_is_installed(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path)

        result = run_script("install.sh", ["--ai", "on"], env)

        assert result.returncode == 0, result.stderr
        up = self.up_calls(tmp_path)[0]
        assert up[up.index("--profile") + 1] == "ai"
        assert "Installed the laptop profile with the AI on." in result.stdout

    def test_a_machine_too_small_is_told_so(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path, memory_mib=4096)

        result = run_script("install.sh", [], env)

        assert result.returncode == 1
        assert "too small" in result.stderr
        assert self.compose_calls(tmp_path) == []

    def test_docker_not_running_stops_the_install(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path, docker_running=False)

        result = run_script("install.sh", [], env)

        assert result.returncode == 2
        assert self.compose_calls(tmp_path) == []

    def test_a_profile_that_does_not_start_is_reported(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path, up_exit=1)

        result = run_script("install.sh", [], env)

        assert result.returncode != 0
        assert "The laptop profile did not start." in result.stderr

    @pytest.mark.parametrize("args", [["--ai", "maybe"], ["--unknown"]])
    def test_a_bad_argument_is_refused(self, tmp_path: Path, args: List[str]) -> None:
        env = stand_in_machine(tmp_path)

        result = run_script("install.sh", args, env)

        assert result.returncode == 64
        assert result.stderr.strip() != ""
        assert docker_calls(tmp_path) == []

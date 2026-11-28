from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Dict, List, Tuple

import pytest

from tests.infra.compose.helpers import COMPOSE_DIR, docker_calls, profile_settings, run_script, stand_in_machine

VERBS = ("up", "ps", "stats", "down")
THREE = {"backoffice": "20.5MiB / 15.5GiB", "platform": "300MiB / 15.5GiB", "postgres": "1.5GiB / 15.5GiB"}


class TestMeasureMemory:
    def verbs(self, calls: List[List[str]]) -> List[str]:
        found: List[str] = []
        for argv in calls:
            for verb in VERBS:
                if verb in argv:
                    found.append(verb)
                    break
        return found

    def call_of(self, calls: List[List[str]], verb: str) -> List[str]:
        return next(argv for argv in calls if verb in argv)

    def measure(self, tmp_path: Path, stats: Dict[str, str], up_exit: int = 0) -> Tuple[str, str, int]:
        env = stand_in_machine(tmp_path, stats=stats, up_exit=up_exit)
        done = run_script("measure-memory.sh", ["--rest-s", "0"], env)
        return done.stdout, done.stderr, done.returncode

    def test_three_containers_give_their_lines_and_the_total(self, tmp_path: Path) -> None:
        stdout, _, code = self.measure(tmp_path, THREE)
        lines = stdout.strip().splitlines()
        today = datetime.now(UTC).date().isoformat()
        assert code == 0
        assert lines[0].startswith("Memory at rest of the laptop profile on ")
        assert today in lines[0]
        assert "AI off" in lines[0]
        assert lines[1:] == [
            "backoffice: 20.5 MiB",
            "platform: 300.0 MiB",
            "postgres: 1536.0 MiB",
            "Total: 1856.5 MiB",
        ]

    @pytest.mark.parametrize(
        ("usage", "expected"),
        [("512KiB", "0.5"), ("1048576B", "1.0"), ("2GiB", "2048.0"), ("12.3MiB", "12.3")],
    )
    def test_units_are_converted_to_mebibytes(self, tmp_path: Path, usage: str, expected: str) -> None:
        stdout, _, code = self.measure(tmp_path, {"platform": f"{usage} / 15.5GiB"})
        assert code == 0
        assert f"platform: {expected} MiB" in stdout.splitlines()
        assert f"Total: {expected} MiB" in stdout.splitlines()

    def test_the_calls_come_in_order_up_ps_stats_down(self, tmp_path: Path) -> None:
        self.measure(tmp_path, THREE)
        assert self.verbs(docker_calls(tmp_path)) == ["up", "ps", "stats", "down"]

    def test_up_uses_the_base_file_and_the_laptop_overlay_and_waits(self, tmp_path: Path) -> None:
        self.measure(tmp_path, THREE)
        calls = docker_calls(tmp_path)
        up = self.call_of(calls, "up")
        base = str(COMPOSE_DIR / "compose.yaml")
        laptop = str(COMPOSE_DIR / profile_settings()["LAPTOP_COMPOSE_FILE"])
        for call in [argv for argv in calls if "compose" in argv]:
            files = [call[i + 1] for i, word in enumerate(call) if word == "-f"]
            assert [str(Path(f).resolve()) for f in files] == [str(Path(base).resolve()), str(Path(laptop).resolve())]
        assert "--detach" in up
        assert "--wait" in up

    def test_no_call_enables_the_ai_profile(self, tmp_path: Path) -> None:
        self.measure(tmp_path, THREE)
        for argv in docker_calls(tmp_path):
            assert "--profile" not in argv
            assert "ai" not in argv

    def test_a_stack_that_does_not_start_is_reported_and_taken_down(self, tmp_path: Path) -> None:
        _, stderr, code = self.measure(tmp_path, THREE, up_exit=1)
        verbs = self.verbs(docker_calls(tmp_path))
        assert code == 1
        assert "The laptop profile did not start." in stderr
        assert "stats" not in verbs
        assert verbs[-1] == "down"

    def test_a_bad_argument_gives_exit_64(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path, stats=THREE)
        done = run_script("measure-memory.sh", ["--bogus"], env)
        assert done.returncode == 64

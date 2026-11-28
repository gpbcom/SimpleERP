from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest

from tests.infra.compose.helpers import profile_settings, run_script, stand_in_machine


class TestCheckMachine:
    def test_the_settings_hold_the_budget(self) -> None:
        settings = profile_settings()
        assert int(settings["MEMORY_MIN_MIB"]) == 8192
        assert int(settings["CPUS_MIN"]) == 4
        assert int(settings["DISK_FREE_MIN_GIB"]) == 20

    def test_a_machine_above_the_budget_fits(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path)
        result = run_script("check-machine.sh", [], env)
        assert result.returncode == 0
        assert "The machine fits the laptop profile:" in result.stdout
        assert "MiB of memory" in result.stdout
        assert "cores" in result.stdout
        assert "GiB of free disk." in result.stdout

    def test_a_machine_exactly_at_every_minimum_fits(self, tmp_path: Path) -> None:
        settings = profile_settings()
        memory = int(settings["MEMORY_MIN_MIB"])
        cpus = int(settings["CPUS_MIN"])
        disk = int(settings["DISK_FREE_MIN_GIB"])
        env = stand_in_machine(tmp_path, memory_mib=memory, cpus=cpus, disk_free_gib=disk)
        result = run_script("check-machine.sh", [], env)
        assert result.returncode == 0
        assert (
            f"The machine fits the laptop profile: {memory} MiB of memory, {cpus} cores, {disk} GiB of free disk."
            in result.stdout
        )

    @pytest.mark.parametrize(
        ("name", "minimum_key", "short_key"),
        [
            ("memory", "MEMORY_MIN_MIB", "memory_mib"),
            ("cores", "CPUS_MIN", "cpus"),
            ("disk", "DISK_FREE_MIN_GIB", "disk_free_gib"),
        ],
    )
    def test_one_value_below_its_minimum_makes_the_machine_too_small(
        self, tmp_path: Path, name: str, minimum_key: str, short_key: str
    ) -> None:
        minimum = int(profile_settings()[minimum_key])
        found = minimum - 1
        messages: Dict[str, str] = {
            "memory": f"Not enough memory: {found} MiB. The laptop profile needs at least {minimum} MiB.",
            "cores": f"Not enough cores: {found}. The laptop profile needs at least {minimum}.",
            "disk": f"Not enough free disk: {found} GiB. The laptop profile needs at least {minimum} GiB.",
        }
        env = stand_in_machine(tmp_path, **{short_key: found})
        result = run_script("check-machine.sh", [], env)
        assert result.returncode == 1
        assert messages[name] in result.stderr
        assert "This machine is too small for the laptop profile." in result.stderr
        for other, message in messages.items():
            if other != name:
                assert message.split(":")[0] not in result.stderr

    def test_a_machine_short_on_all_three_lists_the_three_shortfalls(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path, memory_mib=1024, cpus=1, disk_free_gib=1)
        result = run_script("check-machine.sh", [], env)
        assert result.returncode == 1
        assert "Not enough memory: 1024 MiB." in result.stderr
        assert "Not enough cores: 1." in result.stderr
        assert "Not enough free disk: 1 GiB." in result.stderr
        assert "This machine is too small for the laptop profile." in result.stderr

    def test_docker_not_running_cannot_be_checked(self, tmp_path: Path) -> None:
        env = stand_in_machine(tmp_path, docker_running=False)
        result = run_script("check-machine.sh", [], env)
        assert result.returncode == 2
        assert "Cannot check the machine: Docker is not installed or not running." in result.stderr

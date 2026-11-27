from __future__ import annotations

from pathlib import Path
from typing import List

import pytest

from tests.infra.compose.profiles.helpers import (
    LAPTOP,
    ONE_SERVER,
    compose,
    docker_available,
    sandbox,
    services_of,
)


class TestLaptopProfile:
    def published(self) -> List[object]:
        ports: List[object] = []
        for service in services_of(LAPTOP).values():
            ports.extend(service.get("ports") or [])
        return ports

    def test_the_override_sets_no_image_and_no_build(self) -> None:
        assert LAPTOP.is_file()
        for name, service in services_of(LAPTOP).items():
            assert "image" not in service, name
            assert "build" not in service, name

    def test_the_override_only_names_services_of_the_one_server_profile(self) -> None:
        assert LAPTOP.is_file()
        assert set(services_of(LAPTOP)) <= set(services_of(ONE_SERVER))

    def test_every_published_port_is_bound_to_the_loopback_address(self) -> None:
        assert LAPTOP.is_file()
        for port in self.published():
            if isinstance(port, dict):
                assert port.get("host_ip") == "127.0.0.1", port
            else:
                assert str(port).startswith("127.0.0.1:"), port

    def test_the_laptop_profile_runs_the_same_images_as_the_one_server_profile(self, tmp_path: Path) -> None:
        if not docker_available():
            pytest.skip("docker compose is not installed")
        directory = sandbox(tmp_path)
        alone = compose(directory, ["compose.yaml"], "config", "--images")
        merged = compose(directory, ["compose.yaml", "compose.laptop.yaml"], "config", "--images")
        assert alone.returncode == 0, alone.stderr
        assert merged.returncode == 0, merged.stderr
        assert sorted(merged.stdout.split()) == sorted(alone.stdout.split())

from __future__ import annotations

import shutil
import subprocess
from typing import Dict, List

import pytest

from tests.infra.compose.e2e.helpers import (
    BUILT_SERVICES,
    COMPOSE,
    PROVIDED_VARIABLES,
    ROOT,
    SERVICES,
    depends_on,
    environment,
    healthcheck_command,
    service,
    services,
    variables_without_default,
)


class TestComposeE2e:
    def test_the_file_is_at_the_repository_root(self) -> None:
        assert COMPOSE == ROOT / "compose.e2e.yaml"
        assert COMPOSE.is_file()

    def test_it_declares_exactly_the_platform_the_backoffice_and_postgres(self) -> None:
        assert sorted(services()) == sorted(SERVICES)

    @pytest.mark.parametrize("name", ["platform", "backoffice"])
    def test_a_built_service_uses_the_image_of_the_workflows(self, name: str) -> None:
        assert service(name)["image"] == f"${{ERP_IMAGE_PREFIX}}-{name}:${{ERP_IMAGE_TAG}}"

    @pytest.mark.parametrize("name", sorted(BUILT_SERVICES))
    def test_a_built_service_builds_from_the_repository_root(self, name: str) -> None:
        build = service(name)["build"]
        assert isinstance(build, dict)
        assert build["context"] == "."
        assert build["dockerfile"] == BUILT_SERVICES[name]

    def test_postgres_is_the_official_image_pinned_by_digest(self) -> None:
        image = service("postgres")["image"]
        assert isinstance(image, str)
        assert image.split("@")[0].split(":")[0].endswith("postgres")
        assert "@sha256:" in image
        assert "build" not in service("postgres")

    @pytest.mark.parametrize("name", SERVICES)
    def test_every_service_has_a_healthcheck(self, name: str) -> None:
        assert service(name)["healthcheck"]

    def test_the_platform_healthcheck_calls_the_health_endpoint(self) -> None:
        assert "/v1/health" in healthcheck_command("platform")

    def test_the_postgres_healthcheck_uses_pg_isready(self) -> None:
        assert "pg_isready" in healthcheck_command("postgres")

    @pytest.mark.parametrize(
        ("name", "dependency"),
        [("platform", "postgres"), ("backoffice", "platform")],
    )
    def test_a_service_waits_for_its_dependency_to_be_healthy(self, name: str, dependency: str) -> None:
        assert depends_on(name)[dependency]["condition"] == "service_healthy"

    def test_postgres_publishes_no_port(self) -> None:
        assert not service("postgres").get("ports")

    @pytest.mark.parametrize("name", SERVICES)
    def test_no_password_or_secret_holds_a_literal_value(self, name: str) -> None:
        for key, value in environment(name).items():
            if "PASSWORD" in key or "SECRET" in key:
                assert value == "" or value.startswith("$") or value.endswith("_FILE"), key

    def test_only_the_two_variables_of_the_workflows_have_no_default(self) -> None:
        assert variables_without_default() <= PROVIDED_VARIABLES

    def test_docker_compose_resolves_the_file_with_only_those_two_variables(self) -> None:
        if shutil.which("docker") is None:
            pytest.skip("docker is not on the PATH")
        env: Dict[str, str] = {
            "PATH": "/usr/bin:/bin:/usr/local/bin",
            "ERP_IMAGE_PREFIX": "ghcr.io/o/r",
            "ERP_IMAGE_TAG": "t1",
        }
        base: List[str] = ["docker", "compose", "-f", str(COMPOSE)]
        assert COMPOSE.is_file()
        subprocess.run([*base, "config", "--quiet"], env=env, check=True, capture_output=True, cwd=ROOT)
        listed = subprocess.run(
            [*base, "config", "--images"], env=env, check=True, capture_output=True, text=True, cwd=ROOT
        ).stdout.split()
        assert "ghcr.io/o/r-platform:t1" in listed
        assert "ghcr.io/o/r-backoffice:t1" in listed
        assert str(service("postgres")["image"]) in listed

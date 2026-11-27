from __future__ import annotations

from pathlib import Path
from typing import List

import pytest

from tests.infra.compose.profiles.helpers import (
    GITIGNORE,
    ONE_SERVER,
    SERVICES,
    compose,
    docker_available,
    load,
    sandbox,
    services_of,
    variable_names,
)


class TestOneServerProfile:
    def environment_of(self, name: str) -> dict:
        environment = services_of(ONE_SERVER)[name].get("environment") or {}
        if isinstance(environment, list):
            environment = dict(item.partition("=")[::2] for item in environment)
        assert isinstance(environment, dict)
        return environment

    def test_the_profile_declares_exactly_the_platform_the_back_office_and_postgres(self) -> None:
        assert ONE_SERVER.is_file()
        assert sorted(services_of(ONE_SERVER)) == SERVICES

    @pytest.mark.parametrize("name", ["platform", "backoffice"])
    def test_the_application_images_come_from_the_prefix_and_the_tag(self, name: str) -> None:
        image = str(services_of(ONE_SERVER)[name]["image"])
        assert variable_names(image) == ["ERP_IMAGE_PREFIX", "ERP_IMAGE_TAG"]
        assert f"/{name}:" in image or f"-{name}:" in image

    @pytest.mark.parametrize("name", ["platform", "backoffice"])
    def test_the_application_services_are_never_built(self, name: str) -> None:
        assert "build" not in services_of(ONE_SERVER)[name]

    def test_the_postgres_image_is_pinned_by_digest(self) -> None:
        assert "@sha256:" in str(services_of(ONE_SERVER)["postgres"]["image"])

    @pytest.mark.parametrize("name", SERVICES)
    def test_every_service_has_a_healthcheck(self, name: str) -> None:
        assert services_of(ONE_SERVER)[name].get("healthcheck")

    @pytest.mark.parametrize("name", SERVICES)
    def test_every_service_restarts_unless_stopped(self, name: str) -> None:
        assert services_of(ONE_SERVER)[name].get("restart") == "unless-stopped"

    def test_postgres_keeps_its_data_on_a_named_volume(self) -> None:
        declared = load(ONE_SERVER).get("volumes") or {}
        assert isinstance(declared, dict)
        volumes: List[object] = list(services_of(ONE_SERVER)["postgres"].get("volumes") or [])
        sources = [
            str(volume.get("source")) if isinstance(volume, dict) else str(volume).split(":")[0] for volume in volumes
        ]
        assert any(source in declared for source in sources)

    def test_postgres_publishes_no_port(self) -> None:
        assert not services_of(ONE_SERVER)["postgres"].get("ports")

    def test_the_postgres_password_comes_from_a_secret_file_under_the_secrets_folder(self) -> None:
        assert "POSTGRES_PASSWORD_FILE" in self.environment_of("postgres")
        assert "POSTGRES_PASSWORD" not in self.environment_of("postgres")
        secrets = load(ONE_SERVER)["secrets"]
        assert isinstance(secrets, dict)
        used = [name for name in services_of(ONE_SERVER)["postgres"].get("secrets") or [] if name in secrets]
        assert used
        for name in used:
            assert str(secrets[name]["file"]).removeprefix("./").startswith("secrets/")

    @pytest.mark.parametrize("name", SERVICES)
    def test_no_secret_or_password_variable_holds_a_literal_value(self, name: str) -> None:
        for key, value in self.environment_of(name).items():
            if "PASSWORD" in key.upper() or "SECRET" in key.upper():
                assert key.endswith("_FILE") or value in (None, "") or str(value).startswith("${"), key

    def test_the_secrets_folder_is_ignored_by_git(self) -> None:
        assert GITIGNORE.is_file()
        lines = [line.strip() for line in GITIGNORE.read_text(encoding="utf-8").splitlines()]
        assert any(line in ("secrets/", "/secrets/", "secrets", "/secrets") for line in lines)

    def test_one_command_with_only_the_image_tag_is_enough(self, tmp_path: Path) -> None:
        if not docker_available():
            pytest.skip("docker compose is not installed")
        directory = sandbox(tmp_path)
        result = compose(directory, ["compose.yaml"], "config", "--quiet")
        assert result.returncode == 0, result.stderr

from __future__ import annotations

# Standard library imports
import os
import shutil
import subprocess
from pathlib import Path
from typing import ClassVar, Dict, List

# Third-party imports
import pytest

# First-party imports
from tests.infra.compose.images.helpers import (
    E2E,
    LAPTOP,
    ONE_SERVER,
    PREFIX,
    ROOT,
    SERVICES,
    TAG,
    environment,
    image_of,
    resolve,
)


class TestSameImages:
    FILES: ClassVar[Dict[str, List[Path]]] = {
        "e2e": [E2E],
        "one-server": [ONE_SERVER],
        "laptop": [ONE_SERVER, LAPTOP],
    }

    def images(self, service: str) -> Dict[str, str]:
        env = environment()
        return {name: image_of(paths, service, env) for name, paths in self.FILES.items()}

    @pytest.mark.parametrize("service", SERVICES)
    def test_the_stages_and_the_profiles_resolve_a_service_to_the_same_image(self, service: str) -> None:
        images = self.images(service)
        assert len(set(images.values())) == 1, images

    @pytest.mark.parametrize("service", ["platform", "backoffice"])
    def test_an_application_image_carries_the_prefix_and_the_commit_tag(self, service: str) -> None:
        for image in self.images(service).values():
            assert image.startswith(f"{PREFIX}-{service}:")
            assert image.endswith(f":{TAG}")

    def test_the_postgresql_image_is_pinned_by_digest_in_every_file(self) -> None:
        for image in self.images("postgres").values():
            assert "@sha256:" in image

    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("${ERP_IMAGE_TAG}", TAG),
            ("${MISSING:-fallback}", "fallback"),
            ("${ERP_IMAGE_PREFIX:-other}-platform", f"{PREFIX}-platform"),
        ],
    )
    def test_the_resolver_reads_the_compose_variable_forms(self, text: str, expected: str) -> None:
        assert resolve(text, environment()) == expected

    def test_the_resolver_refuses_a_required_variable_that_is_unset(self) -> None:
        with pytest.raises(KeyError):
            resolve("${MISSING:?must be set}", environment())

    def test_docker_compose_lists_the_same_images_for_the_three_files(self) -> None:
        if shutil.which("docker") is None:
            pytest.skip("docker is not on the PATH")
        env = {**os.environ, **environment()}
        listed: Dict[str, List[str]] = {}
        for name, paths in self.FILES.items():
            command = ["docker", "compose"]
            for path in paths:
                command += ["-f", str(path)]
            command += ["config", "--images"]
            result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, check=True)
            listed[name] = sorted(line for line in result.stdout.splitlines() if line)
        assert listed["e2e"] == listed["one-server"] == listed["laptop"]

from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import ClassVar, Dict, Iterator, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest


@pytest.mark.timeout(900)
class TestImage:
    """The platform image, built and run once for the class, then removed with its container.

    Notes:
        - **Each run tags its image ``simpleerp-platform:test-<pid>`` and labels its image and its container with its
          process id**, so that two runs at once never remove each other's image.
        - An image or a container of this test whose process is gone, or the ``simpleerp-platform:test`` image tagged
          before this naming, is a leftover: a killed run could not remove it, so the next run removes it first.
    """

    REPOSITORY: ClassVar[str] = "simpleerp-platform"
    TAG_PREFIX: ClassVar[str] = "test"
    PID_LABEL: ClassVar[str] = "org.simpleerp.test-pid"
    DOCKERFILE: ClassVar[str] = "backend/services/platform/Dockerfile"
    ROOT: ClassVar[Path] = Path(__file__).resolve().parents[5]
    START_TIMEOUT_S: ClassVar[int] = 60
    BUILD_TIMEOUT_S: ClassVar[int] = 800
    DOCKER_TIMEOUT_S: ClassVar[int] = 60
    CLEANUP_TEST: ClassVar[str] = "test_the_class_leaves_no_image_and_no_container_behind"

    def tag(self) -> str:
        return f"{self.REPOSITORY}:{self.TAG_PREFIX}-{os.getpid()}"

    def docker(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["docker", *arguments], capture_output=True, text=True, timeout=self.DOCKER_TIMEOUT_S, check=False
        )

    def skip_without_docker(self) -> None:
        if shutil.which("docker") is None:
            pytest.skip("The environment has no Docker: the docker command is missing.")
        if self.docker("info").returncode != 0:
            pytest.skip("The environment has no Docker: its daemon does not answer.")

    def is_left_over(self, pid: Optional[int]) -> bool:
        if pid is None:
            return True
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return True
        except PermissionError:
            return False
        return False

    def owner(self, value: str) -> Optional[int]:
        suffix = value.removeprefix(f"{self.TAG_PREFIX}-")
        return int(suffix) if suffix.isdigit() else None

    def left_over_images(self) -> List[str]:
        listed = self.docker("images", "--filter", f"reference={self.REPOSITORY}", "--format", "{{.Tag}}")
        tags = [line.strip() for line in listed.stdout.splitlines() if line.strip()]
        return sorted(
            f"{self.REPOSITORY}:{tag}"
            for tag in tags
            if (tag == self.TAG_PREFIX or tag.startswith(f"{self.TAG_PREFIX}-")) and self.is_left_over(self.owner(tag))
        )

    def left_over_containers(self) -> List[str]:
        label = f'{{{{.Label "{self.PID_LABEL}"}}}}'
        listed = self.docker("ps", "-a", "--filter", f"label={self.PID_LABEL}", "--format", f"{{{{.ID}}}} {label}")
        rows = [line.split() for line in listed.stdout.splitlines() if line.strip()]
        return sorted(row[0] for row in rows if self.is_left_over(self.owner(row[1]) if len(row) > 1 else None))

    def remove_left_overs(self) -> None:
        containers = self.left_over_containers()
        if containers:
            self.docker("rm", "-f", *containers)
        images = self.left_over_images()
        if images:
            self.docker("rmi", *images)

    def remove_own(self) -> None:
        listed = self.docker("ps", "-aq", "--filter", f"label={self.PID_LABEL}={os.getpid()}")
        containers = [line.strip() for line in listed.stdout.splitlines() if line.strip()]
        if containers:
            self.docker("rm", "-f", *containers)
        self.docker("rmi", self.tag())

    def free_port(self) -> int:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 0))
            return int(sock.getsockname()[1])

    def get(self, port: int, path: str) -> Tuple[int, str, str]:
        url = f"http://127.0.0.1:{port}{path}"
        try:
            with urlopen(url, timeout=5) as response:
                return response.status, response.headers.get("content-type", ""), response.read().decode("utf-8")
        except HTTPError as error:
            return error.code, error.headers.get("content-type", ""), error.read().decode("utf-8")

    def wait_for_health(self, port: int) -> Tuple[int, str, str]:
        deadline = time.monotonic() + self.START_TIMEOUT_S
        last_error = "no answer"
        while time.monotonic() < deadline:
            try:
                return self.get(port, "/v1/health")
            except (URLError, ConnectionError, TimeoutError, OSError) as error:
                last_error = type(error).__name__
                time.sleep(1)
        raise AssertionError(f"The container did not answer within {self.START_TIMEOUT_S} s: {last_error}.")

    @pytest.fixture(scope="class")
    def container(self) -> Iterator[Tuple[str, int]]:
        self.skip_without_docker()
        self.remove_left_overs()
        label = f"{self.PID_LABEL}={os.getpid()}"
        try:
            subprocess.run(
                ["docker", "build", "-f", self.DOCKERFILE, "-t", self.tag(), "--label", label, "."],
                cwd=self.ROOT,
                check=True,
                timeout=self.BUILD_TIMEOUT_S,
            )
            port = self.free_port()
            started = subprocess.run(
                ["docker", "run", "-d", "--label", label, "-p", f"{port}:8000", self.tag()],
                capture_output=True,
                text=True,
                timeout=self.DOCKER_TIMEOUT_S,
                check=True,
            )
            yield started.stdout.strip(), port
        finally:
            self.remove_own()

    def test_the_health_call_answers_ok_after_the_start(self, container: Tuple[str, int]) -> None:
        status, _, body = self.wait_for_health(container[1])
        assert status == 200
        assert json.loads(body) == {"status": "ok"}

    def test_a_call_without_a_company_is_refused_as_problem_json(self, container: Tuple[str, int]) -> None:
        self.wait_for_health(container[1])
        status, content_type, body = self.get(container[1], "/v1/anything")
        problem: Dict[str, object] = json.loads(body)
        assert status >= 400
        assert content_type.startswith("application/problem+json")
        assert "code" in problem

    def test_the_container_is_still_running_after_the_calls(self, container: Tuple[str, int]) -> None:
        self.wait_for_health(container[1])
        self.get(container[1], "/v1/anything")
        inspected = subprocess.run(
            ["docker", "inspect", "-f", "{{.State.Running}}", container[0]],
            capture_output=True,
            text=True,
            check=True,
        )
        assert inspected.stdout.strip() == "true"

    def test_the_class_leaves_no_image_and_no_container_behind(self) -> None:
        self.skip_without_docker()

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                f"{Path(__file__).resolve()}::TestImage",
                "-k",
                f"not {self.CLEANUP_TEST}",
                "-q",
                "-p",
                "no:cacheprovider",
                "-p",
                "no:xdist",
            ],
            cwd=self.ROOT,
            capture_output=True,
            text=True,
            timeout=self.BUILD_TIMEOUT_S + self.START_TIMEOUT_S,
            check=False,
        )

        assert result.returncode == 0, result.stdout + result.stderr
        assert "3 passed" in result.stdout
        assert self.left_over_images() == []
        assert self.left_over_containers() == []

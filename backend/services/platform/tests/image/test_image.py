from __future__ import annotations

import json
import shutil
import socket
import subprocess
import time
from pathlib import Path
from typing import ClassVar, Dict, Iterator, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest


@pytest.mark.timeout(900)
class TestImage:
    IMAGE_TAG: ClassVar[str] = "simpleerp-platform:test"
    DOCKERFILE: ClassVar[str] = "backend/services/platform/Dockerfile"
    START_TIMEOUT_S: ClassVar[int] = 60

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
        if shutil.which("docker") is None:
            pytest.skip("The environment has no Docker: the docker command is missing.")
        info = subprocess.run(["docker", "info"], capture_output=True, text=True, timeout=60, check=False)
        if info.returncode != 0:
            pytest.skip("The environment has no Docker: its daemon does not answer.")
        root = Path(__file__).resolve().parents[5]
        subprocess.run(
            ["docker", "build", "-f", self.DOCKERFILE, "-t", self.IMAGE_TAG, "."],
            cwd=root,
            check=True,
            timeout=800,
        )
        port = self.free_port()
        started = subprocess.run(
            ["docker", "run", "-d", "-p", f"{port}:8000", self.IMAGE_TAG],
            capture_output=True,
            text=True,
            check=True,
        )
        container_id = started.stdout.strip()
        try:
            yield container_id, port
        finally:
            subprocess.run(["docker", "rm", "-f", container_id], capture_output=True, check=False)

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

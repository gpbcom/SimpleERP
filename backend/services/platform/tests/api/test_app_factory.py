from __future__ import annotations

import os
import signal
import socket
import subprocess
import time
from pathlib import Path
from typing import ClassVar, Dict, Optional

import httpx
import pytest
from erp_platform.api.app_factory import AppFactory
from fastapi import FastAPI


class TestAppFactory:
    SERVICE_DIR: ClassVar[Path] = Path(__file__).resolve().parents[2]
    START_TIMEOUT_S: ClassVar[float] = 30.0
    POLL_INTERVAL_S: ClassVar[float] = 0.2

    @pytest.fixture
    def server_port(self) -> int:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.bind(("127.0.0.1", 0))
            return int(probe.getsockname()[1])

    def spawn(self, port: int, extra_env: Optional[Dict[str, str]] = None) -> subprocess.Popen[str]:
        environment = {**os.environ, **(extra_env or {})}
        return subprocess.Popen(
            [
                "uv",
                "run",
                "--package",
                "platform",
                "uvicorn",
                "--factory",
                "erp_platform.api.app_factory:AppFactory.create",
                "--host",
                "127.0.0.1",
                "--port",
                str(port),
            ],
            cwd=self.SERVICE_DIR,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

    def wait_until_healthy(self, process: subprocess.Popen[str], port: int) -> httpx.Response:
        deadline = time.monotonic() + self.START_TIMEOUT_S
        while time.monotonic() < deadline:
            assert process.poll() is None, "uvicorn exited before it served."
            try:
                return httpx.get(f"http://127.0.0.1:{port}/v1/health", timeout=2.0)
            except httpx.TransportError:
                time.sleep(self.POLL_INTERVAL_S)
        raise AssertionError("uvicorn did not serve within the timeout.")

    def test_the_factory_builds_an_application_that_answers_health(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.chdir(self.SERVICE_DIR)
        application = AppFactory.create()
        assert isinstance(application, FastAPI)

    def test_uvicorn_serves_the_factory_and_ends_cleanly_on_sigterm(self, server_port: int) -> None:
        process = self.spawn(server_port)
        try:
            response = self.wait_until_healthy(process, server_port)
            assert response.status_code == 200
            assert response.json() == {"status": "ok"}
            process.send_signal(signal.SIGTERM)
            assert process.wait(timeout=self.START_TIMEOUT_S) in (0, 128 + signal.SIGTERM, -signal.SIGTERM)
        finally:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=self.START_TIMEOUT_S)

    def test_an_empty_error_codes_path_stops_the_service_before_it_serves(self, server_port: int) -> None:
        canary = "canary-secret-value-4f9a"
        process = self.spawn(server_port, {"ERP__ERROR_CODES_PATH": "''", "ERP_TEST_CANARY": canary})
        try:
            output, _ = process.communicate(timeout=self.START_TIMEOUT_S)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate(timeout=self.START_TIMEOUT_S)
        assert process.returncode != 0
        assert "Uvicorn running on" not in output
        assert canary not in output

    async def test_the_factory_application_answers_health_through_asgi(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.chdir(self.SERVICE_DIR)
        transport = httpx.ASGITransport(app=AppFactory.create())
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            response = await client.get("/v1/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

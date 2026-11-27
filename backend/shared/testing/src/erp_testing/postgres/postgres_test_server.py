from __future__ import annotations

# Standard library imports
import shutil
import socket
import subprocess
import tempfile
import threading
import time
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from erp_lifecycle.runnables.runnable import Runnable

from erp_testing.models.postgres.exceptions import (
    SEPostgresTestServerNotStartedError,
    SEPostgresTestServerStartFailedError,
)
from erp_testing.models.postgres.postgres_connection import PostgresConnection
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.postgres.postgres_binaries import PostgresBinaries


class PostgresTestServer(Runnable):
    """A throw-away PostgreSQL server, started in a temporary folder for a test session.

    Attributes:
        HOST (str): The address the server listens on.
        COMMAND_TIMEOUT_S (float): How long one PostgreSQL command may run, in seconds.
        POLL_INTERVAL_S (float): The pause between two readiness checks, in seconds.
        config (PostgresServerConfig): The settings of the server.
        root (Optional[Path]): The temporary folder, or ``None`` before ``initialize`` and after ``close``.
        port (Optional[int]): The port the server listens on, or ``None`` until chosen.
        bin_dir (Optional[Path]): The folder of the PostgreSQL binaries, or ``None`` until found.
        started (bool): Whether ``pg_ctl start`` succeeded and the server was not yet stopped.
        closed (threading.Event): Set by ``close`` to release ``run``.
        logger (Logger): Logger instance.

    Notes:
        - **The server trusts every local connection and holds no password.** It listens on ``HOST`` only.
        - ``close`` is safe before ``initialize``, after a failed one, and twice.
    """

    HOST: ClassVar[str] = "127.0.0.1"
    COMMAND_TIMEOUT_S: ClassVar[float] = 120.0
    POLL_INTERVAL_S: ClassVar[float] = 0.1

    def __init__(self, config: PostgresServerConfig, logger: Optional[Logger] = None) -> None:
        """Create the server, not yet started.

        Args:
            config (PostgresServerConfig): The settings of the server.
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        super().__init__(logger)
        self.config = config
        self.root: Optional[Path] = None
        self.port: Optional[int] = None
        self.bin_dir: Optional[Path] = None
        self.started = False
        self.closed = threading.Event()

    ############################
    # Internal Helpers Methods #
    ############################

    def _free_port(self) -> int:
        """Ask the system for a free port on ``HOST``.

        Returns:
            int: A port that was free a moment ago.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.bind((self.HOST, 0))
            port: int = probe.getsockname()[1]
        self.logger.debug("Chose port %d.", port)
        return port

    def _execute(self, name: str, arguments: List[str]) -> subprocess.CompletedProcess[str]:
        """Run one PostgreSQL binary, without a shell.

        Args:
            name (str): The binary's name, such as ``initdb``.
            arguments (List[str]): Its arguments.

        Returns:
            subprocess.CompletedProcess[str]: The finished process, with its output decoded as UTF-8.

        Raises:
            SEPostgresTestServerStartFailedError: If the binary cannot run or does not finish in time.
        """
        if self.bin_dir is None:
            self.logger.error("The PostgreSQL binaries are not known yet.")
            raise SEPostgresTestServerStartFailedError("The PostgreSQL binaries are not known yet.")
        self.logger.debug("Running %s.", name)
        try:
            return subprocess.run(
                [str(self.bin_dir / name), *arguments],
                capture_output=True,
                check=False,
                encoding="utf-8",
                errors="replace",
                timeout=self.COMMAND_TIMEOUT_S,
            )
        except (OSError, subprocess.SubprocessError) as error:
            self.logger.error("Could not run %s: %s.", name, type(error).__name__)
            raise SEPostgresTestServerStartFailedError(f"Could not run {name}: {type(error).__name__}.") from error

    def _require(self, name: str, arguments: List[str]) -> None:
        """Run one binary and demand that it succeeds.

        Args:
            name (str): The binary's name.
            arguments (List[str]): Its arguments.

        Raises:
            SEPostgresTestServerStartFailedError: If it exits with a non-zero code.
        """
        result = self._execute(name, arguments)
        if result.returncode != 0:
            self.logger.error("%s failed with code %d: %s", name, result.returncode, result.stderr.strip())
            raise SEPostgresTestServerStartFailedError(
                f"{name} failed with code {result.returncode}. "  # noqa: E501
                f"Its error output was {result.stderr.strip()!r}."
            )

    def _wait_until_ready(self, port: int) -> None:
        """Poll ``pg_isready`` until the server accepts connections.

        Args:
            port (int): The port to check.

        Raises:
            SEPostgresTestServerStartFailedError: If the server is not ready within ``start_timeout_s``.
        """
        deadline = time.monotonic() + self.config.start_timeout_s
        while True:
            result = self._execute("pg_isready", ["-h", self.HOST, "-p", str(port)])
            if result.returncode == 0:
                self.logger.debug("The server is ready on port %d.", port)
                return
            if time.monotonic() >= deadline:
                self.logger.error("The server was not ready after %.1f s.", self.config.start_timeout_s)
                raise SEPostgresTestServerStartFailedError(
                    f"The server was not ready within {self.config.start_timeout_s} s. "  # noqa: E501
                    f"Its last readiness code was {result.returncode}."
                )
            time.sleep(self.POLL_INTERVAL_S)

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def data_dir(self) -> Path:
        """Return the temporary folder that holds the server's files.

        Returns:
            Path: The folder, which exists from ``initialize`` until ``close``.

        Raises:
            SEPostgresTestServerNotStartedError: If ``initialize`` has not created it.
        """
        if self.root is None:
            self.logger.error("The PostgreSQL test server has no folder yet.")
            raise SEPostgresTestServerNotStartedError("The PostgreSQL test server has no folder yet.")
        return self.root

    @property
    def connection(self) -> PostgresConnection:
        """Describe how to reach the running server.

        Returns:
            PostgresConnection: The host, port, database and user, with no password.

        Raises:
            SEPostgresTestServerNotStartedError: If the server is not started.
        """
        if not self.started or self.port is None:
            self.logger.error("The PostgreSQL test server is not started.")
            raise SEPostgresTestServerNotStartedError("The PostgreSQL test server is not started.")
        return PostgresConnection(host=self.HOST, port=self.port, database=self.config.database, user=self.config.user)

    def initialize(self) -> None:
        """Create the folder, initialise the cluster, start the server and create the database.

        Raises:
            SEPostgresBinariesNotFoundError: If no PostgreSQL binaries are found.
            SEPostgresTestServerStartFailedError: If a command fails or the server is not ready in time.
        """
        self.closed.clear()
        self.bin_dir = PostgresBinaries(self.config, self.logger).find()
        self.root = Path(tempfile.mkdtemp(prefix="erp_postgres_"))
        pgdata = self.root / "data"
        self.logger.debug("Initialising the cluster in %s.", pgdata)
        self._require("initdb", ["-D", str(pgdata), "-A", "trust", "-U", self.config.user])
        port = self._free_port()
        self.port = port
        options = f"-p {port} -k {self.root} -c listen_addresses={self.HOST}"
        self._require("pg_ctl", ["start", "-W", "-D", str(pgdata), "-l", str(self.root / "server.log"), "-o", options])
        self.started = True
        self._wait_until_ready(port)
        quoted = '"' + self.config.database.replace('"', '""') + '"'
        self._require(
            "psql",
            [
                "-h",
                self.HOST,
                "-p",
                str(port),
                "-U",
                self.config.user,
                "-d",
                "postgres",
                "-c",
                f"CREATE DATABASE {quoted}",
            ],
        )
        self.logger.info("Started a PostgreSQL test server on port %d.", port)

    def run(self) -> None:
        """Block until ``close`` is called."""
        self.logger.debug("Serving until closed.")
        self.closed.wait()

    def close(self) -> None:
        """Stop the server and remove its folder, safely before or after a failed ``initialize``, and twice."""
        self.closed.set()
        root = self.root
        if self.started and root is not None:
            try:
                result = self._execute("pg_ctl", ["stop", "-m", "fast", "-D", str(root / "data")])
                if result.returncode != 0:
                    self.logger.warning("pg_ctl stop failed with code %d.", result.returncode)
                else:
                    self.logger.info("Stopped the PostgreSQL test server.")
            except SEPostgresTestServerStartFailedError:
                self.logger.warning("The PostgreSQL test server could not be stopped.")
            self.started = False
        if root is not None:
            shutil.rmtree(root, ignore_errors=True)
            self.logger.debug("Removed %s.", root)
            self.root = None

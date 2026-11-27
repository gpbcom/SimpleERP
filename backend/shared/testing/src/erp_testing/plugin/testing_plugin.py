from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Iterator, Optional

# Third-party imports
import pytest

# First-party imports
from erp_testing.context.synthetic_company_context import SyntheticCompanyContext
from erp_testing.factories.postgres.postgres_test_server_factory import PostgresTestServerFactory
from erp_testing.factories.stand_in.stand_in_server_factory import StandInServerFactory
from erp_testing.logs.log_capture import LogCapture
from erp_testing.models.postgres.exceptions import SEPostgresBinariesNotFoundError
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from erp_testing.postgres.postgres_test_server import PostgresTestServer
from erp_testing.stand_in.stand_in_server import StandInServer
from erp_testing.synthetic.company_builder import CompanyBuilder
from erp_testing.synthetic.user_builder import UserBuilder


class TestingPlugin:
    """Pytest plugin that offers every helper of the library as a fixture.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - A conftest registers one instance with ``config.pluginmanager.register(TestingPlugin(), "erp-testing")``.
        - Runnables are built through their factories only, and closed in a ``finally`` block.
        - **``postgres_server`` is session scoped**, so one server serves every test of the session.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create the plugin.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @pytest.fixture
    def stand_in_server(self) -> Iterator[StandInServer]:
        """Give a started stand-in server, closed after the test.

        Yields:
            StandInServer: The running server.
        """
        server = StandInServerFactory(logger=self.logger).create()
        try:
            server.initialize()
            self.logger.debug("Started the stand-in server fixture.")
            yield server
        finally:
            server.close()
            self.logger.debug("Stopped the stand-in server fixture.")

    @pytest.fixture(scope="session")
    def postgres_server(self) -> Iterator[PostgresTestServer]:
        """Give a PostgreSQL test server started once for the session.

        Yields:
            PostgresTestServer: The running server.

        Notes:
            The test is skipped, with the error's message, when no PostgreSQL binaries are installed.
        """
        server = PostgresTestServerFactory(PostgresServerConfig(), self.logger).create()
        try:
            try:
                server.initialize()
            except SEPostgresBinariesNotFoundError as error:
                self.logger.debug("No PostgreSQL binaries: skipping.")
                pytest.skip(str(error))
            self.logger.debug("Started the PostgreSQL server fixture.")
            yield server
        finally:
            server.close()
            self.logger.debug("Stopped the PostgreSQL server fixture.")

    @pytest.fixture(scope="session")
    def synthetic_catalog(self) -> SyntheticCatalog:
        """Load the shipped synthetic catalogue.

        Returns:
            SyntheticCatalog: The catalogue at its default path.
        """
        self.logger.debug("Loading the synthetic catalog fixture.")
        return SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH)

    @pytest.fixture
    def company_builder(self, synthetic_catalog: SyntheticCatalog) -> CompanyBuilder:
        """Give a company builder on the first sector, with seed ``0``.

        Args:
            synthetic_catalog (SyntheticCatalog): The catalogue.

        Returns:
            CompanyBuilder: The builder.
        """
        self.logger.debug("Building the company builder fixture.")
        return CompanyBuilder(synthetic_catalog, synthetic_catalog.sectors[0], seed=0)

    @pytest.fixture
    def user_builder(self, synthetic_catalog: SyntheticCatalog, company_builder: CompanyBuilder) -> UserBuilder:
        """Give a user builder for a company of ``company_builder``, with seed ``0``.

        Args:
            synthetic_catalog (SyntheticCatalog): The catalogue.
            company_builder (CompanyBuilder): The builder of the user's company.

        Returns:
            UserBuilder: The builder.
        """
        self.logger.debug("Building the user builder fixture.")
        return UserBuilder(synthetic_catalog, company_builder.build(), seed=0)

    @pytest.fixture
    def company_context(self, user_builder: UserBuilder) -> Iterator[SyntheticCompanyContext]:
        """Make a synthetic company and user the current context for the test.

        Args:
            user_builder (UserBuilder): The builder of the user, which holds the company the user belongs to.

        Yields:
            SyntheticCompanyContext: The entered context, whose company is the user's own company.
        """
        context = SyntheticCompanyContext(user_builder.company, user_builder.build(), self.logger)
        with context:
            self.logger.debug("Entered the company context fixture.")
            yield context
        self.logger.debug("Left the company context fixture.")

    @pytest.fixture
    def log_capture(self) -> Iterator[LogCapture]:
        """Capture the log records of the test.

        Yields:
            LogCapture: The attached capture.
        """
        capture = LogCapture()
        capture.attach()
        self.logger.debug("Attached the log capture fixture.")
        try:
            yield capture
        finally:
            capture.detach()
            self.logger.debug("Detached the log capture fixture.")

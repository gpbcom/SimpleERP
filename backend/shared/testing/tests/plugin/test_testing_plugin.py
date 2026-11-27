from __future__ import annotations

import json
import logging
import subprocess
import urllib.request

from erp_context.storage.context.request_context_store import RequestContextStore
from erp_testing.context.synthetic_company_context import SyntheticCompanyContext
from erp_testing.logs.log_capture import LogCapture
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.stand_in_answer import StandInAnswer
from erp_testing.models.stand_in.stand_in_route import StandInRoute
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from erp_testing.models.synthetic.synthetic_company import SyntheticCompany
from erp_testing.models.synthetic.synthetic_user import SyntheticUser
from erp_testing.postgres.postgres_binaries import PostgresBinaries
from erp_testing.postgres.postgres_test_server import PostgresTestServer
from erp_testing.stand_in.stand_in_server import StandInServer
from erp_testing.synthetic.company_builder import CompanyBuilder
from erp_testing.synthetic.user_builder import UserBuilder


class TestTestingPlugin:
    def test_the_stand_in_server_fixture_gives_a_started_server(self, stand_in_server: StandInServer) -> None:
        assert stand_in_server.url.startswith("http://")

    def test_a_route_without_an_answer_replies_with_the_empty_value_of_its_model(
        self, stand_in_server: StandInServer
    ) -> None:
        stand_in_server.route(StandInRoute(method=HttpMethod.GET, path="/answers", model=StandInAnswer))

        with urllib.request.urlopen(f"{stand_in_server.url}/answers", timeout=5) as response:
            body = json.loads(response.read())

        assert response.status == 200
        assert StandInAnswer.model_validate(body) == StandInAnswer()

    def test_a_many_route_without_an_answer_replies_with_an_empty_list(self, stand_in_server: StandInServer) -> None:
        stand_in_server.route(StandInRoute(method=HttpMethod.GET, path="/answers", model=StandInAnswer, many=True))

        with urllib.request.urlopen(f"{stand_in_server.url}/answers", timeout=5) as response:
            assert json.loads(response.read()) == []

    def test_the_synthetic_catalog_fixture_is_the_shipped_catalog(self, synthetic_catalog: SyntheticCatalog) -> None:
        assert synthetic_catalog == SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH)

    def test_the_company_builder_builds_a_company_of_the_first_sector(
        self, company_builder: CompanyBuilder, synthetic_catalog: SyntheticCatalog
    ) -> None:
        assert company_builder.build().sector == synthetic_catalog.sectors[0]

    def test_the_user_builder_builds_a_user_on_the_catalog_domain(
        self, user_builder: UserBuilder, synthetic_catalog: SyntheticCatalog
    ) -> None:
        user = user_builder.build()

        assert isinstance(user, SyntheticUser)
        assert user.email.endswith(f"@{synthetic_catalog.email_domain}")

    def test_the_company_context_fixture_is_the_current_context(self, company_context: SyntheticCompanyContext) -> None:
        current = RequestContextStore().get()

        assert current is not None
        assert current == company_context.context

    def test_the_company_context_fixture_belongs_to_a_synthetic_company(
        self, company_context: SyntheticCompanyContext
    ) -> None:
        assert isinstance(company_context, SyntheticCompanyContext)
        assert company_context.context.user.company_id is not None

    def test_the_company_context_fixture_user_belongs_to_the_context_company(
        self, company_context: SyntheticCompanyContext
    ) -> None:
        assert company_context.user.company_id == company_context.company.id
        assert company_context.company.id == company_context.context.user.company_id

    def test_the_log_capture_fixture_captures_a_line_logged_in_the_test(self, log_capture: LogCapture) -> None:
        logging.getLogger("erp_testing_plugin_test").warning("A synthetic line %d.", 7)

        assert log_capture.contains("A synthetic line 7.", logging.WARNING)

    def test_the_postgres_server_fixture_answers_pg_isready(self, postgres_server: PostgresTestServer) -> None:
        connection = postgres_server.connection
        binaries = PostgresBinaries(PostgresServerConfig()).find()

        result = subprocess.run(
            [f"{binaries}/pg_isready", "-h", connection.host, "-p", str(connection.port)],
            capture_output=True,
            check=False,
            timeout=30,
        )

        assert result.returncode == 0

    def test_the_synthetic_company_type_is_the_one_the_builders_give(self, company_builder: CompanyBuilder) -> None:
        assert isinstance(company_builder.build(), SyntheticCompany)

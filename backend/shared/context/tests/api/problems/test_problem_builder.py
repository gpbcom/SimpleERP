from __future__ import annotations

import pytest
from erp_context.api.problems.problem_builder import ProblemBuilder
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessError
from erp_context.models.refusals.refusal_catalog import RefusalCatalog

from tests.api.middleware.helpers import load_catalog


class TestProblemBuilder:
    @pytest.fixture
    def catalog(self) -> RefusalCatalog:
        return load_catalog()

    @pytest.mark.parametrize("reason", list(RefusalReason))
    def test_a_problem_is_filled_from_the_catalogue_entry_of_the_reason(
        self, catalog: RefusalCatalog, reason: RefusalReason
    ) -> None:
        entry = catalog.code_for(reason)
        problem = ProblemBuilder(catalog).build(SEAccessError(reason, "A refusal."), "req-1")
        assert problem.title == entry.title_key
        assert problem.detail == entry.why_key
        assert problem.code == entry.code
        assert problem.action == entry.action_key
        assert problem.reference == entry.reference
        assert problem.status == entry.status

    def test_the_instance_is_the_request_id(self, catalog: RefusalCatalog) -> None:
        problem = ProblemBuilder(catalog).build(SEAccessError(RefusalReason.NO_COMPANY, "A refusal."), "req-42")
        assert problem.instance == "req-42"

    def test_a_missing_request_id_leaves_no_instance(self, catalog: RefusalCatalog) -> None:
        problem = ProblemBuilder(catalog).build(SEAccessError(RefusalReason.NO_USER, "A refusal."), None)
        assert problem.instance is None

    def test_the_type_is_about_blank(self, catalog: RefusalCatalog) -> None:
        problem = ProblemBuilder(catalog).build(SEAccessError(RefusalReason.NO_USER, "A refusal."), "req-1")
        assert problem.type == "about:blank"

    def test_the_error_message_never_reaches_the_problem(self, catalog: RefusalCatalog) -> None:
        error = SEAccessError(RefusalReason.NO_COMPANY, "Bearer s3cr3t-token-value was refused.")
        problem = ProblemBuilder(catalog).build(error, "req-1")
        assert "s3cr3t" not in problem.model_dump_json()

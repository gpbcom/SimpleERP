from __future__ import annotations

import logging
from pathlib import Path
from re import fullmatch
from typing import Dict

import pytest
from erp_models.errors.entries.error_code_entry import ErrorCodeEntry
from erp_platform.models.problems.problem_details import ProblemDetails
from erp_platform.service.problems.exceptions import SEProblemError, SEProblemUnknownCodeError
from erp_platform.service.problems.problem_service import ProblemService
from erp_platform.storage.catalogs.error_code_repository import ErrorCodeRepository


class TestProblemService:
    CASES = [
        ("PLATFORM-ROUTE-01", 404),
        ("PLATFORM-METHOD-01", 405),
        ("PLATFORM-REQUEST-01", 422),
        ("PLATFORM-INTERNAL-01", 500),
    ]

    def real_path(self) -> Path:
        return Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "error_codes.yaml"

    @pytest.mark.parametrize(("code", "status"), CASES)
    def test_a_code_gives_a_problem_with_its_keys_and_status(self, code: str, status: int) -> None:
        entry = ErrorCodeRepository(self.real_path()).load().resolve(code)

        problem = ProblemService(self.real_path()).problem(code, status)

        assert isinstance(problem, ProblemDetails)
        assert problem.title == entry.title
        assert problem.detail == entry.why
        assert problem.code == code
        assert problem.status == status

    def test_an_unknown_code_is_refused(self) -> None:
        with pytest.raises(SEProblemUnknownCodeError):
            ProblemService(self.real_path()).problem("PLATFORM-NOPE-99", 500)

    def test_an_unknown_code_error_is_a_problem_error(self) -> None:
        with pytest.raises(SEProblemError):
            ProblemService(self.real_path()).problem("PLATFORM-NOPE-99", 500)

    def test_an_unknown_code_writes_an_error_log_line(self, caplog: pytest.LogCaptureFixture) -> None:
        service = ProblemService(self.real_path())

        with caplog.at_level(logging.DEBUG), pytest.raises(SEProblemUnknownCodeError):
            service.problem("PLATFORM-NOPE-99", 500)

        assert [record for record in caplog.records if record.levelno == logging.ERROR]

    @pytest.mark.parametrize(("code", "status"), CASES)
    def test_the_serialised_body_holds_only_keys_the_code_and_the_status(self, code: str, status: int) -> None:
        body: Dict[str, object] = ProblemService(self.real_path()).problem(code, status).model_dump(mode="json")

        assert set(body) == {"title", "detail", "code", "status"}
        assert body["code"] == code
        assert body["status"] == status
        for member in ("title", "detail"):
            value = body[member]
            assert isinstance(value, str)
            assert fullmatch(ErrorCodeEntry.MESSAGE_KEY_PATTERN, value) is not None

    def test_a_given_logger_is_accepted(self) -> None:
        service = ProblemService(self.real_path(), logging.getLogger("tests.problem_service"))

        assert service.problem("PLATFORM-ROUTE-01", 404).status == 404

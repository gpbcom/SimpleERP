from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import ROOT, SCRIPTS, jobs, runs, step_using, triggers, with_of

NAME = "python.yml"


class TestPythonWorkflow:
    INPUTS: ClassVar[List[str]] = ["services", "packages", "repository"]
    PROJECT_JOBS: ClassVar[List[str]] = ["services", "packages"]

    def test_it_is_a_reusable_workflow_with_the_services_the_packages_and_the_repository_flag(self) -> None:
        call = triggers(NAME)["workflow_call"]
        assert list(triggers(NAME)) == ["workflow_call"]
        assert list(cast(Dict[str, JsonValue], call["inputs"])) == self.INPUTS

    @pytest.mark.parametrize("job", PROJECT_JOBS)
    def test_each_project_is_its_own_matrix_entry(self, job: str) -> None:
        matrix = cast(Dict[str, Dict[str, str]], jobs(NAME)[job]["strategy"])["matrix"]
        assert matrix["folder"] == f"${{{{ fromJSON(inputs.{job}) }}}}"
        assert jobs(NAME)[job]["if"] == f"inputs.{job} != '[]'"

    @pytest.mark.parametrize("job", ["services", "packages", "repository"])
    def test_every_job_installs_the_locked_workspace_with_uv(self, job: str) -> None:
        assert with_of(step_using(NAME, job, "astral-sh/setup-uv"))["enable-cache"] is True
        assert "uv sync --locked" in runs(NAME, job)

    @pytest.mark.parametrize("job", PROJECT_JOBS)
    def test_each_project_runs_the_shared_check_script(self, job: str) -> None:
        assert 'bash .github/scripts/check_python_project.sh "$FOLDER" "$name"' in runs(NAME, job)

    def test_the_check_script_runs_ruff_mypy_and_pytest_with_a_junit_report(self) -> None:
        script = (SCRIPTS / "check_python_project.sh").read_text(encoding="utf-8")
        assert 'uv run ruff check "$folder"' in script
        assert 'uv run ruff format --check "$folder"' in script
        assert 'uv run mypy "$folder/src"' in script
        assert 'uv run pytest "$folder/tests" -n 2 --junitxml="reports/$report.xml"' in script

    def test_the_repository_job_lints_the_harness_and_runs_every_repository_test(self) -> None:
        script = runs(NAME, "repository")
        assert "uv run ruff check .claude .github/scripts tests" in script
        assert "uv run ruff format --check .claude .github/scripts tests" in script
        assert "uv run pytest tests -n 2 --junitxml=reports/repository.xml" in script

    def test_the_repository_job_runs_in_a_shallow_checkout(self) -> None:
        checkout = step_using(NAME, "repository", "actions/checkout")
        assert "fetch-depth" not in with_of(checkout)

    def test_python_comes_from_the_python_version_file(self) -> None:
        assert (ROOT / ".python-version").read_text(encoding="utf-8").strip() == "3.13"
        for job in jobs(NAME):
            assert "python-version" not in with_of(step_using(NAME, job, "astral-sh/setup-uv"))

    @pytest.mark.parametrize("job", ["services", "packages", "repository"])
    def test_every_job_keeps_its_reports_even_when_it_fails(self, job: str) -> None:
        upload = step_using(NAME, job, "actions/upload-artifact")
        assert upload["if"] == "always()"
        assert str(with_of(upload)["name"]).startswith("test-report-python-")

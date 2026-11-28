from __future__ import annotations

# Standard library imports
import tomllib
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import ROOT, SCRIPTS, jobs, runs, step_using, steps, triggers, with_of

NAME = "python.yml"


class TestPythonWorkflow:
    INPUTS: ClassVar[List[str]] = ["services", "packages", "repository"]
    PROJECT_JOBS: ClassVar[List[str]] = ["services", "packages"]
    BRUNO_STEP: ClassVar[str] = "Bruno collection up to date (REQ-T05-05)"

    def bruno_step(self) -> Dict[str, JsonValue]:
        found = [step for step in steps(NAME, "services") if step.get("name") == self.BRUNO_STEP]
        assert len(found) == 1, f"The services job has no step named {self.BRUNO_STEP!r}."
        return found[0]

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

    @pytest.mark.parametrize("job", ["services", "packages", "repository"])
    def test_every_job_installs_every_workspace_member(self, job: str) -> None:
        # The root is not a package (package = false): without --all-packages, erp_models and the libraries are not
        # installed, and their tests cannot import them.
        assert "uv sync --locked --all-packages" in runs(NAME, job)

    def test_the_tests_of_every_package_need_no_docstrings(self) -> None:
        ignores = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["tool"]["ruff"]["lint"]
        assert "D" in ignores["per-file-ignores"]["**/tests/**"]

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

    def test_the_services_job_checks_that_the_bruno_collection_is_up_to_date(self) -> None:
        run = str(self.bruno_step()["run"])
        assert 'uv run python .github/scripts/bruno_collection.py check --service "$FOLDER"' in run

    def test_the_bruno_check_comes_after_the_workspace_is_installed(self) -> None:
        names = [step.get("name") for step in steps(NAME, "services")]
        assert "Install the workspace" in names
        assert self.BRUNO_STEP in names
        assert names.index(self.BRUNO_STEP) > names.index("Install the workspace")

    def test_the_bruno_check_is_never_skipped_nor_allowed_to_fail(self) -> None:
        step = self.bruno_step()
        assert "if" not in step
        assert "continue-on-error" not in step

    def test_the_bruno_check_reads_no_input_directly(self) -> None:
        assert "${{ inputs" not in str(self.bruno_step().get("run", ""))

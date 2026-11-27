from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict, List, Tuple, cast

# Third-party imports
import pytest

# First-party imports
from tests.ci.workflows.helpers import jobs, runs, step_using, steps, triggers, with_of

NAME = "release.yml"


class TestReleaseWorkflow:
    SUITES: ClassVar[List[str]] = ["python", "typescript"]
    REPORTS: ClassVar[List[Tuple[str, str, str]]] = [
        ("python.yml", "services", "test-report-python-"),
        ("python.yml", "packages", "test-report-python-"),
        ("python.yml", "repository", "test-report-python-repository"),
        ("typescript.yml", "check", "test-report-ts-"),
    ]

    def test_a_release_is_started_by_hand_from_develop_only(self) -> None:
        assert list(triggers(NAME)) == ["workflow_dispatch"]
        assert jobs(NAME)["version"]["if"] == "github.ref == 'refs/heads/develop'"

    def test_no_release_starts_without_its_token(self) -> None:
        assert "RELEASE_TOKEN is missing" in runs(NAME, "version")

    def test_every_suite_of_ci_runs_with_everything_selected(self) -> None:
        assert "detect_changes.py --all" in runs(NAME, "changes")
        for suite in self.SUITES:
            assert jobs(NAME)[suite]["uses"] == f"./.github/workflows/{suite}.yml"

    def test_the_python_suite_gets_the_services_the_packages_and_the_repository(self) -> None:
        inputs = cast(Dict[str, str], jobs(NAME)["python"]["with"])
        assert set(inputs) == {"services", "packages", "repository"}

    def test_the_release_is_written_only_when_every_suite_passed(self) -> None:
        prepare = jobs(NAME)["prepare"]
        assert set(cast(List[str], prepare["needs"])) == {"version", "changes", *self.SUITES}
        condition = str(prepare["if"])
        assert "!contains(needs.*.result, 'failure')" in condition
        assert "!contains(needs.*.result, 'cancelled')" in condition

    def test_the_changelog_notes_and_test_reports_go_to_master_by_a_pull_request(self) -> None:
        script = runs(NAME, "prepare")
        assert with_of(step_using(NAME, "prepare", "actions/download-artifact"))["pattern"] == "test-report-*"
        assert 'release_notes.py write --version "$VERSION" --reports reports' in script
        assert 'git add --force CHANGELOG.md "docs/releases/v$VERSION"' in script
        assert 'git push --quiet origin "release/$VERSION"' in script
        assert '--base master --head "release/$VERSION" --label automerge' in script

    def test_the_pull_request_is_opened_with_the_release_token_so_that_ci_runs(self) -> None:
        [create] = [step for step in steps(NAME, "prepare") if "gh pr create" in str(step.get("run", ""))]
        assert cast(Dict[str, str], create["env"])["GH_TOKEN"] == "${{ secrets.RELEASE_TOKEN }}"
        checkout = step_using(NAME, "prepare", "actions/checkout")
        assert with_of(checkout)["token"] == "${{ secrets.RELEASE_TOKEN }}"

    @pytest.mark.parametrize(("name", "job", "artifact"), REPORTS)
    def test_every_suite_keeps_its_test_report_even_when_it_fails(self, name: str, job: str, artifact: str) -> None:
        uploads = [step for step in steps(name, job) if "upload-artifact" in str(step.get("uses", ""))]
        assert len(uploads) == 1
        assert uploads[0]["if"] == "always()"
        assert str(with_of(uploads[0])["name"]).startswith(artifact)

    def test_pytest_writes_junit_reports(self) -> None:
        assert "--junitxml=" in runs("python.yml", "repository")

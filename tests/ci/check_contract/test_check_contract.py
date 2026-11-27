from __future__ import annotations

# Standard library imports
import subprocess
from pathlib import Path
from typing import ClassVar, Dict, Tuple

# Third-party imports
import pytest


class TestCheckContract:
    SCRIPT: ClassVar[Path] = Path(__file__).resolve().parents[3] / ".github" / "scripts" / "check_contract.sh"
    FOLDER: ClassVar[str] = "backend/services/platform"
    UV_CALL: ClassVar[str] = "run --package platform pytest backend/services/platform/tests/contracts -n 2"

    def run(
        self, repo: Path, environment: Dict[str, str], *arguments: str, uv_exit: int = 0
    ) -> subprocess.CompletedProcess[str]:
        env = {**environment, "STAND_IN_UV_EXIT": str(uv_exit)}
        return subprocess.run(
            ["bash", str(self.SCRIPT), *arguments], cwd=repo, env=env, capture_output=True, text=True, check=False
        )

    def recorded(self, bin_folder: Path, name: str) -> str:
        path = bin_folder / name
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def test_a_service_without_a_committed_document_is_not_applicable_and_never_calls_uv(
        self, repo: Path, environment: Dict[str, str], bin_folder: Path
    ) -> None:
        (repo / "backend" / "services" / "other").mkdir()
        done = self.run(repo, environment, "backend/services/other", "HEAD")
        assert done.returncode == 0
        assert "not applicable" in (done.stdout + done.stderr).lower()
        assert not (bin_folder / "args.txt").exists()

    def test_the_first_commit_as_base_runs_the_service_contract_tests_with_its_document_as_baseline(
        self,
        repo: Path,
        environment: Dict[str, str],
        bin_folder: Path,
        first_commit: str,
        documents: Tuple[str, str],
    ) -> None:
        done = self.run(repo, environment, self.FOLDER, first_commit)
        assert done.returncode == 0, done.stderr
        assert self.recorded(bin_folder, "args.txt").strip() == self.UV_CALL
        assert self.recorded(bin_folder, "baseline_state.txt").strip() == "set"
        assert self.recorded(bin_folder, "baseline.txt") == documents[0]

    @pytest.mark.parametrize("base", ["", "0" * 40, "1234567890abcdef1234567890abcdef12345678", "no-such-ref"])
    def test_an_empty_zero_or_unknown_base_runs_the_contract_tests_without_a_baseline(
        self, repo: Path, environment: Dict[str, str], bin_folder: Path, base: str
    ) -> None:
        done = self.run(repo, environment, self.FOLDER, base)
        assert done.returncode == 0, done.stderr
        assert self.recorded(bin_folder, "args.txt").strip() == self.UV_CALL
        assert self.recorded(bin_folder, "baseline_state.txt").strip() == "unset"

    def test_a_base_without_the_document_runs_the_contract_tests_without_a_baseline(
        self, repo: Path, environment: Dict[str, str], bin_folder: Path, commit_without_document: str
    ) -> None:
        done = self.run(repo, environment, self.FOLDER, commit_without_document)
        assert done.returncode == 0, done.stderr
        assert self.recorded(bin_folder, "args.txt").strip() == self.UV_CALL
        assert self.recorded(bin_folder, "baseline_state.txt").strip() == "unset"

    def test_a_failing_contract_test_makes_the_script_exit_one(
        self, repo: Path, environment: Dict[str, str], first_commit: str
    ) -> None:
        done = self.run(repo, environment, self.FOLDER, first_commit, uv_exit=1)
        assert done.returncode == 1

    def test_a_missing_folder_argument_exits_non_zero_with_the_usage(
        self, repo: Path, environment: Dict[str, str], bin_folder: Path
    ) -> None:
        done = self.run(repo, environment)
        assert done.returncode != 0
        assert "usage" in (done.stdout + done.stderr).lower()
        assert not (bin_folder / "args.txt").exists()

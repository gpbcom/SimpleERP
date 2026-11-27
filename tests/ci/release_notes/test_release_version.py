from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.release_notes.helpers import git, make_repo, run


class TestReleaseVersion:
    def test_the_first_release_is_0_1_0(self, tmp_path: Path) -> None:
        git(tmp_path, "init", "-q", "-b", "develop")
        git(tmp_path, "commit", "-q", "--allow-empty", "-m", "Initial commit")
        assert run(tmp_path, "version").stdout.strip() == "version=0.1.0"

    def test_the_next_release_bumps_the_minor_version_of_the_last_tag(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        assert run(root, "version").stdout.strip() == "version=0.2.0"

    def test_a_requested_version_is_taken_as_it_is(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        assert run(root, "version", "--requested", "v1.0.0").stdout.strip() == "version=1.0.0"

    def test_a_version_already_released_is_refused(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        result = run(root, "version", "--requested", "0.1.0")
        assert result.returncode == 1
        assert "already released" in result.stderr

    @pytest.mark.parametrize("requested", ["1.0", "one", "1.0.0-rc"])
    def test_a_malformed_version_is_refused(self, tmp_path: Path, requested: str) -> None:
        root = make_repo(tmp_path)
        assert run(root, "version", "--requested", requested).returncode == 2

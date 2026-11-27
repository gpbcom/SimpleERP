from __future__ import annotations

# Standard library imports
import os
import subprocess
import sys
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.harness.roadmap_gantt.helpers import (
    BLOCKED_BY,
    EPICS,
    PHASES,
    TICKETS,
    make_roadmap_repo,
    run_script,
)

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / ".claude" / "scripts" / "github" / "board.py"
TAKEN = "Validation failed: Target issue has already been taken"
OFFLINE = "To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN"
PROBE = (
    "import sys; sys.path.insert(0, {scripts!r}); import board; "
    "print(board.gh(['api', 'graphql'], {{}}, tolerate_existing={tolerate}))"
)


def fake_gh(folder: Path, message: str) -> Path:
    """Write a ``gh`` that fails like GitHub does when a link already exists."""
    folder.mkdir()
    gh = folder / "gh"
    gh.write_text(f"#!/bin/sh\necho 'gh: {message}' >&2\nexit 1\n", encoding="utf-8")
    gh.chmod(0o755)
    return folder


def probe(tmp_path: Path, tolerate: bool, message: str = TAKEN) -> subprocess.CompletedProcess[str]:
    path = fake_gh(tmp_path / "bin", message)
    code = PROBE.format(scripts=str(SCRIPT.parent), tolerate=tolerate)
    return subprocess.run(
        [sys.executable, "-c", code],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={**os.environ, "PATH": f"{path}{os.pathsep}{os.environ['PATH']}"},
    )


class TestBoard:
    def test_a_link_made_before_a_stop_counts_as_made_on_resume(self, tmp_path: Path) -> None:
        result = probe(tmp_path, tolerate=True)
        assert result.returncode == 0, result.stderr
        assert result.stdout.strip() == "None"

    def test_an_existing_link_is_still_an_error_when_not_expected(self, tmp_path: Path) -> None:
        assert probe(tmp_path, tolerate=False).returncode != 0

    @pytest.mark.parametrize("message", ["Could not resolve to a node", "Bad credentials"])
    def test_any_other_error_stops_the_bootstrap(self, tmp_path: Path, message: str) -> None:
        result = probe(tmp_path, tolerate=True, message=message)
        assert result.returncode != 0
        assert message in result.stderr

    def test_the_dry_run_counts_every_phase_without_calling_github(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        offline = fake_gh(tmp_path / "bin", OFFLINE)
        result = run_script("github/board.py", repo, "bootstrap", "--dry-run", path=str(offline))
        assert result.returncode == 0, result.stderr
        lines = result.stdout.splitlines()
        assert lines[-1] == f"{len(PHASES)} phases, {EPICS} epics, {TICKETS} tickets, {BLOCKED_BY} blocked-by"
        assert f"🏷️  {8 + len(PHASES)} labels" in lines
        assert "🏆 milestone P10: Hosted services" in lines
        assert "📝 issue T10.03: Shared code for hosted services" in lines

    def test_the_dry_run_stops_cleanly_while_the_roadmap_has_no_phase_page(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path, with_roadmap=False)
        offline = fake_gh(tmp_path / "bin", OFFLINE)
        result = run_script("github/board.py", repo, "bootstrap", "--dry-run", path=str(offline))
        assert result.returncode == 1
        assert "No phase page in docs/specs/00-vision/roadmap/phases/" in result.stderr
        assert "Traceback" not in result.stderr

    def test_show_lists_phase_p10_from_the_cache(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        offline = fake_gh(tmp_path / "bin", OFFLINE)
        assert run_script("github/board.py", repo, "bootstrap", "--dry-run", path=str(offline)).returncode == 0
        shown = run_script("github/board.py", repo, "show", path=str(offline))
        assert shown.returncode == 0, shown.stderr
        assert any(line.startswith("  P10 ") for line in shown.stdout.splitlines())

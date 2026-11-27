from __future__ import annotations

# Standard library imports
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

# Third-party imports
import pytest

ROOT = Path(__file__).resolve().parents[3]
GIT_ENV = {
    "GIT_AUTHOR_NAME": "T",
    "GIT_AUTHOR_EMAIL": "t@example.com",
    "GIT_COMMITTER_NAME": "T",
    "GIT_COMMITTER_EMAIL": "t@example.com",
}
TICKET = "T9.01"
MINE = "backend/services/mine/src/erp_mine/a.py"
THEIRS = "backend/services/theirs/src/erp_theirs/b.py"


def git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, env={**os.environ, **GIT_ENV})


def changed(repo: Path) -> List[str]:
    code = (
        f"import sys; sys.path.insert(0, {str(ROOT / '.claude' / 'scripts' / 'tickets')!r}); import checks; "
        f"print('\\n'.join(checks.changed_files('develop', {TICKET!r}, __import__('pathlib').Path({str(repo)!r}))))"
    )
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    return [line for line in result.stdout.splitlines() if line]


def two_tickets_at_work(tmp_path: Path, paths: object) -> Path:
    git(tmp_path, "init", "-b", "develop")
    (tmp_path / "base.txt").write_text("base\n", encoding="utf-8")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-m", "base")
    for name in (MINE, THEIRS, f"docs/tickets/{TICKET}/TICKET.md"):
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text("x = 1\n", encoding="utf-8")
    state = tmp_path / ".git" / "erp" / TICKET
    state.mkdir(parents=True)
    (state / "state.json").write_text(json.dumps({"ticket": TICKET, "paths": paths}), encoding="utf-8")
    return tmp_path


def clean_tree(repo: Path) -> Dict[str, object]:
    code = (
        f"import sys, json; sys.path.insert(0, {str(ROOT / '.claude' / 'scripts' / 'tickets')!r}); import checks; "
        f"from pathlib import Path; repo = Path({str(repo)!r}); "
        f"tree = checks.isolated_tree(checks.changed_files('develop', {TICKET!r}, repo), repo); "
        f"files = sorted(str(p.relative_to(tree)) for p in tree.rglob('*') if p.is_file() and '.git' not in p.parts); "
        f"texts = {{name: (tree / name).read_text() for name in files}}; "
        f"checks.remove_tree(tree, repo); "
        f"print(json.dumps({{'files': files, 'texts': texts, 'gone': not tree.exists()}}))"
    )
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    loaded: Dict[str, object] = json.loads(result.stdout)
    return loaded


class TestChecks:
    def test_a_ticket_is_checked_on_its_own_files_only(self, tmp_path: Path) -> None:
        repo = two_tickets_at_work(tmp_path, [MINE, f"docs/tickets/{TICKET}/"])
        assert changed(repo) == [MINE, f"docs/tickets/{TICKET}/TICKET.md"]

    def test_a_ticket_without_recorded_files_is_checked_on_every_change(self, tmp_path: Path) -> None:
        repo = two_tickets_at_work(tmp_path, None)
        assert THEIRS in changed(repo)

    def test_the_checks_run_on_a_clean_tree_of_the_ticket_s_own_work_only(self, tmp_path: Path) -> None:
        repo = two_tickets_at_work(
            tmp_path, ["backend/services/mine/", "base.txt", "gone.txt", f"docs/tickets/{TICKET}/"]
        )
        (repo / "gone.txt").write_text("old\n", encoding="utf-8")
        (repo / "shared.txt").write_text("committed\n", encoding="utf-8")
        git(repo, "add", "gone.txt", "shared.txt")
        git(repo, "commit", "-m", "two more files")
        (repo / "gone.txt").unlink()
        (repo / "base.txt").write_text("changed by the ticket\n", encoding="utf-8")
        (repo / "shared.txt").write_text("changed by another ticket\n", encoding="utf-8")
        verdict = clean_tree(repo)
        assert verdict["files"] == [MINE, "base.txt", f"docs/tickets/{TICKET}/TICKET.md", "shared.txt"]
        texts = verdict["texts"]
        assert isinstance(texts, dict)
        assert texts["base.txt"] == "changed by the ticket\n"
        assert texts["shared.txt"] == "committed\n"
        assert verdict["gone"] is True
        listed = subprocess.run(["git", "worktree", "list"], cwd=repo, capture_output=True, text=True, check=True)
        assert len(listed.stdout.splitlines()) == 1

    @pytest.mark.parametrize(
        ("code", "out", "environment"),
        [
            (127, "command not found: pnpm", True),
            (1, "ModuleNotFoundError: No module named 'asyncpg'", True),
            (1, "ModuleNotFoundError: No module named 'tests.api'", False),
            (1, "ModuleNotFoundError: No module named 'erp_sales.api'", False),
            (1, "ModuleNotFoundError: No module named 'asyncpg'\nNo module named 'tests.api'", False),
            (1, "AssertionError: 1 != 2", False),
        ],
    )
    def test_a_missing_module_of_the_project_is_the_code_s_fault_not_the_environment_s(
        self, tmp_path: Path, code: int, out: str, environment: bool
    ) -> None:
        (tmp_path / "tests").mkdir()
        (tmp_path / "backend/services/sales/src/erp_sales").mkdir(parents=True)
        script = (
            f"import sys; sys.path.insert(0, {str(ROOT / '.claude' / 'scripts' / 'tickets')!r}); import checks; "
            f"from pathlib import Path; print(checks.environment_failure({code!r}, {out!r}, Path({str(tmp_path)!r})))"
        )
        result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True)
        assert result.stdout.strip() == str(environment)

    def test_a_failure_goes_to_the_file_the_tool_names_not_to_the_first_file_it_was_given(self) -> None:
        changed = [
            "backend/services/sales/src/erp_sales/__init__.py",
            "backend/services/sales/tests/service/quotes/test_quote_service.py",
            "backend/services/sales/tests/service/orders/test_order_service.py",
        ]
        out = (
            f"$ uv run ruff check {' '.join(changed)}\n"
            "PLW1510 `subprocess.run` without explicit `check` argument\n"
            "  --> backend/services/sales/tests/service/quotes/test_quote_service.py:27:18\n"
            "PLW1510 `subprocess.run` without explicit `check` argument\n"
            "  --> /tmp/erp-checks-x/backend/services/sales/tests/service/orders/test_order_service.py:27:18\n"
            "Found 2 errors.\n"
        )
        script = (
            f"import sys, json; sys.path.insert(0, {str(ROOT / '.claude' / 'scripts' / 'tickets')!r}); import checks; "
            f"print(json.dumps(checks.failing_files({out!r}, {changed!r})))"
        )
        result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True)
        named = json.loads(result.stdout)
        assert [path for path, _ in named] == changed[1:]
        assert ":27:18" in named[0][1]

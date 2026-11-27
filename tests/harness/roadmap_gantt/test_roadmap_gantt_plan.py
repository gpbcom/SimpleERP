from __future__ import annotations

# Standard library imports
import json
import re
from pathlib import Path

# First-party imports
from tests.harness.roadmap_gantt.helpers import (
    FIELD,
    LAST,
    MERGED,
    PHASES,
    ROADMAP,
    TICKETS,
    make_roadmap_repo,
    run_script,
)

SCRIPT = "reports/roadmap_gantt.py"


class TestRoadmapGanttPlan:
    def test_build_reads_every_phase_page_whatever_their_number(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        result = run_script(SCRIPT, repo, "build")
        assert result.returncode == 0, result.stderr
        page = (repo / ROADMAP / "parallel-plan.md").read_text(encoding="utf-8")
        assert f"1 of the {TICKETS} tickets are merged" in page
        assert "P10 Hosted services (" in page
        assert re.search(r"^    P10 Hosted services \(\d+\) :p10, ", page, re.MULTILINE)
        assert "<!-- gantt:plan -->" in page
        assert "<!-- /gantt:plan -->" in page

    def test_the_interactive_page_has_a_colour_and_a_row_per_phase(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        assert run_script(SCRIPT, repo, "build").returncode == 0
        html = (repo / ROADMAP / "gantt" / "parallel-plan.html").read_text(encoding="utf-8")
        assert re.findall(r"__[A-Z0-9_]+__", html) == []
        assert html.count("--p10:#") == 3
        data = json.loads(re.search(r"const DATA = (\{.*?\});\n", html).group(1))  # type: ignore[union-attr]
        assert len(data["phases"]) == len(PHASES)
        assert data["phases"][-1] == "P10 Hosted services"
        rows = {row["id"]: row for row in data["t"]}
        assert MERGED not in rows
        assert rows[LAST]["p"] == len(PHASES) - 1
        assert rows[LAST]["sp"] == "S11"
        assert "fd" in rows[FIELD]
        assert data["road"]["end"] == "2029-06-26"

    def test_check_prints_nothing_once_built_and_names_a_stale_output(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        assert run_script(SCRIPT, repo, "build").returncode == 0
        fresh = run_script(SCRIPT, repo, "check")
        assert fresh.returncode == 0, fresh.stdout
        assert fresh.stdout == ""
        graph = repo / ROADMAP / "gantt" / "ticket-graph.json"
        content = json.loads(graph.read_text(encoding="utf-8"))
        content["tickets"][LAST]["size"] = "S"
        graph.write_text(json.dumps(content), encoding="utf-8")
        stale = run_script(SCRIPT, repo, "check")
        assert stale.returncode == 1
        assert "parallel-plan.html: out of date" in stale.stdout

    def test_a_ticket_missing_from_the_graph_is_named(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        graph = repo / ROADMAP / "gantt" / "ticket-graph.json"
        content = json.loads(graph.read_text(encoding="utf-8"))
        del content["tickets"][LAST]
        graph.write_text(json.dumps(content), encoding="utf-8")
        result = run_script(SCRIPT, repo, "build")
        assert result.returncode == 1
        assert LAST in result.stderr

    def test_without_a_phase_page_it_stops_with_what_is_missing(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path, with_roadmap=False)
        result = run_script(SCRIPT, repo, "build")
        assert result.returncode == 1
        assert "No phase page in docs/specs/00-vision/roadmap/phases/" in result.stderr
        assert "Traceback" not in result.stderr

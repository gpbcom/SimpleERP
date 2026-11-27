from __future__ import annotations

# Standard library imports
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

GIT_ENV: Dict[str, str] = {
    "GIT_AUTHOR_NAME": "Test",
    "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test",
    "GIT_COMMITTER_EMAIL": "test@example.com",
}
REPOSITORY_ENV = "ERP_REPOSITORY"
ROADMAP = Path("docs/specs/00-vision/roadmap/phases")
PHASES: List[str] = [
    "Foundations",
    "DevOps agents",
    "Platform",
    "Customers and sales",
    "Purchasing and stock",
    "Accounting",
    "HR and projects",
    "Plugins",
    "Growth and insight",
    "Sectors",
    "Hosted services",
]
MERGED = "T0.01"
LAST = "T10.03"
FIELD = "T10.02"
PARTNER = "P-01"
EPICS = len(PHASES)
TICKETS = 3 * len(PHASES)
BLOCKED_BY = 2 + 3 * (len(PHASES) - 1)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True, env={**os.environ, **GIT_ENV}
    )
    return result.stdout.strip()


def slug(name: str) -> str:
    return name.lower().replace(" ", "-")


def phase_page(number: int, name: str) -> str:
    """Return a phase page in the roadmap's format: title, note, epics, sprints and ticket rows."""
    sprint = f"S{number + 1:02d}"
    rows = [
        f"| T{number}.01 Service for {name.lower()} | The `{slug(name)}` service | `backend/services/svc{number}` | "
        "Its tests pass |",
        f"| T{number}.02 Screens for {name.lower()} | The screens | `frontend/backoffice` | Playwright passes |",
    ]
    last = f"| T{number}.03 Shared code for {name.lower()} | A library | `backend/shared/lib{number}` | It is used |"
    if number == len(PHASES) - 1:
        last = f"| T{number}.03 | {sprint} | E{number}.1 | Shared code for hosted services; a library | It is used |"
    return "\n".join(
        [
            f"# 🛣️ P{number}: {name}",
            "",
            "> [!NOTE]",
            f"> P{number} delivers {name.lower()}.",
            "",
            '## <a id="epics"></a>🪜 Epics',
            "",
            "| Epic | Name | Delivers | Where | Tickets | Parallel tasks |",
            "| --- | --- | --- | --- | --- | --- |",
            f"| E{number}.1 | {name} | What P{number} gives | `backend/services/svc{number}` | "
            f"3: T{number}.01 to T{number}.03 | Tests, code, documents |",
            "",
            '## <a id="sprints"></a>🗓️ Sprint plan',
            "",
            "| Sprint | Dates | Tickets | Sprint goal | What can be shown |",
            "| --- | --- | --- | --- | --- |",
            f"| [{sprint}](#{sprint.lower()}) | Two weeks | T{number}.01 One · T{number}.02 Two · T{number}.03 Three | "
            "A goal | A demo |",
            "",
            f'### <a id="{sprint.lower()}"></a>{sprint}',
            "",
            "| Ticket | Delivers | Where | Done when |",
            "| --- | --- | --- | --- |",
            *rows,
            last,
            "",
        ]
    )


def graph() -> Dict[str, object]:
    tickets: Dict[str, Dict[str, object]] = {}
    for number in range(len(PHASES)):
        first = [f"T{number - 1}.03"] if number else []
        tickets[f"T{number}.01"] = {"deps": first, "external": [], "area": f"backend/services/svc{number}", "size": "M"}
        tickets[f"T{number}.02"] = {
            "deps": [f"T{number}.01"],
            "external": [],
            "area": "frontend/backoffice",
            "size": "S",
        }
        tickets[f"T{number}.03"] = {
            "deps": [f"T{number}.01"],
            "external": [],
            "area": f"backend/shared/lib{number}",
            "size": "L",
        }
    tickets[LAST]["external"] = [PARTNER]
    tickets[FIELD]["field"] = {"after": PARTNER, "start": "2028-03-01", "end": "2028-04-01"}
    return {
        "hours": {"agent": {"S": 0.4, "M": 0.8, "L": 1.6}, "human": {"S": 0.3, "M": 0.5, "L": 1.0}, "per_day": 6.0},
        "lanes": [
            ["serial", 1, 1.0],
            ["k2", 2, 1.0],
            ["k3", 3, 1.0],
            ["k4", 4, 1.0],
            ["k4_light", 4, 0.5],
            ["k6_light", 6, 0.5],
        ],
        "external_items": {"partners": [[PARTNER, "2028-02-01", "Pilot company", "README.md#pilot"]]},
        "tickets": tickets,
    }


def readme() -> str:
    lines = ["# 🛣️ Phases", "", "```mermaid", "gantt", "    dateFormat YYYY-MM-DD"]
    for number, name in enumerate(PHASES):
        lines.append(
            f"    P{number} {name} :p{number}, {2027 + number // 4}-0{1 + 2 * (number % 4)}-04, "
            f"{2027 + number // 4}-0{2 + 2 * (number % 4)}-26"
        )
    return "\n".join([*lines, "```", ""])


def make_roadmap_repo(base: Path, with_roadmap: bool = True) -> Path:
    """Create a repository on ``develop`` with the 11 phase pages, their README, the graph, and MERGED merged."""
    repo = base / "repo"
    (repo / "docs" / "tickets" / MERGED).mkdir(parents=True)
    git(repo, "init", "-q", "-b", "develop")
    (repo / "docs" / "tickets" / MERGED / "EXPLAIN.md").write_text("# Explain\n", encoding="utf-8")
    if with_roadmap:
        folder = repo / ROADMAP
        (folder / "gantt").mkdir(parents=True)
        for number, name in enumerate(PHASES):
            page = folder / f"{number + 1:02d}-p{number}-{slug(name)}.md"
            page.write_text(phase_page(number, name), encoding="utf-8")
        (folder / "README.md").write_text(readme(), encoding="utf-8")
        (folder / "12-parking-notes.md").write_text("# Not a phase\n", encoding="utf-8")
        (folder / "gantt" / "ticket-graph.json").write_text(json.dumps(graph(), indent=1), encoding="utf-8")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", f"{MERGED}: done")
    return repo


def run_script(script: str, repo: Path, *args: str, path: str = "") -> subprocess.CompletedProcess[str]:
    """Run a harness script of this repository on ``repo``, with ``path`` first on ``PATH`` when given."""
    env = {**os.environ, **GIT_ENV, REPOSITORY_ENV: str(repo)}
    if path:
        env["PATH"] = f"{path}{os.pathsep}{os.environ['PATH']}"
    return subprocess.run(
        [sys.executable, str(repo_root() / ".claude" / "scripts" / script), *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=120,
    )

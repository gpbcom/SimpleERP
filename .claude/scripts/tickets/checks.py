#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

USAGE = """Run every applicable check of a ticket deterministically, save the evidence, and print the verdict as JSON.

Usage, from the repository root, on the ticket branch:
    python3 .claude/scripts/tickets/checks.py --ticket T0.01 [--base develop]

Which checks apply is decided here, never by a model (TKT-6): a check whose target does not exist yet (no pnpm
workspace, no front-end package, no Python source for mypy, no ``helm`` on the PATH) is reported under
``not_applicable`` with its reason. Only project code is checked with the AGENT.md tools (``backend/``, ``frontend/``,
``plugins/``, ``sdk/``, ``infra/``, ``packs/``, ``tests/``, the layout of decision D438); the ticket's documents are
covered by ``ticket_refs.py check`` (TICKET.md, PLAN.md and PROGRESS.md refer to the specification, TKT-2), which
always runs, and ``plan.py check`` (the readable view of PLAN.md is up to date). Each check's output is saved to
``docs/tickets/<ID>/tests-evidences/<check>.txt``. The last line printed is the JSON verdict:
``{"passed": bool, "failures": [{"check", "file", "detail", "environment"}], "not_applicable": [...], "passed_checks": [...]}``.
A failure with ``environment: true`` comes from a missing tool or module, not from the code.

Several tickets share the main checkout (TKT-16), and the AGENT.md tools read a whole workspace (``uv`` every
member of the workspace, ``pnpm -r`` every package), so another ticket's half-built work would fail this one. When
the ticket has recorded its own files, every check runs in a clean temporary worktree of ``HEAD`` holding only the
ticket's own changes (TKT-6), removed afterwards; the evidence is still written to the ticket's folder.
"""

ROOT = Path(__file__).resolve().parents[3]
PROJECT_PREFIXES = ("backend/", "frontend/", "plugins/", "sdk/", "infra/", "packs/", "tests/")
# The source folders of the Python packages (D438): the shared models, the shared libraries, the services, the
# plugins and the plugin SDK.
MYPY_SOURCE_GLOBS = ("backend/models/src", "backend/shared/*/src", "backend/services/*/src", "plugins/*/src", "sdk/src")
# The folders of the Python packages, each with its own ``tests/`` folder beside its ``src/``.
PACKAGE_GLOBS = ("backend/models", "backend/shared/*", "backend/services/*", "plugins/*", "sdk")
# A change to code every package depends on runs the tests of every package, as CI does.
SHARED_PREFIXES = ("backend/models/", "backend/shared/")
SHARED_FILES = ("pyproject.toml", "uv.lock")
TIMEOUT_S = 900
# git with its LFS filter turned off: files stored in Git LFS are checked out as their pointers.
GIT_WITHOUT_LFS = ["git", "-c", "filter.lfs.smudge=", "-c", "filter.lfs.process=", "-c", "filter.lfs.required=false"]
# A failure whose output holds one of these is caused by the environment (a missing tool or module), not by the
# ticket's code: fixer agents cannot repair it, so the run stops and the person fixes the environment (TKT-6).
ENVIRONMENT_MARKERS = ("command not found",)
# A missing module is the environment's fault only when it is not the project's own code: ``No module named
# 'tests.api'`` or ``'erp_sales'`` is a wrong import or a wrong path in the ticket, which its owner fixes (L-28).
MISSING_MODULE = re.compile(r"No module named '([^']+)'")


def run(command: List[str], cwd: Path = ROOT, env: Optional[Dict[str, str]] = None) -> Tuple[int, str]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_S,
            check=False,
            env={**os.environ, **env} if env else None,
        )
        return result.returncode, (result.stdout + result.stderr).strip()
    except FileNotFoundError as error:
        return 127, f"command not found: {error.filename}"
    except subprocess.TimeoutExpired:
        return 124, f"timed out after {TIMEOUT_S} s"


def first_party(module: str, root: Path = ROOT) -> bool:
    """Tell whether a module name belongs to the repository: its tests, or one of its Python packages (D438)."""
    top = module.split(".")[0]
    if top in ("tests", "conftest") or (root / top).exists():
        return True
    return any(any(root.glob(f"{folder}/{top}")) for folder in MYPY_SOURCE_GLOBS)


def environment_failure(code: int, out: str, root: Path = ROOT) -> bool:
    """Tell whether a failed check comes from the environment (a missing tool or third-party module), not the code."""
    if code == 127 or any(marker in out for marker in ENVIRONMENT_MARKERS):
        return True
    missing = MISSING_MODULE.findall(out)
    # L-34 c: the clean tree holds only the ticket's files, so a module of the project that exists in the main
    # checkout is a wrong import or a missing file of the ticket, never the environment.
    return bool(missing) and not any(first_party(name, root) or first_party(name, ROOT) for name in missing)


def own_paths(ticket: str, root: Path = ROOT) -> Optional[List[str]]:
    """Return the files and folders the ticket recorded as its own (TKT-16), or None when it recorded none."""
    if not ticket:
        return None
    _, common = run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=root)
    state = Path(common.strip()) / "erp" / ticket / "state.json"
    paths = json.loads(state.read_text(encoding="utf-8")).get("paths") if state.is_file() else None
    return [str(path) for path in paths] if isinstance(paths, list) else None


def isolated_tree(changed: List[str], root: Path = ROOT) -> Path:
    """Make a clean worktree of ``HEAD`` holding only the given changes of ``root``, and return its folder.

    Every other ticket's uncommitted work stays out (L-22): each changed file is copied from ``root``, and a changed
    file that no longer exists there is deleted. The caller removes the tree with ``remove_tree``. The Git LFS filter
    is turned off for the checkout, so the tree holds the LFS pointers, not the images: no check reads an image, and
    downloading the tens of thousands of mock-up images of ``docs/specs/`` took minutes for every check round (TKT-6).
    """
    tree = Path(tempfile.mkdtemp(prefix="erp-checks-"))
    code, out = run([*GIT_WITHOUT_LFS, "worktree", "add", "--detach", "--force", str(tree), "HEAD"], cwd=root)
    if code != 0:
        shutil.rmtree(tree, ignore_errors=True)
        raise RuntimeError(f"Could not make the clean worktree for the checks: {out}")
    for name in changed:
        source, target = root / name, tree / name
        if source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            # A fresh modification time, never the source's (copy2): a tool that judges freshness by time (the mypy
            # cache) must see the copy as new, never reuse what it built from an older version of the file.
            shutil.copy(source, target)
        elif target.is_file() or target.is_symlink():
            target.unlink()
    return tree


def remove_tree(tree: Path, root: Path = ROOT) -> None:
    """Remove a worktree made by ``isolated_tree``, whatever its state."""
    run(["git", "worktree", "remove", "--force", str(tree)], cwd=root)
    shutil.rmtree(tree, ignore_errors=True)
    run(["git", "worktree", "prune"], cwd=root)


def changed_files(base: str, ticket: str = "", root: Path = ROOT) -> List[str]:
    # The ticket's work stays uncommitted until the ticket is done (TKT-5): compare the working tree, untracked files
    # included, with the point where the branch left the base. Several tickets share the checkout (TKT-16): when the
    # ticket recorded its own files, only those are checked, so another ticket's half-done work never fails it.
    code, merge_base = run(["git", "merge-base", base, "HEAD"], cwd=root)
    if code != 0:
        return []
    _, tracked = run(["git", "diff", "--name-only", merge_base.strip()], cwd=root)
    _, untracked = run(["git", "ls-files", "--others", "--exclude-standard"], cwd=root)
    found = sorted({line for line in f"{tracked}\n{untracked}".splitlines() if line})
    own = own_paths(ticket, root)
    if own is None:
        return found
    return [name for name in found if any(name == path or name.startswith(path.rstrip("/") + "/") for path in own)]


FAILING_FILES_MAX = 10
PRINTED_PATH = re.compile(r"[\w.\-]+(?:/[\w.\-]+)+")


def names_file(line: str, name: str) -> bool:
    """Tell whether an output line names a changed file (L-34 d).

    The line holds the whole path, or a path printed from a package root: a printed path of at least two components
    that the changed file's path ends with (``src/app.ts`` names ``frontend/backoffice/src/app.ts``).
    """
    if name in line:
        return True
    return any(name.endswith("/" + printed) for printed in PRINTED_PATH.findall(line))


def failing_files(out: str, changed: List[str]) -> List[Tuple[str, str]]:
    """Return the ticket's files a failed check's output names, each with the output lines that name it (L-32).

    A tool reports the file it fails on (``backend/services/sales/tests/service/test_x.py:27:18``), which is rarely
    the first file it was given: the failure goes to the owner of the file named, so that the right task fixes it.
    """
    # A line naming many of the ticket's files is a list (an echoed command, a list of files checked), not a failure.
    lines = [line for line in out.splitlines() if sum(names_file(line, name) for name in changed) <= 2]
    found: List[Tuple[str, str]] = []
    for name in sorted(changed, key=len, reverse=True):
        hits = [line for line in lines if names_file(line, name)]
        if hits and not any(name in other for other, _ in found):
            found.append((name, "\n".join(hits[:12])))
    order = {name: index for index, name in enumerate(changed)}
    return sorted(found, key=lambda pair: order.get(pair[0], 0))[:FAILING_FILES_MAX]


class Checks:
    def __init__(self, ticket: str, root: Path = ROOT, changed: Optional[List[str]] = None) -> None:
        self.root = root
        self.changed = changed or []
        self.evidence = ROOT / "docs" / "tickets" / ticket / "tests-evidences"
        self.evidence.mkdir(parents=True, exist_ok=True)
        self.failures: List[Dict[str, Union[str, bool]]] = []
        self.not_applicable: List[str] = []
        self.passed: List[str] = []

    def check(
        self, name: str, command: List[str], file: str, cwd: Optional[Path] = None, env: Optional[Dict[str, str]] = None
    ) -> bool:
        folder = cwd if cwd else self.root
        code, out = run(command, folder, env)
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        where = "the ticket's own files only" if self.root != ROOT else "the main checkout"
        (self.evidence / f"{slug}.txt").write_text(
            f"$ {' '.join(command)}\n(cwd {folder.relative_to(self.root) or '.'}, on {where})\n\n{out}\n",
            encoding="utf-8",
        )
        if code == 0:
            self.passed.append(name)
            return True
        detail = "\n".join(out.splitlines()[-12:])
        environment = environment_failure(code, out, self.root)
        named = [] if environment else failing_files(out, self.changed)
        if not named:
            self.failures.append({"check": name, "file": file, "detail": detail[:1500], "environment": environment})
            return False
        for path, lines in named:
            self.failures.append(
                {"check": name, "file": path, "detail": f"{lines}\n...\n{detail}"[:1500], "environment": False}
            )
        return False

    def skip(self, name: str, reason: str) -> None:
        self.not_applicable.append(f"{name}: {reason}")


def package_of(name: str) -> Optional[str]:
    """Return the folder of the Python package (D438) a changed file belongs to, or None."""
    for pattern in PACKAGE_GLOBS:
        depth = pattern.count("/") + 1
        parts = name.split("/")
        if len(parts) > depth and Path("/".join(parts[:depth])).match(pattern):
            return "/".join(parts[:depth])
    return None


def test_folders(changed: List[str], root: Path) -> List[str]:
    """Return the test folders pytest runs, one at a time: ``tests/``, then each changed package's own ``tests/``.

    A change to the shared models, a shared library, the workspace's ``pyproject.toml`` or ``uv.lock`` reaches every
    package, so it runs the tests of every package.
    """
    shared = any(name.startswith(SHARED_PREFIXES) or name in SHARED_FILES for name in changed)
    if shared:
        packages = {str(path.relative_to(root)) for pattern in PACKAGE_GLOBS for path in root.glob(pattern)}
    else:
        packages = {package for package in (package_of(name) for name in changed) if package}
    folders = ["tests"] if (root / "tests").is_dir() else []
    return folders + sorted(f"{package}/tests" for package in packages if (root / package / "tests").is_dir())


def python_checks(checks: Checks, changed: List[str]) -> None:
    root = checks.root
    files = [f for f in changed if f.endswith(".py") and f.startswith(PROJECT_PREFIXES) and (root / f).exists()]
    if not files:
        checks.skip("python", "no Python project file changed")
        return
    checks.check("ruff check", ["uv", "run", "ruff", "check", *files], files[0])
    checks.check("ruff format", ["uv", "run", "ruff", "format", "--check", *files], files[0])
    sources = sorted(str(p.relative_to(root)) for pattern in MYPY_SOURCE_GLOBS for p in root.glob(pattern))
    if sources:
        # Each source folder is a module root, as CI's check_python_project.sh gives each project (MYPYPATH): with
        # explicit_package_bases and no mypy_path, mypy would also name a library's file after its path from the root
        # (backend.shared.<lib>.src.erp_<lib>) and refuse it as found twice (TKT-6).
        checks.check(
            "mypy",
            ["uv", "run", "--all-packages", "mypy", *sources],
            sources[0],
            env={"MYPYPATH": os.pathsep.join(sources)},
        )
    else:
        checks.skip("mypy", f"not run, no source folder in the tree ({', '.join(MYPY_SOURCE_GLOBS)})")
    folders = test_folders(changed, root)
    if not folders:
        checks.skip("pytest", "no test folder in the tree")
    for folder in folders:
        name = "pytest" if folder == "tests" else f"pytest {folder.removesuffix('/tests')}"
        checks.check(name, ["uv", "run", "--all-packages", "pytest", folder, "-q", "-n", "2"], folder)


FRONT_END_PACKAGES = ("frontend/*/package.json", "frontend/portals/*/package.json", "frontend/packages/*/package.json")
WORKSPACE_FILES = ("package.json", "pnpm-workspace.yaml", "pnpm-lock.yaml")


def typescript_checks(checks: Checks, changed: List[str]) -> None:
    if not any(f.startswith("frontend/") or f in WORKSPACE_FILES for f in changed):
        checks.skip("typescript", "no front-end change")
        return
    root = checks.root
    if not any((root / name).is_file() for name in WORKSPACE_FILES[:2]):
        checks.skip("typescript", "no pnpm workspace at the repository root yet (package.json, pnpm-workspace.yaml)")
        return
    checks.check("pnpm install", ["pnpm", "install", "--frozen-lockfile"], "pnpm-lock.yaml")
    packages = [p for pattern in FRONT_END_PACKAGES for p in root.glob(pattern)]
    if not packages:
        for name in ("lint", "typecheck", "test"):
            checks.skip(name, "no front-end workspace package yet")
        return
    checks.check("lint", ["pnpm", "-r", "--if-present", "lint"], "frontend")
    checks.check("typecheck", ["pnpm", "-r", "--if-present", "typecheck"], "frontend")
    checks.check("test", ["pnpm", "-r", "--if-present", "test"], "frontend")


def helm_charts(changed: List[str], root: Path) -> List[str]:
    """Return the charts under ``infra/helm/`` the changed files belong to: the nearest folder with a ``Chart.yaml``."""
    charts = set()
    for name in changed:
        if not name.startswith("infra/helm/"):
            continue
        folder = Path(name).parent
        while folder.parts[:2] == ("infra", "helm"):
            if (root / folder / "Chart.yaml").is_file():
                charts.add(str(folder))
                break
            folder = folder.parent
    return sorted(charts)


def helm_checks(checks: Checks, changed: List[str]) -> None:
    charts = helm_charts(changed, checks.root)
    if not charts:
        checks.skip("helm lint", "no Helm chart change")
        return
    if shutil.which("helm") is None:
        checks.skip("helm lint", "helm is not installed on the PATH")
        return
    for chart in charts:
        checks.check(f"helm lint {chart}", ["helm", "lint", chart], chart)


def terraform_checks(checks: Checks, changed: List[str]) -> None:
    tf = [f for f in changed if f.startswith("infra/terraform/") and f.endswith((".tf", ".tftest.hcl"))]
    if not tf:
        checks.skip("terraform", "no Terraform change")
        return
    checks.check("terraform fmt", ["terraform", "fmt", "-check", "-recursive", "infra/terraform"], "infra/terraform")
    folders = sorted({str(Path(f).parent) if not f.endswith(".tftest.hcl") else str(Path(f).parent.parent) for f in tf})
    for folder in folders:
        path = checks.root / folder
        if not list(path.glob("*.tf")):
            continue
        if not checks.check(
            f"terraform init {folder}", ["terraform", "init", "-backend=false", "-input=false"], folder, path
        ):
            continue
        checks.check(f"terraform validate {folder}", ["terraform", "validate"], folder, path)
        if (path / "tests").is_dir():
            checks.check(f"terraform test {folder}", ["terraform", "test"], folder, path)


def main() -> int:
    args = sys.argv[1:]
    ticket = args[args.index("--ticket") + 1] if "--ticket" in args else ""
    base = args[args.index("--base") + 1] if "--base" in args else "develop"
    if not re.fullmatch(r"T\d{1,2}\.\d{2}", ticket):
        print(USAGE, file=sys.stderr)
        return 2
    changed = changed_files(base, ticket)
    tree = isolated_tree(changed) if own_paths(ticket) is not None else ROOT
    try:
        verdict = run_checks(ticket, base, changed, tree)
    except Exception as error:
        print(f"The checks stopped: {type(error).__name__}: {error}", file=sys.stderr)
        raise
    finally:
        if tree != ROOT:
            remove_tree(tree)
    print(json.dumps(verdict))
    return 0 if verdict["passed"] else 1


def run_checks(
    ticket: str, base: str, changed: List[str], root: Path
) -> Dict[str, Union[bool, List[str], List[Dict[str, Union[str, bool]]]]]:
    """Run every applicable check of the ticket in ``root`` and return the verdict."""
    checks = Checks(ticket, root, changed)
    python_checks(checks, changed)
    typescript_checks(checks, changed)
    terraform_checks(checks, changed)
    helm_checks(checks, changed)
    folder = f"docs/tickets/{ticket}"
    checks.check(
        "ticket refs", ["python3", ".claude/scripts/tickets/ticket_refs.py", "check", "--ticket", ticket], folder
    )
    if (root / folder / "PLAN.md").is_file():
        checks.check(
            "plan view",
            ["python3", ".claude/scripts/tickets/plan.py", "check", "--ticket", ticket],
            f"{folder}/PLAN.md",
        )
    return {
        "passed": not checks.failures,
        "failures": checks.failures,
        "not_applicable": checks.not_applicable,
        "passed_checks": checks.passed,
    }


if __name__ == "__main__":
    sys.exit(main())

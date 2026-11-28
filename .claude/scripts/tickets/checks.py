#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from types import ModuleType
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
ticket's own changes (TKT-6), made on disk beside the main checkout (``.<repository>-erp-checks/``, never ``/tmp``)
and removed afterwards; the evidence is still written to the ticket's folder. Because that tree leaves the other
tickets out, ``structure with open tickets`` counts the Python files of each folder with every open ticket's files.
Each changed image is built and scanned with Trivy as CI's images job does (``trivy <folder>``), then removed.
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
TREE_PREFIX = "erp-checks-"
# The clean trees are made on disk, in one folder beside the main checkout (``.<repository>-erp-checks``), never in
# ``/tmp``: ``/tmp`` is a tmpfs with a quota per user, which a few trees and their pytest files filled (2026-11-28).
CHECKS_FOLDER_SUFFIX = "-erp-checks"
# Where each open ticket records its own files (TKT-16): ``<git common dir>/erp/<ID>/state.json``.
STATE_FOLDER = "erp"
STATE_FILE = "state.json"
TICKET_ID = re.compile(r"T\d{1,2}\.\d{2}")
# The folder limit of AGENT.md and the folders it covers, as tests/conventions/ enforces them.
CONVENTION_RULES = "tests/conventions/helpers.py"
# A clean tree whose name carries no process id (made before TKT-27) is stale once untouched for this long.
UNNAMED_TREE_STALE_S = 3600
PYTEST_SUFFIX = "-pytest"
# git with its LFS filter turned off: files stored in Git LFS are checked out as their pointers.
GIT_WITHOUT_LFS = ["git", "-c", "filter.lfs.smudge=", "-c", "filter.lfs.process=", "-c", "filter.lfs.required=false"]
# A failure whose output holds one of these is caused by the environment (a missing tool or module), not by the
# ticket's code: fixer agents cannot repair it, so the run stops and the person fixes the environment (TKT-6).
ENVIRONMENT_MARKERS = (
    "command not found",
    "Cannot connect to the Docker daemon",
    "failed to download vulnerability DB",
)
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
    common = common_dir(root)
    return recorded_paths(common / STATE_FOLDER / ticket / STATE_FILE) if common is not None else None


def recorded_paths(state: Path) -> Optional[List[str]]:
    """Return the ``paths`` a ticket's ``state.json`` records, or None when the file or the list is missing."""
    paths = json.loads(state.read_text(encoding="utf-8")).get("paths") if state.is_file() else None
    return [str(path) for path in paths] if isinstance(paths, list) else None


def common_dir(root: Path = ROOT) -> Optional[Path]:
    """Return git's common directory of ``root`` (the main checkout's ``.git``), or None outside a repository."""
    code, out = run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=root)
    return Path(out.strip()) if code == 0 and out.strip() else None


def main_checkout(root: Path = ROOT) -> Path:
    """Return the main checkout of the repository ``root`` belongs to, ``root`` itself when it is no linked worktree."""
    common = common_dir(root)
    return common.parent if common is not None and common.name == ".git" else root


def checks_folder(root: Path = ROOT) -> Path:
    """Return the folder on disk where the checks make their clean trees, beside the main checkout, made if needed.

    The folder is ``<parent>/.<repository>-erp-checks/``: one per repository, shared by its linked worktrees, and
    never in ``/tmp``, a tmpfs whose quota per user the trees and their pytest files filled (TKT-27).

    Notes:
        A folder inside git's common directory (``.git/erp/checks/``) takes a worktree, but every folder under
        ``.git`` is inside a git directory for git: pytest's temporary folders, which sit beside the tree, would
        resolve every git command a test runs outside a repository of its own to the main repository's ``.git``.
    """
    main = main_checkout(root)
    folder = main.parent / f".{main.name}{CHECKS_FOLDER_SUFFIX}"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def isolated_tree(changed: List[str], root: Path = ROOT, temp: Optional[Path] = None) -> Path:
    """Make a clean worktree of ``HEAD`` holding only the given changes of ``root``, and return its folder.

    Every other ticket's uncommitted work stays out (L-22): each changed file is copied from ``root``, and a changed
    file that no longer exists there is deleted. The caller removes the tree with ``remove_tree``. The Git LFS filter
    is turned off for the checkout, so the tree holds the LFS pointers, not the images: no check reads an image, and
    downloading the tens of thousands of mock-up images of ``docs/specs/`` took minutes for every check round (TKT-6).
    The tree is named after this process (``erp-checks-<pid>-``), so that ``sweep_stale_trees`` can tell a tree still
    in use from one a killed run left behind, and a tree that cannot be made or filled leaves nothing (TKT-27). It is
    made in ``temp`` when given, else in ``checks_folder``, on disk.
    """
    folder = temp if temp is not None else checks_folder(root)
    tree = Path(tempfile.mkdtemp(prefix=f"{TREE_PREFIX}{os.getpid()}-", dir=folder))
    code, out = run([*GIT_WITHOUT_LFS, "worktree", "add", "--detach", "--force", str(tree), "HEAD"], cwd=root)
    if code != 0:
        remove_tree(tree, root)
        raise RuntimeError(f"Could not make the clean worktree for the checks: {out}")
    try:
        for name in changed:
            source, target = root / name, tree / name
            if source.is_file():
                target.parent.mkdir(parents=True, exist_ok=True)
                # A fresh modification time, never the source's (copy2): a tool that judges freshness by time (the
                # mypy cache) must see the copy as new, never reuse what it built from an older version of the file.
                shutil.copy(source, target)
            elif target.is_file() or target.is_symlink():
                target.unlink()
    except BaseException:
        remove_tree(tree, root)
        raise
    return tree


def pytest_temp(tree: Path) -> Path:
    """Return the folder beside a clean tree where pytest keeps its temporary files, removed with the tree."""
    return tree.with_name(tree.name + PYTEST_SUFFIX)


def remove_tree(tree: Path, root: Path = ROOT) -> None:
    """Remove a worktree made by ``isolated_tree``, whatever its state, with pytest's temporary files beside it."""
    run(["git", "worktree", "remove", "--force", str(tree)], cwd=root)
    shutil.rmtree(tree, ignore_errors=True)
    shutil.rmtree(pytest_temp(tree), ignore_errors=True)
    run(["git", "worktree", "prune"], cwd=root)


def process_alive(pid: int) -> bool:
    """Tell whether a process with this id is running."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def stale_tree(tree: Path) -> bool:
    """Tell whether a clean tree was left by a run that is gone: its process ended, or, unnamed, it is old."""
    match = re.match(rf"{re.escape(TREE_PREFIX)}(\d+)-", tree.name)
    if match:
        return not process_alive(int(match.group(1)))
    return time.time() - tree.stat().st_mtime > UNNAMED_TREE_STALE_S


def sweep_stale_trees(root: Path = ROOT, temp: Optional[Path] = None) -> List[Path]:
    """Remove the clean trees that killed runs of the checks left behind, and return them (TKT-27).

    A run removes its own tree when it ends, but a run killed before that (a command timeout) cannot; the next run
    removes it, and prunes git's list of worktrees, before it makes its own. A tree still in use by a running process
    is kept. The trees are looked for in ``temp`` when given, else in ``checks_folder``, where ``isolated_tree`` makes
    them.
    """
    folder = temp if temp is not None else checks_folder(root)
    trees = [
        tree
        for tree in sorted(folder.glob(f"{TREE_PREFIX}*"))
        if tree.is_dir() and not tree.name.endswith(PYTEST_SUFFIX)
    ]
    removed = [tree for tree in trees if stale_tree(tree)]
    orphans = [
        temp_folder
        for temp_folder in sorted(folder.glob(f"{TREE_PREFIX}*{PYTEST_SUFFIX}"))
        if not temp_folder.with_name(temp_folder.name.removesuffix(PYTEST_SUFFIX)).exists() and stale_tree(temp_folder)
    ]
    for orphan in orphans:
        shutil.rmtree(orphan, ignore_errors=True)
    for tree in removed:
        remove_tree(tree, root)
    run(["git", "worktree", "prune"], cwd=root)
    return removed


def pytest_command(folder: str, root: Path) -> List[str]:
    """Return the pytest command of a test folder.

    In a clean tree, pytest keeps its temporary files beside it (``pytest_temp``), never in ``/tmp/pytest-of-<user>``,
    so that they go with the tree; beside it rather than inside, so that no scan of the tree finds the files a test
    writes there (TKT-27).
    """
    command = ["uv", "run", "--all-packages", "pytest", folder, "-q", "-n", "2"]
    if root.name.startswith(TREE_PREFIX):
        # pytest makes its --basetemp folder but not the folders above it.
        pytest_temp(root).mkdir(parents=True, exist_ok=True)
        command += ["--basetemp", str(pytest_temp(root) / folder.replace("/", "-"))]
    return command


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


IMAGE_TESTS = "/tests/image/"


def image_test_dockerfiles(out: str, files: List[str], root: Path) -> List[str]:
    """Return the Dockerfile of each package whose image tests (``<package>/tests/image/``) a failed check names.

    An image test builds the package's image and starts it: when it fails, the cause is as often the ``Dockerfile``
    as the test (T0.14: the service crashed in its container, and the fix rounds went to the test only). The failure
    goes to the owners of both. The paths are those of the failure and those the output prints, absolute ones
    included (a traceback in the clean tree).
    """
    printed = ["/" + path for path in [*files, *PRINTED_PATH.findall(out)] if IMAGE_TESTS in "/" + path]
    found = []
    for pattern in PACKAGE_GLOBS:
        for folder in sorted(root.glob(pattern)):
            package = str(folder.relative_to(root))
            if (folder / "Dockerfile").is_file() and any(f"/{package}{IMAGE_TESTS}" in path for path in printed):
                found.append(f"{package}/Dockerfile")
    return found


class Checks:
    def __init__(self, ticket: str, root: Path = ROOT, changed: Optional[List[str]] = None) -> None:
        self.ticket = ticket
        self.root = root
        self.changed = changed or []
        self.evidence = ROOT / "docs" / "tickets" / ticket / "tests-evidences"
        self.evidence.mkdir(parents=True, exist_ok=True)
        self.failures: List[Dict[str, Union[str, bool]]] = []
        self.not_applicable: List[str] = []
        self.passed: List[str] = []

    def save(self, name: str, command: str, context: str, out: str) -> None:
        """Write a check's output to its evidence file, ``tests-evidences/<check>.txt``."""
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        where = "the ticket's own files only" if self.root != ROOT else "the main checkout"
        (self.evidence / f"{slug}.txt").write_text(f"{command}\n({context}, on {where})\n\n{out}\n", encoding="utf-8")

    def check(
        self,
        name: str,
        command: List[str],
        file: str,
        cwd: Optional[Path] = None,
        env: Optional[Dict[str, str]] = None,
        route: bool = True,
    ) -> bool:
        """Run one check and record its result.

        A failure goes to the ticket's files its output names (``failing_files``), else to ``file``; with ``route``
        off, always to ``file``. A failed image test also goes to its package's ``Dockerfile``.
        """
        folder = cwd if cwd else self.root
        code, out = run(command, folder, env)
        self.save(name, f"$ {' '.join(command)}", f"cwd {folder.relative_to(self.root) or '.'}", out)
        if code == 0:
            self.passed.append(name)
            return True
        detail = "\n".join(out.splitlines()[-12:])
        environment = environment_failure(code, out, self.root)
        if environment:
            self.failures.append({"check": name, "file": file, "detail": detail[:1500], "environment": True})
            return False
        named = failing_files(out, self.changed) if route else []
        found = [(path, f"{lines}\n...\n{detail}") for path, lines in named] or [(file, detail)]
        for dockerfile in image_test_dockerfiles(out, [path for path, _ in found], self.root):
            if dockerfile not in (path for path, _ in found):
                found.append((dockerfile, f"An image test built from this Dockerfile failed.\n{detail}"))
        for path, text in found:
            self.failures.append({"check": name, "file": path, "detail": text[:1500], "environment": False})
        return False

    def record(self, name: str, out: str, problems: List[Tuple[str, str]]) -> bool:
        """Record a check made in this process, with its evidence: it passes when it found no problem.

        Each problem is the file it goes to, with its detail.
        """
        self.save(name, f"# {name}", "checked by checks.py itself", out)
        if not problems:
            self.passed.append(name)
            return True
        for path, text in problems:
            self.failures.append({"check": name, "file": path, "detail": text[:1500], "environment": False})
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
        checks.check(name, pytest_command(folder, root), folder)


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


IMAGE_TAG = "scan"
# The scan of CI's images job (.github/workflows/images.yml), word for word: a fixed HIGH or CRITICAL vulnerability
# fails it.
TRIVY_SCAN = ["trivy", "image", "--severity", "HIGH,CRITICAL", "--ignore-unfixed", "--exit-code", "1"]


def image_folders(changed: List[str], root: Path) -> List[str]:
    """Return the image folders the changed files belong to: the nearest folder above each one with a ``Dockerfile``."""
    folders = set()
    for name in changed:
        folder = Path(name).parent
        while folder != Path("."):
            if (root / folder / "Dockerfile").is_file():
                folders.add(str(folder))
                break
            folder = folder.parent
    return sorted(folders)


def trivy_checks(checks: Checks, changed: List[str]) -> None:
    """Build the image of each changed image folder from the clean tree, scan it as CI does, then remove it.

    CI's images job scans every image it builds with Trivy, and the local checks did not: a vulnerable image was found
    only in CI (#894). Each image is tagged after this process (``erp-checks-<pid>-<folder>:scan``) and removed
    whatever the build and the scan gave (TKT-27). A failure of either goes to the folder's ``Dockerfile``. Without
    ``docker`` or ``trivy`` on the PATH, the scan is not applicable: a missing tool is never a failure.
    """
    folders = image_folders(changed, checks.root)
    if not folders:
        checks.skip("trivy", "no image folder changed (a folder with a Dockerfile)")
        return
    missing = [tool for tool in ("docker", "trivy") if shutil.which(tool) is None]
    if missing:
        checks.skip("trivy", f"{' and '.join(missing)} not installed on the PATH")
        return
    for folder in folders:
        dockerfile = f"{folder}/Dockerfile"
        image = f"{TREE_PREFIX}{os.getpid()}-{re.sub(r'[^a-z0-9]+', '-', folder.lower()).strip('-')}:{IMAGE_TAG}"
        try:
            build = ["docker", "build", "-f", dockerfile, "-t", image, "."]
            if checks.check(f"docker build {folder}", build, dockerfile, route=False):
                checks.check(f"trivy {folder}", [*TRIVY_SCAN, image], dockerfile, route=False)
        finally:
            run(["docker", "image", "rm", "--force", image], cwd=checks.root)


def python_file_counts(paths: List[str], root: Path) -> Dict[str, List[str]]:
    """Return the Python files of each folder the folder limit covers, as ``tests/conventions/`` counts them.

    The rule is read from ``tests/conventions/helpers.py`` of ``root``, so that it is the one the ticket's tree tests:
    the files under a package's source folder or under a test folder, ``__init__.py`` and ``conftest.py`` left out.
    """
    rules = load_convention_rules(root)
    globs = [*rules.SOURCE_GLOBS, *rules.TEST_GLOBS]
    folders: Dict[str, List[str]] = {}
    for path in paths:
        parts = Path(path).parts
        if not path.endswith(".py") or parts[-1] in rules.FOLDER_LIMIT_IGNORES:
            continue
        covered = any(
            len(parts) > pattern.count("/") + 1 and Path(*parts[: pattern.count("/") + 1]).match(pattern)
            for pattern in globs
        )
        if covered:
            folders.setdefault(str(Path(path).parent), []).append(path)
    return folders


def load_convention_rules(root: Path) -> ModuleType:
    """Load ``tests/conventions/helpers.py`` of ``root``, where the folder limit and the folders it covers are set."""
    spec = importlib.util.spec_from_file_location("convention_rules", root / CONVENTION_RULES)
    if spec is None or spec.loader is None:
        raise FileNotFoundError(root / CONVENTION_RULES)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def open_ticket_files(main: Path) -> Dict[str, List[str]]:
    """Return the files of every open ticket (TKT-16), its recorded folders expanded from the main checkout.

    A recorded path that the main checkout no longer has is listed too: the ticket deleted it.
    """
    common = common_dir(main)
    states = common / STATE_FOLDER if common is not None else None
    found: Dict[str, List[str]] = {}
    for folder in sorted(states.iterdir()) if states is not None and states.is_dir() else []:
        paths = recorded_paths(folder / STATE_FILE) if TICKET_ID.fullmatch(folder.name) else None
        if paths is None:
            continue
        files = []
        for path in paths:
            if path.endswith("/") or (main / path).is_dir():
                top = main / path.rstrip("/")
                files += sorted(str(f.relative_to(main)) for f in top.rglob("*.py") if "__pycache__" not in f.parts)
            else:
                files.append(path)
        found[folder.name] = files
    return found


def structure_checks(checks: Checks) -> None:
    """Check the folder limit on the code as it will be once every open ticket is merged.

    Each ticket's checks run in a clean tree with its own files only (TKT-6), so two tickets that each keep a folder
    at five Python files break the limit together, seen only by CI on the shared pull request (T0.18 and T0.19). This
    check takes the files of ``HEAD``, adds every open ticket's own files from the main checkout and counts the Python
    files of each folder as ``tests/conventions/`` does. A folder over the limit fails when this ticket and another
    open ticket both have files in it; the failure goes to this ticket's files there.
    """
    name = "structure with open tickets"
    main = main_checkout(checks.root)
    tickets = open_ticket_files(main)
    others = sorted(ticket for ticket in tickets if ticket != checks.ticket)
    if not others:
        checks.skip(name, "no other ticket is open")
        return
    if not (checks.root / CONVENTION_RULES).is_file():
        checks.skip(name, f"no {CONVENTION_RULES} in the tree")
        return
    _, listed = run(["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=main)
    files = set(listed.splitlines())
    owners: Dict[str, List[str]] = {}
    for ticket, paths in tickets.items():
        for path in paths:
            owners.setdefault(path, []).append(ticket)
            if (main / path).is_file():
                files.add(path)
            else:
                files.discard(path)
    rules = load_convention_rules(checks.root)
    report: List[str] = []
    problems: List[Tuple[str, str]] = []
    for folder, paths in sorted(python_file_counts(sorted(files), checks.root).items()):
        holders = sorted({ticket for path in paths for ticket in owners.get(path, [])})
        if len(paths) <= rules.FOLDER_LIMIT or checks.ticket not in holders or len(holders) < 2:
            continue
        shares = "; ".join(
            f"{ticket} has {', '.join(Path(p).name for p in paths if ticket in owners.get(p, []))}"
            for ticket in holders
        )
        committed = [Path(p).name for p in paths if p not in owners]
        text = (
            f"{folder} would hold {len(paths)} Python files once the open tickets {', '.join(holders)} are merged. "
            f"The limit is {rules.FOLDER_LIMIT} (AGENT.md, File shape): {shares}"
            + (f"; already committed: {', '.join(committed)}." if committed else ".")
        )
        report.append(text)
        problems += [(path, text) for path in paths if checks.ticket in owners.get(path, [])]
    checks.record(name, "\n".join(report) or f"No folder goes over the limit with {', '.join(others)}.", problems)


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
    if not TICKET_ID.fullmatch(ticket):
        print(USAGE, file=sys.stderr)
        return 2
    changed = changed_files(base, ticket)
    sweep_stale_trees()
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
    trivy_checks(checks, changed)
    structure_checks(checks)
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

from __future__ import annotations

# Standard library imports
import os
import subprocess
from pathlib import Path
from typing import List

SCRIPT = Path(__file__).resolve().parents[3] / ".github" / "scripts" / "playwright.sh"
FAKE_PNPM = """#!/usr/bin/env bash
printf '%s|%s\\n' "$(pwd)" "$*" >> "$FAKE_PNPM_LOG"
[ -e fail ] && exit 1
exit 0
"""


def make_project(root: Path, relative: str, config: bool = False, failing: bool = False) -> Path:
    """Create a front end with an e2e folder, and return the front end's folder."""
    project = root / relative
    (project / "e2e").mkdir(parents=True)
    if config:
        (project / "e2e" / "playwright.config.ts").write_text("export default {};\n", encoding="utf-8")
    if failing:
        (project / "fail").write_text("", encoding="utf-8")
    return project


def run_script(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    """Run the real script in ``root`` with a stand-in pnpm first on PATH."""
    bin_dir = root / "bin"
    bin_dir.mkdir(exist_ok=True)
    pnpm = bin_dir / "pnpm"
    pnpm.write_text(FAKE_PNPM, encoding="utf-8")
    pnpm.chmod(0o755)
    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}", "FAKE_PNPM_LOG": str(root / "pnpm.log")}
    return subprocess.run(
        ["bash", str(SCRIPT), *arguments], cwd=root, env=env, capture_output=True, text=True, check=False
    )


def playwright_calls(root: Path) -> List[str]:
    """Return the `playwright test` calls as `<folder relative to root>|<arguments>`."""
    log = root / "pnpm.log"
    if not log.exists():
        return []
    calls: List[str] = []
    prefix = "exec playwright test"
    for line in log.read_text(encoding="utf-8").splitlines():
        folder, arguments = line.split("|", 1)
        if arguments.startswith(prefix):
            calls.append(f"{Path(folder).relative_to(root)}|{arguments[len(prefix) :].strip()}")
    return calls

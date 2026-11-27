from __future__ import annotations

# Standard library imports
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

# Third-party imports
import pytest


@pytest.fixture
def documents() -> Tuple[str, str]:
    first = '{"openapi": "3.1.0", "info": {"title": "platform", "version": "1"}}\n'
    second = '{"openapi": "3.1.0", "info": {"title": "platform", "version": "2"}}\n'
    return first, second


@pytest.fixture
def repo(tmp_path: Path, documents: Tuple[str, str]) -> Path:
    folder = tmp_path / "repo"
    document = folder / "backend" / "services" / "platform" / "openapi.json"
    document.parent.mkdir(parents=True)
    steps: List[List[str]] = [
        ["init", "-q"],
        ["config", "user.email", "tests@example.com"],
        ["config", "user.name", "Tests"],
        ["config", "commit.gpgsign", "false"],
    ]
    for step in steps:
        subprocess.run(["git", *step], cwd=folder, check=True, capture_output=True)
    document.write_text(documents[0], encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=folder, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-q", "-m", "first"], cwd=folder, check=True, capture_output=True)
    document.write_text(documents[1], encoding="utf-8")
    subprocess.run(["git", "commit", "-q", "-am", "second"], cwd=folder, check=True, capture_output=True)
    return folder


@pytest.fixture
def first_commit(repo: Path) -> str:
    done = subprocess.run(
        ["git", "rev-list", "--max-parents=0", "HEAD"], cwd=repo, check=True, capture_output=True, text=True
    )
    return done.stdout.strip()


@pytest.fixture
def commit_without_document(repo: Path) -> str:
    tree = subprocess.run(
        ["git", "hash-object", "-t", "tree", "-w", "--stdin"],
        cwd=repo,
        input="",
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    done = subprocess.run(
        ["git", "commit-tree", tree, "-m", "empty"], cwd=repo, check=True, capture_output=True, text=True
    )
    return done.stdout.strip()


@pytest.fixture
def bin_folder(tmp_path: Path) -> Path:
    folder = tmp_path / "bin"
    folder.mkdir()
    stand_in = folder / "uv"
    script = (
        "#!/usr/bin/env bash\n"
        'here="$(dirname "$0")"\n'
        'echo "$*" >> "$here/args.txt"\n'
        'if [ -n "${ERP_CONTRACT_BASELINE+x}" ]; then\n'
        '  echo set > "$here/baseline_state.txt"\n'
        '  cat "$ERP_CONTRACT_BASELINE" > "$here/baseline.txt"\n'
        "else\n"
        '  echo unset > "$here/baseline_state.txt"\n'
        "fi\n"
        'exit "${STAND_IN_UV_EXIT:-0}"\n'
    )
    stand_in.write_text(script, encoding="utf-8")
    stand_in.chmod(0o755)
    return folder


@pytest.fixture
def environment(bin_folder: Path) -> Dict[str, str]:
    env = {key: value for key, value in os.environ.items() if key != "ERP_CONTRACT_BASELINE"}
    env["PATH"] = f"{bin_folder}{os.pathsep}{env['PATH']}"
    return env

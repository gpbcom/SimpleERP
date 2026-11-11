from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

import pytest
from pydantic import JsonValue


class FakeGh:
    """Puts a fake ``gh`` first on ``PATH`` and tells what it was asked.

    Each rule answers the calls whose arguments start with its ``args``. Nothing reaches GitHub.
    """

    STUB = Path(__file__).resolve().parent / "gh_stub.py"

    def __init__(self, folder: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        self.folder = folder
        self.bin = folder / "bin"
        self.bin.mkdir(parents=True)
        self.rules: List[Dict[str, JsonValue]] = []
        self.executable = self.bin / "gh"
        self.executable.write_text(
            f'#!/bin/sh\nexec "{sys.executable}" -I "{self.STUB}" "{folder}" "$@"\n', encoding="utf-8"
        )
        self.executable.chmod(0o755)
        (folder / "calls.jsonl").write_text("", encoding="utf-8")
        self.save()
        monkeypatch.setenv("PATH", f"{self.bin}{os.pathsep}{os.environ.get('PATH', '')}")

    def save(self) -> None:
        (self.folder / "rules.json").write_text(json.dumps(self.rules), encoding="utf-8")

    def answer(
        self,
        args: List[str],
        stdout: str = "",
        exit_code: int = 0,
        files: Optional[Dict[str, JsonValue]] = None,
        stderr: str = "",
    ) -> None:
        arguments: List[JsonValue] = list(args)
        self.rules.append(
            {"args": arguments, "stdout": stdout, "exit": exit_code, "files": files or {}, "stderr": stderr}
        )
        self.save()

    def calls(self) -> List[List[str]]:
        lines = (self.folder / "calls.jsonl").read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines if line.strip()]

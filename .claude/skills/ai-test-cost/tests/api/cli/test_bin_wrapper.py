from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


class TestBinWrapper:
    WRAPPER = Path(__file__).resolve().parents[3] / "bin" / "ai-cost"

    def test_the_wrapper_runs_the_gate_from_any_folder(self, tmp_path: Path) -> None:
        hook = json.dumps({"tool_input": {"command": "pytest -m 'llm'"}})
        environment = {key: value for key, value in os.environ.items() if key != "VIRTUAL_ENV"}
        done = subprocess.run(
            [str(self.WRAPPER), "gate"],
            input=hook,
            capture_output=True,
            text=True,
            cwd=tmp_path,
            env=environment,
            timeout=120,
            check=False,
        )
        assert done.returncode == 0, done.stderr
        assert json.loads(done.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny"

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from harness_core.testing.fake_program import FakeProgram


class TestFakeProgram:
    def test_the_program_runs_its_body(self, tmp_path: Path) -> None:
        path = FakeProgram(tmp_path / "bin").write("mmdc", 'echo "rendered $*"; exit 3')
        assert path == tmp_path / "bin" / "mmdc"
        assert os.access(path, os.X_OK)
        result = subprocess.run([str(path), "-i", "x"], capture_output=True, text=True, check=False)
        assert result.stdout == "rendered -i x\n"
        assert result.returncode == 3

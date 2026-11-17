"""The stage workflow resolves the ref it is given to a full commit SHA before checking it out (GH-13)."""

from __future__ import annotations

from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[2]
STAGE = ROOT / ".github" / "workflows" / "stage.yml"
CHECKOUT = "uses: actions/checkout@"
RESOLVE = "id: ref"


class TestStageWorkflow:
    def lines(self) -> List[str]:
        return STAGE.read_text(encoding="utf-8").splitlines()

    def step_lines(self, marker: str) -> List[str]:
        lines = self.lines()
        start = next(index for index, line in enumerate(lines) if marker in line)
        indent = len(lines[start]) - len(lines[start].lstrip(" -"))
        step = [lines[start]]
        for line in lines[start + 1 :]:
            stripped = line.lstrip(" ")
            if stripped.startswith("- ") and len(line) - len(line.lstrip(" -")) <= indent:
                break
            step.append(line)
        return step

    def test_the_ref_is_resolved_before_the_checkout(self) -> None:
        lines = self.lines()
        resolve = next((index for index, line in enumerate(lines) if RESOLVE in line), None)
        checkout = next(index for index, line in enumerate(lines) if CHECKOUT in line)
        assert resolve is not None
        assert resolve < checkout

    def test_the_resolution_asks_github_for_the_full_commit(self) -> None:
        step = "\n".join(self.step_lines(RESOLVE))
        assert "gh api" in step
        assert "repos/${{ github.repository }}/commits/" in step
        assert "REF: ${{ inputs.ref || github.sha }}" in step
        assert "GH_TOKEN: ${{ github.token }}" in step
        assert '>> "$GITHUB_OUTPUT"' in step

    def test_an_unknown_ref_fails_with_a_message_naming_it(self) -> None:
        step = "\n".join(self.step_lines(RESOLVE))
        assert "::error" in step
        assert "$REF" in step
        assert "exit 1" in step

    def test_the_checkout_uses_the_resolved_sha(self) -> None:
        step = "\n".join(self.step_lines(CHECKOUT))
        assert "ref: ${{ steps.ref.outputs.sha }}" in step

    def test_the_input_never_reaches_a_script_directly(self) -> None:
        step = self.step_lines(RESOLVE)
        run = [line for line in step if "inputs.ref" in line and "REF:" not in line]
        assert not run

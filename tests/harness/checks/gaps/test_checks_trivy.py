"""The checks scan each changed image with Trivy, as CI's images job does, and remove it afterwards (TKT-6, TKT-27).

The local checks never scanned an image, so a vulnerable one was found only in CI (#894). ``docker`` and ``trivy``
are stand-ins on the ``PATH`` here, small scripts that log their arguments.
"""

from __future__ import annotations

# Standard library imports
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Third-party imports
import pytest

# First-party imports
from tests.harness.checks.helpers import ROOT, call

FOLDER = "backend/services/sales"
DOCKERFILE = f"{FOLDER}/Dockerfile"
SOURCE = f"{FOLDER}/src/erp_sales/app.py"
IMAGE = re.compile(r"erp-checks-\d+-backend-services-sales:scan")
DAEMON_DOWN = "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?"


def stand_in(folder: Path, name: str, log: Path, exit_code: int = 0, output: str = "") -> None:
    """Write an executable ``name`` in ``folder`` that logs its arguments to ``log``, prints ``output`` and exits."""
    script = folder / name
    script.write_text(
        f"#!{sys.executable}\nimport json, sys\n"
        f"with open({str(log)!r}, 'a', encoding='utf-8') as log:\n"
        f"    log.write(json.dumps([{name!r}, *sys.argv[1:]]) + '\\n')\n"
        f"print({output!r})\nsys.exit({exit_code})\n",
        encoding="utf-8",
    )
    script.chmod(0o755)


def an_image_folder(tmp_path: Path) -> Path:
    root = tmp_path / "root"
    for name in (DOCKERFILE, SOURCE):
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text("x\n", encoding="utf-8")
    return root


def scan(
    tmp_path: Path,
    changed: List[str],
    tools: Tuple[str, ...] = ("docker", "trivy"),
    exits: Optional[Dict[str, int]] = None,
    outputs: Optional[Dict[str, str]] = None,
) -> Tuple[Dict[str, object], List[List[str]]]:
    """Scan ``changed`` with stand-ins for ``tools`` alone on the PATH, and return the verdict and the tools' log."""
    root = an_image_folder(tmp_path)
    tools_folder = tmp_path / "bin"
    tools_folder.mkdir()
    log = tmp_path / "tools.log"
    for tool in tools:
        stand_in(tools_folder, tool, log, (exits or {}).get(tool, 0), (outputs or {}).get(tool, ""))
    setup = (
        f"root = Path({str(root)!r}); checks.ROOT = root\n"
        f"c = checks.Checks('T9.05', root, {changed!r})\n"
        f"checks.trivy_checks(c, {changed!r})"
    )
    verdict = call(
        "{'failures': c.failures, 'not_applicable': c.not_applicable, 'passed': c.passed}",
        setup,
        env={"PATH": str(tools_folder)},
    )
    assert isinstance(verdict, dict)
    lines = log.read_text(encoding="utf-8").splitlines() if log.is_file() else []
    return verdict, [json.loads(line) for line in lines]


class TestChecksTrivy:
    @pytest.mark.parametrize("changed", [[SOURCE], [DOCKERFILE]])
    def test_a_changed_image_is_built_from_the_tree_scanned_as_ci_does_and_removed(
        self, tmp_path: Path, changed: List[str]
    ) -> None:
        verdict, log = scan(tmp_path, changed)
        assert [command[:2] for command in log] == [["docker", "build"], ["trivy", "image"], ["docker", "image"]]
        build, trivy, remove = log
        image = build[build.index("-t") + 1]
        assert IMAGE.fullmatch(image)
        assert build == ["docker", "build", "-f", DOCKERFILE, "-t", image, "."]
        assert trivy == ["trivy", "image", "--severity", "HIGH,CRITICAL", "--ignore-unfixed", "--exit-code", "1", image]
        assert remove == ["docker", "image", "rm", "--force", image]
        assert verdict["passed"] == [f"docker build {FOLDER}", f"trivy {FOLDER}"]
        assert verdict["failures"] == []

    def test_the_scan_is_the_one_of_ci_s_images_job(self, tmp_path: Path) -> None:
        _, log = scan(tmp_path, [SOURCE])
        workflow = (ROOT / ".github" / "workflows" / "images.yml").read_text(encoding="utf-8")
        assert f"run: {' '.join(log[1][:-1])} " in workflow

    def test_a_vulnerable_image_fails_on_its_dockerfile_and_is_still_removed(self, tmp_path: Path) -> None:
        verdict, log = scan(
            tmp_path, [SOURCE], exits={"trivy": 1}, outputs={"trivy": "Total: 1 (HIGH: 1, CRITICAL: 0)"}
        )
        failures = verdict["failures"]
        assert isinstance(failures, list)
        assert [(f["check"], f["file"], f["environment"]) for f in failures] == [(f"trivy {FOLDER}", DOCKERFILE, False)]
        assert "HIGH: 1" in failures[0]["detail"]
        assert log[-1][:3] == ["docker", "image", "rm"]

    def test_an_image_that_does_not_build_is_not_scanned_fails_on_its_dockerfile_and_is_removed(
        self, tmp_path: Path
    ) -> None:
        verdict, log = scan(tmp_path, [SOURCE], exits={"docker": 1}, outputs={"docker": f"{SOURCE}: not found"})
        failures = verdict["failures"]
        assert isinstance(failures, list)
        assert [(f["check"], f["file"]) for f in failures] == [(f"docker build {FOLDER}", DOCKERFILE)]
        assert [command[0] for command in log] == ["docker", "docker"]
        assert log[-1][:3] == ["docker", "image", "rm"]

    def test_a_docker_daemon_that_is_down_is_the_environment_s_fault(self, tmp_path: Path) -> None:
        verdict, _ = scan(tmp_path, [SOURCE], exits={"docker": 1}, outputs={"docker": DAEMON_DOWN})
        failures = verdict["failures"]
        assert isinstance(failures, list)
        assert [f["environment"] for f in failures] == [True]

    @pytest.mark.parametrize(
        ("tools", "reason"),
        [
            (("docker",), "trivy: trivy not installed on the PATH"),
            (("trivy",), "trivy: docker not installed on the PATH"),
            ((), "trivy: docker and trivy not installed on the PATH"),
        ],
    )
    def test_a_missing_tool_makes_the_scan_not_applicable_never_failed(
        self, tmp_path: Path, tools: Tuple[str, ...], reason: str
    ) -> None:
        verdict, log = scan(tmp_path, [SOURCE], tools)
        assert verdict["not_applicable"] == [reason]
        assert verdict["failures"] == []
        assert log == []

    def test_no_change_in_an_image_folder_scans_nothing(self, tmp_path: Path) -> None:
        verdict, log = scan(tmp_path, ["docs/README.md", "backend/services/README.md"])
        assert verdict["not_applicable"] == ["trivy: no image folder changed (a folder with a Dockerfile)"]
        assert log == []

    def test_the_checks_of_a_ticket_include_the_scan(self, tmp_path: Path) -> None:
        root = an_image_folder(tmp_path)
        setup = (
            f"root = Path({str(root)!r}); checks.ROOT = root\n"
            "checks.run = lambda command, cwd=None, env=None: (0, '')\n"
            "checks.shutil.which = lambda name: None\n"
            f"verdict = checks.run_checks('T9.05', 'develop', ['docs/README.md'], root)"
        )
        verdict = call("verdict", setup)
        assert isinstance(verdict, dict)
        assert "trivy: no image folder changed (a folder with a Dockerfile)" in verdict["not_applicable"]

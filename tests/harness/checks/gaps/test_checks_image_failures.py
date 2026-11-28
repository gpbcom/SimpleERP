"""A failed image test goes to the owner of its package's Dockerfile too, not only to the test's (TKT-6).

An image test builds the image and starts it: in T0.14 the service crashed in its container, and every fix round went
to the test, whose owner could not change the Dockerfile.
"""

from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Dict, List

# Third-party imports
import pytest

# First-party imports
from tests.harness.checks.helpers import call

PACKAGE = "backend/services/sales"
DOCKERFILE = f"{PACKAGE}/Dockerfile"
IMAGE_TEST = f"{PACKAGE}/tests/image/test_image.py"
SERVICE_TEST = f"{PACKAGE}/tests/service/test_orders.py"


def a_package(tmp_path: Path, dockerfile: bool = True) -> Path:
    root = tmp_path / "root"
    for name in (IMAGE_TEST, SERVICE_TEST, *([DOCKERFILE] if dockerfile else [])):
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text("x\n", encoding="utf-8")
    return root


def failures(root: Path, changed: List[str], out: str) -> List[Dict[str, object]]:
    """Run a pytest check of the package that fails with ``out``, and return the failures it records."""
    setup = (
        f"root = Path({str(root)!r}); checks.ROOT = root\n"
        f"checks.run = lambda command, cwd=None, env=None: (1, {out!r})\n"
        f"c = checks.Checks('T9.06', root, {changed!r})\n"
        f"c.check('pytest {PACKAGE}', ['uv', 'run', 'pytest', '{PACKAGE}/tests'], '{PACKAGE}/tests')"
    )
    found = call("c.failures", setup)
    assert isinstance(found, list)
    return found


class TestChecksImageFailures:
    def test_a_failed_image_test_goes_to_the_test_and_to_the_dockerfile(self, tmp_path: Path) -> None:
        out = f"FAILED {IMAGE_TEST}::TestImage::test_the_service_answers - AssertionError: exited with 3"
        found = failures(a_package(tmp_path), [IMAGE_TEST, DOCKERFILE], out)
        assert [f["file"] for f in found] == [IMAGE_TEST, DOCKERFILE]
        assert all(set(f) == {"check", "file", "detail", "environment"} for f in found)
        assert all(f["check"] == f"pytest {PACKAGE}" and f["environment"] is False for f in found)
        assert "exited with 3" in str(found[1]["detail"])

    def test_an_image_test_the_ticket_did_not_change_still_sends_the_failure_to_the_dockerfile(
        self, tmp_path: Path
    ) -> None:
        out = f"FAILED {IMAGE_TEST}::TestImage::test_the_service_answers - AssertionError"
        found = failures(a_package(tmp_path), [DOCKERFILE], out)
        assert [f["file"] for f in found] == [f"{PACKAGE}/tests", DOCKERFILE]

    def test_an_absolute_path_in_a_traceback_names_the_image_test(self, tmp_path: Path) -> None:
        out = f"/home/me/.repo-erp-checks/erp-checks-12-ab/{IMAGE_TEST}:31: AssertionError"
        found = failures(a_package(tmp_path), [IMAGE_TEST], out)
        assert [f["file"] for f in found] == [IMAGE_TEST, DOCKERFILE]

    @pytest.mark.parametrize("dockerfile", [True, False])
    def test_no_dockerfile_is_added_for_another_test_or_a_package_without_an_image(
        self, tmp_path: Path, dockerfile: bool
    ) -> None:
        test = SERVICE_TEST if dockerfile else IMAGE_TEST
        found = failures(a_package(tmp_path, dockerfile), [test], f"FAILED {test}::TestOrders::test_x")
        assert [f["file"] for f in found] == [test]

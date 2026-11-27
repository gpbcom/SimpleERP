"""House rules that a reviewer should not have to catch by eye."""

from __future__ import annotations

from tests.conventions.convention_scanner import ConventionScanner
from tests.conventions.helpers import ROOT


class TestAttributeNames:
    def test_no_instance_attribute_starts_with_an_underscore(self) -> None:
        assert not ConventionScanner(ROOT).underscore_instance_attributes()

    def test_no_class_attribute_starts_with_an_underscore(self) -> None:
        assert not ConventionScanner(ROOT).underscore_class_attributes()

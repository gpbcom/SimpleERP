"""Each layer only calls the one below it, and every layer may use ``models``."""

from __future__ import annotations

from tests.conventions.convention_scanner import ConventionScanner
from tests.conventions.helpers import ROOT


class TestLayers:
    def test_no_layer_imports_what_it_may_not(self) -> None:
        assert not ConventionScanner(ROOT).layer_imports()

    def test_every_service_has_every_layer(self) -> None:
        assert not ConventionScanner(ROOT).services_missing_layers()

    def test_no_layer_package_sits_at_the_top_of_a_source_folder(self) -> None:
        assert not ConventionScanner(ROOT).top_level_layer_packages()

    def test_no_service_imports_another_service(self) -> None:
        assert not ConventionScanner(ROOT).foreign_service_imports()

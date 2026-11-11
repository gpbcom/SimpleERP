from __future__ import annotations

import json
from pathlib import Path

from pr_watch.storage.costs.cost_ledger_reader import CostLedgerReader


class TestCostLedgerReader:
    def test_only_the_four_keys_are_read(self, tmp_path: Path) -> None:
        ledger = {"ticket": "GH-12", "cap_usd": 20, "spent_usd": 3.5, "blocked": False, "calls": [{"usd": 3.5}]}
        (tmp_path / "GH-12.json").write_text(json.dumps(ledger), encoding="utf-8")
        read = CostLedgerReader(tmp_path).read("GH-12")
        assert read is not None
        assert (read.spent_usd, read.cap_usd, read.blocked) == (3.5, 20, False)

    def test_a_missing_ledger_is_no_cost(self, tmp_path: Path) -> None:
        assert CostLedgerReader(tmp_path).read("GH-12") is None

    def test_an_unreadable_ledger_is_no_cost(self, tmp_path: Path) -> None:
        (tmp_path / "GH-12.json").write_text('{"ticket": "GH-12", "cap_usd": "lots"}', encoding="utf-8")
        (tmp_path / "GH-13.json").write_text("{", encoding="utf-8")
        assert CostLedgerReader(tmp_path).read("GH-12") is None
        assert CostLedgerReader(tmp_path).read("GH-13") is None

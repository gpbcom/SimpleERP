from __future__ import annotations

# Standard library imports
from datetime import date
from decimal import Decimal
from typing import Dict, List, Tuple, Union

# Third-party imports
from erp_models.money.money import Money

VALUE_CASES: List[Tuple[str, date, Union[Money, Decimal]]] = [
    ("standard-rate", date(2024, 1, 1), Decimal("19.6")),
    ("standard-rate", date(2025, 12, 31), Decimal("19.6")),
    ("standard-rate", date(2026, 1, 1), Decimal("20")),
    ("standard-rate", date(2027, 6, 30), Decimal("20")),
    ("standard-rate", date(2027, 7, 1), Decimal("21")),
    ("stamp-duty", date(2024, 1, 1), Money(amount=Decimal("0.10"), currency="EUR")),
    ("stamp-duty", date(2026, 12, 31), Money(amount=Decimal("0.10"), currency="EUR")),
    ("stamp-duty", date(2027, 1, 1), Money(amount=Decimal("0.20"), currency="EUR")),
]

CASE_DAYS: Dict[str, List[date]] = {
    "standard-rate": [case[1] for case in VALUE_CASES if case[0] == "standard-rate"],
    "stamp-duty": [case[1] for case in VALUE_CASES if case[0] == "stamp-duty"],
}

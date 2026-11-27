from __future__ import annotations

from erp_models.money.exceptions.se_invalid_money_exception import SEInvalidMoneyException


class SEMoneyCurrencyMismatch(SEInvalidMoneyException):
    """Exception raised when two amounts in different currencies are added."""

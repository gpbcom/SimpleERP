from __future__ import annotations

from erp_models.money.exceptions.se_invalid_money_exception import SEInvalidMoneyException


class SEMoneyInvalidCurrency(SEInvalidMoneyException):
    """Exception raised when an invalid ``currency`` is provided."""

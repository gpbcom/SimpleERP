from __future__ import annotations

# Standard library imports
import argparse
from decimal import Decimal, InvalidOperation
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from ai_cost.models.enums import AiCostCommand


class AiCostParser:
    """Describes the ``ai-cost`` command line.

    Attributes:
        logger (Logger): Logger instance.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _amount(self, text: str) -> Decimal:
        """Read an amount in USD from the command line.

        Args:
            text (str): The amount as typed.

        Returns:
            Decimal: The amount.

        Raises:
            argparse.ArgumentTypeError: When the text is not a number.
        """
        try:
            amount = Decimal(text)
        except InvalidOperation as error:
            self.logger.warning("Refused the amount %r.", text)
            raise argparse.ArgumentTypeError(f"{text!r} is not an amount in USD.") from error
        if not amount.is_finite():
            self.logger.warning("Refused the amount %r.", text)
            raise argparse.ArgumentTypeError(f"{text!r} is not an amount in USD.")
        return amount

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self) -> argparse.ArgumentParser:
        """Build the parser.

        Returns:
            argparse.ArgumentParser: The parser of every command.
        """
        root = argparse.ArgumentParser(
            prog="ai-cost", description="Run the paid AI tests of a ticket within its cap ($20 together by default)."
        )
        commands = root.add_subparsers(dest="command", required=True)
        run = commands.add_parser(AiCostCommand.RUN.value, help="run a paid AI test within its ticket's cap")
        run.add_argument("--ticket", required=True, help="the ticket the cost is charged to, such as GH-12")
        run.add_argument("--estimate-usd", type=self._amount, required=True, help="what the run should cost")
        run.add_argument("--label", default="", help="what the run tests")
        run.add_argument("--soft", action="store_true", help="charge the estimate instead of measuring the run")
        run.add_argument("--on-kill", help="a command that stops what the run started elsewhere")
        run.add_argument("argv", nargs=argparse.REMAINDER, help="-- then the command")
        status = commands.add_parser(AiCostCommand.STATUS.value, help="print a ticket's spend and runs")
        status.add_argument("ticket")
        remaining = commands.add_parser(AiCostCommand.REMAINING.value, help="print what a ticket may still spend")
        remaining.add_argument("ticket")
        charge = commands.add_parser(AiCostCommand.CHARGE.value, help="charge a cost measured elsewhere")
        charge.add_argument("ticket")
        charge.add_argument("usd", type=self._amount)
        charge.add_argument("--label", required=True)
        charge.add_argument("--note")
        raise_cap = commands.add_parser(AiCostCommand.RAISE_CAP.value, help="set a ticket's cap, for the human only")
        raise_cap.add_argument("ticket")
        raise_cap.add_argument("usd", type=self._amount)
        commands.add_parser(AiCostCommand.GATE.value, help="answer the PreToolUse hook on Bash")
        self.logger.debug("Built the ai-cost parser.")
        return root

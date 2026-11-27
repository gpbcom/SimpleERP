from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import Optional


class SyntheticBuilder[T](ABC):
    """Abstract base of the builders of synthetic data.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - A builder returns the next generated value at each ``build()``, and **the sequence is the same for the same
          inputs and seed**, so that a test can be repeated.
        - A builder holds no data of its own: every word comes from the synthetic catalogue.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create the builder.

        Args:
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def build(self) -> T:
        """Build the next value of the sequence.

        Returns:
            T: The next generated value.
        """

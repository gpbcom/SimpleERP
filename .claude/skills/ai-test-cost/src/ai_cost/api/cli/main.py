from __future__ import annotations

# Standard library imports
import sys

# First-party imports
from ai_cost.api.factories.cli.cli_command_factory import CliCommandFactory
from ai_cost.models.settings.guard_settings import GuardSettings
from harness_core.logs.harness_logging import HarnessLogging


def main() -> int:
    """Run the ``ai-cost`` command line.

    Returns:
        int: The exit code: the test's own for ``run``, 3 when refused or killed at the cap, 2 on a usage error.

    Notes:
        The logs go to the harness log file only, because the hook's standard output is its answer.
    """
    logger = HarnessLogging("ai-test-cost").logger("ai_cost")
    settings_file = GuardSettings.SKILL_DIR / "conf" / "settings.yaml"
    cli = CliCommandFactory(settings_file, logger).cli(sys.argv[1:], sys.stdin, sys.stdout, sys.stderr)
    cli.execute()
    return cli.exit_code

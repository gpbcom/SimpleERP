from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidStageDeploymentException(SEPrWatchError):
    """Exception raised when an invalid StageDeployment is provided."""

from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_stage_deployment_exception import SEInvalidStageDeploymentException


class SEStageDeploymentInvalidLink(SEInvalidStageDeploymentException):
    """Exception raised when an invalid ``link`` is provided."""

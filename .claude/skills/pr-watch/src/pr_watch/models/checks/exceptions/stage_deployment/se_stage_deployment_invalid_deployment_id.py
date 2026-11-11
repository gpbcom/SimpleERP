from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_stage_deployment_exception import SEInvalidStageDeploymentException


class SEStageDeploymentInvalidDeploymentId(SEInvalidStageDeploymentException):
    """Exception raised when an invalid ``deployment_id`` is provided."""

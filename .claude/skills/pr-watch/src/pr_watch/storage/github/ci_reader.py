from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import PurePosixPath
from typing import ClassVar, List, Optional

from harness_core.github.github_connection import GithubConnection
from harness_core.github.json_payload import JsonPayload

# First-party imports
from pr_watch.models.checks.check_run import CheckRun
from pr_watch.models.checks.pending_approval import PendingApproval
from pr_watch.models.checks.stage_deployment import StageDeployment
from pr_watch.models.checks.workflow_run import WorkflowRun


class CiReader:
    """Reads what GitHub ran on a commit: check runs, workflow runs, stage deployments and pending approvals.

    Attributes:
        WAITING (str): The status of a workflow run that waits for an approval.
        connection (GithubConnection): The HTTP client.
        repository (str): The repository, ``<owner>/<name>``.
        logger (Logger): Logger instance.

    Notes:
        - A deployment's latest status is the first one GitHub lists.
        - A pending approval waits since its wait timer started, or else since its run last changed: the run changes
          to ``waiting`` when it reaches the protected environment.
    """

    WAITING: ClassVar[str] = "waiting"

    def __init__(self, connection: GithubConnection, repository: str, logger: Optional[Logger] = None) -> None:
        """Set the repository.

        Args:
            connection (GithubConnection): The HTTP client.
            repository (str): The repository, ``<owner>/<name>``.
            logger (Optional[Logger]): Logger instance.
        """
        self.connection = connection
        self.repository = repository
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    async def _deployment(self, environment: str, sha: str) -> Optional[StageDeployment]:
        """Read the latest deployment of a commit to one environment.

        Args:
            environment (str): The environment.
            sha (str): The commit.

        Returns:
            Optional[StageDeployment]: The deployment and its latest status, ``None`` when there is none.
        """
        deployments = await self.connection.pages(
            f"/repos/{self.repository}/deployments", {"sha": sha, "environment": environment}
        )
        if not deployments:
            return None
        deployment_id = deployments[0].get("id")
        statuses = await self.connection.pages(f"/repos/{self.repository}/deployments/{deployment_id}/statuses")
        latest = statuses[0] if statuses else {}
        link = JsonPayload.text(latest, "log_url") or JsonPayload.text(latest, "target_url")
        return StageDeployment(
            environment=environment,
            deployment_id=deployment_id,
            state=JsonPayload.text(latest, "state") or None,
            link=link or None,
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    async def check_runs(self, sha: str) -> List[CheckRun]:
        """List the check runs of a commit.

        Args:
            sha (str): The commit.

        Returns:
            List[CheckRun]: Each check run.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        items = await self.connection.pages(f"/repos/{self.repository}/commits/{sha}/check-runs", key="check_runs")
        runs = [
            CheckRun(
                id=item.get("id"),
                name=item.get("name"),
                conclusion=JsonPayload.text(item, "conclusion") or None,
                link=JsonPayload.text(item, "html_url") or None,
                suite_id=JsonPayload.child(item, "check_suite").get("id"),
            )
            for item in items
        ]
        self.logger.debug("%s has %d check runs.", sha[:8], len(runs))
        return runs

    async def workflow_runs(self, branch: str, sha: str) -> List[WorkflowRun]:
        """List the workflow runs of a commit on a branch.

        Args:
            branch (str): The branch.
            sha (str): The commit.

        Returns:
            List[WorkflowRun]: Each run, the newest first.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        items = await self.connection.pages(
            f"/repos/{self.repository}/actions/runs", {"branch": branch, "head_sha": sha}, key="workflow_runs"
        )
        runs = [
            WorkflowRun(
                id=item.get("id"),
                workflow=PurePosixPath(JsonPayload.text(item, "path")).name or JsonPayload.text(item, "name"),
                conclusion=JsonPayload.text(item, "conclusion") or None,
                link=item.get("html_url"),
                suite_id=item.get("check_suite_id"),
            )
            for item in items
        ]
        self.logger.debug("%s has %d workflow runs.", sha[:8], len(runs))
        return runs

    async def deployments(self, sha: str, environments: List[str]) -> List[StageDeployment]:
        """Read the latest deployment of a commit to each environment.

        Args:
            sha (str): The commit.
            environments (List[str]): The environments, such as ``dev`` and ``qa``.

        Returns:
            List[StageDeployment]: One per environment the commit was deployed to.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        found = [await self._deployment(environment, sha) for environment in environments]
        deployments = [deployment for deployment in found if deployment is not None]
        self.logger.debug("%s was deployed to %d environments.", sha[:8], len(deployments))
        return deployments

    async def pending_approvals(self, sha: str) -> List[PendingApproval]:
        """List the deployments of a commit that wait for an approval.

        Args:
            sha (str): The commit.

        Returns:
            List[PendingApproval]: One per waiting run and environment.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        runs = await self.connection.pages(
            f"/repos/{self.repository}/actions/runs", {"head_sha": sha, "status": self.WAITING}, key="workflow_runs"
        )
        approvals: List[PendingApproval] = []
        for run in runs:
            payload = await self.connection.get(
                f"/repos/{self.repository}/actions/runs/{run.get('id')}/pending_deployments"
            )
            for pending in JsonPayload.objects(payload):
                approvals.append(
                    PendingApproval(
                        run_id=run.get("id"),
                        environment=JsonPayload.text(JsonPayload.child(pending, "environment"), "name"),
                        waiting_since=JsonPayload.text(pending, "wait_timer_started_at") or run.get("updated_at"),
                    )
                )
        self.logger.debug("%s has %d deployments waiting for approval.", sha[:8], len(approvals))
        return approvals

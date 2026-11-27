# DevOps

How the platform is operated day to day: environments, infrastructure as code, GitOps, secrets, on-call, runbooks.
Nothing of the target is built yet.

## Today

The pipeline and stages of today are in [CI/CD and stages](../delivery/ci-cd-and-stages.md).

## Target design (specified in GH-2, not built yet)

**GitOps (D420).** Infrastructure in Terraform; cluster contents (Helm charts, versions, settings) declared in a Git
repository and applied by Argo CD; no manual change on a cluster; every change reviewed, and rolled back by a revert.

**Environments.** Ephemeral dev and QA stages per change (as today), a long-lived staging with seeded companies that
mirrors production, then production; releases are promoted from staging with canary rollouts, a few companies first.

**On-call.** An on-call rota of hosting engineers (U48, D452) paged by the SLO alerts
([Observability](observability.md)); every fix kind the hosted support assistant may propose (F20) is a scripted, tested
runbook; incidents get a timeline and a blameless review; the status page is updated from the incident tool.

Decided in [D420](../../specs/06-decisions/technical/d420-devops-practice.md).

**DevOps agents as a team** (Proposed,
[D567](../../specs/06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md),
[FL-F25-08](../../specs/02-functional/f25-devops-agents/flows/fl-f25-08-team-builds-a-ticket.md)): an approved ticket is
built by agent roles (architect, back end, front end, tests, read-only reviewer, release) under a work contract the
maintainer approves, in worktrees from one starting commit, verified on one candidate commit and delivered as a draft
pull request; one active run per repository, a 30-minute timeout, two repair cycles at most, checkpoints on GitHub so a
rerun resumes.

Last reviewed: 2026-11-12 (GH-2)

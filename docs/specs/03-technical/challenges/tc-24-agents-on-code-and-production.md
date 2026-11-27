🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🤖 TC-24 Agents that read production and write code

# 🤖 TC-24 Agents that read production and write code

**Status:** ✅ listed for the technical interviews

## Challenge

Let DevOps agents read the fully managed SimpleERP, the repository and the specs, file USER features, draft spec
changes and propose fixes as pull requests, while maintainers keep every approval, merge and deployment.

## Raised by

- [F25 DevOps agents (hosted edition)](../../02-functional/f25-devops-agents/README.md)
- [F20 Hosted support assistant (hosted edition)](../../02-functional/f20-hosted-support-assistant/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md)
- [T6 MCP and A2A gateway](../t06-mcp-and-a2a-gateway/README.md)

## Why it is hard

- Production access is powerful: read-only, per customer, masked, audited.
- Agent-written pull requests must pass the same checks as people's, tests first.
- Approval must be enforced by the tooling, not by trust.
- Many requests at once must not flood the maintainers.

## Already decided

- [D388](../../06-decisions/vision/d388-hosted-edition-open-core.md) Hosted edition: closed services around the open
  core
- [D393](../../06-decisions/f20-hosted-support-assistant/d393-hosted-support-assistant-coverage.md) Hosted support
  assistant: access and approvals
- [D432](../../06-decisions/f25-devops-agents/d432-devops-agents-coverage.md) DevOps agents
- [D434](../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md) Maintainers approve agents' work
- [D435](../../06-decisions/f25-devops-agents/d435-agents-access-and-limits.md) The agents' access and limits

## Options to weigh

- GitHub App tokens with the narrowest scopes, per repository.
- The harness check refusing Ready while needs-maintainer-approval is on. Revised by
  [D441](../../06-decisions/f25-devops-agents/d441-approval-label-reported-and-reverted.md): a workflow reports and
  reverts label removals and status moves by non-maintainers, with branch protection; Backlog is the only status allowed
  while the label is on (harness ticket GH-23, pull request #24, pending until merged).
- Agent runs on the durable workflow engine, metered and budgeted.

- (Proposed) The agent team of
  [FL-F25-08](../../02-functional/f25-devops-agents/flows/fl-f25-08-team-builds-a-ticket.md): one active run per
  repository with the workers in parallel inside it, worktrees from one starting commit, verification on one candidate
  commit, two repair cycles at most, checkpoints kept on GitHub. Decided in
  [D567](../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).

## Settled in

- 19f Security ([chapter](../../../technical/security/security.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- 19z DevOps ([chapter](../../../technical/operations/devops.md))
- 19o Tests: unit, GUI, E2E and load ([chapter](../../../technical/delivery/tests-and-traceability.md))
- Then the technical capabilities: [T6 MCP and A2A gateway](../t06-mcp-and-a2a-gateway/README.md),
  [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md).

## Questions for the interview

- How many agent runs at once?
- Which repositories may the agents read besides SimpleERP's?

---

⬅️ [TC-23 Many connectors, connected in few steps, kept working](tc-23-many-connectors-few-steps.md) ·
⬆️ [Up](README.md)

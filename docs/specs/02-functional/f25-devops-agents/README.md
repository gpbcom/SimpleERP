🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🤖 F25 DevOps agents (hosted edition)

# 🤖 F25 DevOps agents (hosted edition)

**Status:** ✅ specified

Build step: 1. DevOps agents.

## Summary

In the hosted edition, customers' bug reports and feature requests become GitHub USER features with one ticket labelled
USER-FEATURE-REQUEST or USER-REPORTED-BUG; DevOps agents, with read access to the fully managed simple-ERP and to the
repository and specs, prepare the work (SPECS features with spec pull requests, or PRODUCT tickets with fixes as pull
requests), and maintainers approve ([D432](../../06-decisions/f25-devops-agents/d432-devops-agents-coverage.md),
[D433](../../06-decisions/f25-devops-agents/d433-user-family-and-labels.md),
[D434](../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md)). A closed hosted service around the open
product ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)).

## Scope

- **Intake:** reports and requests from the app and the support assistant, USER features and tickets, duplicates.
- **Features:** study of specs and code, spec pull requests, SPECS features and tickets.
- **Bugs:** read-only reproduction, root cause, failing test and fix, PRODUCT tickets.
- **Govern:** maintainers' approval, revisions, rights, costs, quality.
- **Tell:** status, shipping, feature-factory offers, the AI assistant.
- **Triage, security and votes:** severity and priority with target times, vulnerability handling under the CRA, checks
  on agents' spec pull requests, a public list of declined requests with votes (D482).
- **Agent team:** (Proposed) an approved ticket is built by six agent roles under a work contract the maintainer
  approves, each implementation role in its own worktree, integrated in dependency order, verified on one candidate
  commit by a test role and a read-only reviewer, and delivered as a draft pull request with its evidence; at most two
  repair cycles; one active run per repository, resumed from its checkpoint. The maintainer still reviews, approves and
  merges (D434). Flow [FL-F25-08](flows/fl-f25-08-team-builds-a-ticket.md), decision
  [D567](../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U07 Administrator](../../01-users/personas/u07-administrator.md),
[U47 simple-ERP maintainer](../../01-users/personas/u47-simple-erp-maintainer.md),
[U48 Hosting engineer](../../01-users/personas/u48-hosting-engineer.md).

**Build study:** [How to build the DevOps agents](build-study.md).

## Out of scope

- Merging and deploying: maintainers (D434).
- Support conversations: F20.
- Paid custom features: F19.

## Technical capabilities used

- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md) (GitHub and repository tools)
- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md) (read-only production
  access)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 1, DevOps agents, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🛠️ |  | [How to build the DevOps agents](build-study.md) | ✅ |
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Integrations hub](../f24-integrations-hub/README.md) · ⬆️ [Up](../README.md)

🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-23 No worker starts before the contract is approved

# 📏 BR-F25-23 No worker starts before the contract is approved

**Status:** 🔄 waiting for the owner

## Statement

No worker of the agent team starts, and no worker commit is made, before a maintainer has approved the work contract of
the ticket. An approval belongs to one version of the contract: any change after it puts the contract back to Draft and
needs a new approval. The contract's approval adds to the ticket's approval and to the review of the pull request, and
never replaces them.

## Why

The owner asked that the contract be approved before the workers start
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
Approval stays the maintainers' ([D434](../../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md)) and
is enforced by the tooling, not by the agents' instructions
([D441](../../../06-decisions/f25-devops-agents/d441-approval-label-reported-and-reverted.md)).

## Examples

| Case | Result |
|---|---|
| A Proposed contract | no worker runs |
| Contract version 2 approved | the workers start from its starting commit |
| The Architect revises an approved contract | back to Draft, the workers wait for a new approval |
| An agent role approves its own contract | refused and audited |
| An approved contract and its pull request | still reviewed and merged by a maintainer only (BR-F25-05) |

## Applies to

- [UC-F25-30](../use-cases/08-team-builds-a-ticket/uc-f25-30-approve-the-work-contract.md)
- [BR-F25-05 Agents never merge or deploy](br-f25-05-agents-never-merge-or-deploy.md)
- [BR-F25-07 Approval before Ready](br-f25-07-approval-before-ready.md)
- [E-F25-19 Work contract](../data/e-f25-19-work-contract.md)

## Exceptions

None.

## Configurable

No: the approval cannot be turned off.

## Open questions

None.

---

⬅️ [BR-F25-22 A contract gives each role its own files](br-f25-22-a-contract-gives-each-role-its-own-files.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F25-24 One role, one worktree, one starting commit](br-f25-24-one-role-one-worktree-one-starting-commit.md)

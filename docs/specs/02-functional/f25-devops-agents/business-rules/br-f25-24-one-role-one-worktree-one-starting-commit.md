🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-24 One role, one worktree, one starting commit

# 📏 BR-F25-24 One role, one worktree, one starting commit

**Status:** ✅ specified

## Statement

Each implementation role of a run works in one git worktree, on one branch of its own, created from the starting commit
the approved contract records. Every worker of the run starts from that same commit, and no worker shares a worktree or
a branch with another role.

## Why

Workers that start from different commits, or share a folder, cannot be integrated in a known order, and their failures
spill over each other. The owner asked for isolated worktrees from one recorded starting commit
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).

## Examples

| Case | Result |
|---|---|
| Three roles with tasks | three worktrees, three branches, one starting commit |
| A worker created from the latest head instead | refused, the run uses the recorded commit |
| Two roles asked to share a branch | refused |
| A role with no task | no worktree |
| The Code Reviewer | no worktree to write in, it reads the candidate commit (BR-F25-27) |

## Applies to

- [UC-F25-31](../use-cases/08-team-builds-a-ticket/uc-f25-31-build-in-isolated-worktrees.md)
- [E-F25-20 Agent role](../data/e-f25-20-agent-role.md)
- [BR-F25-22](br-f25-22-a-contract-gives-each-role-its-own-files.md)
- [BR-F25-23](br-f25-23-no-worker-starts-before-the-contract-is-approved.md)
- [E-F25-19 Work contract](../data/e-f25-19-work-contract.md)

## Exceptions

A repair cycle ([UC-F25-35](../use-cases/08-team-builds-a-ticket/uc-f25-35-repair-a-rejected-candidate.md))
starts the repairing worker from the rejected candidate commit, recorded as the starting commit of that cycle.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-23](br-f25-23-no-worker-starts-before-the-contract-is-approved.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-25](br-f25-25-a-handoff-without-its-commits-and-checks-is-refused.md)

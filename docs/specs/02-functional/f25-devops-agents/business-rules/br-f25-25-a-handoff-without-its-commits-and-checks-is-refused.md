🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-25 A handoff without its commits and checks is refused

# 📏 BR-F25-25 A handoff without its commits and checks is refused

**Status:** ✅ specified

## Statement

A worker's handoff is accepted only if it carries its role, worktree, branch and starting commit, every commit in order
after the starting commit, the files those commits change, every required check of its role with its command and exit
code, and its blockers, and only if those facts match the branch and the recorded check runs. Otherwise it is refused,
and nothing of it is integrated.

## Why

A summary written by an agent may leave out what failed. The owner asked for a structured handoff with the commits, the
files, the checks and their exit codes
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
Every run already keeps what it read and wrote ([BR-F25-11](br-f25-11-agents-metered-and-audited.md)).

## Examples

| Case | Result |
|---|---|
| Every commit, file and check listed, exit codes 0 | Accepted |
| A commit on the branch that is not listed | Refused, the commit named |
| A check listed as passed with no exit code | Refused |
| A required check at exit code 1, with its blocker | Blocked, the maintainer decides |
| A changed file owned by another role | Refused (BR-F25-22) |

## Applies to

- [UC-F25-32](../use-cases/08-team-builds-a-ticket/uc-f25-32-hand-over-a-workers-result.md)
- [E-F25-21 Worker handoff](../data/e-f25-21-worker-handoff.md)
- [BR-F25-11 Agents are metered and audited](br-f25-11-agents-metered-and-audited.md)
- [BR-F25-22](br-f25-22-a-contract-gives-each-role-its-own-files.md)
- [BR-F25-24](br-f25-24-one-role-one-worktree-one-starting-commit.md)
- [E-F25-19 Work contract](../data/e-f25-19-work-contract.md)

## Exceptions

None.

## Configurable

The contract may ask for more evidence than these items, such as screenshots for a screen change, never for
less.

## Open questions

None.

---

⬅️ [BR-F25-24 One role, one worktree, one starting commit](br-f25-24-one-role-one-worktree-one-starting-commit.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F25-26](br-f25-26-a-conflict-goes-back-to-the-architect-never-guessed.md)

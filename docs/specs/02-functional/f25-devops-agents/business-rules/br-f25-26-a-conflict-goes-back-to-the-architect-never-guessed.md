🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-26 A conflict goes back to the architect, never guessed

# 📏 BR-F25-26 A conflict goes back to the architect, never guessed

**Status:** ✅ specified

## Statement

When a worker's commit does not apply cleanly during integration, the Release Engineer aborts that pick and stops. It
never edits a file, chooses a side or merges to resolve the conflict. The conflict, with its files, roles and commits,
goes back to the Architect, who changes the contract, and the changed contract needs a maintainer's approval before any
worker resumes.

## Why

A guessed resolution may drop one role's change without anyone seeing it. The owner asked that a conflict go back to the
architect, never guessed, with the conflicted pick aborted
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
A conflict means two roles touched the same thing, which the contract should have prevented
([BR-F25-22](br-f25-22-a-contract-gives-each-role-its-own-files.md)).

## Examples

| Case | Result |
|---|---|
| A clean pick | applied, the next one follows |
| A conflicted pick | aborted, the integration stopped, the Architect told |
| The Architect gives the file to one role | contract version 3 in Draft, approval asked (BR-F25-23) |
| The Release Engineer edits the file to make it apply | refused: it has no write tool on the workers' files |
| Commits applied before the conflict | kept on the integration branch and reused at the next integration |

## Applies to

- [UC-F25-33](../use-cases/08-team-builds-a-ticket/uc-f25-33-integrate-the-workers-commits.md)
- [BR-F25-05 Agents never merge or deploy](br-f25-05-agents-never-merge-or-deploy.md)
- [BR-F25-22](br-f25-22-a-contract-gives-each-role-its-own-files.md)
- [BR-F25-23](br-f25-23-no-worker-starts-before-the-contract-is-approved.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-25](br-f25-25-a-handoff-without-its-commits-and-checks-is-refused.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-27 An approval belongs to one commit](br-f25-27-an-approval-belongs-to-one-commit.md)

🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-22 A contract gives each role its own files

# 📏 BR-F25-22 A contract gives each role its own files

**Status:** ✅ specified

## Statement

A work contract gives every file the ticket may change to exactly one role. A worker edits only the files its role owns,
and a file no role owns is not changed. The contract also lists the acceptance criteria with the check of each, the
shared API and data contracts, the tasks with their dependencies, the required checks and the evidence each handoff
carries.

## Why

Two workers editing the same file produce conflicts that someone must then guess how to resolve. The owner asked for an
agent team whose roles work in parallel from an approved contract
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
The contract is built from what the agents studied first ([BR-F25-06](br-f25-06-specs-and-code-studied-first.md)).

## Examples

| Case | Result |
|---|---|
| A file listed under the Backend Engineer | only the Backend Engineer edits it |
| A file owned by two roles | flagged as an overlap, the contract cannot be approved |
| A file the study note names that no role owns | flagged as a gap |
| A worker's commit changes a file of another role | its handoff is refused (BR-F25-25) |
| A data shape used by two roles | written once in the shared contracts, both build against it |

## Applies to

- [UC-F25-29](../use-cases/08-team-builds-a-ticket/uc-f25-29-write-the-work-contract-of-a-ticket.md)
- [E-F25-19 Work contract](../data/e-f25-19-work-contract.md)
- [BR-F25-06 Specs and code studied first](br-f25-06-specs-and-code-studied-first.md)
- [BR-F25-25](br-f25-25-a-handoff-without-its-commits-and-checks-is-refused.md)
- [E-F25-20 Agent role](../data/e-f25-20-agent-role.md)

## Exceptions

A generated file, such as a lock file, belongs to the role whose task generates it, named in the contract.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-21 The changelog shows installed modules only](br-f25-21-the-changelog-shows-installed-modules-only.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F25-23](br-f25-23-no-worker-starts-before-the-contract-is-approved.md)

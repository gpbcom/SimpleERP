🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-29 A draft pull request carries its evidence and screenshots

# 📏 BR-F25-29 A draft pull request carries its evidence and screenshots

**Status:** ✅ specified

## Statement

A draft pull request of the agent team carries in its body, kept outside every tracked source file: the issue and the
problem, the changes, the acceptance results, the exact verified commit, the commands with their exit codes and
evidence, the known limits and the instructions for the review. Its head equals the verified commit. For a FRONTEND
ticket, the work contract and the pull request show the screenshots of its specification. The GitHub CI results are
reported apart from the local checks. One branch has one pull request, updated and never duplicated, and no agent marks
it ready, approves it or merges it.

## Why

The maintainer must see what was checked, on which commit, before reviewing
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
The owner added the screenshots of a FRONTEND ticket's specification to the harness's ticket rule (GIT-10) on 2026-11-16
(ticket #34). Agents never merge ([D434](../../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md),
[BR-F25-05](br-f25-05-agents-never-merge-or-deploy.md)).

## Examples

| Case | Result |
|---|---|
| Head 9f2c4e1, verified 9f2c4e1 | the draft opens |
| Head moved to a1c0d22 after the PASS | not opened: a1c0d22 is verified first |
| A FRONTEND ticket without screenshots of its specification | refused |
| A second run on the same branch | the same pull request updated |
| Local checks passed, GitHub CI failed | both shown apart, the maintainer told |

## Applies to

- [UC-F25-36](../use-cases/08-team-builds-a-ticket/uc-f25-36-open-the-draft-pull-request-with-its-evidence.md)
- [UC-F25-12](../use-cases/04-approve-and-govern/uc-f25-12-approve-or-refuse-agents-tickets.md)
- [BR-F25-05 Agents never merge or deploy](br-f25-05-agents-never-merge-or-deploy.md)
- [BR-F25-27 An approval belongs to one commit](br-f25-27-an-approval-belongs-to-one-commit.md)

## Exceptions

None.

## Configurable

The order and the wording of the body's sections, by the maintainers; no section may be removed.

## Open questions

None.

---

⬅️ [BR-F25-28](br-f25-28-two-repair-cycles-at-most-then-a-maintainer-decides.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-30](br-f25-30-one-active-run-per-repository-resumed-from-its-checkpoint.md)

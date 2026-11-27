🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-27 An approval belongs to one commit

# 📏 BR-F25-27 An approval belongs to one commit

**Status:** 🔄 waiting for the owner

## Statement

A verification and the code reviewer's PASS hold for the exact candidate commit they name and for no other. Any change
to the code, a new commit, a rebase or an amended commit, voids them; the new commit is verified again by the test
engineer and reviewed again by the code reviewer. A required check that cannot run makes the verification Blocked, never
Passed. During the verification the test engineer never edits a source file and never weakens a test. The PASS is an
extra gate before the maintainer, never a replacement of the maintainer's review.

## Why

An approval of other code proves nothing about the code under review: "an approval belongs to a commit; change the code,
earn it again", as the owner asked on 2026-11-16
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
The maintainer still approves and merges
([D434](../../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md),
[BR-F25-05](br-f25-05-agents-never-merge-or-deploy.md)).

## Examples

| Case | Result |
|---|---|
| Every check passed and PASS on 9f2c4e1 | Passed for 9f2c4e1 only |
| A commit pushed after the PASS | Superseded: verified and reviewed again |
| The end-to-end tests cannot start | Blocked, not Passed |
| The test engineer removes a failing assertion | refused and recorded |
| PASS from the code reviewer | the maintainer still reviews and approves (FL-F25-04) |

## Applies to

- [UC-F25-34](../use-cases/08-team-builds-a-ticket/uc-f25-34-verify-the-candidate-commit.md)
- [E-F25-22 Verification](../data/e-f25-22-verification.md)
- [BR-F25-05 Agents never merge or deploy](br-f25-05-agents-never-merge-or-deploy.md)
- [BR-F25-08 Fixes start with a failing test](br-f25-08-fixes-test-first.md)

## Exceptions

None.

## Configurable

(Proposed) The list of required checks, per ticket in its work contract; build, tests and the acceptance criteria are
always required.

## Open questions

None.

---

⬅️ [BR-F25-26](br-f25-26-a-conflict-goes-back-to-the-architect-never-guessed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-28](br-f25-28-two-repair-cycles-at-most-then-a-maintainer-decides.md)

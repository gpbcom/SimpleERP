🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-28 Two repair cycles at most, then a maintainer decides

# 📏 BR-F25-28 Two repair cycles at most, then a maintainer decides

**Status:** 🔄 waiting for the owner

## Statement

A rejected candidate is repaired at most twice. If the second repaired candidate is still rejected, no third cycle
starts: the run stops and its blockers go to the maintainer, who decides. A repair never weakens a test, and a finding
in a file no role owns needs a contract change approved by the maintainer.

## Why

Repairs without a limit cost money and hide a problem the team cannot solve alone, as the owner asked on 2026-11-16
[D567](../../../06-decisions/f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md).
Runs stay within their budget ([BR-F25-11](br-f25-11-agents-metered-and-audited.md),
[D398](../../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md)) and the maintainer keeps the
last word ([D434](../../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md)).

## Examples

| Case | Result |
|---|---|
| Rejected once, repaired, then PASS | the draft pull request opens |
| Rejected after the second repair | blockers to the maintainer |
| A Blocked check | to the maintainer at once, no cycle used |
| A test made looser to pass | refused, the finding stays open |
| A finding outside every role's files | a contract change for the maintainer |

## Applies to

- [UC-F25-35](../use-cases/08-team-builds-a-ticket/uc-f25-35-repair-a-rejected-candidate.md)
- [E-F25-22 Verification](../data/e-f25-22-verification.md)
- [BR-F25-22](br-f25-22-a-contract-gives-each-role-its-own-files.md)
- [BR-F25-23](br-f25-23-no-worker-starts-before-the-contract-is-approved.md)

## Exceptions

None.

## Configurable

(Proposed) A maintainer may set fewer cycles for a repository, never more than two.

## Open questions

None.

---

⬅️ [BR-F25-27 An approval belongs to one commit](br-f25-27-an-approval-belongs-to-one-commit.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-29](br-f25-29-a-draft-pull-request-carries-its-evidence-and-screenshots.md)

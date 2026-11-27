🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-07 Approval before Ready

# 📏 BR-F25-07 Approval before Ready

**Status:** ✅ specified

## Statement

Agent-created features and tickets carry needs-maintainer-approval and stay in Backlog until a maintainer removes the
label.

Removing the label, or moving the ticket out of Backlog, by anyone but a maintainer is reported and reverted by a
workflow, with branch protection; Backlog is the only status allowed while the label is on
([D441](../../../06-decisions/f25-devops-agents/d441-approval-label-reported-and-reverted.md); harness ticket GH-23,
pull request #24, pending until merged).

## Why

See [D434](../../../06-decisions/f25-devops-agents/d434-maintainer-approval-label.md).

## Examples

| Case | Result |
|---|---|
| Agent ticket moved to Ready | Reported and moved back to Backlog by the workflow (D441) |

## Applies to

Every F25 use case concerned.

- [UC-F25-21 Triage requests by severity and priority](../use-cases/01-intake/uc-f25-21-triage-requests-by-severity-and-priority.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-06 Specs and code studied first](br-f25-06-specs-and-code-studied-first.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-08 Fixes start with a failing test](br-f25-08-fixes-test-first.md)

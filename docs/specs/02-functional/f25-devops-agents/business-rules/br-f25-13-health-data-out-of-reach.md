🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-13 Health data out of the agents' reach

# 📏 BR-F25-13 Health data out of the agents' reach

**Status:** ✅ specified

## Statement

A company holding health data (SC09) is excluded from the DevOps agents' masked copies and from every model they call,
unless the hosting and the whole model path are HDS-certified; the request then goes to a person.

## Why

Health data must stay with an HDS-certified host (CR-FR-055). See the review of 2026-11-12 (R27) and
[D435](../../../06-decisions/f25-devops-agents/d435-agents-access-and-limits.md).

## Examples

| Case | Result |
|---|---|
| A bug reported by a medical practice | Handled by a person, no agent run on its data |
| The same with an HDS-certified model path | The agents run as usual |

## Applies to

Every F25 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-12 Security reports stay private](br-f25-12-security-reports-stay-private.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-14](br-f25-14-triage-with-severity-priority-and-target-times.md)

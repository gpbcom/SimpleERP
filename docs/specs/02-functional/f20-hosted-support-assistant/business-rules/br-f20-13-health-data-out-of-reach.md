🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-13 Health data out of the models' reach

# 📏 BR-F20-13 Health data out of the models' reach

**Status:** ✅ specified

## Statement

A namespace holding health data (SC09) is excluded from the support assistant's model access unless the hosting and the
whole model path are HDS-certified; an engineer handles the request.

## Why

Health data must stay with an HDS-certified host (CR-FR-055). See the review of 2026-11-12 (R27).

## Examples

| Case | Result |
|---|---|
| A medical practice reports a problem | An engineer handles it, no model reads its namespace |

## Applies to

Every F20 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F20-12 Conversations kept and exportable](br-f20-12-conversations-kept-and-exportable.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-14 Maintenance announced ahead](br-f20-14-maintenance-announced-ahead.md)

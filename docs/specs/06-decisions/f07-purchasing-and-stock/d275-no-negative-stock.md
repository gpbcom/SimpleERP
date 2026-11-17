🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📦 [Decisions: F7 Purchasing and stock](README.md) ›
📜 D275 No negative stock

# 📜 D275 No negative stock

**Status:** ✅ decided

## Context

Whether stock can go negative.

## Options

- Blocked.
- Allowed, flagged.
- Allowed silently.

## Choice

Blocked: a move that would make stock negative is refused with what is missing; a manager can allow it per warehouse for
urgent cases, flagged for a count.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F7-08.

## Related

- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md)

---

⬅️ [D274 F7 use cases and thresholds](d274-f7-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D276 The AI assistant reaches every capability](../f03-assistant/d276-assistant-reaches-every-capability.md)

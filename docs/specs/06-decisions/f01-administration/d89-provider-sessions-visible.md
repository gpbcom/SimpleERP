🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D89 Provider sessions are visible

# 📜 D89 Provider sessions are visible

**Status:** ✅ decided

## Context

Whether the client is told when the provider enters its company (D53).

## Options

- Yes, a visible log and a notification.
- A log only.
- Not told.

## Choice

Yes: the client's administrators see each provider session in a provider access log (who, when, what) and are notified
when one starts.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The client always knows; it cannot refuse (D53).

## Related

- [UC-F1-11](../../02-functional/f01-administration/use-cases/08-provider-and-client-companies/uc-f01-11-enter-a-client-company-to-support-it.md)
- [BR-F1-20](../../02-functional/f01-administration/business-rules/br-f01-20-provider-sessions-are-visible.md)

---

⬅️ [D88 Client company from a template](d88-client-company-from-a-template.md) · ⬆️ [Up](README.md) ·
➡️ [D90 The provider sees everything](d90-provider-sees-everything.md)

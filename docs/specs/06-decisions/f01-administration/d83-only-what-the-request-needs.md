🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D83 Only what the request needs

# 📜 D83 Only what the request needs

**Status:** ✅ decided

## Context

What is sent when a feature uses an external provider.

## Options

- Only what the request needs.
- Masked personal data.
- Anything.

## Choice

Only the question and the passages retrieved for it, within the user's permissions. The administrator sees a warning
when choosing the provider, and every answer shows the provider's name.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No bulk data ever goes to a provider.

## Related

- [UC-F1-08](../../02-functional/f01-administration/use-cases/06-choose-an-ai-provider/uc-f01-08-choose-the-ai-provider-of-a-feature.md)
- [BR-F1-15](../../02-functional/f01-administration/business-rules/br-f01-15-only-what-the-request-needs.md)

---

⬅️ [D82 AI provider per feature](d82-ai-provider-per-feature.md) · ⬆️ [Up](README.md) ·
➡️ [D84 Fall back to the local model](d84-fall-back-to-local.md)

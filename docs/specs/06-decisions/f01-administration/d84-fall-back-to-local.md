🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D84 Fall back to the local model

# 📜 D84 Fall back to the local model

**Status:** ✅ decided

## Context

What happens if the external provider fails or is too slow.

## Options

- Fall back to the local model.
- Show an error.

## Choice

The feature answers with the local model and says so.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Every feature keeps a local model ready.

## Related

- [UC-F1-08](../../02-functional/f01-administration/use-cases/06-choose-an-ai-provider/uc-f01-08-choose-the-ai-provider-of-a-feature.md)
- [BR-F1-16](../../02-functional/f01-administration/business-rules/br-f01-16-fall-back-to-the-local-model.md)

---

⬅️ [D83 Only what the request needs](d83-only-what-the-request-needs.md) · ⬆️ [Up](README.md) ·
➡️ [D85 Single sign-on providers](d85-single-sign-on-providers.md)

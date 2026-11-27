🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D82 AI provider per feature

# 📜 D82 AI provider per feature

**Status:** ✅ decided

## Context

Which AI features get their own provider setting (D5).

## Options

- Assistant (F3).
- Meetings (F4).
- Legal assistant (F15).
- Social media drafts (F5).

## Choice

All four, with meetings split in two: Assistant (F3); Meetings: speech-to-text (F4); Meetings: summaries (F4); Legal
assistant (F15); Social media drafts (F5).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Five settings, each local by default (D5).

Clarified on 2026-11-12 after the review (R13, the owner's yes): a Default setting covers every AI feature without its
own setting (E-F1-09); the hosted-only services use the providers of D440.

## Related

- [UC-F1-08](../../02-functional/f01-administration/use-cases/06-choose-an-ai-provider/uc-f01-08-choose-the-ai-provider-of-a-feature.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)

---

⬅️ [D81 Confirmation per connection](d81-confirmation-per-connection.md) · ⬆️ [Up](README.md) ·
➡️ [D83 Only what the request needs](d83-only-what-the-request-needs.md)

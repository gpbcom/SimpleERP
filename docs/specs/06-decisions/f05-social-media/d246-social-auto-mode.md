🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📣 [Decisions: F5 Social media](README.md) ›
📜 D246 Automatic mode

# 📜 D246 Automatic mode

**Status:** ✅ decided

## Context

The owner: "Add an auto mode. the auto-mode will be push without approval. The post will be triggered by events internal
or external it can be configured per event type it can be templated as well."

## Options

- Automatic mode per event type.
- Approval always.

## Choice

An automatic mode publishes without approval, triggered by internal events (a new product, a finished project, a job
opening, a review received) or external ones (a webhook, a feed item, a mention), configured per event type, from a
template.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F5-02; guard rails: daily limit per account, words never published, a stop switch, and a log of every
automatic post.

Revised by D439 on 2026-11-12: automatic posts are an automation tier: only for event types an administrator switched to
automatic, within limits, every post audited and a sample checked by a person.

## Related

- [F5 Social media](../../02-functional/f05-social-media/README.md)
- [D29](../foundations/d29-social-media-module.md)

---

⬅️ [D245 AI for social media](d245-social-ai.md) · ⬆️ [Up](README.md) · ➡️ [D247 F5 use cases](d247-f5-use-cases.md)

🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🤖 [Assistant](README.md) › 🤖 AI

# 🤖 AI

**Status:** ✅ specified

## What the AI assistant can do

Every action of every capability (F1 to F16) can be triggered here, within the user's roles
([BR-F3-34](business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

Answer from the company's data with sources and exact figures; answer about the screen; create and change records after
confirmation, never delete or do irreversible acts; summarise and draft in the company style; find and guide, with Show
me; use outside tools; read photos; listen and speak. See the [use cases](use-cases/README.md).

## Permissions

Exactly the user's (D12); outside data within each connection's categories (D169); knowledge within each item's audience
(D174). Everyone may use the AI assistant; the tools that would read or change what the user's role may not are disabled
([BR-F3-34](business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
[D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)).

## Models

Eight AI features each choose a provider in F1, local by default (D5, D82, D187): the AI assistant, AI assistant voice
and photo reading here; meetings speech-to-text and summaries (F4); the legal assistant (F15); social media drafts (F5);
workflow AI steps (F2). Only what a request needs leaves for an external provider (D83). Failing calls are retried 3
times with exponential backoff (BR-F3-32).

## Open questions

None.

---

⬅️ [Integrations](integrations.md) · ⬆️ [Up](README.md) · ➡️ [Regulatory](regulatory.md)

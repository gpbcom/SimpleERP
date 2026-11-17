🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D238 Static workflows or agents

# 📜 D238 Static workflows or agents

**Status:** ✅ decided

## Context

The owner: it must work either with static workflows or with a fully agentic system.

## Options

- Both, on one connector contract.
- Static only.
- Agentic only.

## Choice

Both. Every connector exposes typed actions (read or write, input and output schema, idempotency key, dry run); a static
workflow (F2) calls them in fixed steps; an agent calls the same actions as tools, under its procedure, allow-list,
budget and confirmation policy.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

One catalogue, two ways to drive it (REQ-T12-02, REQ-T12-03).

Revised by D439 on 2026-11-12: in automatic, a support agent prepares a refund or any other payment; a person approves
it.

## Related

- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)

---

⬅️ [D237 Customer support agents](d237-customer-support-agents.md) · ⬆️ [Up](README.md) ·
➡️ [D239 Connectors and scrapers generated on the fly](d239-scraper-factory.md)

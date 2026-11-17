🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D301 F3 benchmark additions

# 📜 D301 F3 benchmark additions

**Status:** ✅ decided

## Context

The owner asked that F2 to F14 cover every feature of the benchmark set (PLAN D30); a reading of the benchmark found
these gaps in F3: ai agents, agent governance, ai fields and the AI assistant in chat apps.

## Options

- Add them all.
- Add with changes.

## Choice

Added, as confirmed by the owner on 2026-11-11: UC-F3-10 Create and run AI agents; UC-F3-11 Govern AI agents; UC-F3-12
Add AI fields to records; UC-F3-13 Use the AI assistant in chat apps. Each is reachable from the AI assistant within the
user's roles (BR-F3-34); a legal value it needs comes from the country pack (D293).

## Decided by

The owner, on 2026-11-11, in the specification interview.

## Consequences

New use cases, rules, entities, screens and the flow Benchmark additions.

Revised by D439 on 2026-11-12: an agent acts alone only within a procedure an administrator switched to automatic,
within its limits, audited and sampled; never for payments, legal sendings, deletions or decisions about a person.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)

---

⬅️ [D300 F2 benchmark additions](../f02-no-code-configuration/d300-f2-benchmark-gaps.md) · ⬆️ [Up](README.md) ·
➡️ [D302 F4 benchmark additions](../f04-meetings/d302-f4-benchmark-gaps.md)

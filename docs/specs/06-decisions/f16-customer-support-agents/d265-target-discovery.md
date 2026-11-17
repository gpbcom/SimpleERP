🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D265 Finding where to go

# 📜 D265 Finding where to go

**Status:** ✅ decided

## Context

The owner: customers sometimes give the URL to go to, sometimes not; then the agentic system shall try to discover where
to go.

## Options

- Given URL first, discovery otherwise.
- Always ask the customer.

## Choice

When the customer gives the address (a portal, a login page, a website), it is used as given. Otherwise the system
discovers it: a rule-based finder first, then a discovery agent searching the web, returning ranked candidates with
their evidence.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

REQ-T12-13; credentials only ever go to a confirmed address.

## Related

- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)

---

⬅️ [D264 Human sampling](d264-human-sampling.md) · ⬆️ [Up](README.md) ·
➡️ [D266 Purchasing and stock scope](../f07-purchasing-and-stock/d266-purchasing-and-stock-scope.md)

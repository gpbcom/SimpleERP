🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏪 [Decisions: F10 Point of sale (plugin)](README.md) ›
📜 D298 Delivery platforms through connectors

# 📜 D298 Delivery platforms through connectors

**Status:** ✅ decided

## Context

How orders from food-delivery platforms reach the till.

## Options

- Through T12 connectors.
- Built into F10.
- Out of scope for v1.

## Choice

Each delivery platform is a connector of the T12 catalogue, static or agentic; a new platform needs no F10 change.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

UC-F10-17; BR-F10-13.

## Related

- [F10 Point of sale](../../02-functional/f10-point-of-sale/README.md)

---

⬅️ [D297 Point of sale personas](d297-pos-personas.md) · ⬆️ [Up](README.md) ·
➡️ [D299 F10 use cases](d299-f10-use-cases.md)

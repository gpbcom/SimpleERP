🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-03 A scenario runs on a copy

# 📏 BR-F23-03 A scenario runs on a copy

**Status:** ✅ specified

## Statement

A scenario never changes live data: it runs on a copy or an overlay of the company's data, isolated from other companies
and from other scenarios.

## Why

See [D402](../../../06-decisions/f23-what-if-simulation/d402-impact-through-the-real-rules.md).

## Examples

| Case | Result |
|---|---|
| Price rise in a scenario | Live price list unchanged |

## Applies to

Every F23 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F23-02 The baseline comes from history and plans](br-f23-02-baseline-from-history-and-plans.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F23-04 The same rules as the ERP](br-f23-04-same-rules-as-the-erp.md)

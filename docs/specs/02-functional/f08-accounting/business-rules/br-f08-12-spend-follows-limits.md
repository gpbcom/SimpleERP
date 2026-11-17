🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-12 Spend follows card and approval limits

# 📏 BR-F8-12 Spend follows card and approval limits

**Status:** ✅ specified

## Statement

A card or a payment above its limit, or outside its categories, is refused or sent for approval, for people and agents
alike (BR-F3-35).

## Why

See [D306](../../../06-decisions/f08-accounting/d306-f8-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| 1 200 EUR on a 1 000 EUR card | Refused |

## Applies to

UC-F8-18

## Exceptions

None.

## Configurable

Limits per card and role.

## Open questions

None.

---

⬅️ [BR-F8-11 Revenue follows performance obligations](br-f08-11-revenue-follows-performance-obligations.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-13](br-f08-13-client-money-is-segregated-and-never-negative-per-client.md)

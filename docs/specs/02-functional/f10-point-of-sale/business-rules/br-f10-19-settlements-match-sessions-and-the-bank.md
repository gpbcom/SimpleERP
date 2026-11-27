🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-19 Settlements match sessions and the bank

# 📏 BR-F10-19 Settlements match sessions and the bank

**Status:** ✅ specified

## Statement

A card settlement's gross matches the sessions' card payments and its net the bank line; fees are posted and compared
with the contract.

## Why

Card fees and missing settlements go unnoticed otherwise.

## Examples

| Case | Result |
|---|---|
| Gross 6,420 = sessions | Matched |
| Fees 1.1 % vs 0.9 % | Flagged |

## Applies to

- [UC-F10-24 Match card-terminal settlements net of fees](../use-cases/09-cash-and-settlements/uc-f10-24-match-card-terminal-settlements-net-of-fees.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F10-18 Cash moves are counted by two](br-f10-18-cash-moves-are-counted-by-two.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-20](br-f10-20-recognised-customers-agreed-transferred-items-are-reserved.md)

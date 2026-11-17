🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-18 Cash moves are counted by two

# 📏 BR-F10-18 Cash moves are counted by two

**Status:** ✅ specified

## Statement

Every move of cash between a till, the safe, a deposit and the collector is counted by two people and traced; a
difference needs a reason.

## Why

Cash goes missing between the till and the bank without a trace.

## Examples

| Case | Result |
|---|---|
| To the safe | Two counters |
| 20 EUR short | Reason required |

## Applies to

- [UC-F10-23 Manage the safe, bank deposits and cash collection](../use-cases/09-cash-and-settlements/uc-f10-23-manage-the-safe-bank-deposits-and-cash-collection.md)

## Exceptions

None.

## Configurable

The threshold for telling the owner.

## Open questions

None.

---

⬅️ [BR-F10-17 Restricted items need an age check](br-f10-17-restricted-items-need-an-age-check.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F10-19 Settlements match sessions and the bank](br-f10-19-settlements-match-sessions-and-the-bank.md)

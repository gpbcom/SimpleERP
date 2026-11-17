🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F10-03 Cash within the legal limit

# 📏 BR-F10-03 Cash within the legal limit

**Status:** ✅ specified

## Statement

A cash payment above the country pack's cash limit is refused and another method is asked; in France:
[CR-FR-022 Cash payment limit](../../../10-country-packs/france/payments/cr-fr-022-cash-payment-limit.md).

## Why

See [D296](../../../06-decisions/f10-point-of-sale/d296-till-certified-before-france.md).

## Examples

| Case | Result |
|---|---|
| 950 EUR in cash, French resident | Accepted |
| 1 200 EUR in cash, French resident | Refused: pay 1 000 in cash at most and the rest by card |

## Applies to

Every F10 use case concerned.

- [UC-F10-23 Manage the safe, bank deposits and cash collection](../use-cases/09-cash-and-settlements/uc-f10-23-manage-the-safe-bank-deposits-and-cash-collection.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F10-02 One session per till, counted at closing](br-f10-02-one-session-per-till.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-04 Refunds link the original sale](br-f10-04-refunds-link-the-original.md)

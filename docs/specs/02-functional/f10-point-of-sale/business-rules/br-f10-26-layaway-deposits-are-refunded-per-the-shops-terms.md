🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-26 Layaway deposits are refunded per the shop's terms

# 📏 BR-F10-26 Layaway deposits are refunded per the shop's terms

**Status:** ✅ specified

## Statement

Before a deposit is taken, the screen shows the shop's terms (minimum deposit, holding time, what is refunded on
cancellation or expiry) and the customer accepts them; the deposit is then refunded, kept or partly kept exactly as
those terms say, and every refund links the original deposit.

## Why

A deposit is money held for someone else's purchase. Disputes come from unclear terms and refunds nobody can trace. The
owner's answer: "Layaway and parked sales"
([D529](../../../06-decisions/f10-point-of-sale/d529-benchmark-gaps-f10-point-of-sale.md)).

## Examples

| Case | Result |
|---|---|
| The terms say full refund within 14 days | a cancellation on day 10 refunds the deposit in full |
| The terms keep 20 percent after 14 days | a cancellation on day 20 refunds 80 percent |
| The collection date passes without contact | expired, refunded per the terms |
| The customer pays the balance | no refund, the sale completes |
| The shop cancels because the item is damaged | the deposit is refunded in full |

## Applies to

- [UC-F10-32 Hold an item with a deposit or park a sale](../use-cases/12-takeaway-softpos-and-labels/uc-f10-32-hold-an-item-with-a-deposit-or-park-a-sale.md)
- [E-F10-24 Layaway](../data/e-f10-24-layaway.md)
- [UC-F10-04 Refund or exchange](../use-cases/03-after-sales/uc-f10-04-refund-or-exchange.md)

## Exceptions

A cancellation caused by the shop is always a full refund.

## Configurable

Yes: the minimum deposit, the holding time and the refund conditions are set per shop.

## Open questions

None.

---

⬅️ [BR-F10-25 Label prices always match the till price](br-f10-25-label-prices-always-match-the-till-price.md) ·
⬆️ [Up](README.md)

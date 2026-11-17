🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-08 Balances are shown before each sale

# 📏 BR-SC17-08 Balances are shown before each sale

**Status:** 🔄 waiting for the owner

## Statement

The balances of a customer (sessions, included services, vouchers, points and open invoices) are shown before each sale
so that the user can apply them; a balance is never applied without the user's choice, and an expired balance is never
offered.

## Why

A customer who pays for what they already hold, or who loses a balance they did not know about, complains. The owner
asked for customer balances ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| Package 4 sessions, voucher 18 EUR | both shown before the sale |
| Expired voucher | shown greyed |
| Open invoice | shown first |
| Package ending in 20 days | flagged |
| Guest with no record | no balance |

## Applies to

- [UC-SC17-08](../use-cases/02-packages-and-memberships/uc-sc17-08-follow-customer-balances.md)
- [E-SC17-04 Session package](../data/e-sc17-04-session-package.md)
- [E-SC17-06 Gift voucher](../data/e-sc17-06-gift-voucher.md)

## Exceptions

None.

## Configurable

The days before the end at which a balance is flagged, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-07 Vouchers keep their legal validity period](br-sc17-07-vouchers-keep-their-legal-validity-period.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC17-09 Retail sales go through the certified till](br-sc17-09-retail-sales-go-through-the-certified-till.md)

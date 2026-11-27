🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-17 The removal quote binds once signed

# 📏 BR-SC07-17 The removal quote binds once signed

**Status:** ✅ specified

## Statement

Once the customer has signed the quote of a removal, its price, its volume and its services bind both parties. Any
change needs a new quote that the customer signs, and the earlier signed version is kept. Extra time is billed only at
the rate the quote states.

## Why

A price changed after the signature starts the disputes that removal companies lose, and a customer who cannot see what
they signed distrusts the crew. The owner asked for removals
([D551](../../../06-decisions/sectors/d551-benchmark-gaps-sc07-transport.md)). The France-pack rule on removal quotes is
[CR-FR-276 Removal quotes and delivery reserves](../../../10-country-packs/france/transport/cr-fr-276-removal-quotes.md).

## Examples

| Case | Result |
|---|---|
| Quote signed, move as quoted | the invoice equals the quote |
| Price changed after signing | a new version needs a new signature |
| Move takes 2 h more because there is no parking | 2 h billed at the quoted rate |
| Service added before signing | quote recomputed, signed once |
| Customer cancels the day before | the cancellation fee of the quote applies |

## Applies to

- [UC-SC07-22](../use-cases/07-passengers-removals-courier-and-freight/uc-sc07-22-quote-and-run-house-removals.md)
- [E-SC07-19 Removal](../data/e-sc07-19-removal.md)
- [E-F6-03 Quote](../../../02-functional/f06-customers-and-sales/data/e-f06-03-quote.md)

## Exceptions

None.

## Configurable

The extra-time rate and the cancellation fee, in the price list by the owner.

## Open questions

None.

---

⬅️ [BR-SC07-16](br-sc07-16-drivers-hold-the-licence-for-the-vehicle-class.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-18](br-sc07-18-a-failed-delivery-gets-a-new-slot-or-a-relay-point.md)

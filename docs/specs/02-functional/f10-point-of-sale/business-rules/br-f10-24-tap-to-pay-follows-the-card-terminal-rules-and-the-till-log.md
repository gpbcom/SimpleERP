🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-24 Tap to pay follows the card-terminal rules and the till log

# 📏 BR-F10-24 Tap to pay follows the card-terminal rules and the till log

**Status:** ✅ specified

## Statement

A tap payment on a phone is accepted only on a registered phone through the payment provider's certified software, with
the PIN for amounts over the contactless ceiling, and it is written in the till log with its amount, method, last four
digits and device; card numbers and PINs are never stored or shown by SimpleERP, and a payment that cannot be
authorised online is declined, never accepted for later.

## Why

A phone that takes cards is a card terminal in the eyes of the schemes and of the law. The rules of a terminal apply to
it, and the till log is the proof that each payment was taken and recorded. The owner's answer: "Tap to pay on phone"
([D529](../../../06-decisions/f10-point-of-sale/d529-benchmark-gaps-f10-point-of-sale.md)).

## Examples

| Case | Result |
|---|---|
| A tap of 38.50 euros on a registered phone | accepted and logged |
| A tap of 120 euros | the PIN is asked on the screen |
| The phone has lost the network | no payment, the seller uses another means |
| An unregistered phone | Tap to pay is not offered |
| An auditor reads the till log | sees the last four digits, never the number |

## Applies to

- [UC-F10-30 Take payment by tap on phone](../use-cases/12-takeaway-softpos-and-labels/uc-f10-30-take-payment-by-tap-on-phone.md)
- [UC-F10-03 Take payment](../use-cases/02-sell-at-the-counter/uc-f10-03-take-payment.md)
- [UC-F10-14 Sell on the move and offline](../use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md)

## Exceptions

None: the rules of a card terminal have no exception.

## Configurable

Yes: the contactless ceiling follows the provider and the scheme and is read from them, not typed here.

## Open questions

None.

---

⬅️ [BR-F10-23 Online orders stay within kitchen capacity](br-f10-23-online-orders-stay-within-kitchen-capacity.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F10-25 Label prices always match the till price](br-f10-25-label-prices-always-match-the-till-price.md)

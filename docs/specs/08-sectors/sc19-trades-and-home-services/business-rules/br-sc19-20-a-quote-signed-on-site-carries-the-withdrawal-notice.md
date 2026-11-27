🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-20 A quote signed on site carries the withdrawal notice

# 📏 BR-SC19-20 A quote signed on site carries the withdrawal notice

**Status:** ✅ specified

## Statement

A quote signed at the customer's home carries the withdrawal notice and form and states the 14-day withdrawal delay.
No payment and no consideration of any kind is taken for 7 days from the signature, except for an urgent repair the
customer expressly asked for, limited to the parts and work strictly needed for the emergency. The customer always
receives a signed copy.

## Why

A quote signed at home without the notice can be cancelled and the company can be fined
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The withdrawal delay of 14
days is read in
[CR-FR-036 Consumer withdrawal right](../../../10-country-packs/france/consumer/cr-fr-036-withdrawal-right.md).
For a contract signed at the customer's home the law forbids any payment or consideration for 7 days from the
signature (Code de la consommation L221-10), and an urgent repair the customer expressly asked for, limited to the parts
and work strictly needed, has no withdrawal right (L221-28); the 14-day withdrawal right stays for everything else. The
owner chose to follow the law rather than a longer ban ([D575](../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md)).

## Examples

| Case | Result |
|---|---|
| Quote signed at home | notice and form attached, delay stated |
| Deposit asked on the day | refused |
| Payment asked on day 5 after the signature | refused |
| Payment asked on day 8, the customer has not withdrawn | taken; the withdrawal right still runs to day 14 |
| Urgent repair the customer expressly asked for | that part starts at once and may be paid, with no withdrawal right for it |
| Customer without email | paper copy handed over |
| Customer withdraws in the delay | the quote is cancelled and nothing is due |

## Applies to

- [UC-SC19-20](../use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-20-quote-on-site-and-sign-on-the-phone.md)
- [E-F6-03 Quote](../../../02-functional/f06-customers-and-sales/data/e-f06-03-quote.md)
- [E-F2-14](../../../02-functional/f02-no-code-configuration/data/e-f02-14-signature-request.md)

## Exceptions

None.

## Configurable

The notice text, the 14-day withdrawal delay and the 7-day payment ban, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-19 Each van is counted at every reload](br-sc19-19-each-van-is-counted-at-every-reload.md) ·
⬆️ [Up](README.md)

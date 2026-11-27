🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-13 Immediate advance on request

# 📏 BR-SC04-13 Immediate advance on request

**Status:** ✅ specified

## Statement

A client who chose the immediate advance pays only their share: URSSAF pays the whole service to the provider and
debits the client for the remainder once the request is validated, by the client within 48 hours or automatically
after them; in France:
[CR-FR-104 Immediate advance of the tax credit](../../../10-country-packs/france/tax-and-vat/cr-fr-104-immediate-advance-of-tax-credit.md).

## Why

The joining steps and deadlines are those of [CR-FR-104 Immediate advance of the tax credit](../../../10-country-packs/france/tax-and-vat/cr-fr-104-immediate-advance-of-tax-credit.md):
the provider is authorised on a URSSAF API and registers the client, the client activates the account from a link valid
7 days, each request is validated within 48 hours or automatically, and URSSAF debits the remainder 2 days later.

## Examples

| Case | Result |
|---|---|
| 200 EUR invoice, validated by the client | URSSAF pays the provider 200, debits the client 100 |
| 200 EUR invoice, no answer within 48 hours | Validated automatically, same payment and debit |

## Applies to

Every SC04 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC04-12 Yearly certificate before 31 March](br-sc04-12-yearly-certificate-before-march.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC04-14 Complaints answered](br-sc04-14-complaints-answered.md)

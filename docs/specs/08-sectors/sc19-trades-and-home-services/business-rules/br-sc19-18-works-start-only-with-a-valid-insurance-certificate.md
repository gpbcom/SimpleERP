🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-18 Works start only with a valid insurance certificate

# 📏 BR-SC19-18 Works start only with a valid insurance certificate

**Status:** ✅ specified

## Statement

Works start only while the company holds a valid insurance certificate that covers the activity, and the insurer and the
cover are shown on the quote and the invoice. At the handover the customer receives the warranty terms with their end
dates.

## Why

Works without cover leave the customer unprotected and the company in breach
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The France-pack rule is
[CR-FR-259 Builders' ten-year insurance certificate](../../../10-country-packs/france/construction/cr-fr-259-builders-warranty-insurance.md):
the ten-year insurance is in place before work starts, and its certificate is given to the client and attached to quotes
and invoices.

## Examples

| Case | Result |
|---|---|
| Valid certificate, covered activity | the quote may be sent |
| Activity not covered | quote refused |
| Certificate expired | quotes for works refused |
| Handover without a date | end dates not computed |
| Certificate expiring in 60 days | owner warned |

## Applies to

- [UC-SC19-18](../use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-18-keep-builders-warranties-and-certificates.md)
- [E-SC19-12 Warranty certificate](../data/e-sc19-12-warranty-certificate.md)
- [E-SC19-12 Warranty certificate](../data/e-sc19-12-warranty-certificate.md)
- [E-F6-03 Quote](../../../02-functional/f06-customers-and-sales/data/e-f06-03-quote.md)
- France-pack rule:
  [CR-FR-259 Builders' ten-year insurance certificate](../../../10-country-packs/france/construction/cr-fr-259-builders-warranty-insurance.md)

## Exceptions

None.

## Configurable

The days of warning before expiry and the warranty durations, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-17](br-sc19-17-call-out-surcharges-are-shown-before-dispatch.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-19 Each van is counted at every reload](br-sc19-19-each-van-is-counted-at-every-reload.md)

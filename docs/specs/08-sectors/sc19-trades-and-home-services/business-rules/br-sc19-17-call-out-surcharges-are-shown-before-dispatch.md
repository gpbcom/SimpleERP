🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-17 Call-out surcharges are shown before dispatch

# 📏 BR-SC19-17 Call-out surcharges are shown before dispatch

**Status:** 🔄 waiting for the owner

## Statement

The call-out price and the surcharge of the hour, night, weekend or holiday are shown to the customer and accepted
before an on-call technician is dispatched. A rota week without a backup or that breaks the legal rest of a technician
is refused.

## Why

A surcharge announced only on the invoice is a dispute and a breach of the price information the law requires
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Call at 11 pm | night surcharge shown and accepted before dispatch |
| Customer refuses the surcharge | no dispatch, call closed with its reason |
| Week without a backup | flagged |
| Rest time broken | week refused for that person |
| Holiday | holiday surcharge shown |

## Applies to

- [UC-SC19-17](../use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-17-run-the-emergency-on-call-service.md)
- [E-SC19-11 On-call rota](../data/e-sc19-11-on-call-rota.md)
- [E-SC19-11 On-call rota](../data/e-sc19-11-on-call-rota.md)
- [E-SC19-04 Intervention](../data/e-sc19-04-intervention.md)

## Exceptions

None.

## Configurable

The surcharge table by hour band and the call-out terms, set by the owner.

## Open questions

None.

---

⬅️ [BR-SC19-16](br-sc19-16-refrigerant-handling-needs-a-certified-technician.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-18](br-sc19-18-works-start-only-with-a-valid-insurance-certificate.md)

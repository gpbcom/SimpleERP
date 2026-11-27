🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-08 The invoice follows the signed report

# 📏 BR-SC19-08 The invoice follows the signed report

**Status:** ✅ specified

## Statement

The invoice of an intervention is issued from the report only after the customer has signed it. An intervention under a
maintenance contract is not invoiced and its report is attached to the contract. A refusal to sign is recorded with its
reason and the office is told.

## Why

An invoice before acceptance starts disputes, and a signature on the spot lets the customer pay at once
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The France-pack rule is
[CR-FR-020 Proof of acceptance and e-signature](../../../10-country-packs/france/invoicing/cr-fr-020-electronic-acceptance-and-signature.md):
the signed report keeps who signed, when and which version.

## Examples

| Case | Result |
|---|---|
| Signed report | invoice issued and sent |
| Refused signature | no invoice, the office is told |
| Customer absent | remote signature by SMS, then invoice |
| Intervention under a contract | no invoice, report attached |
| Amount changed after the signature | refused |

## Applies to

- [UC-SC19-08](../use-cases/02-on-site-intervention/uc-sc19-08-sign-and-invoice-on-the-spot.md)
- [E-SC19-05 Site report](../data/e-sc19-05-site-report.md)
- [E-F6-05 Invoice](../../../02-functional/f06-customers-and-sales/data/e-f06-05-invoice.md)

## Exceptions

None.

## Configurable

The payment methods offered on the phone, set by accounting.

## Open questions

None.

---

⬅️ [BR-SC19-07 Parts used lower the van's stock](br-sc19-07-parts-used-lower-the-vans-stock.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-09 Only eligible services carry the tax credit](br-sc19-09-only-eligible-services-carry-the-tax-credit.md)

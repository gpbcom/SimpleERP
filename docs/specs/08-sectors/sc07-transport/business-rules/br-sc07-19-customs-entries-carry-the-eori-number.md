🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-19 Customs entries carry the EORI number

# 📏 BR-SC07-19 Customs entries carry the EORI number

**Status:** ✅ specified

## Statement

A customs entry is lodged only when it carries the EORI number of the declarant and of every party outside the EU that
the declaration names. A file with a missing number stays in Documents and the missing number is asked for.

## Why

A declaration without the right operator number is rejected or delays the goods at the border at the customer's cost.
The owner asked for freight forwarding ([D551](../../../06-decisions/sectors/d551-benchmark-gaps-sc07-transport.md)).
The France-pack rule is
[CR-FR-172 EORI number and import declarations](../../../10-country-packs/france/trade/cr-fr-172-eori-and-imports.md).

## Examples

| Case | Result |
|---|---|
| Declarant and consignee with their EORI numbers | declaration accepted for lodging |
| Consignee outside the EU with no number | refused |
| Sale to another EU country | no customs entry |
| Declarant's number expired | refused until renewed |
| Number with the wrong format | refused with the format shown |

## Applies to

- [UC-SC07-24](../use-cases/07-passengers-removals-courier-and-freight/uc-sc07-24-forward-freight-and-clear-customs.md)
- [E-SC07-21 Shipment file](../data/e-sc07-21-shipment-file.md)
- [E-F6-24](../../../02-functional/f06-customers-and-sales/data/e-f06-24-company-identifier.md)

## Exceptions

Sales between EU countries need no customs entry and so no EORI number on this file.

## Configurable

The formats of the numbers per country, in the country pack.

## Open questions

None.

---

⬅️ [BR-SC07-18](br-sc07-18-a-failed-delivery-gets-a-new-slot-or-a-relay-point.md) · ⬆️ [Up](README.md)

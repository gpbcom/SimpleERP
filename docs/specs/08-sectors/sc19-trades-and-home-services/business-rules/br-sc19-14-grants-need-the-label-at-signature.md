🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-14 Grants need the label at signature

# 📏 BR-SC19-14 Grants need the label at signature

**Status:** ✅ specified

## Statement

A grant request is filed only when the installer's label covers the work at the quote's signature date and every
document of the file is attached. A grant the label does not cover is dropped from the file before the customer signs.

## Why

A request with a label that does not cover the work is refused and the customer loses the grant
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The France-pack rule is
[CR-FR-226 Renovation grants and the RGE label](../../../10-country-packs/france/construction/cr-fr-226-renovation-grants-and-rge.md):
MaPrimeRénov' works are done by an RGE professional, who visits the site first and puts the visit date on the quote and
the invoice.

## Examples

| Case | Result |
|---|---|
| Label covers heat pumps | the file may be filed |
| Label expired at signature | refused, grant dropped |
| Document missing | listed, file stays Draft |
| Body asks for a document | file returns to Draft |
| Request refused | reason recorded, customer told |

## Applies to

- [UC-SC19-14](../use-cases/04-installations-and-labels/uc-sc19-14-file-grants-and-certificates.md)
- [E-SC19-08 Grant file](../data/e-sc19-08-grant-file.md)
- [E-SC19-08 Grant file](../data/e-sc19-08-grant-file.md)
- [E-SC19-09 Label](../data/e-sc19-09-label.md)

## Exceptions

None.

## Configurable

The grants and their conditions, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-13 Works start after the grant file is filed](br-sc19-13-works-start-after-the-grant-file-is-filed.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-15 Label audits are planned before expiry](br-sc19-15-label-audits-are-planned-before-expiry.md)

🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏗️ [SC01 Construction](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC01-19 Grants need the RGE label at signature

# 📏 BR-SC01-19 Grants need the RGE label at signature

**Status:** 🔄 waiting for the owner

## Statement

A quote is signed as a grant job only when the company, or the subcontractor doing the work, holds a valid RGE label for
each domain of work at the signature date. A domain not covered is shown, and the quote can be signed without the grant
for that work only if the customer is told.

## Why

A grant refused for a missing label falls on the customer, who then disputes the quote. The owner asked for
energy-renovation grants ([D545](../../../06-decisions/sectors/d545-benchmark-gaps-sc01-construction.md)).
The France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Label for insulation to 2027-03-31, insulation quote signed 2026-11-20 | covered |
| Heat pump on the quote, no heating label | not covered, shown before signature |
| Label ended 2026-10-31, signature 2026-11-20 | not covered |
| Work by a subcontractor with the label | covered through the subcontractor's label |

## Applies to

- [UC-SC01-19](../use-cases/06-revision-developers-bim-and-grants/uc-sc01-19-prepare-renovation-grant-files.md)
- [E-SC01-18 Grant file](../data/e-sc01-18-grant-file.md)
- [E-F6-03 Quote](../../../02-functional/f06-customers-and-sales/data/e-f06-03-quote.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-226 Renovation grants and the RGE label](../../../10-country-packs/france/construction/cr-fr-226-renovation-grants-and-rge.md)

## Exceptions

None.

## Configurable

The reminder before a label ends (60 days by default), by the owner.

## Open questions

None.

---

⬅️ [BR-SC01-18 Quantities keep a link to the model version](br-sc01-18-quantities-keep-a-link-to-the-model-version.md) ·
⬆️ [Up](README.md)

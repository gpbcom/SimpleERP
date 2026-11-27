🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-11 Billing splits between funders

# 📏 BR-SC04-11 Billing splits between funders

**Status:** 🔄 waiting for the owner

## Statement

Each visit's price is split between the funders and the recipient by the shared multi-payer invoicing:
[BR-F6-13 Each payer pays its share up to its cap](../../../02-functional/f06-customers-and-sales/business-rules/br-f06-13-each-payer-pays-its-share-up-to-its-cap.md)
gives each payer its share up to its cap from the funder agreements
([E-F6-14](../../../02-functional/f06-customers-and-sales/data/e-f06-14-funder-agreement.md)). Home care adds only this:
the shares and hours come from the signed care plan, and the département is billed in its own format; in France:
[CR-FR-105 Billing the département for allowances](../../../10-country-packs/france/home-care/cr-fr-105-departmental-allowances-billing.md).

## Why

(Proposed) The allowances' billing rules are still to read.

## Examples

| Case | Result |
|---|---|
| 30 h, 20 h funded | Funder billed 20 h, recipient 10 h |

## Applies to

Every SC04 use case concerned.

## Exceptions

None.

## Configurable

Shares per plan.

## Open questions

None.

---

⬅️ [BR-SC04-10 Family sees what is shared](br-sc04-10-family-sees-what-is-shared.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC04-12 Yearly certificate before 31 March](br-sc04-12-yearly-certificate-before-march.md)

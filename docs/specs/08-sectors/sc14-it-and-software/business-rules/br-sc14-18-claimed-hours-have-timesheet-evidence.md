🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💻 [SC14 IT and software](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC14-18 Claimed hours have timesheet evidence

# 📏 BR-SC14-18 Claimed hours have timesheet evidence

**Status:** 🔄 waiting for the owner

## Statement

The hours claimed for a project in a research tax credit never exceed the approved timesheet hours of the people on that
project in the period. Hours without an approved line are left out of the claim, and the claim is exported only with the
project's description.

## Why

A claim that the tax office can challenge needs the hours and the work behind it. The owner asked for the research tax
credit ([D558](../../../06-decisions/sectors/d558-benchmark-gaps-sc14-it-and-software.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| 1,200 hours claimed, 1,150 approved | the claim is 1,150 hours |
| Week without an approved timesheet | its hours are not counted |
| Person without a recorded qualification | their hours are held |
| Project with a grant | the grant is deducted from the expenses |
| Project without a description | no evidence file |

## Applies to

- [UC-SC14-24](../use-cases/07-hardware-licences-and-tax-credits/uc-sc14-24-claim-research-tax-credits.md)
- [E-SC14-19 R&D project](../data/e-sc14-19-r-d-project.md)
- [E-F9-17](../../../02-functional/f09-hr-and-projects/data/e-f09-17-timesheet-line.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-246 Research and innovation tax credits](../../../10-country-packs/france/tax-and-vat/cr-fr-246-research-tax-credit.md)

## Exceptions

None.

## Configurable

The list of eligible expense types and the staff cost per hour, by accounting within the limits of the country pack.

## Open questions

None.

---

⬅️ [BR-SC14-17](br-sc14-17-seats-billed-match-the-distributors-statement.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC14-19](br-sc14-19-sponsor-tiers-are-invoiced-like-subscriptions.md)

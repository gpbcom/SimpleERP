🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🤲 [SC08 Non-profit association](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC08-17 Aid per position follows the approval

# 📏 BR-SC08-17 Aid per position follows the approval

**Status:** ✅ specified

## Statement

The aid claimed for a month follows the structure's agreement with the State: it covers only people with a valid eligibility on that month, at most the
structure's agreed positions, and in proportion to the contract hours below 35 and to the post's occupation. A person with no valid eligibility brings no aid.

## Why

Aid claimed beyond the agreement is recovered with penalties and puts the structure's agreement at risk. The owner asked
for work-integration enterprises ([D552](../../../06-decisions/sectors/d552-benchmark-gaps-sc08-non-profit.md)).
The France-pack rule is
[CR-FR-237 Work-integration enterprises (IAE)](../../../10-country-packs/france/non-profit/cr-fr-237-work-integration-iae.md).

## Examples

| Case | Result |
|---|---|
| Person eligible, full month | 1.00 position |
| Person eligible, 104 of 151.67 hours | 0.69 position |
| Eligibility ended last week | no aid after the end date |
| 22 people for 20 agreed positions | capped at 20 |
| Early exit on the 12th | aid stops at the exit date |

## Applies to

- [UC-SC08-22](../use-cases/07-foundations-integration-and-federations/uc-sc08-22-run-a-work-integration-enterprise.md)
- [E-SC08-17 Integration pathway](../data/e-sc08-17-integration-pathway.md)
- [E-F9-02 Contract](../../../02-functional/f09-hr-and-projects/data/e-f09-02-contract.md)
- France-pack rule:
  [CR-FR-237 Work-integration enterprises (IAE)](../../../10-country-packs/france/non-profit/cr-fr-237-work-integration-iae.md)

## Exceptions

None.

## Configurable

The aid per position by structure type and the hours of a full position, in the country pack.

## Open questions

None.

---

⬅️ [BR-SC08-16 Members with a conflict do not vote](br-sc08-16-members-with-a-conflict-do-not-vote.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC08-18 Dues follow each club's headcount](br-sc08-18-dues-follow-each-clubs-headcount.md)

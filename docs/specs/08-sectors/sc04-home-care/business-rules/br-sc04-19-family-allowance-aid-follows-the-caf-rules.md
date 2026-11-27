🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-19 Family allowance aid follows the CAF rules

# 📏 BR-SC04-19 Family allowance aid follows the CAF rules

**Status:** 🔄 waiting for the owner

## Statement

The aid for childcare at home is computed only from the table of the family allowance fund in the country pack, the
child's age, the family's recorded resources and the hours; the parents' share is the cost less that aid, and with no
resources recorded no aid is applied.

## Why

An aid computed by hand drifts from the fund's rules and parents may be asked to repay it. The owner asked for childcare
at home ([D548](../../../06-decisions/sectors/d548-benchmark-gaps-sc04-home-care.md)). (Proposed) The France-pack rule
is written later.

## Examples

| Case | Result |
|---|---|
| Cost 1,200.00 EUR, aid 480.00 EUR | parents' share 720.00 EUR |
| No resources recorded | no aid, share flagged |
| Child reaches a new age band | aid recomputed from the birthday |
| Aid table updated by the pack | applied from its date, the old months unchanged |

## Applies to

- [UC-SC04-19](../use-cases/06-care-homes-cesu-and-nursing/uc-sc04-19-provide-childcare-at-home.md)
- [E-SC04-17 Childcare contract](../data/e-sc04-17-childcare-contract.md)
- [E-SC04-02 Care funding](../data/e-sc04-02-care-funding.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-232 Childcare at home and the PAJE aid](../../../10-country-packs/france/home-care/cr-fr-232-childcare-paje.md)

## Exceptions

None.

## Configurable

The aid table, as data of the country pack, by an administrator of the pack.

## Open questions

None.

---

⬅️ [BR-SC04-18 In agent mode the family is the employer](br-sc04-18-in-agent-mode-the-family-is-the-employer.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC04-20 Care acts need a prescription](br-sc04-20-care-acts-need-a-prescription.md)

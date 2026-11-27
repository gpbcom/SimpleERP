🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-26 Days worked never exceed the package

# 📏 BR-F13-26 Days worked never exceed the package

**Status:** ✅ specified

## Statement

The days worked in a reference year, counted from the confirmed monthly declarations, never exceed the package of the
contract; a declaration that would pass it is refused until a person with the right to change the package changes it.

## Why

A package is a promise of a number of days: working beyond it silently breaks the contract and the rest rules. The owner
asked for days-based contracts ([D532](../../../06-decisions/f13-payroll/d532-benchmark-gaps-f13-payroll.md)).
The France-pack rule on the follow-up of days-based workers is
[CR-FR-219 Days-based contracts (forfait jours)](../../../10-country-packs/france/labour/cr-fr-219-days-based-contracts.md): at most
218 days a year, 235 when rest days are waived, and a regular check of the workload.

## Examples

| Case | Result |
|---|---|
| 218 days package, 187 worked, 20 declared | accepted, 31 left after |
| 218 days package, 214 worked, 6 declared | refused, 4 days left |
| A month of leave counted as days worked | never: leave days are counted apart |
| A part-year contract of 120 days | the package is prorated to the contract's dates |
| A package raised by an amendment | accepted once the new contract is signed |

## Applies to

- [UC-F13-36](../use-cases/10-special-contracts-and-outsourcing/uc-f13-36-follow-days-based-contracts.md)
- [E-F13-29 Days package](../data/e-f13-29-days-package.md)
- [E-F9-02 Contract](../../f09-hr-and-projects/data/e-f09-02-contract.md)
- France-pack rule:
  [CR-FR-219 Days-based contracts (forfait jours)](../../../10-country-packs/france/labour/cr-fr-219-days-based-contracts.md)

## Exceptions

A higher package after a signed amendment, dated from the amendment.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F13-25](br-f13-25-a-posting-needs-an-a1-certificate-or-a-sipsi-declaration.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-27 Inputs are frozen once handed over](br-f13-27-inputs-are-frozen-once-handed-over.md)

🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-17 Special contracts paid by their own rules

# 📏 BR-F13-17 Special contracts paid by their own rules

**Status:** 🔄 waiting for the owner

## Statement

Apprentices, interns, company officers, intermittent performers and farm workers are paid by the rules of their contract
kind in the country pack: their pay grid, their contribution set and the body they are declared to.

## Why

Their pay, contributions and declarations differ from an ordinary contract (D470); in France the values are (Proposed)
to read: the apprentice grid by age and year, the intern allowance above the stay length the law sets, officers outside
unemployment insurance, the performers' scheme and the MSA (with CR-FR-167 for seasonal farm workers).

## Examples

| Case | Result |
|---|---|
| Apprentice of 19 in the second year, grid read from the pack | passes |
| Intern of 3 months, allowance per hour read from the pack | passes |
| Officer paid with unemployment-insurance lines | fails: refused, the line is removed |
| Contract kind with no rule set in the pack | fails: the employee is held out of the run |

## Applies to

- [UC-F13-22 Pay an apprentice or an intern](../use-cases/07-schemes-and-special-contracts/uc-f13-22-pay-an-apprentice-or-an-intern.md)
- [UC-F13-23 Pay a company officer](../use-cases/07-schemes-and-special-contracts/uc-f13-23-pay-a-company-officer.md)
- [UC-F13-24 Pay intermittent performers](../use-cases/07-schemes-and-special-contracts/uc-f13-24-pay-intermittent-performers.md)
- [UC-F13-25 Pay farm workers under the MSA](../use-cases/07-schemes-and-special-contracts/uc-f13-25-pay-farm-workers-under-the-msa.md)

## Exceptions

None.

## Configurable

No: the values come from the country pack (BR-F13-01).

## Open questions

None.

---

⬅️ [BR-F13-16](br-f13-16-every-employee-covered-by-the-mandatory-schemes.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-18 Special regimes declared to their own bodies](br-f13-18-special-regimes-declared-to-their-own-bodies.md)

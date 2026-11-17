🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-21 Profit-sharing once the threshold is reached

# 📏 BR-F13-21 Profit-sharing once the threshold is reached

**Status:** 🔄 waiting for the owner

## Statement

A company that reaches the headcount threshold of the country pack sets up profit-sharing; the reserve is computed each
year by the legal formula, shared by the agreed keys within the per-employee ceiling, then paid or invested in the
employee savings plan by each employee's choice.

## Why

Participation is mandatory from 50 employees in France (D470); the headcount count follows CR-FR-046, the formula and
ceilings are (Proposed) to read (Code du travail L3322-2, L3324-1).

## Examples

| Case | Result |
|---|---|
| Company of 52 employees over 5 consecutive years (Proposed) | passes: profit-sharing set up |
| Reserve 40 000.00 EUR, half by salary, half by time worked | passes |
| Employee's share above the individual ceiling | passes: capped, the surplus shared again |
| No choice made by the employee within the delay | passes: invested by default (Proposed) to read |

## Applies to

- [UC-F13-28 Compute profit-sharing and employee savings](../use-cases/08-deductions-savings-and-leave-pay/uc-f13-28-compute-profit-sharing-and-employee-savings.md)

## Exceptions

Companies below the threshold may set it up voluntarily.

## Configurable

The keys and the plan are set by the company's agreement within the law.

## Open questions

None.

---

⬅️ [BR-F13-20 Advances recovered from the next pay](br-f13-20-advances-recovered-from-the-next-pay.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-22 Leave pay is the higher of two methods](br-f13-22-leave-pay-is-the-higher-of-two-methods.md)

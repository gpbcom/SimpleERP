🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-23 Payroll cost split by the analytic axes

# 📏 BR-F13-23 Payroll cost split by the analytic axes

**Status:** ✅ specified

## Statement

Every payroll cost (gross plus employer contributions) is split by site, project and the analytic axes of F8 in the
proportions of the time recorded in F9; time not recorded goes to the employee's default site; amounts are shown only to
the roles allowed (BR-F13-12).

## Why

The owner and accounting need the cost per site and project (D470), and pay amounts stay restricted.

## Examples

| Case | Result |
|---|---|
| Carer with 120 h on agency A, 31 h on agency B | passes: cost split 79.5 % and 20.5 % |
| Consultant with no time recorded in March | passes: all on the default site, flagged |
| Manager opening the analysis | fails: amounts hidden, headcount shown |

## Applies to

- [UC-F13-34 Analyse payroll cost by site, project and analytic axis](../use-cases/05-reports-and-rules/uc-f13-34-analyse-payroll-cost-by-site-project-and-analytic-axis.md)
- [UC-F13-13 Post payroll entries to accounting](../use-cases/03-declarations-and-payments/uc-f13-13-post-payroll-entries-to-accounting.md)

## Exceptions

None.

## Configurable

The company chooses the axes it uses from F8.

## Open questions

None.

---

⬅️ [BR-F13-22 Leave pay is the higher of two methods](br-f13-22-leave-pay-is-the-higher-of-two-methods.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-24 Agreement family rules dated and complete](br-f13-24-agreement-family-rules-dated-and-complete.md)

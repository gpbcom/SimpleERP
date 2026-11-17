🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-03 Inputs closed before the run

# 📏 BR-F13-03 Inputs closed before the run

**Status:** ✅ specified

## Statement

Time, leave, absences and expenses from F9 are closed for the period before the run; late inputs go to the next run.

## Why

See [D365](../../../06-decisions/f13-payroll/d365-payroll-coverage.md).

## Examples

| Case | Result |
|---|---|
| Overtime entered after closing | Next month |

## Applies to

Every F13 use case concerned.

- [UC-F13-31 Apply the home-help agreement](../use-cases/09-collective-agreements-by-family/uc-f13-31-apply-the-home-help-agreement.md)
- [UC-F13-03 Collect pay inputs from F9](../use-cases/02-monthly-pay-run/uc-f13-03-collect-pay-inputs-from-f9.md)

## Exceptions

None.

## Configurable

Closing day.

## Open questions

None.

---

⬅️ [BR-F13-02 Rates dated by period](br-f13-02-rates-dated-by-period.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-04 Never below the minimum wage](br-f13-04-never-below-the-minimum-wage.md)

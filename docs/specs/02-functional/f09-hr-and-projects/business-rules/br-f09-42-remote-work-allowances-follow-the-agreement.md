🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-42 Remote-work allowances follow the agreement

# 📏 BR-F9-42 Remote-work allowances follow the agreement

**Status:** ✅ specified

## Statement

A remote-work day earns an allowance only when it is a validated day within the days per week and the monthly ceiling of
the company's remote-work agreement; a day over the quota is refused or validated as an exception that earns nothing,
and the allowance is passed to payroll once per validated day.

## Why

Remote-work allowances are paid money and are checked by auditors: the quota and the ceiling come from the agreement the
company signed, not from each manager's habit. The owner's answer: "Remote-work days"
([D528](../../../06-decisions/f09-hr-and-projects/d528-benchmark-gaps-f09-hr-and-projects.md)).

## Examples

| Case | Result |
|---|---|
| The agreement allows 2 days a week at 10 euros, Claire declares 2 | both validated, 20 euros that week |
| Claire declares a third home day | refused, or validated as an exception without allowance |
| A day is declared during time off | refused, the absence wins |
| The manager validates after the month is closed | the day counts in the next month |
| A day is withdrawn after being passed to payroll | a correction goes to payroll, audited |

## Applies to

- [UC-F9-43 Declare remote-work days](../use-cases/15-work-location-headcount-and-learning/uc-f09-43-declare-remote-work-days.md)
- [E-F9-48 Work location day](../data/e-f09-48-work-location-day.md)
- [UC-F9-04 Use employee self-service](../use-cases/01-people/uc-f09-04-use-employee-self-service.md)

## Exceptions

A company without an agreement may still record days for the calendar; none earns an allowance.

## Configurable

Yes: the days per week, the allowance per day and the monthly ceiling are set in the agreement record by HR.

## Open questions

None.

---

⬅️ [BR-F9-41 The LinkedIn account's limits are respected](br-f09-41-linkedin-account-limits-respected.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-43 A requisition needs a budgeted position](br-f09-43-a-requisition-needs-a-budgeted-position.md)

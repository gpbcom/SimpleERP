🏠 [Specs](../../../../README.md) › 🎨 [UX](../../../README.md) › 🪟 [Views](../../README.md) ›
🧑‍💼 [Manager: app shell and home](../README.md) › 🧭 [Journeys](README.md) ›
🧭 J-U02-01 Approve requests and follow the team

# 🧭 J-U02-01 Approve requests and follow the team

**Status:** ✅ specified

## Persona

[U02 Manager](../../../../01-users/personas/u02-manager.md)

## Goal

Approve requests quickly, from anywhere, and see how the team and site are doing.

## Journey

Satisfaction at each step, from 1 (painful) to 5 (effortless): these scores are drawn from the
specs and confirmed by the owner (D572).

```mermaid
journey
  title Approve requests and follow the team
  section FL-F9-03 Time
    Approves a time-off request: 5: U02
  section FL-F8-02 Purchase to pay
    Approves an expense: 4: U02
  section FL-F9-06 Plan and deliver work
    Plans the team's shifts: 3: U02
  section FL-F15-02 Receive a legal warning
    Reads the legal warning on the schedule and fixes it: 3: U02
  section FL-F8-04 Tax, assets and analytics
    Follows the team's budget: 4: U02
```

## Flowchart

The same steps; each problem is the first error flow of the step's use case (once per use case), shown with the error
message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)).

```mermaid
flowchart TD
  S1["1. Approves a time-off request"]
  S1 -- problem --> E1["Not enough balance: an extra allocation can be requested."]
  E1 -. fixed .-> S1
  S2["2. Approves an expense"]
  S2 -- problem --> E2["No receipt: refused unless the category allows it."]
  E2 -. fixed .-> S2
  S1 -- done --> S2
  S3["3. Plans the team's shifts"]
  S3 -- problem --> E3["A conflict: refused with the reason."]
  E3 -. fixed .-> S3
  S2 -- done --> S3
  S4["4. Reads the legal warning on the schedule and fixes it"]
  S4 -- problem --> E4["The corpus is unavailable: no warning, the save goes through, the administrators are told."]
  E4 -. fixed .-> S4
  S3 -- done --> S4
  S5["5. Follows the team's budget"]
  S5 -- problem --> E5["A mandatory plan missing on a line: refused."]
  E5 -. fixed .-> S5
  S4 -- done --> S5
```

## Steps

| Step | Screen | Use case | What the persona does | What the system does |
|---|---|---|---|---|
| 1 | [S-F9-09 Time off](../../../../02-functional/f09-hr-and-projects/screens/03-time/s-f09-09-time-off.md) | [UC-F9-09 Request and approve time off](../../../../02-functional/f09-hr-and-projects/use-cases/03-time/uc-f09-09-request-and-approve-time-off.md) | Approves a time-off request | Records the approval in one or several steps (BR-F9-05); planning and payroll see it. |
| 2 | [S-F8-12 Expenses](../../../../02-functional/f08-accounting/screens/02-purchase-to-pay/s-f08-12-expenses.md) | [UC-F8-12 Submit and approve expenses](../../../../02-functional/f08-accounting/use-cases/02-purchase-to-pay/uc-f08-12-submit-and-approve-expenses.md) | Approves an expense | Records the approval (BR-F8-05); accounting reimburses by transfer or payslip. |
| 3 | [S-F9-15 Planning](../../../../02-functional/f09-hr-and-projects/screens/06-plan-and-deliver-work/s-f09-15-planning.md) | [UC-F9-15 Plan shifts](../../../../02-functional/f09-hr-and-projects/use-cases/06-plan-and-deliver-work/uc-f09-15-plan-shifts.md) | Plans the team's shifts | Fills open shifts by auto-plan (BR-F9-09); publishes the drafts and notifies employees. |
| 4 | [S-F15-02 Legal warning](../../../../02-functional/f15-legal-assistant/screens/02-receive-a-legal-warning/s-f15-02-legal-warning.md) | [UC-F15-02 Receive a legal warning](../../../../02-functional/f15-legal-assistant/use-cases/02-receive-a-legal-warning/uc-f15-02-receive-a-legal-warning.md) | Reads the legal warning on the schedule and fixes it | Shows the rule, its article, version and date, and the facts it used (BR-F15-01). |
| 5 | [S-F8-09 Analytics and budgets](../../../../02-functional/f08-accounting/screens/04-tax-assets-and-analytics/s-f08-09-analytics-and-budgets.md) | [UC-F8-09 Track analytics and budgets](../../../../02-functional/f08-accounting/use-cases/04-tax-assets-and-analytics/uc-f08-09-track-analytics-and-budgets.md) | Follows the team's budget | Shows budget against actual, committed and forecast; overspends alert. |

This persona's images of these flows (D120):
[FL-F9-03 Time](../../../../02-functional/f09-hr-and-projects/images/03-time/u02-manager/README.md),
[FL-F8-02 Purchase to pay](../../../../02-functional/f08-accounting/images/02-purchase-to-pay/u02-manager/README.md),
[FL-F9-06 Plan and deliver work](../../../../02-functional/f09-hr-and-projects/images/06-plan-and-deliver-work/u02-manager/README.md),
[FL-F15-02 Receive a legal warning](../../../../02-functional/f15-legal-assistant/images/02-receive-a-legal-warning/u02-manager/README.md),
[FL-F8-04 Tax, assets and analytics](../../../../02-functional/f08-accounting/images/04-tax-assets-and-analytics/u02-manager/README.md).

## Open questions

None.

---

⬆️ [Up](README.md)

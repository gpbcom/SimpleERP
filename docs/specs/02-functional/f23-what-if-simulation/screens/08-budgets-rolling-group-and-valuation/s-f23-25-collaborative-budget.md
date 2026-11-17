🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-08 Budgets, rolling forecasts, group and valuation](README.md) › 🖥️ S-F23-25 Collaborative budget

# 🖥️ S-F23-25 Collaborative budget

**Status:** 🔄 waiting for the owner

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md): their department's contribution, with its envelope and
  comments.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): every department, the total and the approval.

## Purpose

Collect each department's contribution to the budget, review it and consolidate it for approval.

## Entry points

What-if simulation › Collaborative budget; a manager's request; the accounting budget screen.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Budget 2027      Envelope 420,000   Proposed 438,000   Due 2026-12-05      [Consolidate]       |
|---------------------------------------------------------------------------------------------|
| DEPARTMENT   MANAGER   ENVELOPE   CONTRIBUTION  ASSUMPTIONS               STATE            |
| Sales        Claire P. 120,000    131,000       2 hires, trade fair        Submitted, over  |
| Operations   Marc L.   200,000    198,000       stock +4 %                 Accepted         |
| Support      Anna R.   100,000    -             -                          Draft            |
| [Open] [Return with comment] [Accept] [Approve the budget]                                  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-08 step 1, U02 | desktop | ![FL-F23-08 step 1, U02, light](../../images/08-budgets-rolling-group-and-valuation/u02-manager/1-collaborative-budget-desktop-light.png) | ![FL-F23-08 step 1, U02, dark](../../images/08-budgets-rolling-group-and-valuation/u02-manager/1-collaborative-budget-desktop-dark.png) |
| FL-F23-08 step 1, U02 | phone | ![FL-F23-08 step 1, U02, light](../../images/08-budgets-rolling-group-and-valuation/u02-manager/1-collaborative-budget-phone-light.png) | ![FL-F23-08 step 1, U02, dark](../../images/08-budgets-rolling-group-and-valuation/u02-manager/1-collaborative-budget-phone-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/08-budgets-rolling-group-and-valuation/u02-manager/e1-the-budget-is-frozen-desktop-light.png) | ![Error E1, U02, dark](../../images/08-budgets-rolling-group-and-valuation/u02-manager/e1-the-budget-is-frozen-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/08-budgets-rolling-group-and-valuation/u02-manager/e1-the-budget-is-frozen-phone-light.png) | ![Error E1, U02, dark](../../images/08-budgets-rolling-group-and-valuation/u02-manager/e1-the-budget-is-frozen-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-25-collaborative-budget-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-25-collaborative-budget-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-25-collaborative-budget-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-25-collaborative-budget-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-25-collaborative-budget-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-25-collaborative-budget-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-25-collaborative-budget-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-25-collaborative-budget-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Department and manager | E-F23-15 department | text | no | yes |
| Envelope | E-F23-15 envelope | amount with currency | accounting only | yes |
| Contribution lines | E-F23-15 lines | account or analytic target, amount | manager while Draft | yes |
| Assumptions | E-F23-15 assumptions | text per line | manager while Draft | yes |
| Comment | E-F23-15 comment | text | accounting | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Submit | contribution | manager | sends the contribution to accounting |
| Return with comment | row | accounting | sends it back to the manager |
| Accept | row | accounting | marks the contribution ready to consolidate |
| Approve the budget | header | owner | writes the budget plan and freezes the contributions |

## States

- Normal: the departments with envelope, contribution, assumptions and state, and the total.
- Empty: No round open, with Open a round for the year.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  change after approval shows that the contribution is Frozen and how to revise the budget.
- Read-only: A Frozen contribution shows its lines and assumptions; the way to revise is a new budget version in the
  accounting.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F23-15 Budget contribution](../../data/e-f23-15-budget-contribution.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-15 Budget contribution | Draft | Badge "Draft"; a new record starts here; next: Submitted (UC-F23-31); fields editable within the role | U02, U05 | `u02-manager/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-draft-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-draft-desktop-{light,dark}.png` |
| E-F23-15 Budget contribution | Submitted | Badge "Submitted"; next: Returned or Accepted (UC-F23-31); fields editable within the role | U02, U05 | `u02-manager/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-submitted-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-submitted-desktop-{light,dark}.png` |
| E-F23-15 Budget contribution | Returned | Badge "Returned"; next: Draft (UC-F23-31); fields editable within the role | U02, U05 | `u02-manager/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-returned-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-returned-desktop-{light,dark}.png` |
| E-F23-15 Budget contribution | Accepted | Badge "Accepted"; next: Frozen (BR-F23-18); fields editable within the role | U02, U05 | `u02-manager/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-accepted-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-accepted-desktop-{light,dark}.png` |
| E-F23-15 Budget contribution | Frozen | Badge "Frozen"; final: read-only, no next state; the history shows how it got here | U02, U05 | `u02-manager/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-frozen-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f23-25-collaborative-budget-e-f23-15-budget-contribution-frozen-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F23-08](../../flows/fl-f23-08-budgets-rolling-group-and-valuation.md)

## Open questions

None.

---

⬅️ [S-F23-24 Sector drivers](../07-accuracy-and-drivers/s-f23-24-sector-drivers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-26 Rolling forecast](s-f23-26-rolling-forecast.md)

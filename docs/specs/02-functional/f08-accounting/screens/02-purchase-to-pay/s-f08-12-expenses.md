🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-02 Purchase to pay](README.md) ›
🖥️ S-F8-12 Expenses

# 🖥️ S-F8-12 Expenses

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Submit and approve expenses.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-02 step 3, U01 | phone | ![FL-F8-02 step 3, U01, light](../../images/02-purchase-to-pay/u01-employee/3-expenses-phone-light.png) | ![FL-F8-02 step 3, U01, dark](../../images/02-purchase-to-pay/u01-employee/3-expenses-phone-dark.png) |
| FL-F8-02 step 3, U01 | desktop | ![FL-F8-02 step 3, U01, light](../../images/02-purchase-to-pay/u01-employee/3-expenses-desktop-light.png) | ![FL-F8-02 step 3, U01, dark](../../images/02-purchase-to-pay/u01-employee/3-expenses-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-12-expenses-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-12-expenses-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-12-expenses-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-12-expenses-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-12-expenses-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-12-expenses-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-12-expenses-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-12-expenses-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Submit and approve expenses, as the wireframe shows.
- Empty: No expense yet for the period, with New expense.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F8-09 Expense claim](../../data/e-f08-09-expense-claim.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-09 Expense claim | Draft | Badge "Draft"; a new record starts here; next: Submitted or Refused (UC-F8-12); fields editable within the role | U01, U02, U05 | `u01-employee/s-f08-12-expenses-e-f08-09-expense-claim-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-12-expenses-e-f08-09-expense-claim-draft-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-12-expenses-e-f08-09-expense-claim-draft-desktop-{light,dark}.png` |
| E-F8-09 Expense claim | Submitted | Badge "Submitted"; next: Approved or Refused (UC-F8-12); fields editable within the role | U01, U02, U05 | `u01-employee/s-f08-12-expenses-e-f08-09-expense-claim-submitted-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-12-expenses-e-f08-09-expense-claim-submitted-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-12-expenses-e-f08-09-expense-claim-submitted-desktop-{light,dark}.png` |
| E-F8-09 Expense claim | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f08-12-expenses-e-f08-09-expense-claim-refused-{desktop,phone}-{light,dark}.png` |
| E-F8-09 Expense claim | Approved | Badge "Approved"; next: Reimbursed or Refused (UC-F8-12); fields editable within the role | U01, U02, U05 | `u01-employee/s-f08-12-expenses-e-f08-09-expense-claim-approved-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-12-expenses-e-f08-09-expense-claim-approved-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-12-expenses-e-f08-09-expense-claim-approved-desktop-{light,dark}.png` |
| E-F8-09 Expense claim | Reimbursed | Badge "Reimbursed"; final: read-only, no next state; the history shows how it got here | U01, U02, U05 | `u01-employee/s-f08-12-expenses-e-f08-09-expense-claim-reimbursed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-12-expenses-e-f08-09-expense-claim-reimbursed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-12-expenses-e-f08-09-expense-claim-reimbursed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F8-02 Purchase to pay](../../flows/fl-f08-02-purchase-to-pay.md)

## Open questions

None.

---

⬅️ [S-F8-11 Financial reports](../05-close-report-and-consolidate/s-f08-11-financial-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-13 Consolidation](../05-close-report-and-consolidate/s-f08-13-consolidation.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-08 Deductions, savings and leave pay](README.md) › 🖥️ S-F13-24 Garnishments and advances

# 🖥️ S-F13-24 Garnishments and advances

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md), who records orders and approves advances
- [U01 Employee](../../../../01-users/personas/u01-employee.md), who asks for an advance from their space

## Purpose

Record wage garnishments and approve pay advances, with what is deducted each month.

## Entry points

Payroll menu, Garnishments and advances; the "advance requested" notification; for the employee, "Ask for an advance" in
their space.

## Wireframe

```text
Garnishments and advances                      [Orders] [Advances 2 to approve]
-------------------------------------------------------------------------------
Employee       Kind           Reference   Due        Monthly    Remaining
Karim Haddad   tax notice     ATD 2026-118 1 840.00   427.64     1 412.36
-------------------------------------------------------------------------------
Advances: Sophie Bernard 300.00 asked 03-15, earned 1 050.00  [Approve] [Refuse]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-08 step 1, U45 | desktop | ![FL-F13-08 step 1, U45, light](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/1-garnishments-and-advances-desktop-light.png) | ![FL-F13-08 step 1, U45, dark](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/1-garnishments-and-advances-desktop-dark.png) |
| Error E1, U45 | desktop | ![Error E1, U45, light](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/e1-garnishments-and-advances-refused-desktop-light.png) | ![Error E1, U45, dark](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/e1-garnishments-and-advances-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-24-garnishments-and-advances-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-24-garnishments-and-advances-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-24-garnishments-and-advances-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-24-garnishments-and-advances-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-24-garnishments-and-advances-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-24-garnishments-and-advances-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-24-garnishments-and-advances-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-24-garnishments-and-advances-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Employee | E-F13-19 employee | name | no | yes |
| Kind | E-F13-19 kind | court order, maintenance order, tax notice | yes | yes |
| Creditor and IBAN | E-F13-19 creditor | name, IBAN | yes | yes |
| Amount due | E-F13-19 amount due | EUR | yes | yes |
| Monthly deduction | computed | EUR | no | no |
| Advance amount | E-F13-20 amount | EUR | yes (employee) | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Record an order | orders tab | payroll officer | order ranked and deducted from the next run |
| Lift | order panel | payroll officer | order lifted from the date |
| Ask for an advance | employee space | employee | request sent |
| Approve or refuse | advances tab | payroll officer | transfer prepared or employee told |

## States

- Normal: active orders with their monthly deduction and remaining amount; advances waiting for approval.
- Empty: "No garnishment or advance": shown when there is none; the employee's request form shows the amount available.
- Loading: the frame and titles show at once with placeholder rows for the orders and the advances; within 1 second
  (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: an invalid IBAN, a deduction capped at the protected amount, or an advance above the net earned.
- Read-only: settled and lifted orders are read-only; the employee sees only their own advances.
- Offline: The employee's form shows the amount last loaded but cannot send a request offline. Nothing else is queued:
  D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost and the
  actions come back with it.

Shown entities (VD-15): [E-F13-19 Garnishment](../../data/e-f13-19-garnishment.md),
[E-F13-20 Pay advance](../../data/e-f13-20-pay-advance.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-19 Garnishment | Received | Badge "Received"; a new record starts here; next: Active (UC-F13-26); fields editable within the role | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-received-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-received-desktop-{light,dark}.png` |
| E-F13-19 Garnishment | Active | Badge "Active"; next: Settled or Lifted (UC-F13-26); fields editable within the role | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-active-desktop-{light,dark}.png` |
| E-F13-19 Garnishment | Settled | Badge "Settled"; final: read-only, no next state; the history shows how it got here | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-settled-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-settled-desktop-{light,dark}.png` |
| E-F13-19 Garnishment | Lifted | Badge "Lifted"; final: read-only, no next state; the history shows how it got here | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-lifted-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-19-garnishment-lifted-desktop-{light,dark}.png` |
| E-F13-20 Pay advance | Asked | Badge "Asked"; a new record starts here; next: Approved or Refused (UC-F13-09); fields editable within the role | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-asked-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-asked-desktop-{light,dark}.png` |
| E-F13-20 Pay advance | Approved | Badge "Approved"; next: Paid (UC-F13-27); fields editable within the role | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-approved-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-approved-desktop-{light,dark}.png` |
| E-F13-20 Pay advance | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-refused-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-refused-desktop-{light,dark}.png` |
| E-F13-20 Pay advance | Paid | Badge "Paid"; next: Recovered (UC-F13-09); fields editable within the role | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-paid-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-paid-desktop-{light,dark}.png` |
| E-F13-20 Pay advance | Recovered | Badge "Recovered"; final: read-only, no next state; the history shows how it got here | U01, U45 | `u01-employee/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-recovered-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-24-garnishments-and-advances-e-f13-20-pay-advance-recovered-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the payroll officer; the employee's request works on a phone (D34).

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-08 Deductions, savings and leave pay](../../flows/fl-f13-08-deductions-savings-and-leave-pay.md)

## Open questions

None.

---

⬅️ [S-F13-23 Special regimes](../07-schemes-and-special-contracts/s-f13-23-special-regimes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-25 Profit-sharing](s-f13-25-profit-sharing.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-08 Deductions, savings and leave pay](README.md) › 🖥️ S-F13-26 Leave pay valuation

# 🖥️ S-F13-26 Leave pay valuation

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

Show, for each leave taken, maintained pay and one tenth, the amount kept and the end-of-period adjustments.

## Entry points

The pay run's "Leave" tab; Payroll menu, Leave pay.

## Wireframe

```text
Leave pay, August 2026                          [This month] [End of period]
-------------------------------------------------------------------------------
Employee      Leave            Maintained   One tenth   Kept     Paid by
Marc Petit    5 d, 08-03       480.00       512.00      512.00   company
Paul Garnier  10 d, 08-10      -            -           -        BTP fund
-------------------------------------------------------------------------------
End of period: 3 adjustments, total 112.40          [Add to the June run]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-08 step 4, U45 | desktop | ![FL-F13-08 step 4, U45, light](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/4-leave-pay-valuation-desktop-light.png) | ![FL-F13-08 step 4, U45, dark](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/4-leave-pay-valuation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-26-leave-pay-valuation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-26-leave-pay-valuation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-26-leave-pay-valuation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-26-leave-pay-valuation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-26-leave-pay-valuation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-26-leave-pay-valuation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-26-leave-pay-valuation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-26-leave-pay-valuation-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Employee | E-F13-22 employee | name | no | yes |
| Leave | E-F13-22 leave taken | days and dates | no | yes |
| Maintained pay | E-F13-22 maintained pay | EUR | no | yes |
| One tenth | E-F13-22 one tenth | EUR | no | yes |
| Kept | E-F13-22 kept | EUR | no | yes |
| Paid by | E-F13-22 paid by | company, fund | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Check | list | payroll officer | comparison marked as checked |
| Add adjustments | end-of-period tab | payroll officer | adjustment lines added to the run |

## States

- Normal: each leave of the month with both amounts and the amount kept.
- Empty: "No paid leave taken this month".
- Loading: the frame and titles show at once with placeholder rows for the leave of the month; within 1 second (D408)
  the data replaces them, and a longer load shows a progress line saying what loads.
- Error: an incomplete reference gross, flagged on the employee's row.
- Read-only: a paid run's comparisons are read-only (BR-F13-10).
- Offline: not available offline: part of the pay run, office work on a desktop. D38 keeps only today's schedule, time
  and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action
  is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-22 Leave pay valuation](../../data/e-f13-22-leave-pay-valuation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-22 Leave pay valuation | Computed | Badge "Computed"; a new record starts here; next: Paid or Adjusted (UC-F13-29); fields editable within the role | U45 | `u45-payroll-officer/s-f13-26-leave-pay-valuation-e-f13-22-leave-pay-valuation-computed-desktop-{light,dark}.png` |
| E-F13-22 Leave pay valuation | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U45 | `u45-payroll-officer/s-f13-26-leave-pay-valuation-e-f13-22-leave-pay-valuation-paid-desktop-{light,dark}.png` |
| E-F13-22 Leave pay valuation | Adjusted | Badge "Adjusted"; next: Paid (UC-F13-29); fields editable within the role | U45 | `u45-payroll-officer/s-f13-26-leave-pay-valuation-e-f13-22-leave-pay-valuation-adjusted-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only (part of the pay run).

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-08 Deductions, savings and leave pay](../../flows/fl-f13-08-deductions-savings-and-leave-pay.md)

## Open questions

None.

---

⬅️ [S-F13-25 Profit-sharing](s-f13-25-profit-sharing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-27 Payroll analytics](../05-reports-and-rules/s-f13-27-payroll-analytics.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-08 Deductions, savings and leave pay](README.md) › 🖥️ S-F13-25 Profit-sharing

# 🖥️ S-F13-25 Profit-sharing

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md), who computes and settles
- [U13 Owner](../../../../01-users/personas/u13-owner.md), who signs off the reserve
- [U01 Employee](../../../../01-users/personas/u01-employee.md), who chooses paid or invested

## Purpose

Compute the year's profit-sharing reserve, share it, and collect each employee's choice.

## Entry points

Payroll menu, Profit-sharing; the "reserve ready" notification for the owner; the "your share" notification for
employees.

## Wireframe

```text
Profit-sharing 2026                 Reserve 40 000.00   [Sign off] (owner)
-------------------------------------------------------------------------------
Keys: 50 % salary, 50 % time worked      Ceiling applied to 2 employees
Employee         Share     Choice      Deadline
Marc Petit       812.40    paid        2027-05-15
Sophie Bernard   640.10    -           2027-05-15
-------------------------------------------------------------------------------
[Export investments] [Post entries]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-08 step 3, U45 | desktop | ![FL-F13-08 step 3, U45, light](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/3-profit-sharing-desktop-light.png) | ![FL-F13-08 step 3, U45, dark](../../images/08-deductions-savings-and-leave-pay/u45-payroll-officer/3-profit-sharing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-25-profit-sharing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-25-profit-sharing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-25-profit-sharing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-25-profit-sharing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-25-profit-sharing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-25-profit-sharing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-25-profit-sharing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-25-profit-sharing-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Year | E-F13-21 year | year | yes | yes |
| Reserve | E-F13-21 reserve | EUR | no (computed) | yes |
| Keys | E-F13-21 keys | percent per key | no (from the agreement) | yes |
| Share | E-F13-21 employee share | EUR | no | yes |
| Choice | E-F13-21 choice | paid, invested | yes (employee) | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Compute | header | payroll officer | reserve computed from F8 |
| Sign off | header | owner | shares computed and announced |
| Choose | employee space | employee | choice saved |
| Export investments | footer | payroll officer | file for the savings-plan keeper |

## States

- Normal: the reserve, the keys and each employee's share and choice.
- Empty: "No profit-sharing year yet": shown before the first closed year, with the threshold of BR-F13-21.
- Loading: the frame and titles show at once with placeholder rows for the year's shares; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: a year not closed in F8, or a negative reserve, with what to do.
- Read-only: a settled year is read-only; employees see only their own share.
- Offline: The employee sees the share last loaded; the choice is sent only online. Nothing else is queued: D38 keeps
  only today's schedule, time and intervention records offline; a banner says the connection is lost and the actions
  come back with it.

Shown entities (VD-15): [E-F13-21 Profit-sharing year](../../data/e-f13-21-profit-sharing-year.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-21 Profit-sharing year | Computed | Badge "Computed"; a new record starts here; next: Announced (UC-F13-28); fields editable within the role | U01, U13, U45 | `u01-employee/s-f13-25-profit-sharing-e-f13-21-profit-sharing-year-computed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f13-25-profit-sharing-e-f13-21-profit-sharing-year-computed-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-25-profit-sharing-e-f13-21-profit-sharing-year-computed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the employee's choice on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-08 Deductions, savings and leave pay](../../flows/fl-f13-08-deductions-savings-and-leave-pay.md)

## Open questions

None.

---

⬅️ [S-F13-24 Garnishments and advances](s-f13-24-garnishments-and-advances.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-26 Leave pay valuation](s-f13-26-leave-pay-valuation.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-07 Schemes and special contracts](README.md) › 🖥️ S-F13-22 Special contracts

# 🖥️ S-F13-22 Special contracts

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md), who sets the regime and pay
- [U13 Owner](../../../../01-users/personas/u13-owner.md), who records an officer's pay decision
- [U06 Human resources](../../../../01-users/personas/u06-hr.md), who records the contract in F9

## Purpose

Set the pay regime of apprentices, interns and company officers, with their grid or contribution set.

## Entry points

Payroll menu, Special contracts; the "new special contract" notification; an employee's pay profile.

## Wireframe

```text
Special contracts                       [Apprentices] [Interns] [Officers]
-------------------------------------------------------------------------------
Name          Regime      Grid position        Pay          Next change
Lucas Martin  apprentice  18 to 20, year 2     grid         2026-11-20 (21)
Emma Roux     intern      3 months, 35 h/week  allowance    -
Chair         officer     -                    4 000.00     -
-------------------------------------------------------------------------------
[Regime panel] regime, training body, start, pay, [Simulate payslip] [Confirm]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-07 step 2, U45 | desktop | ![FL-F13-07 step 2, U45, light](../../images/07-schemes-and-special-contracts/u45-payroll-officer/2-special-contracts-desktop-light.png) | ![FL-F13-07 step 2, U45, dark](../../images/07-schemes-and-special-contracts/u45-payroll-officer/2-special-contracts-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-22-special-contracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-22-special-contracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-22-special-contracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-22-special-contracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-22-special-contracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-22-special-contracts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-22-special-contracts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-22-special-contracts-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Name | E-F13-18 employee | name | no | yes |
| Regime | E-F13-18 regime | apprentice, intern, officer | yes | yes |
| Grid position | E-F13-18 grid position | age band and year | no (computed) | for apprentices |
| Training body | E-F13-18 training body | name and SIRET | yes | for apprentices and interns |
| Pay | E-F13-02 pay | EUR per month or hour | yes | yes |
| Next change | computed | date and reason | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Confirm regime | regime panel | payroll officer | regime saved, used in the next run |
| Simulate payslip | regime panel | payroll officer, owner | simulated payslip shown (UC-F13-16) |
| Record decision | officers tab | owner | officer's pay decision saved |

## States

- Normal: one tab per contract kind with each person's regime, pay and the next grid change.
- Empty: "No apprentice, intern or officer": shown per tab when the company has none; a short text says what each regime
  is for.
- Loading: the frame and titles show at once with placeholder rows for the special contracts; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: a pay below the grid, an unemployment line on an officer, or a missing grid for the period, each next to its
  field.
- Read-only: HR and the owner read the regimes; only the owner sees officers' pay; a past regime is read-only.
- Offline: not available offline: payroll set-up is office work on a desktop. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-18 Special pay regime](../../data/e-f13-18-special-pay-regime.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-18 Special pay regime | Active | Badge "Active"; a new record starts here; next: Changed or Ended (UC-F13-22, UC-F13-24); fields editable within the role | U06, U13, U45 | `u06-hr/s-f13-22-special-contracts-e-f13-18-special-pay-regime-active-desktop-{light,dark}.png`, `u13-owner/s-f13-22-special-contracts-e-f13-18-special-pay-regime-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-22-special-contracts-e-f13-18-special-pay-regime-active-desktop-{light,dark}.png` |
| E-F13-18 Special pay regime | Changed | Badge "Changed"; next: Active (UC-F13-22); fields editable within the role | U06, U13, U45 | `u06-hr/s-f13-22-special-contracts-e-f13-18-special-pay-regime-changed-desktop-{light,dark}.png`, `u13-owner/s-f13-22-special-contracts-e-f13-18-special-pay-regime-changed-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-22-special-contracts-e-f13-18-special-pay-regime-changed-desktop-{light,dark}.png` |
| E-F13-18 Special pay regime | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U06, U13, U45 | `u06-hr/s-f13-22-special-contracts-e-f13-18-special-pay-regime-ended-desktop-{light,dark}.png`, `u13-owner/s-f13-22-special-contracts-e-f13-18-special-pay-regime-ended-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-22-special-contracts-e-f13-18-special-pay-regime-ended-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet with the panel over the list; not on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-07 Schemes and special contracts](../../flows/fl-f13-07-schemes-and-special-contracts.md)

## Open questions

None.

---

⬅️ [S-F13-21 Schemes](s-f13-21-schemes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-23 Special regimes](s-f13-23-special-regimes.md)

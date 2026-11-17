🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-05 Reports and rules](README.md) › 🖥️ S-F13-27 Payroll analytics

# 🖥️ S-F13-27 Payroll analytics

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md), who reviews the cost per site and project
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md), who exports and posts
- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

Show the payroll cost of each run by site, project and analytic axis, with headcount and changes.

## Entry points

Payroll menu, Analytics; the owner's dashboard card; the run approved notification.

## Wireframe

```text
Payroll analytics      Period [March 2026]  Axis [Site v]       [Export]
-------------------------------------------------------------------------------
Site            Cost         Headcount   Overtime   vs Feb
Agency Nord     48 210.00    22          3.1 %      +2.4 %
Agency Sud      31 480.00    15          1.8 %      -0.6 %
Default site     2 412.80     1 (flagged)
-------------------------------------------------------------------------------
[Chart: cost per site over 12 months]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-05 step 3, U13 | desktop | ![FL-F13-05 step 3, U13, light](../../images/05-reports-and-rules/u13-owner/3-payroll-analytics-desktop-light.png) | ![FL-F13-05 step 3, U13, dark](../../images/05-reports-and-rules/u13-owner/3-payroll-analytics-desktop-dark.png) |
| FL-F13-05 step 3, U13 | phone | ![FL-F13-05 step 3, U13, light](../../images/05-reports-and-rules/u13-owner/3-payroll-analytics-phone-light.png) | ![FL-F13-05 step 3, U13, dark](../../images/05-reports-and-rules/u13-owner/3-payroll-analytics-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-27-payroll-analytics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-27-payroll-analytics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-27-payroll-analytics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-27-payroll-analytics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-27-payroll-analytics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-27-payroll-analytics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f13-27-payroll-analytics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f13-27-payroll-analytics-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Axis value | E-F13-24 axis, value | text | no | yes |
| Cost | E-F13-24 cost | EUR | no | yes |
| Headcount | computed | number | no | yes |
| Overtime share | computed | percent | no | no |
| Change | computed | percent | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Choose period and axis | header | owner, accounting, payroll officer | analysis refreshed |
| Drill into | row | same | employees of that value |
| Export | header | accounting, payroll officer | Excel or CSV |

## States

- Normal: costs per value of the chosen axis with a 12-month chart.
- Empty: "No approved run in this period": shown before the first approved run or for a future period.
- Loading: the frame and titles show at once with placeholder rows for the cost per site; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: employees with no time recorded, flagged on the default site.
- Read-only: managers see headcount and hours of their teams only, amounts hidden.
- Offline: The owner's phone shows the figures last loaded with their date; nothing refreshes offline. Nothing else is
  queued: D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost
  and the actions come back with it.

Shown entities (VD-15): [E-F13-24 Payroll cost allocation](../../data/e-f13-24-payroll-cost-allocation.md),
[E-F13-25 Analytic axis](../../data/e-f13-25-analytic-axis.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-24 Payroll cost allocation | Computed | Badge "Computed"; a new record starts here; next: Posted (UC-F13-13); fields editable within the role | U05, U13, U45 | `u05-accounting/s-f13-27-payroll-analytics-e-f13-24-payroll-cost-allocation-computed-desktop-{light,dark}.png`, `u13-owner/s-f13-27-payroll-analytics-e-f13-24-payroll-cost-allocation-computed-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-27-payroll-analytics-e-f13-24-payroll-cost-allocation-computed-desktop-{light,dark}.png` |
| E-F13-24 Payroll cost allocation | Posted | Badge "Posted"; final: read-only, no next state; the history shows how it got here | U05, U13, U45 | `u05-accounting/s-f13-27-payroll-analytics-e-f13-24-payroll-cost-allocation-posted-desktop-{light,dark}.png`, `u13-owner/s-f13-27-payroll-analytics-e-f13-24-payroll-cost-allocation-posted-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-27-payroll-analytics-e-f13-24-payroll-cost-allocation-posted-desktop-{light,dark}.png` |
| E-F13-25 Analytic axis | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13, U45 | `u05-accounting/s-f13-27-payroll-analytics-e-f13-25-analytic-axis-active-desktop-{light,dark}.png`, `u13-owner/s-f13-27-payroll-analytics-e-f13-25-analytic-axis-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-27-payroll-analytics-e-f13-25-analytic-axis-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the owner reads the table and chart on a phone (D34).

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-05 Reports and rules](../../flows/fl-f13-05-reports-and-rules.md)

## Open questions

None.

---

⬅️ [S-F13-26 Leave pay valuation](../08-deductions-savings-and-leave-pay/s-f13-26-leave-pay-valuation.md) ·
⬆️ [Up](README.md) · ➡️ [S-F13-28 Posted workers](../10-special-contracts-and-outsourcing/s-f13-28-posted-workers.md)

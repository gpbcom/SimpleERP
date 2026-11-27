🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-09 Sell on the road and steer sales](README.md) › 🖥️ S-F6-21 Targets and commissions

# 🖥️ S-F6-21 Targets and commissions

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md)

## Purpose

Set targets and commission plans and approve statements.

## Entry points

Sales › Targets and commissions; the rep's progress.

## Wireframe

```text
+------------------------------------------------------------------+
| 2027-Q1   Plan: 3 %, 5 % above target, on paid invoices           |
| Rep        Target     Paid       %      Commission   Status       |
| Lea Roux   180,000    200,000    112 %  6,400 EUR    to approve   |
| Tom Petit  150,000    120,000    80 %   3,600 EUR    to approve   |
|                                    [Approve] [Send to payroll]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-09 step 3, U02 | desktop | ![FL-F6-09 step 3, U02, light](../../images/09-sell-on-the-road-and-steer-sales/u02-manager/3-targets-and-commissions-desktop-light.png) | ![FL-F6-09 step 3, U02, dark](../../images/09-sell-on-the-road-and-steer-sales/u02-manager/3-targets-and-commissions-desktop-dark.png) |
| FL-F6-09 step 3, U02 | phone | ![FL-F6-09 step 3, U02, light](../../images/09-sell-on-the-road-and-steer-sales/u02-manager/3-targets-and-commissions-phone-light.png) | ![FL-F6-09 step 3, U02, dark](../../images/09-sell-on-the-road-and-steer-sales/u02-manager/3-targets-and-commissions-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-21-targets-and-commissions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-21-targets-and-commissions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-21-targets-and-commissions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-21-targets-and-commissions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-21-targets-and-commissions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-21-targets-and-commissions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-21-targets-and-commissions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-21-targets-and-commissions-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Targets, paid, commission | E-F6-18, E-F6-19 | targets and plan |

## Actions

| Action | Who | Result |
|---|---|---|
| Approve | manager | Statement approved |
| Send to payroll | manager | Pay inputs (F13) |

## States

- Normal: set targets and commission plans and approve statements.
- Empty: no plan yet: Create a plan.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a rep sees only their own line.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-18 Commission plan and target](../../data/e-f06-18-commission-plan-and-target.md),
[E-F6-19 Commission line](../../data/e-f06-19-commission-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-18 Commission plan and target | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F6-25); fields editable within the role | U02 | `u02-manager/s-f06-21-targets-and-commissions-e-f06-18-commission-plan-and-target-draft-{desktop,phone}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Active | Badge "Active"; next: Closed (UC-SC11-17); fields editable within the role | U02 | `u02-manager/s-f06-21-targets-and-commissions-e-f06-18-commission-plan-and-target-active-{desktop,phone}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f06-21-targets-and-commissions-e-f06-18-commission-plan-and-target-closed-{desktop,phone}-{light,dark}.png` |
| E-F6-19 Commission line | Approved | Badge "Approved"; a new record starts here; next: Paid (UC-F6-25); fields editable within the role | U02 | `u02-manager/s-f06-21-targets-and-commissions-e-f06-19-commission-line-approved-{desktop,phone}-{light,dark}.png` |
| E-F6-19 Commission line | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f06-21-targets-and-commissions-e-f06-19-commission-line-paid-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; progress on a phone for reps.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-09 Sell on the road and steer sales](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md)

## Open questions

None.

---

⬅️ [S-F6-20 Instalments and disputes](../08-collect-and-settle/s-f06-20-instalments-and-disputes.md) ·
⬆️ [Up](README.md) · ➡️ [S-F6-22 Sales reports](s-f06-22-sales-reports.md)

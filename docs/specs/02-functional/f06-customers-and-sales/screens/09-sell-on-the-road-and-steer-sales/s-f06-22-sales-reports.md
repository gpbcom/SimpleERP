🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-09 Sell on the road and steer sales](README.md) › 🖥️ S-F6-22 Sales reports

# 🖥️ S-F6-22 Sales reports

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Show sales and margin per rep, territory, customer and product, against targets and last year.

## Entry points

Reports › Sales.

## Wireframe

```text
+------------------------------------------------------------------+
| Sales 2026   [By territory v]   vs 2025   vs target               |
| Territory   Sales       Margin   Margin %   vs 2025   Target      |
| South       1.20 M      264 k    22 %       +8 %      104 %       |
| North       0.85 M      170 k    20 %       -3 %      91 %        |
| Margin unknown on 40 invoices                       [Export]      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-09 step 4, U13 | desktop | ![FL-F6-09 step 4, U13, light](../../images/09-sell-on-the-road-and-steer-sales/u13-owner/4-sales-reports-desktop-light.png) | ![FL-F6-09 step 4, U13, dark](../../images/09-sell-on-the-road-and-steer-sales/u13-owner/4-sales-reports-desktop-dark.png) |
| FL-F6-09 step 4, U13 | phone | ![FL-F6-09 step 4, U13, light](../../images/09-sell-on-the-road-and-steer-sales/u13-owner/4-sales-reports-phone-light.png) | ![FL-F6-09 step 4, U13, dark](../../images/09-sell-on-the-road-and-steer-sales/u13-owner/4-sales-reports-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-22-sales-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-22-sales-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-22-sales-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-22-sales-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-22-sales-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-22-sales-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-22-sales-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-22-sales-reports-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Sales, margin, comparisons | computed from E-F6-05 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Drill in | managers, owner | Reps, customers, invoices |
| Export | managers, owner | File |

## States

- Normal: show sales and margin per rep, territory, customer and product, against targets and last year.
- Empty: no invoice in the period: "Nothing invoiced yet".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: reports are computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-18 Commission plan and target](../../data/e-f06-18-commission-plan-and-target.md),
[E-F6-05 Invoice](../../data/e-f06-05-invoice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-18 Commission plan and target | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F6-25); fields editable within the role | U13 | `u13-owner/s-f06-22-sales-reports-e-f06-18-commission-plan-and-target-draft-{desktop,phone}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Active | Badge "Active"; next: Closed (UC-SC11-17); fields editable within the role | U13 | `u13-owner/s-f06-22-sales-reports-e-f06-18-commission-plan-and-target-active-{desktop,phone}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f06-22-sales-reports-e-f06-18-commission-plan-and-target-closed-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U13 | `u13-owner/s-f06-22-sales-reports-e-f06-05-invoice-sent-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U13 | `u13-owner/s-f06-22-sales-reports-e-f06-05-invoice-received-{desktop,phone}-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U13 | `u13-owner/s-f06-22-sales-reports-e-f06-05-invoice-paid-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

- [FL-F6-09 Sell on the road and steer sales](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md)

## Open questions

None.

---

⬅️ [S-F6-21 Targets and commissions](s-f06-21-targets-and-commissions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-23 Pro-forma invoice](../07-special-invoicing/s-f06-23-pro-forma-invoice.md)

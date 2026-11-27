🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-11 Store reports](README.md) › 🖥️ S-F10-27 Store reports

# 🖥️ S-F10-27 Store reports

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Show hourly sales, staff performance and basket analysis.

## Entry points

Point of sale › Store reports.

## Wireframe

```text
+------------------------------------------------------------------+
| Store reports  Lyon  [Last 4 weeks v]                              |
| Hourly: Sat 15-17 h = 28 % of sales     [heat map by weekday/hour]|
| Staff   Lea 182 baskets, avg 38 EUR   Tom 140 baskets, avg 31 EUR  |
| Baskets: coffee + croissant 34 % of mornings   [Create combo]      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-11 step 1, U23 | desktop | ![FL-F10-11 step 1, U23, light](../../images/11-store-reports/u23-store-manager/1-store-reports-desktop-light.png) | ![FL-F10-11 step 1, U23, dark](../../images/11-store-reports/u23-store-manager/1-store-reports-desktop-dark.png) |
| FL-F10-11 step 1, U23 | phone | ![FL-F10-11 step 1, U23, light](../../images/11-store-reports/u23-store-manager/1-store-reports-phone-light.png) | ![FL-F10-11 step 1, U23, dark](../../images/11-store-reports/u23-store-manager/1-store-reports-phone-dark.png) |
| FL-F10-11 step 1, U23 | tablet | ![FL-F10-11 step 1, U23, light](../../images/11-store-reports/u23-store-manager/1-store-reports-tablet-light.png) | ![FL-F10-11 step 1, U23, dark](../../images/11-store-reports/u23-store-manager/1-store-reports-tablet-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/11-store-reports/u23-store-manager/e1-store-reports-refused-desktop-light.png) | ![Error E1, U23, dark](../../images/11-store-reports/u23-store-manager/e1-store-reports-refused-desktop-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/11-store-reports/u23-store-manager/e1-store-reports-refused-phone-light.png) | ![Error E1, U23, dark](../../images/11-store-reports/u23-store-manager/e1-store-reports-refused-phone-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/11-store-reports/u23-store-manager/e1-store-reports-refused-tablet-light.png) | ![Error E1, U23, dark](../../images/11-store-reports/u23-store-manager/e1-store-reports-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-27-store-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-27-store-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-27-store-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-27-store-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-27-store-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-27-store-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-27-store-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-27-store-reports-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Hourly sales, staff, pairs | E-F10-03, E-F10-02 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Create combo | store manager | Combo drafted (UC-F10-06) |

## States

- Normal: show hourly sales, staff performance and basket analysis.
- Empty: no closed session in the period: "Close sessions to see reports".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-03 Point of sale order | Draft | Badge "Draft"; a new record starts here; next: Paid (UC-F10-03); fields editable within the role | U13, U23 | `u13-owner/s-f10-27-store-reports-e-f10-03-point-of-sale-order-draft-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-f10-27-store-reports-e-f10-03-point-of-sale-order-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Paid | Badge "Paid"; next: Invoiced (UC-F10-04); fields editable within the role | U13, U23 | `u13-owner/s-f10-27-store-reports-e-f10-03-point-of-sale-order-paid-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-f10-27-store-reports-e-f10-03-point-of-sale-order-paid-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Invoiced | Badge "Invoiced"; next: Refunded (UC-F10-03); fields editable within the role | U13, U23 | `u13-owner/s-f10-27-store-reports-e-f10-03-point-of-sale-order-invoiced-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-f10-27-store-reports-e-f10-03-point-of-sale-order-invoiced-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-03 Point of sale order | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U13, U23 | `u13-owner/s-f10-27-store-reports-e-f10-03-point-of-sale-order-refunded-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-f10-27-store-reports-e-f10-03-point-of-sale-order-refunded-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-11 Store reports](../../flows/fl-f10-11-store-reports.md)

## Open questions

None.

---

⬅️ [S-F10-26 Tax-free](../10-clienteling-transfers-and-tax-free/s-f10-26-tax-free.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-28 Online takeaway](../12-takeaway-softpos-and-labels/s-f10-28-online-takeaway.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-03 Replenish](README.md) › 🖥️ S-F7-21 Stock levels

# 🖥️ S-F7-21 Stock levels

**Status:** ✅ specified

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Set safety stock, minimum and maximum per item and location.

## Entry points

Purchasing › Stock levels.

## Wireframe

```text
+------------------------------------------------------------------+
| Stock levels  [Drinks v] [Lyon v]                                 |
| Item            Stock  Forecast  Lead  Safety  Min   Max          |
| Beer 33cl x24   120    35 (12-04) 5 d  [40]    [80]  [300]        |
| Water 1L x6     400    310       3 d   [60]    [100] [600]        |
|                       [Propose safety stock]  [Save]              |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-03 step 2, U04 | desktop | ![FL-F7-03 step 2, U04, light](../../images/03-replenish/u04-purchasing/2-warehouse-setup-desktop-light.png) | ![FL-F7-03 step 2, U04, dark](../../images/03-replenish/u04-purchasing/2-warehouse-setup-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-21-stock-levels-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-21-stock-levels-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-21-stock-levels-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-21-stock-levels-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-21-stock-levels-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-21-stock-levels-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-21-stock-levels-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-21-stock-levels-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Stock, forecast, lead time | E-F7-06 | no |
| Safety, min, max | E-F7-09 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Propose | purchasing | Safety stock from demand and lead time |
| Save | purchasing | Levels set |

## States

- Normal: set safety stock, minimum and maximum per item and location.
- Empty: no item in the filter: Clear the filters.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for managers, who read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F7-06 Item](../../data/e-f07-06-item.md),
[E-F7-09 Reordering rule](../../data/e-f07-09-reordering-rule.md),
[E-F7-21 Demand forecast](../../data/e-f07-21-demand-forecast.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-06 Item | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U04 | `u02-manager/s-f07-21-stock-levels-e-f07-06-item-active-{desktop,phone}-{light,dark}.png`, `u04-purchasing/s-f07-21-stock-levels-e-f07-06-item-active-desktop-{light,dark}.png` |
| E-F7-09 Reordering rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-21-stock-levels-e-f07-09-reordering-rule-active-desktop-{light,dark}.png` |
| E-F7-21 Demand forecast | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-21-stock-levels-e-f07-21-demand-forecast-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-08 Catalogues and stock levels](../../flows/fl-f07-08-catalogues-and-stock-levels.md)

## Open questions

None.

---

⬅️ [S-F7-20 Buy](../08-catalogues-and-stock-levels/s-f07-20-buy.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-22 Eco-contributions](../09-compliance-and-carbon/s-f07-22-eco-contributions.md)

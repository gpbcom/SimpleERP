🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-07 Supplier agreements and performance](README.md) › 🖥️ S-F7-19 Supplier performance

# 🖥️ S-F7-19 Supplier performance

**Status:** ✅ specified

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Show each supplier's delivery, quality, price and lead-time performance.

## Entry points

Purchasing › Supplier performance.

## Wireframe

```text
+------------------------------------------------------------------+
| Supplier performance  [Last 12 months v]                         |
| Supplier      Receipts  OTIF   Rejects  Price var.  Lead drift  Score|
| Supplier X    50        78 %   4 %      +3 %        +2 d        71 |
| Brasseries R. 120       96 %   0.5 %    0 %         0 d         95 |
|                         [Record a review] [Call for tenders]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-07 step 3, U04 | desktop | ![FL-F7-07 step 3, U04, light](../../images/07-supplier-agreements-and-performance/u04-purchasing/3-supplier-performance-desktop-light.png) | ![FL-F7-07 step 3, U04, dark](../../images/07-supplier-agreements-and-performance/u04-purchasing/3-supplier-performance-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-19-supplier-performance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-19-supplier-performance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-19-supplier-performance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-19-supplier-performance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-19-supplier-performance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-19-supplier-performance-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-19-supplier-performance-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-19-supplier-performance-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Receipts, OTIF, rejects, variance, drift, score | E-F7-16 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Record a review | purchasing | Review on the supplier |
| Call for tenders | purchasing | UC-F7-14 |

## States

- Normal: show each supplier's delivery, quality, price and lead-time performance.
- Empty: no receipt in the period: "No performance to show yet".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: scores are computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F7-16 Supplier score](../../data/e-f07-16-supplier-score.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-16 Supplier score | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U04, U13 | `u04-purchasing/s-f07-19-supplier-performance-e-f07-16-supplier-score-recorded-desktop-{light,dark}.png`, `u13-owner/s-f07-19-supplier-performance-e-f07-16-supplier-score-recorded-{desktop,phone}-{light,dark}.png` |

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
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-07 Supplier agreements and performance](../../flows/fl-f07-07-supplier-agreements-and-performance.md)

## Open questions

None.

---

⬅️ [S-F7-18 Supplier contracts](s-f07-18-supplier-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-20 Buy](../08-catalogues-and-stock-levels/s-f07-20-buy.md)

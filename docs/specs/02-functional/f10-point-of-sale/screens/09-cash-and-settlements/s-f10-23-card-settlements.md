🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-09 Cash and settlements](README.md) › 🖥️ S-F10-23 Card settlements

# 🖥️ S-F10-23 Card settlements

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Match card settlements to sessions and the bank, and post fees.

## Entry points

Accounting › Card settlements.

## Wireframe

```text
+------------------------------------------------------------------+
| Card settlements  [November v]                                     |
| Date   Acquirer  Gross     Fees    Net       Sessions  Bank       |
| 11-12  A         6,420.00  70.62   6,349.38  ok        matched    |
| 11-13  A         5,980.00  71.76   5,908.24  -60.00    waiting    |
| Fee rate 1.2 % (contract 0.9 %)  flagged                         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-09 step 3, U05 | desktop | ![FL-F10-09 step 3, U05, light](../../images/09-cash-and-settlements/u05-accounting/3-card-settlements-desktop-light.png) | ![FL-F10-09 step 3, U05, dark](../../images/09-cash-and-settlements/u05-accounting/3-card-settlements-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-23-card-settlements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-23-card-settlements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-23-card-settlements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-23-card-settlements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-23-card-settlements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-23-card-settlements-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f10-23-card-settlements-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f10-23-card-settlements-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Gross, fees, net, matches | E-F10-18 | matches |

## Actions

| Action | Who | Result |
|---|---|---|
| Post fees | accounting | Entries |
| Investigate | accounting | Payments listed |

## States

- Normal: match card settlements to sessions and the bank, and post fees.
- Empty: no settlement yet: "Connect the acquirer".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: matched settlements of a locked period.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F10-18 Card settlement](../../data/e-f10-18-card-settlement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-18 Card settlement | Matched | Badge "Matched"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f10-23-card-settlements-e-f10-18-card-settlement-matched-desktop-{light,dark}.png` |
| E-F10-18 Card settlement | Gap | Badge "Gap"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f10-23-card-settlements-e-f10-18-card-settlement-gap-desktop-{light,dark}.png` |

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

- [FL-F10-09 Cash and settlements](../../flows/fl-f10-09-cash-and-settlements.md)

## Open questions

None.

---

⬅️ [S-F10-22 Safe and deposits](s-f10-22-safe-and-deposits.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-24 Clienteling](../10-clienteling-transfers-and-tax-free/s-f10-24-clienteling.md)

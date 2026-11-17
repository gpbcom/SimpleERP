🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-07 Supplier agreements and performance](README.md) › 🖥️ S-F7-18 Supplier contracts

# 🖥️ S-F7-18 Supplier contracts

**Status:** ✅ specified

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Record supplier contracts, their prices, rebates and notice dates.

## Entry points

Purchasing › Contracts.

## Wireframe

```text
+------------------------------------------------------------------+
| Supplier contracts                                [+ Contract]   |
| Supplier          Valid until  Notice by    Rebate     Status     |
| Brasseries Rhône  2027-12-31   2027-09-30   2 %/200k   active     |
| Eaux du Sud       2026-12-31   2026-09-30   -          notice past|
| Prices: beer 33cl x24 11.65 (-6 %)  ...          [Open file]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-07 step 1, U04 | desktop | ![FL-F7-07 step 1, U04, light](../../images/07-supplier-agreements-and-performance/u04-purchasing/1-supplier-contracts-desktop-light.png) | ![FL-F7-07 step 1, U04, dark](../../images/07-supplier-agreements-and-performance/u04-purchasing/1-supplier-contracts-desktop-dark.png) |
| Error E1, U04 | desktop | ![Error E1, U04, light](../../images/07-supplier-agreements-and-performance/u04-purchasing/e1-supplier-contracts-refused-desktop-light.png) | ![Error E1, U04, dark](../../images/07-supplier-agreements-and-performance/u04-purchasing/e1-supplier-contracts-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-18-supplier-contracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-18-supplier-contracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-18-supplier-contracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-18-supplier-contracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-18-supplier-contracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-18-supplier-contracts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-18-supplier-contracts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-18-supplier-contracts-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Supplier, validity, notice, prices, rebates | E-F7-15 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Create, renew, end | purchasing | Contract saved |

## States

- Normal: record supplier contracts, their prices, rebates and notice dates.
- Empty: no contract yet: Add a contract.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: ended contracts.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F7-15 Supplier contract](../../data/e-f07-15-supplier-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-15 Supplier contract | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F7-18); fields editable within the role | U04 | `u04-purchasing/s-f07-18-supplier-contracts-e-f07-15-supplier-contract-draft-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Active | Badge "Active"; next: Renewed or Ended (UC-F7-18); fields editable within the role | U04 | `u04-purchasing/s-f07-18-supplier-contracts-e-f07-15-supplier-contract-active-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Renewed | Badge "Renewed"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-18-supplier-contracts-e-f07-15-supplier-contract-renewed-desktop-{light,dark}.png` |
| E-F7-15 Supplier contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-18-supplier-contracts-e-f07-15-supplier-contract-ended-desktop-{light,dark}.png` |

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
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-07 Supplier agreements and performance](../../flows/fl-f07-07-supplier-agreements-and-performance.md)

## Open questions

None.

---

⬅️ [S-F7-17 Repairs](../06-benchmark-additions/s-f07-17-repairs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-19 Supplier performance](s-f07-19-supplier-performance.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-09 Cash and settlements](README.md) › 🖥️ S-F10-22 Safe and deposits

# 🖥️ S-F10-22 Safe and deposits

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Move cash to the safe, prepare deposits and match them to the bank.

## Entry points

Point of sale › Safe.

## Wireframe

```text
+------------------------------------------------------------------+
| Safe Lyon   expected 2,042.30   counted [2,042.30]  float 200     |
| Move from session 412: 1,842.30  counters [Sophie] [Lea]  [Move]  |
| Deposits   bag 0088  1,842.30  prepared 11-12  bank: matched      |
|            bag 0087  1,610.00  prepared 11-11  bank: waiting      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-09 step 1, U23 | desktop | ![FL-F10-09 step 1, U23, light](../../images/09-cash-and-settlements/u23-store-manager/1-safe-and-deposits-desktop-light.png) | ![FL-F10-09 step 1, U23, dark](../../images/09-cash-and-settlements/u23-store-manager/1-safe-and-deposits-desktop-dark.png) |
| FL-F10-09 step 1, U23 | phone | ![FL-F10-09 step 1, U23, light](../../images/09-cash-and-settlements/u23-store-manager/1-safe-and-deposits-phone-light.png) | ![FL-F10-09 step 1, U23, dark](../../images/09-cash-and-settlements/u23-store-manager/1-safe-and-deposits-phone-dark.png) |
| FL-F10-09 step 1, U23 | tablet | ![FL-F10-09 step 1, U23, light](../../images/09-cash-and-settlements/u23-store-manager/1-safe-and-deposits-tablet-light.png) | ![FL-F10-09 step 1, U23, dark](../../images/09-cash-and-settlements/u23-store-manager/1-safe-and-deposits-tablet-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/09-cash-and-settlements/u23-store-manager/e1-safe-and-deposits-refused-desktop-light.png) | ![Error E1, U23, dark](../../images/09-cash-and-settlements/u23-store-manager/e1-safe-and-deposits-refused-desktop-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/09-cash-and-settlements/u23-store-manager/e1-safe-and-deposits-refused-phone-light.png) | ![Error E1, U23, dark](../../images/09-cash-and-settlements/u23-store-manager/e1-safe-and-deposits-refused-phone-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/09-cash-and-settlements/u23-store-manager/e1-safe-and-deposits-refused-tablet-light.png) | ![Error E1, U23, dark](../../images/09-cash-and-settlements/u23-store-manager/e1-safe-and-deposits-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-22-safe-and-deposits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-22-safe-and-deposits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-22-safe-and-deposits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-22-safe-and-deposits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-22-safe-and-deposits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-22-safe-and-deposits-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-22-safe-and-deposits-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-22-safe-and-deposits-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Expected, counted, moves, deposits | E-F10-17 | counts and moves |

## Actions

| Action | Who | Result |
|---|---|---|
| Move | store manager | Cash in the safe |
| Prepare deposit | store manager | Bag numbered |
| Match | accounting | Bank line matched |

## States

- Normal: move cash to the safe, prepare deposits and match them to the bank.
- Empty: no cash in the safe: "Close a session to move its cash".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: matched deposits.
- Offline: Counts can be entered offline on the store's tablet and are synced; matching to the bank needs the network.

Shown entities (VD-15): [E-F10-02 Till session](../../data/e-f10-02-till-session.md),
[E-F10-17 Cash movement](../../data/e-f10-17-cash-movement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-02 Till session | Open | Badge "Open"; a new record starts here; next: Closing (UC-F10-01); fields editable within the role | U05, U23 | `u05-accounting/s-f10-22-safe-and-deposits-e-f10-02-till-session-open-desktop-{light,dark}.png`, `u23-store-manager/s-f10-22-safe-and-deposits-e-f10-02-till-session-open-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-02 Till session | Closing | Badge "Closing"; next: Closed (UC-F10-01); fields editable within the role | U05, U23 | `u05-accounting/s-f10-22-safe-and-deposits-e-f10-02-till-session-closing-desktop-{light,dark}.png`, `u23-store-manager/s-f10-22-safe-and-deposits-e-f10-02-till-session-closing-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-02 Till session | Closed | Badge "Closed"; next: Posted (UC-F10-01); fields editable within the role | U05, U23 | `u05-accounting/s-f10-22-safe-and-deposits-e-f10-02-till-session-closed-desktop-{light,dark}.png`, `u23-store-manager/s-f10-22-safe-and-deposits-e-f10-02-till-session-closed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-17 Cash movement | Matched | Badge "Matched"; a new record starts here; no other state; fields editable within the role | U05, U23 | `u05-accounting/s-f10-22-safe-and-deposits-e-f10-17-cash-movement-matched-desktop-{light,dark}.png`, `u23-store-manager/s-f10-22-safe-and-deposits-e-f10-17-cash-movement-matched-{desktop,phone,tablet}-{light,dark}.png` |

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
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-09 Cash and settlements](../../flows/fl-f10-09-cash-and-settlements.md)

## Open questions

None.

---

⬅️ [S-F10-21 Age check prompt](../08-vouchers-and-age-checks/s-f10-21-age-check-prompt.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-23 Card settlements](s-f10-23-card-settlements.md)

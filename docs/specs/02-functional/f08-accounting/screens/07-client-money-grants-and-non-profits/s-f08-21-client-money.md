🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-07 Client money, grants and non-profits](README.md) › 🖥️ S-F8-21 Client money

# 🖥️ S-F8-21 Client money

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Record client money movements and see each client's balance and the daily check.

## Entry points

Accounting › Client money.

## Wireframe

```text
+------------------------------------------------------------------+
| Client account  Bank 184,100   Ledgers 184,300   Gap -200 (check)|
| Client          Matter          Balance    Last movement         |
| Landlord Blanc  Mandate 2024-118  742.00   rent paid 11-12       |
| Landlord Roux   Mandate 2023-044  2,410.00 works 11-08           |
|                       [Record movement] [Register PDF]           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-07 step 2, U05 | desktop | ![FL-F8-07 step 2, U05, light](../../images/07-client-money-grants-and-non-profits/u05-accounting/2-client-money-desktop-light.png) | ![FL-F8-07 step 2, U05, dark](../../images/07-client-money-grants-and-non-profits/u05-accounting/2-client-money-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-21-client-money-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-21-client-money-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-21-client-money-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-21-client-money-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-21-client-money-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-21-client-money-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-21-client-money-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-21-client-money-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Client, matter, balance, movements | E-F8-17 | movements |

## Actions

| Action | Who | Result |
|---|---|---|
| Record movement | accounting, property managers | Ledger and bank expected |
| Register | accounting | PDF for the guarantor or the CARPA |

## States

- Normal: record client money movements and see each client's balance and the daily check.
- Empty: no client money yet: "Declare a segregated account first".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed ledgers.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-17 Client money ledger](../../data/e-f08-17-client-money-ledger.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-17 Client money ledger | Open | Badge "Open"; a new record starts here; next: Closed (UC-F8-21); fields editable within the role | U05, U34 | `u05-accounting/s-f08-21-client-money-e-f08-17-client-money-ledger-open-desktop-{light,dark}.png`, `u34-property-manager/s-f08-21-client-money-e-f08-17-client-money-ledger-open-{desktop,tablet}-{light,dark}.png` |
| E-F8-17 Client money ledger | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U05, U34 | `u05-accounting/s-f08-21-client-money-e-f08-17-client-money-ledger-closed-desktop-{light,dark}.png`, `u34-property-manager/s-f08-21-client-money-e-f08-17-client-money-ledger-closed-{desktop,tablet}-{light,dark}.png` |

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

- [FL-F8-07 Client money, grants and non-profits](../../flows/fl-f08-07-client-money-grants-and-non-profits.md)

## Open questions

None.

---

⬅️ [S-F8-20 Profitability](../06-benchmark-additions/s-f08-20-profitability.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-22 Grants](s-f08-22-grants.md)

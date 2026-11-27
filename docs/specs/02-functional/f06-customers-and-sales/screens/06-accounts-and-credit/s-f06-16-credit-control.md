🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-06 Accounts and credit](README.md) › 🖥️ S-F6-16 Credit control

# 🖥️ S-F6-16 Credit control

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Set credit limits and release or keep held orders.

## Entry points

Accounting › Credit control.

## Wireframe

```text
+------------------------------------------------------------------+
| Credit control                               [Held orders: 3]    |
| Customer             Limit    Open     Overdue  Status           |
| Brasserie du Parc    20,000   18,000   0        order held       |
| Café Bellecour       5,000    2,100    45 days  order held       |
| Order 3381  6,000 EUR  [Release with reason] [Ask deposit]       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-06 step 2, U05 | desktop | ![FL-F6-06 step 2, U05, light](../../images/06-accounts-and-credit/u05-accounting/2-credit-control-desktop-light.png) | ![FL-F6-06 step 2, U05, dark](../../images/06-accounts-and-credit/u05-accounting/2-credit-control-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-16-credit-control-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-16-credit-control-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-16-credit-control-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-16-credit-control-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-16-credit-control-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-16-credit-control-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-16-credit-control-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-16-credit-control-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Limit, open, overdue, holds | E-F6-12 | limit, release |

## Actions

| Action | Who | Result |
|---|---|---|
| Release | accounting, owner | Order goes on |
| Ask deposit | accounting | Deposit invoice |

## States

- Normal: set credit limits and release or keep held orders.
- Empty: no limit set: "Orders are not checked against a limit".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for sales: status only.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-12 Credit limit](../../data/e-f06-12-credit-limit.md),
[E-F6-04 Order](../../data/e-f06-04-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-12 Credit limit | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f06-16-credit-control-e-f06-12-credit-limit-active-desktop-{light,dark}.png` |
| E-F6-04 Order | Open | Badge "Open"; a new record starts here; next: In progress or Cancelled (UC-F6-05); fields editable within the role | U05 | `u05-accounting/s-f06-16-credit-control-e-f06-04-order-open-desktop-{light,dark}.png` |

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

- [FL-F6-06 Accounts and credit](../../flows/fl-f06-06-accounts-and-credit.md)

## Open questions

None.

---

⬅️ [S-F6-15 Account](s-f06-15-account.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-17 Funders and caps](../07-special-invoicing/s-f06-17-funders-and-caps.md)

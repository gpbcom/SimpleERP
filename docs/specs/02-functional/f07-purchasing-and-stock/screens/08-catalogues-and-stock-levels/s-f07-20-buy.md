🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-08 Catalogues and stock levels](README.md) › 🖥️ S-F7-20 Buy

# 🖥️ S-F7-20 Buy

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Order from the approved catalogue or a supplier's punch-out site.

## Entry points

My requests › Buy.

## Wireframe

```text
+------------------------------------------------------------------+
| Buy   [search the catalogue]      Punch-out: [Office supplier]   |
| Paper A4 x500   3.20 EUR   [+]                                   |
| Toner HP 305    58.00 EUR  [+]                                   |
| Cart: 10 x paper, 1 x toner = 90.00 EUR  Project [Lyon v] [Send] |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-08 step 1, U01 | desktop | ![FL-F7-08 step 1, U01, light](../../images/08-catalogues-and-stock-levels/u01-employee/1-buy-desktop-light.png) | ![FL-F7-08 step 1, U01, dark](../../images/08-catalogues-and-stock-levels/u01-employee/1-buy-desktop-dark.png) |
| FL-F7-08 step 1, U01 | phone | ![FL-F7-08 step 1, U01, light](../../images/08-catalogues-and-stock-levels/u01-employee/1-buy-phone-light.png) | ![FL-F7-08 step 1, U01, dark](../../images/08-catalogues-and-stock-levels/u01-employee/1-buy-phone-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/08-catalogues-and-stock-levels/u01-employee/e1-buy-refused-desktop-light.png) | ![Error E1, U01, dark](../../images/08-catalogues-and-stock-levels/u01-employee/e1-buy-refused-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/08-catalogues-and-stock-levels/u01-employee/e1-buy-refused-phone-light.png) | ![Error E1, U01, dark](../../images/08-catalogues-and-stock-levels/u01-employee/e1-buy-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-20-buy-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-20-buy-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-20-buy-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-20-buy-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-20-buy-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-20-buy-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-20-buy-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-20-buy-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Items, prices, cart | E-F7-17, E-F7-02 | cart |

## Actions

| Action | Who | Result |
|---|---|---|
| Send | employees | Purchase request to approve |
| Punch-out | employees | Supplier's site |

## States

- Normal: order from the approved catalogue or a supplier's punch-out site.
- Empty: no catalogue for the user's department: "Ask purchasing" with a free request.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for items off contract: shown, not orderable.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F7-17 Approved catalogue](../../data/e-f07-17-approved-catalogue.md),
[E-F7-02 Purchase request](../../data/e-f07-02-purchase-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-17 Approved catalogue | Active | Badge "Active"; a new record starts here; next: Closed (UC-F7-20); fields editable within the role | U01 | `u01-employee/s-f07-20-buy-e-f07-17-approved-catalogue-active-{desktop,phone}-{light,dark}.png` |
| E-F7-17 Approved catalogue | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U01 | `u01-employee/s-f07-20-buy-e-f07-17-approved-catalogue-closed-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F7-20, UC-F7-01); fields editable within the role | U01 | `u01-employee/s-f07-20-buy-e-f07-02-purchase-request-draft-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | To approve | Badge "To approve"; next: Approved or Refused (UC-F7-01); fields editable within the role | U01 | `u01-employee/s-f07-20-buy-e-f07-02-purchase-request-to-approve-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | Approved | Badge "Approved"; next: Ordered or Refused (UC-F7-01); fields editable within the role | U01 | `u01-employee/s-f07-20-buy-e-f07-02-purchase-request-approved-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-08 Catalogues and stock levels](../../flows/fl-f07-08-catalogues-and-stock-levels.md)

## Open questions

None.

---

⬅️ [S-F7-19 Supplier performance](../07-supplier-agreements-and-performance/s-f07-19-supplier-performance.md) ·
⬆️ [Up](README.md) · ➡️ [S-F7-21 Stock levels](../03-replenish/s-f07-21-stock-levels.md)

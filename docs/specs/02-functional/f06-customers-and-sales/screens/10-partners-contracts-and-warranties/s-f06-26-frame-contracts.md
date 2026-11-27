🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F6-26 Frame contracts

# 🖥️ S-F6-26 Frame contracts

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the contracts and every call-off.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own contract's balance and call-offs, on a phone.

## Purpose

Agree a frame contract, call off orders and watch the balance.

## Entry points

Customers and sales › Frame contracts; a customer's record; on a phone, the customer portal › My contract.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Frame contract FC-2027-04  Bois et Fils            Active   2027-01-01 to 2027-12-31         |
|---------------------------------------------------------------------------------------------|
| Committed 1,000 units   Called off 200   Balance 800   Value 9,600 EUR left                 |
| ITEM            AGREED PRICE   COMMITTED   CALLED OFF   BALANCE                             |
| Oak plank 30mm  12.00 EUR      1,000       200          800                                 |
| CALL-OFFS  SO-2310  200 units  2027-02-01  Delivered                                        |
| [Call off] [Extend] [Close]                                                                 |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-10 step 3, U03 | desktop | ![FL-F6-10 step 3, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/3-frame-contracts-desktop-light.png) | ![FL-F6-10 step 3, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/3-frame-contracts-desktop-dark.png) |
| FL-F6-10 step 3, U03 | phone | ![FL-F6-10 step 3, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/3-frame-contracts-phone-light.png) | ![FL-F6-10 step 3, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/3-frame-contracts-phone-dark.png) |
| FL-F6-10 step 3, U03 | tablet | ![FL-F6-10 step 3, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/3-frame-contracts-tablet-light.png) | ![FL-F6-10 step 3, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/3-frame-contracts-tablet-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/e1-a-call-off-is-above-the-contract-desktop-light.png) | ![Error E1, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/e1-a-call-off-is-above-the-contract-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/e1-a-call-off-is-above-the-contract-phone-light.png) | ![Error E1, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/e1-a-call-off-is-above-the-contract-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/e1-a-call-off-is-above-the-contract-tablet-light.png) | ![Error E1, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/e1-a-call-off-is-above-the-contract-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-26-frame-contracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-26-frame-contracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-26-frame-contracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-26-frame-contracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-26-frame-contracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-26-frame-contracts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-26-frame-contracts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-26-frame-contracts-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contract | E-F6-25 | number and customer | no | yes |
| Validity | E-F6-25 from, to | two dates | yes while Draft | yes |
| Item and agreed price | E-F6-25 lines | table | yes while Draft | yes |
| Committed, called off, balance | E-F6-25 | three numbers | no | yes |
| Call-offs | E-F6-04 | list of orders | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Call off | header | sales, customer | an order at the agreed price, within the balance |
| Approve above balance | call-off | sales | the call-off goes on at the agreed or list price |
| Extend | header | sales | validity or commitment changed with the customer's agreement |
| Close | header | sales | the contract ends; the unused commitment is reported |

## States

- Normal: the contract's lines with their balance and the list of call-offs.
- Empty: No frame contract yet, with New frame contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  call-off shows the item, the balance and the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-25 Frame contract](../../data/e-f06-25-frame-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-25 Frame contract | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F6-29); fields editable within the role | U03, U09 | `u03-sales/s-f06-26-frame-contracts-e-f06-25-frame-contract-draft-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-26-frame-contracts-e-f06-25-frame-contract-draft-phone-{light,dark}.png` |
| E-F6-25 Frame contract | Active | Badge "Active"; next: Exhausted, Expired or Closed (BR-F6-21, UC-F6-29); fields editable within the role | U03, U09 | `u03-sales/s-f06-26-frame-contracts-e-f06-25-frame-contract-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-26-frame-contracts-e-f06-25-frame-contract-active-phone-{light,dark}.png` |
| E-F6-25 Frame contract | Exhausted | Badge "Exhausted"; next: Closed (UC-F6-29); fields editable within the role | U03, U09 | `u03-sales/s-f06-26-frame-contracts-e-f06-25-frame-contract-exhausted-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-26-frame-contracts-e-f06-25-frame-contract-exhausted-phone-{light,dark}.png` |
| E-F6-25 Frame contract | Expired | Badge "Expired"; next: Closed (UC-F6-29); fields editable within the role | U03, U09 | `u03-sales/s-f06-26-frame-contracts-e-f06-25-frame-contract-expired-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-26-frame-contracts-e-f06-25-frame-contract-expired-phone-{light,dark}.png` |
| E-F6-25 Frame contract | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-f06-26-frame-contracts-e-f06-25-frame-contract-closed-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f06-26-frame-contracts-e-f06-25-frame-contract-closed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The customer's call-off is built for a phone: the balance on top, then a short form with the contract's items. Sales'
screen is desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-10](../../flows/fl-f06-10-partners-contracts-and-warranties.md)

## Open questions

None.

---

⬅️ [S-F6-25 Company identifiers](s-f06-25-company-identifiers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-27 Solvency check](s-f06-27-solvency-check.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-02 Packages and memberships](README.md) › 🖥️ S-SC17-07 Gift vouchers

# 🖥️ S-SC17-07 Gift vouchers

**Status:** 🔄 waiting for the owner

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the vouchers they sell and redeem.

## Purpose

Sell a voucher, read its balance and redeem it at the till.

## Entry points

Beauty and wellness › Gift vouchers; the till; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Gift vouchers                                                          [Sell a voucher]          |
| Code      Kind      Value    Balance   Valid to      State                                       |
| G-4471    amount    50.00    18.00     2027-11-21    Partly used                                 |
| G-4502    Facial    55.00    55.00     2027-11-30    Issued                                      |
| Code [ G-4471 ]  [Read]    Redeem  [ 18.00 ]  [Apply to the sale]                                |
| Unused vouchers at the month end: 1,240.00 EUR                                                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-02 step 3, U52 | tablet | ![FL-SC17-02 step 3, U52, light](../../images/02-packages-and-memberships/u52-beautician/3-gift-vouchers-tablet-light.png) | ![FL-SC17-02 step 3, U52, dark](../../images/02-packages-and-memberships/u52-beautician/3-gift-vouchers-tablet-dark.png) |
| FL-SC17-02 step 3, U52 | phone | ![FL-SC17-02 step 3, U52, light](../../images/02-packages-and-memberships/u52-beautician/3-gift-vouchers-phone-light.png) | ![FL-SC17-02 step 3, U52, dark](../../images/02-packages-and-memberships/u52-beautician/3-gift-vouchers-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-07-gift-vouchers-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-07-gift-vouchers-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-07-gift-vouchers-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-07-gift-vouchers-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-07-gift-vouchers-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-07-gift-vouchers-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-07-gift-vouchers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-07-gift-vouchers-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Code | E-SC17-06 code | text | no | yes |
| Kind | E-SC17-06 kind | amount or service | yes while Issued | yes |
| Value | E-SC17-06 value | amount | no | yes |
| Balance | E-SC17-06 balance | amount | no | no |
| Valid to | E-SC17-06 valid to | date | yes while Issued | yes |
| Buyer and holder | E-SC17-06 buyer | customer names | yes while Issued | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sell a voucher | header | beautician | a voucher is created Issued |
| Apply to the sale | footer | beautician | the balance is reduced and the voucher is Partly used or Redeemed |
| Extend | voucher row | manager | a new end date with a reason |
| Block | voucher row | manager | the voucher becomes Cancelled |

## States

- Normal: the vouchers with their value, balance, end date and state.
- Empty: No voucher yet, with Sell a voucher.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unknown,
  used-up or expired code, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-06 Gift voucher](../../data/e-sc17-06-gift-voucher.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-06 Gift voucher | Issued | Badge "Issued"; a new record starts here; next: Partly used, Redeemed, Expired or Cancelled (UC-SC17-07, BR-SC17-07); fields editable within the role | U52 | `u52-beautician/s-sc17-07-gift-vouchers-e-sc17-06-gift-voucher-issued-{phone,tablet}-{light,dark}.png` |
| E-SC17-06 Gift voucher | Partly used | Badge "Partly used"; next: Redeemed or Expired (UC-SC17-07, BR-SC17-07); fields editable within the role | U52 | `u52-beautician/s-sc17-07-gift-vouchers-e-sc17-06-gift-voucher-partly-used-{phone,tablet}-{light,dark}.png` |
| E-SC17-06 Gift voucher | Redeemed | Badge "Redeemed"; final: read-only, no next state; the history shows how it got here | U52 | `u52-beautician/s-sc17-07-gift-vouchers-e-sc17-06-gift-voucher-redeemed-{phone,tablet}-{light,dark}.png` |
| E-SC17-06 Gift voucher | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U52 | `u52-beautician/s-sc17-07-gift-vouchers-e-sc17-06-gift-voucher-expired-{phone,tablet}-{light,dark}.png` |
| E-SC17-06 Gift voucher | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U52 | `u52-beautician/s-sc17-07-gift-vouchers-e-sc17-06-gift-voucher-cancelled-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The beautician works on the tablet at the chair, the manager on a desktop and the customer on a phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-02 Packages and memberships](../../flows/fl-sc17-02-packages-and-memberships.md)

## Open questions

None.

---

⬅️ [S-SC17-06 Salon memberships](s-sc17-06-salon-memberships.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-08 Customer balances](s-sc17-08-customer-balances.md)

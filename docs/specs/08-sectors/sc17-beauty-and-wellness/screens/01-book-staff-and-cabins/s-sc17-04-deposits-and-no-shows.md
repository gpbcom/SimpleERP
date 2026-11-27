🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-01 Book staff and cabins](README.md) ›
🖥️ S-SC17-04 Deposits and no-shows

# 🖥️ S-SC17-04 Deposits and no-shows

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the terms and the deposits to settle.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own deposits and receipts.

## Purpose

Set the deposit and no-show terms, see the deposits to settle and keep or refund each one.

## Entry points

Beauty and wellness › Booking deposits; a booking's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Deposits: Rue Verte salon                                     No-show rate this month 4%         |
| Terms  Deposit 10.00 EUR on services over 45 min   Free cancellation 24 hours   Fee 20.00 EUR    |
| Booking     Customer     Deposit   State       Visit                                             |
| B-2026-210  Camille R.   10.00     Paid        2026-11-21                                        |
| B-2026-198  Noor A.      10.00     Kept        2026-11-14 no show                                |
| [Keep]  [Refund]  [Waive the fee]                                                                |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-01 step 4, U23 | desktop | ![FL-SC17-01 step 4, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/4-deposits-and-no-shows-desktop-light.png) | ![FL-SC17-01 step 4, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/4-deposits-and-no-shows-desktop-dark.png) |
| FL-SC17-01 step 4, U23 | phone | ![FL-SC17-01 step 4, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/4-deposits-and-no-shows-phone-light.png) | ![FL-SC17-01 step 4, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/4-deposits-and-no-shows-phone-dark.png) |
| FL-SC17-01 step 4, U23 | tablet | ![FL-SC17-01 step 4, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/4-deposits-and-no-shows-tablet-light.png) | ![FL-SC17-01 step 4, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/4-deposits-and-no-shows-tablet-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/e1-the-customer-did-not-come-desktop-light.png) | ![Error E1, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/e1-the-customer-did-not-come-desktop-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/e1-the-customer-did-not-come-phone-light.png) | ![Error E1, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/e1-the-customer-did-not-come-phone-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/01-book-staff-and-cabins/u23-store-manager/e1-the-customer-did-not-come-tablet-light.png) | ![Error E1, U23, dark](../../images/01-book-staff-and-cabins/u23-store-manager/e1-the-customer-did-not-come-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-04-deposits-and-no-shows-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-04-deposits-and-no-shows-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-04-deposits-and-no-shows-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-04-deposits-and-no-shows-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-04-deposits-and-no-shows-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-04-deposits-and-no-shows-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-04-deposits-and-no-shows-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-04-deposits-and-no-shows-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Booking | E-SC17-03 booking | link | no | yes |
| Amount | E-SC17-03 amount | amount | yes while Requested | yes |
| State | E-SC17-03 state | badge | no | no |
| Terms shown on | E-SC17-03 terms shown on | date and time | no | no |
| Fee | E-SC17-03 fee | amount | yes while Paid | no |
| Waiver reason | E-SC17-03 waiver reason | text | yes while Kept | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Request deposit | booking | beautician | a deposit is Requested and the payment link sent |
| Keep | deposit row | manager | the deposit becomes Kept |
| Refund | deposit row | manager | the deposit becomes Refunded |
| Apply to the bill | till | beautician | the deposit becomes Applied |

## States

- Normal: the terms, the deposits with their state and the no-show rate.
- Empty: No deposit yet, with the terms to set.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a fee with no
  terms shown, or a failed refund, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-03 Booking deposit](../../data/e-sc17-03-booking-deposit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-03 Booking deposit | Requested | Badge "Requested"; a new record starts here; next: Paid or Expired (UC-SC17-02, BR-SC17-02); fields editable within the role | U23, U09 | `u23-store-manager/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-requested-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-requested-phone-{light,dark}.png` |
| E-SC17-03 Booking deposit | Paid | Badge "Paid"; next: Applied, Kept or Refunded (UC-SC17-04, BR-SC17-04); fields editable within the role | U23, U09 | `u23-store-manager/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-paid-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-paid-phone-{light,dark}.png` |
| E-SC17-03 Booking deposit | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-expired-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-expired-phone-{light,dark}.png` |
| E-SC17-03 Booking deposit | Applied | Badge "Applied"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-applied-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-applied-phone-{light,dark}.png` |
| E-SC17-03 Booking deposit | Kept | Badge "Kept"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-kept-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-kept-phone-{light,dark}.png` |
| E-SC17-03 Booking deposit | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U23, U09 | `u23-store-manager/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-refunded-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc17-04-deposits-and-no-shows-e-sc17-03-booking-deposit-refunded-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; the customer sees their own deposits on a phone.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-01 Book staff and cabins](../../flows/fl-sc17-01-book-staff-and-cabins.md)

## Open questions

None.

---

⬅️ [S-SC17-03 Desk booking](s-sc17-03-desk-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-05 Packages](../02-packages-and-memberships/s-sc17-05-packages.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-06 Care homes, CESU, agent mode, childcare and nursing](README.md) ›
🖥️ S-SC04-17 CESU

# 🖥️ S-SC04-17 CESU

**Status:** 🔄 waiting for the owner

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md): every voucher, batch and reimbursement.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own vouchers and invoices.

## Purpose

Record vouchers against invoices, send them in batches and reconcile the issuer's payments.

## Entry points

Home care › CESU vouchers; the invoice's Payments tab; the customer portal for the customer.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Batch B-2026-11-02 to issuer CESU-Est                              Sent   [Reconcile]            |
| Vouchers 18   Face value 432.00 EUR   Sent 2026-11-10   Paid 420.00 EUR on 2026-11-13            |
| Voucher       Value    Invoice      State                                                        |
| CS-884120     12.00    2026-441     Reimbursed                                                   |
| CS-884077     12.00    2026-436     REJECTED: expired 2026-09-30                                 |
| Difference 12.00 EUR   [Correct and resend] [Ask the issuer]                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-06 step 2, U25 | desktop | ![FL-SC04-06 step 2, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/2-cesu-desktop-light.png) | ![FL-SC04-06 step 2, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/2-cesu-desktop-dark.png) |
| FL-SC04-06 step 2, U25 | phone | ![FL-SC04-06 step 2, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/2-cesu-phone-light.png) | ![FL-SC04-06 step 2, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/2-cesu-phone-dark.png) |
| Error E1, U25 | desktop | ![Error E1, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/e1-the-voucher-is-rejected-desktop-light.png) | ![Error E1, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/e1-the-voucher-is-rejected-desktop-dark.png) |
| Error E1, U25 | phone | ![Error E1, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/e1-the-voucher-is-rejected-phone-light.png) | ![Error E1, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/e1-the-voucher-is-rejected-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-17-cesu-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-17-cesu-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-17-cesu-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-17-cesu-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-17-cesu-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-17-cesu-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-17-cesu-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-17-cesu-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Voucher number | E-SC04-15 number | text | yes while Received | yes |
| Issuer and face value | E-SC04-15 issuer, value | text and amount | yes while Received | yes |
| Invoice | E-SC04-15 invoice | link | yes while Received | yes |
| Valid to | E-SC04-15 valid to | date | yes while Received | yes |
| Batch and dates | E-SC04-15 batch, sent on, paid on | text and dates | no | no |
| Rejection reason | E-SC04-15 reason | text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add voucher | invoice | coordinator, customer | the voucher is checked and accepted |
| Send batch | header | coordinator | the vouchers become Sent |
| Reconcile | batch | coordinator | each voucher becomes Reimbursed or Rejected |
| Correct and resend | voucher | coordinator | the voucher is Sent again in a later batch |

## States

- Normal: the batch with each voucher, its invoice, its state and the difference with the payment.
- Empty: No voucher yet, with Add a voucher.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an expired or
  used voucher, or a difference with the issuer, with the voucher and the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC04-15 CESU voucher](../../data/e-sc04-15-cesu-voucher.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-15 CESU voucher | Received | Badge "Received"; a new record starts here; next: Sent (UC-SC04-17); fields editable within the role | U25, U09 | `u25-care-coordinator/s-sc04-17-cesu-e-sc04-15-cesu-voucher-received-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-17-cesu-e-sc04-15-cesu-voucher-received-phone-{light,dark}.png` |
| E-SC04-15 CESU voucher | Sent | Badge "Sent"; next: Reimbursed or Rejected (BR-SC04-17); fields editable within the role | U25, U09 | `u25-care-coordinator/s-sc04-17-cesu-e-sc04-15-cesu-voucher-sent-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-17-cesu-e-sc04-15-cesu-voucher-sent-phone-{light,dark}.png` |
| E-SC04-15 CESU voucher | Reimbursed | Badge "Reimbursed"; final: read-only, no next state; the history shows how it got here | U25, U09 | `u25-care-coordinator/s-sc04-17-cesu-e-sc04-15-cesu-voucher-reimbursed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-17-cesu-e-sc04-15-cesu-voucher-reimbursed-phone-{light,dark}.png` |
| E-SC04-15 CESU voucher | Rejected | Badge "Rejected"; next: Sent (UC-SC04-17); fields editable within the role | U25, U09 | `u25-care-coordinator/s-sc04-17-cesu-e-sc04-15-cesu-voucher-rejected-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-17-cesu-e-sc04-15-cesu-voucher-rejected-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the carer and the family use the phone, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC04-06](../../flows/fl-sc04-06-care-homes-cesu-and-nursing.md)

## Open questions

None.

---

⬅️ [S-SC04-16 Care home](s-sc04-16-care-home.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-18 Agent mode](s-sc04-18-agent-mode.md)

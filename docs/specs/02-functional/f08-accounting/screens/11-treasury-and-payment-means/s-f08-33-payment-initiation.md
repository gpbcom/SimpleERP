🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-33 Payment initiation

# 🖥️ S-F8-33 Payment initiation

**Status:** 🔄 waiting for the owner

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the payment orders they prepare and authorise.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the orders waiting for their approval, on a phone.

## Purpose

Build payment orders from approved bills, approve them and send them to the bank.

## Entry points

Accounting › Pay suppliers; the approval notification on a phone.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Payment initiation: run of 2026-11-14       14 orders   62,000 EUR     Awaiting approval 3   |
|---------------------------------------------------------------------------------------------|
| SUPPLIER            AMOUNT    IBAN CHECK   APPROVALS         STATE                          |
| Menuiserie Dupont   18,000    checked      1 of 2 (Claire)   Awaiting approval              |
| Quincaillerie Sud   1,240     checked      1 of 1            Approved                       |
| Limit for one approval: 10,000 EUR                                                           |
| [Approve] [Authorise with the bank] [Send] [Cancel]                                          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-11 step 5, U31 | desktop | ![FL-F8-11 step 5, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/5-payment-initiation-desktop-light.png) | ![FL-F8-11 step 5, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/5-payment-initiation-desktop-dark.png) |
| FL-F8-11 step 5, U31 | phone | ![FL-F8-11 step 5, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/5-payment-initiation-phone-light.png) | ![FL-F8-11 step 5, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/5-payment-initiation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-33-payment-initiation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-33-payment-initiation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-33-payment-initiation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-33-payment-initiation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-33-payment-initiation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-33-payment-initiation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-33-payment-initiation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-33-payment-initiation-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Supplier and bill | E-F8-38 | text and link | no | yes |
| Amount and execution date | E-F8-38 | amount and date | yes while Draft | yes |
| IBAN and check | E-F7-01 | text and badge | no | yes |
| Approvals | E-F8-38 | names and times | no | yes |
| State | E-F8-38 | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve | row, phone | approver | an approval is recorded; above the limit a second approver is needed |
| Authorise with the bank | header | treasurer | the bank's strong authentication |
| Send | header | treasurer | the approved and authorised orders go to the bank |
| Cancel | row | treasurer | the order is cancelled before execution |

## States

- Normal: the orders with their IBAN check, approvals and state, and the limit.
- Empty: No bill to pay, with Open the bills.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a bank
  rejection shows the bank's reason on the order.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-38 Payment order](../../data/e-f08-38-payment-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-38 Payment order | Draft | Badge "Draft"; a new record starts here; next: Awaiting approval or Cancelled (BR-F8-26, UC-F8-34); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-draft-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-draft-{desktop,phone}-{light,dark}.png` |
| E-F8-38 Payment order | Awaiting approval | Badge "Awaiting approval"; next: Approved or Cancelled (BR-F8-26, UC-F8-34); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-awaiting-approval-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-awaiting-approval-{desktop,phone}-{light,dark}.png` |
| E-F8-38 Payment order | Approved | Badge "Approved"; next: Sent or Cancelled (UC-F8-34); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-approved-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-approved-{desktop,phone}-{light,dark}.png` |
| E-F8-38 Payment order | Sent | Badge "Sent"; next: Executed or Rejected (UC-F8-34); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-sent-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-sent-{desktop,phone}-{light,dark}.png` |
| E-F8-38 Payment order | Executed | Badge "Executed"; final: read-only, no next state; the history shows how it got here | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-executed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-executed-{desktop,phone}-{light,dark}.png` |
| E-F8-38 Payment order | Rejected | Badge "Rejected"; next: Draft (UC-F8-34); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-rejected-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-rejected-{desktop,phone}-{light,dark}.png` |
| E-F8-38 Payment order | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U31, U13 | `u31-treasurer/s-f08-33-payment-initiation-e-f08-38-payment-order-cancelled-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-33-payment-initiation-e-f08-38-payment-order-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The owner approves on a phone: the supplier, the amount, the reason and the first approver on one card, with Approve or
Refuse. The treasurer's screen is desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-11 Treasury and payment means](../../flows/fl-f08-11-treasury-and-payment-means.md)

## Open questions

None.

---

⬅️ [S-F8-32 Cash position](s-f08-32-cash-position.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-34 Recurring entries](s-f08-34-recurring-entries.md)

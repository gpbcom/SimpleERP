🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-02 Purchase to pay](README.md) ›
🖥️ S-F8-04 Supplier payments

# 🖥️ S-F8-04 Supplier payments

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Pay suppliers.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-02 step 2, U05 | desktop | ![FL-F8-02 step 2, U05, light](../../images/02-purchase-to-pay/u05-accounting/2-pay-suppliers-desktop-light.png) | ![FL-F8-02 step 2, U05, dark](../../images/02-purchase-to-pay/u05-accounting/2-pay-suppliers-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/02-purchase-to-pay/u05-accounting/e1-iban-changed-desktop-light.png) | ![Error E1, U05, dark](../../images/02-purchase-to-pay/u05-accounting/e1-iban-changed-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/09-pay-analyse-and-report/u05-accounting/e1-supplier-payments-refused-desktop-light.png) | ![Error E1, U05, dark](../../images/09-pay-analyse-and-report/u05-accounting/e1-supplier-payments-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-04-supplier-payments-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-04-supplier-payments-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-04-supplier-payments-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-04-supplier-payments-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-04-supplier-payments-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-04-supplier-payments-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-04-supplier-payments-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-04-supplier-payments-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Pay suppliers, as the wireframe shows.
- Empty: No bill due yet for the period, with Nothing to pay.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-28 Payment run](../../data/e-f08-28-payment-run.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-28 Payment run | Active | Badge "Active"; a new record starts here; next: Waiting for a check or Approved (BR-F8-08, UC-F8-04); fields editable within the role | U05, U13 | `u05-accounting/s-f08-04-supplier-payments-e-f08-28-payment-run-active-desktop-{light,dark}.png`, `u13-owner/s-f08-04-supplier-payments-e-f08-28-payment-run-active-{desktop,phone}-{light,dark}.png` |
| E-F8-28 Payment run | Waiting for a check | Badge "Waiting for a check"; next: Active (BR-F8-08); fields editable within the role | U05, U13 | `u05-accounting/s-f08-04-supplier-payments-e-f08-28-payment-run-waiting-for-a-check-desktop-{light,dark}.png`, `u13-owner/s-f08-04-supplier-payments-e-f08-28-payment-run-waiting-for-a-check-{desktop,phone}-{light,dark}.png` |
| E-F8-28 Payment run | Approved | Badge "Approved"; next: Sent (UC-F8-04); fields editable within the role | U05, U13 | `u05-accounting/s-f08-04-supplier-payments-e-f08-28-payment-run-approved-desktop-{light,dark}.png`, `u13-owner/s-f08-04-supplier-payments-e-f08-28-payment-run-approved-{desktop,phone}-{light,dark}.png` |
| E-F8-28 Payment run | Sent | Badge "Sent"; next: Paid or Refused (UC-F8-06, UC-F8-04); fields editable within the role | U05, U13 | `u05-accounting/s-f08-04-supplier-payments-e-f08-28-payment-run-sent-desktop-{light,dark}.png`, `u13-owner/s-f08-04-supplier-payments-e-f08-28-payment-run-sent-{desktop,phone}-{light,dark}.png` |
| E-F8-28 Payment run | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f08-04-supplier-payments-e-f08-28-payment-run-paid-desktop-{light,dark}.png`, `u13-owner/s-f08-04-supplier-payments-e-f08-28-payment-run-paid-{desktop,phone}-{light,dark}.png` |
| E-F8-28 Payment run | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f08-04-supplier-payments-e-f08-28-payment-run-refused-desktop-{light,dark}.png`, `u13-owner/s-f08-04-supplier-payments-e-f08-28-payment-run-refused-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F8-02 Purchase to pay](../../flows/fl-f08-02-purchase-to-pay.md)
- [FL-F8-09 Pay, analyse and report](../../flows/fl-f08-09-pay-analyse-and-report.md)

## Open questions

None.

---

⬅️ [S-F8-03 Supplier bills](s-f08-03-supplier-bills.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-05 Customer payments](../03-bank-and-collect/s-f08-05-customer-payments.md)

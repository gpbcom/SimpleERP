🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-03 Bank and collect](README.md) ›
🖥️ S-F8-05 Customer payments

# 🖥️ S-F8-05 Customer payments

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Collect customer payments.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-03 step 1, U05 | desktop | ![FL-F8-03 step 1, U05, light](../../images/03-bank-and-collect/u05-accounting/1-collect-payments-desktop-light.png) | ![FL-F8-03 step 1, U05, dark](../../images/03-bank-and-collect/u05-accounting/1-collect-payments-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-05-customer-payments-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-05-customer-payments-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-05-customer-payments-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-05-customer-payments-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-05-customer-payments-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-05-customer-payments-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-05-customer-payments-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-05-customer-payments-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Collect customer payments, as the wireframe shows.
- Empty: No customer payment yet for the period, with Import a statement.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-04 Bank line](../../data/e-f08-04-bank-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-04 Bank line | To reconcile | Badge "To reconcile"; a new record starts here; next: Reconciled (UC-F8-04); fields editable within the role | U05 | `u05-accounting/s-f08-05-customer-payments-e-f08-04-bank-line-to-reconcile-desktop-{light,dark}.png` |

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

- [FL-F8-03 Bank and collect](../../flows/fl-f08-03-bank-and-collect.md)

## Open questions

None.

---

⬅️ [S-F8-04 Supplier payments](../02-purchase-to-pay/s-f08-04-supplier-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-06 Bank reconciliation](s-f08-06-bank-reconciliation.md)

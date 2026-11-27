🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-03 Bank and collect](README.md) ›
🖥️ S-F8-06 Bank reconciliation

# 🖥️ S-F8-06 Bank reconciliation

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Connect banks and reconcile.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-03 step 2, U05 | desktop | ![FL-F8-03 step 2, U05, light](../../images/03-bank-and-collect/u05-accounting/2-reconcile-desktop-light.png) | ![FL-F8-03 step 2, U05, dark](../../images/03-bank-and-collect/u05-accounting/2-reconcile-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-06-bank-reconciliation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-06-bank-reconciliation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-06-bank-reconciliation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-06-bank-reconciliation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-06-bank-reconciliation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-06-bank-reconciliation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-06-bank-reconciliation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-06-bank-reconciliation-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Connect banks and reconcile, as the wireframe shows.
- Empty: No bank account connected yet for the period, with Connect a bank.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-04 Bank line](../../data/e-f08-04-bank-line.md),
[E-F8-05 Reconciliation model](../../data/e-f08-05-reconciliation-model.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-04 Bank line | To reconcile | Badge "To reconcile"; a new record starts here; next: Reconciled (UC-F8-04); fields editable within the role | U05 | `u05-accounting/s-f08-06-bank-reconciliation-e-f08-04-bank-line-to-reconcile-desktop-{light,dark}.png` |
| E-F8-04 Bank line | Reconciled | Badge "Reconciled"; next: In suspense (BR-F8-03); fields editable within the role | U05 | `u05-accounting/s-f08-06-bank-reconciliation-e-f08-04-bank-line-reconciled-desktop-{light,dark}.png` |
| E-F8-04 Bank line | In suspense | Badge "In suspense"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-06-bank-reconciliation-e-f08-04-bank-line-in-suspense-desktop-{light,dark}.png` |
| E-F8-05 Reconciliation model | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f08-06-bank-reconciliation-e-f08-05-reconciliation-model-active-desktop-{light,dark}.png` |

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

⬅️ [S-F8-05 Customer payments](s-f08-05-customer-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-07 VAT returns](../04-tax-assets-and-analytics/s-f08-07-vat-returns.md)

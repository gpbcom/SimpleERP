🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-05 Billing](README.md) › 🖥️ S-F22-16 Client re-billing

# 🖥️ S-F22-16 Client re-billing

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Re-bill clients as an IT provider.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-05 step 2, U11 | desktop | ![FL-F22-05 step 2, U11, light](../../images/05-billing/u11-provider-admin/2-re-billing-desktop-light.png) | ![FL-F22-05 step 2, U11, dark](../../images/05-billing/u11-provider-admin/2-re-billing-desktop-dark.png) |
| Error E1, U11 | desktop | ![Error E1, U11, light](../../images/05-billing/u11-provider-admin/e1-no-contract-desktop-light.png) | ![Error E1, U11, dark](../../images/05-billing/u11-provider-admin/e1-no-contract-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-16-client-re-billing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-16-client-re-billing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-16-client-re-billing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-16-client-re-billing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-16-client-re-billing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-16-client-re-billing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-16-client-re-billing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-16-client-re-billing-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: clients with amounts and invoices.
- Empty: "No client".
- Loading: the frame and titles show at once with placeholder rows for the clients; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: clients read their own.
- Offline: not available offline: invoicing runs online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F22-13 Usage invoice](../../data/e-f22-13-usage-invoice.md),
[E-F22-17 Re-billing rule](../../data/e-f22-17-re-billing-rule.md),
[E-F22-18 Client usage statement](../../data/e-f22-18-client-usage-statement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-13 Usage invoice | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U11 | `u11-provider-admin/s-f22-16-client-re-billing-e-f22-13-usage-invoice-recorded-desktop-{light,dark}.png` |
| E-F22-17 Re-billing rule | Active | Badge "Active"; a new record starts here; next: Changed (UC-F22-25); fields editable within the role | U11 | `u11-provider-admin/s-f22-16-client-re-billing-e-f22-17-re-billing-rule-active-desktop-{light,dark}.png` |
| E-F22-17 Re-billing rule | Changed | Badge "Changed"; next: Active (UC-F22-16); fields editable within the role | U11 | `u11-provider-admin/s-f22-16-client-re-billing-e-f22-17-re-billing-rule-changed-desktop-{light,dark}.png` |
| E-F22-18 Client usage statement | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F22-26); fields editable within the role | U11 | `u11-provider-admin/s-f22-16-client-re-billing-e-f22-18-client-usage-statement-draft-desktop-{light,dark}.png` |
| E-F22-18 Client usage statement | Sent | Badge "Sent"; next: Invoiced (UC-F22-26); fields editable within the role | U11 | `u11-provider-admin/s-f22-16-client-re-billing-e-f22-18-client-usage-statement-sent-desktop-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-05 Billing](../../flows/fl-f22-05-billing.md)

## Open questions

None.

---

⬅️ [S-F22-15 Hosted usage](s-f22-15-hosted-usage.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-17 Platform costs](s-f22-17-platform-costs.md)

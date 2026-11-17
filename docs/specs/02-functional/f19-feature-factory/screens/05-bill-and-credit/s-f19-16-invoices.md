🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-05 Bill and credit](README.md) › 🖥️ S-F19-16 Invoices

# 🖥️ S-F19-16 Invoices

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Invoice features with the right VAT.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-05 step 2, U05 | desktop | ![FL-F19-05 step 2, U05, light](../../images/05-bill-and-credit/u05-accounting/2-invoice-desktop-light.png) | ![FL-F19-05 step 2, U05, dark](../../images/05-bill-and-credit/u05-accounting/2-invoice-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-16-invoices-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-16-invoices-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-16-invoices-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-16-invoices-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-16-invoices-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-16-invoices-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f19-16-invoices-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f19-16-invoices-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: invoices with VAT and e-invoicing state.
- Empty: "No invoice yet".
- Loading: the frame and titles show at once with placeholder rows for the invoices; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: issued invoices are read-only.
- Offline: not available offline: invoices are sent online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-09 Hosted invoice](../../data/e-f19-09-hosted-invoice.md),
[E-F19-15 Factory posting](../../data/e-f19-15-factory-posting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-09 Hosted invoice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f19-16-invoices-e-f19-09-hosted-invoice-active-desktop-{light,dark}.png` |
| E-F19-15 Factory posting | Prepared | Badge "Prepared"; a new record starts here; next: Posted (UC-F19-15); fields editable within the role | U05 | `u05-accounting/s-f19-16-invoices-e-f19-15-factory-posting-prepared-desktop-{light,dark}.png` |

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

- [FL-F19-05 Bill and credit](../../flows/fl-f19-05-bill-and-credit.md)

## Open questions

None.

---

⬅️ [S-F19-15 Credits](s-f19-15-credits.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-17 Compatibility](../02-build-and-check/s-f19-17-compatibility.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F7-01 Procure](README.md) ›
🖥️ S-F7-04 Supplier invoice matching

# 🖥️ S-F7-04 Supplier invoice matching

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Capture and match supplier invoices.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-01 step 3, U05 | desktop | ![FL-F7-01 step 3, U05, light](../../images/01-procure/u05-accounting/3-match-invoice-desktop-light.png) | ![FL-F7-01 step 3, U05, dark](../../images/01-procure/u05-accounting/3-match-invoice-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-04-supplier-invoice-matching-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-04-supplier-invoice-matching-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-04-supplier-invoice-matching-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-04-supplier-invoice-matching-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-04-supplier-invoice-matching-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-04-supplier-invoice-matching-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-04-supplier-invoice-matching-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-04-supplier-invoice-matching-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Capture and match supplier invoices, as the wireframe shows.
- Empty: No supplier invoice to match yet, with Upload invoices.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-03 Purchase order](../../data/e-f07-03-purchase-order.md),
[E-F7-05 Supplier invoice](../../data/e-f07-05-supplier-invoice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-03 Purchase order | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F7-02); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-03-purchase-order-draft-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Sent | Badge "Sent"; next: Confirmed (UC-F7-02); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-03-purchase-order-sent-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Confirmed | Badge "Confirmed"; next: Received (UC-F7-04); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-03-purchase-order-confirmed-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Received | Badge "Received"; next: Billed (UC-F7-01); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-03-purchase-order-received-desktop-{light,dark}.png` |
| E-F7-03 Purchase order | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-03-purchase-order-billed-desktop-{light,dark}.png` |
| E-F7-05 Supplier invoice | Received | Badge "Received"; a new record starts here; next: Matched (UC-F7-04); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-05-supplier-invoice-received-desktop-{light,dark}.png` |
| E-F7-05 Supplier invoice | Matched | Badge "Matched"; next: Sent to accounting or Held (BR-F7-03, UC-F7-04); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-05-supplier-invoice-matched-desktop-{light,dark}.png` |
| E-F7-05 Supplier invoice | Held | Badge "Held"; next: Sent to accounting (BR-F7-03); fields editable within the role | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-05-supplier-invoice-held-desktop-{light,dark}.png` |
| E-F7-05 Supplier invoice | Sent to accounting | Badge "Sent to accounting"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f07-04-supplier-invoice-matching-e-f07-05-supplier-invoice-sent-to-accounting-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; receipts, picking and counts on phones, offline.

## Accessibility

Labelled controls; quantities and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F7-01 Procure](../../flows/fl-f07-01-procure.md)

## Open questions

None.

---

⬅️ [S-F7-03 Receipt](../02-receive-and-store/s-f07-03-receipt.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-05 Replenishment](../03-replenish/s-f07-05-replenishment.md)

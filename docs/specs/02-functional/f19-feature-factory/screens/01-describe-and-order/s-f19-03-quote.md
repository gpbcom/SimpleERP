🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-01 Describe and order](README.md) › 🖥️ S-F19-03 Quote

# 🖥️ S-F19-03 Quote

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Accept the quote.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-01 step 3, U13 | desktop | ![FL-F19-01 step 3, U13, light](../../images/01-describe-and-order/u13-owner/3-quote-desktop-light.png) | ![FL-F19-01 step 3, U13, dark](../../images/01-describe-and-order/u13-owner/3-quote-desktop-dark.png) |
| FL-F19-01 step 3, U13 | phone | ![FL-F19-01 step 3, U13, light](../../images/01-describe-and-order/u13-owner/3-quote-phone-light.png) | ![FL-F19-01 step 3, U13, dark](../../images/01-describe-and-order/u13-owner/3-quote-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-03-quote-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-03-quote-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-03-quote-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-03-quote-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-03-quote-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-03-quote-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-03-quote-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-03-quote-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the quote with price, VAT, delivery date and spending limit.
- Empty: never empty: it opens from an approved specification.
- Loading: the frame and titles show at once with placeholder rows for the quote; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: administrators accept within the limit; above it, the owner.
- Offline: not available offline: acceptance needs the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-11 Delivery commitment](../../data/e-f19-11-delivery-commitment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-11 Delivery commitment | On time | Badge "On time"; a new record starts here; next: Delayed or Delivered (UC-F19-21, UC-F19-03); fields editable within the role | U13 | `u13-owner/s-f19-03-quote-e-f19-11-delivery-commitment-on-time-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Delayed | Badge "Delayed"; next: Late or Delivered (UC-F19-19, UC-F19-03); fields editable within the role | U13 | `u13-owner/s-f19-03-quote-e-f19-11-delivery-commitment-delayed-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Late | Badge "Late"; next: Delivered or Cancelled (UC-F19-03, UC-F19-21); fields editable within the role | U13 | `u13-owner/s-f19-03-quote-e-f19-11-delivery-commitment-late-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-03-quote-e-f19-11-delivery-commitment-cancelled-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-01 Describe and order](../../flows/fl-f19-01-describe-and-order.md)

## Open questions

None.

---

⬅️ [S-F19-02 Specification](s-f19-02-specification.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-04 Generation](../02-build-and-check/s-f19-04-generation.md)

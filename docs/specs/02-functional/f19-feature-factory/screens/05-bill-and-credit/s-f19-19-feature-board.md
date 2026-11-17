🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-05 Bill and credit](README.md) › 🖥️ S-F19-19 Feature board

# 🖥️ S-F19-19 Feature board

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Follow features, costs and credits.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-05 step 3, U13 | desktop | ![FL-F19-05 step 3, U13, light](../../images/05-bill-and-credit/u13-owner/3-board-desktop-light.png) | ![FL-F19-05 step 3, U13, dark](../../images/05-bill-and-credit/u13-owner/3-board-desktop-dark.png) |
| FL-F19-05 step 3, U13 | phone | ![FL-F19-05 step 3, U13, light](../../images/05-bill-and-credit/u13-owner/3-board-phone-light.png) | ![FL-F19-05 step 3, U13, dark](../../images/05-bill-and-credit/u13-owner/3-board-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-19-feature-board-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-19-feature-board-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-19-feature-board-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-19-feature-board-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-19-feature-board-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-19-feature-board-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-19-feature-board-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-19-feature-board-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: subscriptions, costs, credits, refunds and delivery record.
- Empty: "No feature yet".
- Loading: the frame and titles show at once with placeholder rows for the board; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: Figures last loaded stay visible with their date. Nothing else is queued: D38 keeps only today's schedule,
  time and intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F19-08 Promotion credit](../../data/e-f19-08-promotion-credit.md),
[E-F19-12 Feature refund](../../data/e-f19-12-feature-refund.md),
[E-F19-03 Feature subscription](../../data/e-f19-03-feature-subscription.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-08 Promotion credit | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f19-19-feature-board-e-f19-08-promotion-credit-active-desktop-{light,dark}.png`, `u13-owner/s-f19-19-feature-board-e-f19-08-promotion-credit-active-{desktop,phone}-{light,dark}.png` |
| E-F19-12 Feature refund | Proposed | Badge "Proposed"; a new record starts here; next: Issued or Refused (UC-F19-22); fields editable within the role | U05, U13 | `u05-accounting/s-f19-19-feature-board-e-f19-12-feature-refund-proposed-desktop-{light,dark}.png`, `u13-owner/s-f19-19-feature-board-e-f19-12-feature-refund-proposed-{desktop,phone}-{light,dark}.png` |
| E-F19-12 Feature refund | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f19-19-feature-board-e-f19-12-feature-refund-refused-desktop-{light,dark}.png`, `u13-owner/s-f19-19-feature-board-e-f19-12-feature-refund-refused-{desktop,phone}-{light,dark}.png` |
| E-F19-03 Feature subscription | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f19-19-feature-board-e-f19-03-feature-subscription-active-desktop-{light,dark}.png`, `u13-owner/s-f19-19-feature-board-e-f19-03-feature-subscription-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F19-18 Withdrawal](../04-promote/s-f19-18-withdrawal.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-20 Promotion terms](../04-promote/s-f19-20-promotion-terms.md)

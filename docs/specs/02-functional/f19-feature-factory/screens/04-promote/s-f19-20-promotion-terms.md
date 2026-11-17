🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-04 Promote](README.md) › 🖥️ S-F19-20 Promotion terms

# 🖥️ S-F19-20 Promotion terms

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Accept the licence terms of a promotion.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-04 step 5, U13 | desktop | ![FL-F19-04 step 5, U13, light](../../images/04-promote/u13-owner/5-terms-desktop-light.png) | ![FL-F19-04 step 5, U13, dark](../../images/04-promote/u13-owner/5-terms-desktop-dark.png) |
| FL-F19-04 step 5, U13 | phone | ![FL-F19-04 step 5, U13, light](../../images/04-promote/u13-owner/5-terms-phone-light.png) | ![FL-F19-04 step 5, U13, dark](../../images/04-promote/u13-owner/5-terms-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-20-promotion-terms-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-20-promotion-terms-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-20-promotion-terms-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-20-promotion-terms-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-20-promotion-terms-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-20-promotion-terms-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-20-promotion-terms-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-20-promotion-terms-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the promotion terms with the accept button and the copy kept.
- Empty: never empty: it opens from a promotion.
- Loading: the frame and titles show at once with placeholder rows for the terms; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: accepted terms are read-only.
- Offline: not available offline: acceptance needs the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-07 Feature promotion](../../data/e-f19-07-feature-promotion.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-07 Feature promotion | Listed | Badge "Listed"; a new record starts here; next: Submitted (UC-F19-13); fields editable within the role | U13 | `u13-owner/s-f19-20-promotion-terms-e-f19-07-feature-promotion-listed-{desktop,phone}-{light,dark}.png` |
| E-F19-07 Feature promotion | Submitted | Badge "Submitted"; next: Started (UC-F19-20); fields editable within the role | U13 | `u13-owner/s-f19-20-promotion-terms-e-f19-07-feature-promotion-submitted-{desktop,phone}-{light,dark}.png` |
| E-F19-07 Feature promotion | Started | Badge "Started"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-20-promotion-terms-e-f19-07-feature-promotion-started-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-04 Promote](../../flows/fl-f19-04-promote.md)

## Open questions

None.

---

⬅️ [S-F19-19 Feature board](../05-bill-and-credit/s-f19-19-feature-board.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-21 Delivery plan](../01-describe-and-order/s-f19-21-delivery-plan.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-04 Promote](README.md) › 🖥️ S-F19-13 Promotion review

# 🖥️ S-F19-13 Promotion review

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Review a promotion for genericity and privacy.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-04 step 2, U48 | desktop | ![FL-F19-04 step 2, U48, light](../../images/04-promote/u48-hosting-engineer/2-privacy-review-desktop-light.png) | ![FL-F19-04 step 2, U48, dark](../../images/04-promote/u48-hosting-engineer/2-privacy-review-desktop-dark.png) |
| FL-F19-04 step 2, U48 | phone | ![FL-F19-04 step 2, U48, light](../../images/04-promote/u48-hosting-engineer/2-privacy-review-phone-light.png) | ![FL-F19-04 step 2, U48, dark](../../images/04-promote/u48-hosting-engineer/2-privacy-review-phone-dark.png) |
| Error E1, U48 | desktop | ![Error E1, U48, light](../../images/04-promote/u48-hosting-engineer/e1-customer-data-desktop-light.png) | ![Error E1, U48, dark](../../images/04-promote/u48-hosting-engineer/e1-customer-data-desktop-dark.png) |
| Error E1, U48 | phone | ![Error E1, U48, light](../../images/04-promote/u48-hosting-engineer/e1-customer-data-phone-light.png) | ![Error E1, U48, dark](../../images/04-promote/u48-hosting-engineer/e1-customer-data-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-13-promotion-review-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-13-promotion-review-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-13-promotion-review-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-13-promotion-review-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-13-promotion-review-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-13-promotion-review-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-13-promotion-review-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-13-promotion-review-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the feature's code and data to make generic, with the decision.
- Empty: "No promotion to review".
- Loading: the frame and titles show at once with placeholder rows for the review; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: decided reviews are read-only.
- Offline: not available offline: reviews run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F19-07 Feature promotion](../../data/e-f19-07-feature-promotion.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-07 Feature promotion | Listed | Badge "Listed"; a new record starts here; next: Submitted (UC-F19-13); fields editable within the role | U48 | `u48-hosting-engineer/s-f19-13-promotion-review-e-f19-07-feature-promotion-listed-{desktop,phone}-{light,dark}.png` |
| E-F19-07 Feature promotion | Submitted | Badge "Submitted"; next: Started (UC-F19-20); fields editable within the role | U48 | `u48-hosting-engineer/s-f19-13-promotion-review-e-f19-07-feature-promotion-submitted-{desktop,phone}-{light,dark}.png` |
| E-F19-07 Feature promotion | Started | Badge "Started"; final: read-only, no next state; the history shows how it got here | U48 | `u48-hosting-engineer/s-f19-13-promotion-review-e-f19-07-feature-promotion-started-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F19-12 Promotion](s-f19-12-promotion.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-14 Store listing](s-f19-14-store-listing.md)

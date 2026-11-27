🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-02 Buy and licence](README.md) › 🖥️ S-F14-07 Reviews

# 🖥️ S-F14-07 Reviews

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md)

## Purpose

Rate and review.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-02 step 3, U07 | desktop | ![FL-F14-02 step 3, U07, light](../../images/02-buy-and-licence/u07-administrator/3-review-desktop-light.png) | ![FL-F14-02 step 3, U07, dark](../../images/02-buy-and-licence/u07-administrator/3-review-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-07-reviews-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-07-reviews-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-07-reviews-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-07-reviews-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-07-reviews-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-07-reviews-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-07-reviews-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-07-reviews-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: ratings, reviews and the publisher's answers.
- Empty: "No review yet": invites users of the plugin to rate it.
- Loading: the frame and titles show at once with placeholder rows for the reviews; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: users who have not installed the plugin read reviews only.
- Offline: not available offline: reviews are read from the store. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-06 Plugin review](../../data/e-f14-06-plugin-review.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-06 Plugin review | New | Badge "New"; a new record starts here; next: Checked or Refused (BR-F14-10, UC-F14-07); fields editable within the role | U07, U46 | `u07-administrator/s-f14-07-reviews-e-f14-06-plugin-review-new-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-07-reviews-e-f14-06-plugin-review-new-desktop-{light,dark}.png` |
| E-F14-06 Plugin review | Checked | Badge "Checked"; next: Published or Refused (UC-F14-07); fields editable within the role | U07, U46 | `u07-administrator/s-f14-07-reviews-e-f14-06-plugin-review-checked-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-07-reviews-e-f14-06-plugin-review-checked-desktop-{light,dark}.png` |
| E-F14-06 Plugin review | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07, U46 | `u07-administrator/s-f14-07-reviews-e-f14-06-plugin-review-refused-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-07-reviews-e-f14-06-plugin-review-refused-desktop-{light,dark}.png` |
| E-F14-06 Plugin review | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07, U46 | `u07-administrator/s-f14-07-reviews-e-f14-06-plugin-review-published-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-07-reviews-e-f14-06-plugin-review-published-desktop-{light,dark}.png` |

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

- [FL-F14-02 Buy and licence](../../flows/fl-f14-02-buy-and-licence.md)

## Open questions

None.

---

⬅️ [S-F14-06 Licences](s-f14-06-licences.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-08 Submission](../03-publish/s-f14-08-submission.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-03 Review and monitor](README.md) › 🖥️ S-F16-04 Review queue

# 🖥️ S-F16-04 Review queue

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md) (support lead)

## Purpose

Review, correct and escalate.

## Entry points

Support in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-03 step 1, U16 | desktop | ![FL-F16-03 step 1, U16, light](../../images/03-review-and-monitor/u16-office-worker/1-review-queue-desktop-light.png) | ![FL-F16-03 step 1, U16, dark](../../images/03-review-and-monitor/u16-office-worker/1-review-queue-desktop-dark.png) |
| FL-F16-03 step 1, U16 | phone | ![FL-F16-03 step 1, U16, light](../../images/03-review-and-monitor/u16-office-worker/1-review-queue-phone-light.png) | ![FL-F16-03 step 1, U16, dark](../../images/03-review-and-monitor/u16-office-worker/1-review-queue-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-04-review-queue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-04-review-queue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-04-review-queue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-04-review-queue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-04-review-queue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-04-review-queue-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-04-review-queue-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-04-review-queue-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: sampled, low-scored, low-rated and escalated requests to approve or correct.
- Empty: "Queue empty": nothing to review.
- Loading: the frame and titles show at once with placeholder rows for the queue; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: reviewed items are read-only.
- Offline: The items last loaded stay readable; approvals and corrections are sent only online. Nothing else is queued:
  D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost and the
  actions come back with it.

Shown entities (VD-15): [E-F16-03 Resolution review](../../data/e-f16-03-resolution-review.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-03 Resolution review | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U16 | `u16-office-worker/s-f16-04-review-queue-e-f16-03-resolution-review-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the review queue also on the phone.

## Accessibility

Labelled controls; modes and scores as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-03 Review and monitor](../../flows/fl-f16-03-review-and-monitor.md)

## Open questions

None.

---

⬅️ [S-F16-03 Intent rollout](../02-automate-an-intent/s-f16-03-intent-rollout.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-05 Support dashboard](s-f16-05-support-dashboard.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-03 Review and monitor](README.md) › 🖥️ S-F16-05 Support dashboard

# 🖥️ S-F16-05 Support dashboard

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md) (support lead)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Monitor resolution and accuracy.

## Entry points

Support in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-03 step 2, U13 | desktop | ![FL-F16-03 step 2, U13, light](../../images/03-review-and-monitor/u13-owner/2-dashboard-desktop-light.png) | ![FL-F16-03 step 2, U13, dark](../../images/03-review-and-monitor/u13-owner/2-dashboard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-05-support-dashboard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-05-support-dashboard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-05-support-dashboard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-05-support-dashboard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-05-support-dashboard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-05-support-dashboard-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-05-support-dashboard-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-05-support-dashboard-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: volumes, resolved share, modes, accuracy, satisfaction, service levels met and costs.
- Empty: "No data yet": shown before the first request.
- Loading: the frame and titles show at once with placeholder rows for the figures; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: The figures last loaded stay visible with their date. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F16-03 Resolution review](../../data/e-f16-03-resolution-review.md),
[E-F16-02 Intent](../../data/e-f16-02-intent.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-03 Resolution review | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f16-05-support-dashboard-e-f16-03-resolution-review-active-{desktop,phone}-{light,dark}.png` |
| E-F16-02 Intent | New | Badge "New"; a new record starts here; next: Accepted (UC-F16-14); fields editable within the role | U13 | `u13-owner/s-f16-05-support-dashboard-e-f16-02-intent-new-{desktop,phone}-{light,dark}.png` |
| E-F16-02 Intent | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f16-05-support-dashboard-e-f16-02-intent-accepted-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F16-04 Review queue](s-f16-04-review-queue.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-06 Support connections](../01-resolve-a-request/s-f16-06-support-connections.md)

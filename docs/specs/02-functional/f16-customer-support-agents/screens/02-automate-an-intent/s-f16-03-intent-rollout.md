🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-02 Automate an intent](README.md) › 🖥️ S-F16-03 Intent rollout

# 🖥️ S-F16-03 Intent rollout

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md) (support lead)

## Purpose

Roll an intent out: shadow, then automatic.

## Entry points

Support in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-02 step 2, U02 | desktop | ![FL-F16-02 step 2, U02, light](../../images/02-automate-an-intent/u02-manager/2-rollout-desktop-light.png) | ![FL-F16-02 step 2, U02, dark](../../images/02-automate-an-intent/u02-manager/2-rollout-desktop-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/02-automate-an-intent/u02-manager/e1-below-the-bar-desktop-light.png) | ![Error E1, U02, dark](../../images/02-automate-an-intent/u02-manager/e1-below-the-bar-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/02-automate-an-intent/u02-manager/e1-below-the-bar-phone-light.png) | ![Error E1, U02, dark](../../images/02-automate-an-intent/u02-manager/e1-below-the-bar-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-03-intent-rollout-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-03-intent-rollout-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-03-intent-rollout-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-03-intent-rollout-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-03-intent-rollout-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-03-intent-rollout-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-03-intent-rollout-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-03-intent-rollout-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: each intent's mode, accuracy over cases and the bar of BR-F16-01.
- Empty: "No intent yet": links to discovery and the editor.
- Loading: the frame and titles show at once with placeholder rows for the intents; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads; switching is for the lead.
- Offline: not available offline: modes are switched on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-02 Intent](../../data/e-f16-02-intent.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-02 Intent | New | Badge "New"; a new record starts here; next: Accepted (UC-F16-14); fields editable within the role | U02 | `u02-manager/s-f16-03-intent-rollout-e-f16-02-intent-new-{desktop,phone}-{light,dark}.png` |
| E-F16-02 Intent | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-03-intent-rollout-e-f16-02-intent-accepted-{desktop,phone}-{light,dark}.png` |

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

- [FL-F16-02 Automate an intent](../../flows/fl-f16-02-automate-an-intent.md)

## Open questions

None.

---

⬅️ [S-F16-02 Procedure editor](s-f16-02-procedure-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-04 Review queue](../03-review-and-monitor/s-f16-04-review-queue.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-02 Automate an intent](README.md) › 🖥️ S-F16-02 Procedure editor

# 🖥️ S-F16-02 Procedure editor

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md) (support lead)

## Purpose

Write and test a procedure for an intent.

## Entry points

Support in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-02 step 1, U02 | desktop | ![FL-F16-02 step 1, U02, light](../../images/02-automate-an-intent/u02-manager/1-procedure-desktop-light.png) | ![FL-F16-02 step 1, U02, dark](../../images/02-automate-an-intent/u02-manager/1-procedure-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-02-procedure-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-02-procedure-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-02-procedure-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-02-procedure-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-02-procedure-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-02-procedure-editor-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-02-procedure-editor-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-02-procedure-editor-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the intent's procedure, allowed actions, limits, test results and versions.
- Empty: "No procedure yet": the AI assistant offers to draft one from past answers.
- Loading: the frame and titles show at once with placeholder rows for the procedure; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: published versions are read-only; a new version is a draft.
- Offline: not available offline: procedures are tested on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-02 Intent](../../data/e-f16-02-intent.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-02 Intent | New | Badge "New"; a new record starts here; next: Accepted (UC-F16-14); fields editable within the role | U02 | `u02-manager/s-f16-02-procedure-editor-e-f16-02-intent-new-{desktop,phone}-{light,dark}.png` |
| E-F16-02 Intent | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-02-procedure-editor-e-f16-02-intent-accepted-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F16-01 Request inbox](../01-resolve-a-request/s-f16-01-request-inbox.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-03 Intent rollout](s-f16-03-intent-rollout.md)

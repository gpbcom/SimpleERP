🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-05 Act and watch](README.md) › 🖥️ S-F23-17 Actions

# 🖥️ S-F23-17 Actions

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Turn a scenario into actions.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-05 step 1, U13 | desktop | ![FL-F23-05 step 1, U13, light](../../images/05-act-and-watch/u13-owner/1-actions-desktop-light.png) | ![FL-F23-05 step 1, U13, dark](../../images/05-act-and-watch/u13-owner/1-actions-desktop-dark.png) |
| FL-F23-05 step 1, U13 | phone | ![FL-F23-05 step 1, U13, light](../../images/05-act-and-watch/u13-owner/1-actions-phone-light.png) | ![FL-F23-05 step 1, U13, dark](../../images/05-act-and-watch/u13-owner/1-actions-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-17-actions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-17-actions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-17-actions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-17-actions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-17-actions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-17-actions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-17-actions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-17-actions-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: proposals created with their state.
- Empty: "No action".
- Loading: the frame and titles show at once with placeholder rows for the proposals; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: proposals approved in each capability.
- Offline: not available offline: created online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F23-08 Action proposal](../../data/e-f23-08-action-proposal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-08 Action proposal | Draft | Badge "Draft"; a new record starts here; next: Waiting (UC-F23-17); fields editable within the role | U13 | `u13-owner/s-f23-17-actions-e-f23-08-action-proposal-draft-{desktop,phone}-{light,dark}.png` |
| E-F23-08 Action proposal | Waiting | Badge "Waiting"; next: Draft (UC-F23-17); fields editable within the role | U13 | `u13-owner/s-f23-17-actions-e-f23-08-action-proposal-waiting-{desktop,phone}-{light,dark}.png` |

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

- [FL-F23-05 Act and watch](../../flows/fl-f23-05-act-and-watch.md)

## Open questions

None.

---

⬅️ [S-F23-16 Counter-measures](../04-decide/s-f23-16-counter-measures.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-18 Change warnings](s-f23-18-change-warnings.md)

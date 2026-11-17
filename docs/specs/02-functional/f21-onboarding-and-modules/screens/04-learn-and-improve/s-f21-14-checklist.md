🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-04 Learn and improve](README.md) › 🖥️ S-F21-14 Checklist

# 🖥️ S-F21-14 Checklist

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Follow the checklist and resume later.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-04 step 2, U13 | desktop | ![FL-F21-04 step 2, U13, light](../../images/04-learn-and-improve/u13-owner/2-checklist-desktop-light.png) | ![FL-F21-04 step 2, U13, dark](../../images/04-learn-and-improve/u13-owner/2-checklist-desktop-dark.png) |
| FL-F21-04 step 2, U13 | phone | ![FL-F21-04 step 2, U13, light](../../images/04-learn-and-improve/u13-owner/2-checklist-phone-light.png) | ![FL-F21-04 step 2, U13, dark](../../images/04-learn-and-improve/u13-owner/2-checklist-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-14-checklist-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-14-checklist-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-14-checklist-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-14-checklist-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-14-checklist-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-14-checklist-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-14-checklist-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-14-checklist-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the checklist with what is left.
- Empty: "All done".
- Loading: the frame and titles show at once with placeholder rows for the checklist; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: done steps read-only.
- Offline: The checklist last loaded stays visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F21-01 Onboarding progress](../../data/e-f21-01-onboarding-progress.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-01 Onboarding progress | Done | Badge "Done"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f21-14-checklist-e-f21-01-onboarding-progress-done-{desktop,phone}-{light,dark}.png` |
| E-F21-01 Onboarding progress | Closed | Badge "Closed"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f21-14-checklist-e-f21-01-onboarding-progress-closed-{desktop,phone}-{light,dark}.png` |

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

- [FL-F21-04 Learn and improve](../../flows/fl-f21-04-learn-and-improve.md)

## Open questions

None.

---

⬅️ [S-F21-13 Demo data](s-f21-13-demo-data.md) · ⬆️ [Up](README.md) · ➡️ [S-F21-15 Tours](s-f21-15-tours.md)

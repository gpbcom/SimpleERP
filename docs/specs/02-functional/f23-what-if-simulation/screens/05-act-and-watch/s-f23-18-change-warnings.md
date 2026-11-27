🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-05 Act and watch](README.md) › 🖥️ S-F23-18 Change warnings

# 🖥️ S-F23-18 Change warnings

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Be warned when a real change hits the forecast.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-05 step 2, U13 | desktop | ![FL-F23-05 step 2, U13, light](../../images/05-act-and-watch/u13-owner/2-warning-desktop-light.png) | ![FL-F23-05 step 2, U13, dark](../../images/05-act-and-watch/u13-owner/2-warning-desktop-dark.png) |
| FL-F23-05 step 2, U13 | phone | ![FL-F23-05 step 2, U13, light](../../images/05-act-and-watch/u13-owner/2-warning-phone-light.png) | ![FL-F23-05 step 2, U13, dark](../../images/05-act-and-watch/u13-owner/2-warning-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-18-change-warnings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-18-change-warnings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-18-change-warnings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-18-change-warnings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-18-change-warnings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-18-change-warnings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-18-change-warnings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-18-change-warnings-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: warnings with impact.
- Empty: "No warning".
- Loading: the frame and titles show at once with placeholder rows for the warnings; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: Warnings received stay readable. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F23-09 Change warning](../../data/e-f23-09-change-warning.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-09 Change warning | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U31 | `u13-owner/s-f23-18-change-warnings-e-f23-09-change-warning-active-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-18-change-warnings-e-f23-09-change-warning-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F23-17 Actions](s-f23-17-actions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-19 Sharing](../04-decide/s-f23-19-sharing.md)

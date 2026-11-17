🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-04 Learn and improve](README.md) › 🖥️ S-F21-17 First sign-in

# 🖥️ S-F21-17 First sign-in

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Welcome an employee at first sign-in.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-04 step 4, U01 | desktop | ![FL-F21-04 step 4, U01, light](../../images/04-learn-and-improve/u01-employee/4-first-sign-in-desktop-light.png) | ![FL-F21-04 step 4, U01, dark](../../images/04-learn-and-improve/u01-employee/4-first-sign-in-desktop-dark.png) |
| FL-F21-04 step 4, U01 | phone | ![FL-F21-04 step 4, U01, light](../../images/04-learn-and-improve/u01-employee/4-first-sign-in-phone-light.png) | ![FL-F21-04 step 4, U01, dark](../../images/04-learn-and-improve/u01-employee/4-first-sign-in-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-17-first-sign-in-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-17-first-sign-in-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-17-first-sign-in-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-17-first-sign-in-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-17-first-sign-in-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-17-first-sign-in-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-17-first-sign-in-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-17-first-sign-in-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the first sign-in steps.
- Empty: never empty.
- Loading: the frame and titles show at once with placeholder rows for the steps; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: done steps read-only.
- Offline: The current step stays on screen; saving needs the network. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F21-10 Tour](../../data/e-f21-10-tour.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-10 Tour | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f21-17-first-sign-in-e-f21-10-tour-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F21-16 Legal check](../01-first-run/s-f21-16-legal-check.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-18 Prices](../02-modules/s-f21-18-prices.md)

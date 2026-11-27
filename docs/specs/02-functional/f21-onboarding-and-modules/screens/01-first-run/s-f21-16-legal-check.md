🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-01 First run](README.md) › 🖥️ S-F21-16 Legal check

# 🖥️ S-F21-16 Legal check

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Check the legal set-up.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-01 step 6, U13 | desktop | ![FL-F21-01 step 6, U13, light](../../images/01-first-run/u13-owner/6-legal-check-desktop-light.png) | ![FL-F21-01 step 6, U13, dark](../../images/01-first-run/u13-owner/6-legal-check-desktop-dark.png) |
| FL-F21-01 step 6, U13 | phone | ![FL-F21-01 step 6, U13, light](../../images/01-first-run/u13-owner/6-legal-check-phone-light.png) | ![FL-F21-01 step 6, U13, dark](../../images/01-first-run/u13-owner/6-legal-check-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-16-legal-check-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-16-legal-check-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-16-legal-check-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-16-legal-check-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-16-legal-check-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-16-legal-check-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-16-legal-check-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-16-legal-check-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: legal check items with their state.
- Empty: "Run the check".
- Loading: the frame and titles show at once with placeholder rows for the items; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: the check runs online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F21-11 Legal check item](../../data/e-f21-11-legal-check-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-11 Legal check item | Missing | Badge "Missing"; a new record starts here; next: Completed (BR-F21-07); fields editable within the role | U13 | `u13-owner/s-f21-16-legal-check-e-f21-11-legal-check-item-missing-{desktop,phone}-{light,dark}.png` |
| E-F21-11 Legal check item | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f21-16-legal-check-e-f21-11-legal-check-item-completed-{desktop,phone}-{light,dark}.png` |

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

- [FL-F21-01 First run](../../flows/fl-f21-01-first-run.md)

## Open questions

None.

---

⬅️ [S-F21-15 Tours](../04-learn-and-improve/s-f21-15-tours.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-17 First sign-in](../04-learn-and-improve/s-f21-17-first-sign-in.md)

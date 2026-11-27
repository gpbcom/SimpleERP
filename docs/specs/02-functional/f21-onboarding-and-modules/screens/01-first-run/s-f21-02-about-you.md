🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-01 First run](README.md) › 🖥️ S-F21-02 About you

# 🖥️ S-F21-02 About you

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Describe the company.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-01 step 2, U13 | desktop | ![FL-F21-01 step 2, U13, light](../../images/01-first-run/u13-owner/2-company-desktop-light.png) | ![FL-F21-01 step 2, U13, dark](../../images/01-first-run/u13-owner/2-company-desktop-dark.png) |
| FL-F21-01 step 2, U13 | phone | ![FL-F21-01 step 2, U13, light](../../images/01-first-run/u13-owner/2-company-phone-light.png) | ![FL-F21-01 step 2, U13, dark](../../images/01-first-run/u13-owner/2-company-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-02-about-you-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-02-about-you-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-02-about-you-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-02-about-you-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-02-about-you-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-02-about-you-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-02-about-you-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-02-about-you-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: questions with the proposed set-up.
- Empty: never empty: questions shown.
- Loading: the frame and titles show at once with placeholder rows for the questions; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: answered steps can be changed by the owner only.
- Offline: not available offline: the guide is online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F21-02 Company profile](../../data/e-f21-02-company-profile.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-02 Company profile | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f21-02-about-you-e-f21-02-company-profile-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F21-01 Welcome](s-f21-01-welcome.md) · ⬆️ [Up](README.md) · ➡️ [S-F21-03 Templates](s-f21-03-templates.md)

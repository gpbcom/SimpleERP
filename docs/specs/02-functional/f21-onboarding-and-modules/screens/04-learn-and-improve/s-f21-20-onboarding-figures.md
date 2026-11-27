🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-04 Learn and improve](README.md) › 🖥️ S-F21-20 Onboarding figures

# 🖥️ S-F21-20 Onboarding figures

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Measure onboarding and drop-offs.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-04 step 6, U48 | desktop | ![FL-F21-04 step 6, U48, light](../../images/04-learn-and-improve/u48-hosting-engineer/6-figures-desktop-light.png) | ![FL-F21-04 step 6, U48, dark](../../images/04-learn-and-improve/u48-hosting-engineer/6-figures-desktop-dark.png) |
| FL-F21-04 step 6, U48 | phone | ![FL-F21-04 step 6, U48, light](../../images/04-learn-and-improve/u48-hosting-engineer/6-figures-phone-light.png) | ![FL-F21-04 step 6, U48, dark](../../images/04-learn-and-improve/u48-hosting-engineer/6-figures-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-20-onboarding-figures-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-20-onboarding-figures-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-20-onboarding-figures-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-20-onboarding-figures-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-20-onboarding-figures-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-20-onboarding-figures-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-20-onboarding-figures-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-20-onboarding-figures-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: onboarding figures per step and sector.
- Empty: "No figure yet".
- Loading: the frame and titles show at once with placeholder rows for the figures; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: computed online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F21-13 Onboarding figure](../../data/e-f21-13-onboarding-figure.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-13 Onboarding figure | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13, U48 | `u13-owner/s-f21-20-onboarding-figures-e-f21-13-onboarding-figure-recorded-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f21-20-onboarding-figures-e-f21-13-onboarding-figure-recorded-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F21-19 Provider templates](s-f21-19-provider-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-21 Migration](../05-migration-from-another-tool/s-f21-21-migration.md)

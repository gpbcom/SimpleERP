🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-02 Build and check](README.md) › 🖥️ S-F19-05 Checks

# 🖥️ S-F19-05 Checks

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Run the automatic checks.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-02 step 2, U48 | desktop | ![FL-F19-02 step 2, U48, light](../../images/02-build-and-check/u48-hosting-engineer/2-checks-desktop-light.png) | ![FL-F19-02 step 2, U48, dark](../../images/02-build-and-check/u48-hosting-engineer/2-checks-desktop-dark.png) |
| FL-F19-02 step 2, U48 | phone | ![FL-F19-02 step 2, U48, light](../../images/02-build-and-check/u48-hosting-engineer/2-checks-phone-light.png) | ![FL-F19-02 step 2, U48, dark](../../images/02-build-and-check/u48-hosting-engineer/2-checks-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-05-checks-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-05-checks-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-05-checks-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-05-checks-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-05-checks-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-05-checks-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-05-checks-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-05-checks-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: each check with its result.
- Empty: "No check run yet".
- Loading: the frame and titles show at once with placeholder rows for the checks; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: reports are read-only.
- Offline: not available offline: checks run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-05 Feature check report](../../data/e-f19-05-feature-check-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-05 Feature check report | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U48 | `u48-hosting-engineer/s-f19-05-checks-e-f19-05-feature-check-report-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-02 Build and check](../../flows/fl-f19-02-build-and-check.md)

## Open questions

None.

---

⬅️ [S-F19-04 Generation](s-f19-04-generation.md) · ⬆️ [Up](README.md) · ➡️ [S-F19-06 Review](s-f19-06-review.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-04 On site](README.md) › 🖥️ S-SC16-13 Safety

# 🖥️ S-SC16-13 Safety

**Status:** 🔄 waiting for the owner

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)

## Purpose

Used to keep the safety file and register
([UC-SC16-13](../../use-cases/04-on-site/uc-sc16-13-keep-the-safety-file-and-register.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-04 step 2, U43 | desktop | ![FL-SC16-04 step 2, U43, light](../../images/04-on-site/u43-event-producer/2-safety-desktop-light.png) | ![FL-SC16-04 step 2, U43, dark](../../images/04-on-site/u43-event-producer/2-safety-desktop-dark.png) |
| FL-SC16-04 step 2, U43 | phone | ![FL-SC16-04 step 2, U43, light](../../images/04-on-site/u43-event-producer/2-safety-phone-light.png) | ![FL-SC16-04 step 2, U43, dark](../../images/04-on-site/u43-event-producer/2-safety-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-13-safety-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-13-safety-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-13-safety-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-13-safety-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-13-safety-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-13-safety-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-13-safety-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-13-safety-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-14 Safety file](../../data/e-sc16-14-safety-file.md), shown as the entity pages list them, with
their examples.

## Actions

- Prepare the file: [UC-SC16-13](../../use-cases/04-on-site/uc-sc16-13-keep-the-safety-file-and-register.md), step 1.
- Record checks: [UC-SC16-13](../../use-cases/04-on-site/uc-sc16-13-keep-the-safety-file-and-register.md), step 2.
- Check completeness: [UC-SC16-13](../../use-cases/04-on-site/uc-sc16-13-keep-the-safety-file-and-register.md), step 3.
- Open: [UC-SC16-13](../../use-cases/04-on-site/uc-sc16-13-keep-the-safety-file-and-register.md), step 4.

## States

- Normal: the safety file with checks and register.
- Empty: "No file".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a check overdue: opening is blocked.
- Read-only: past checks are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-14 Safety file](../../data/e-sc16-14-safety-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-14 Safety file | Open | Badge "Open"; a new record starts here; no other state; fields editable within the role | U43 | `u43-event-producer/s-sc16-13-safety-e-sc16-14-safety-file-open-{desktop,phone}-{light,dark}.png` |
| E-SC16-14 Safety file | Blocked | Badge "Blocked"; a new record starts here; no other state; fields editable within the role | U43 | `u43-event-producer/s-sc16-13-safety-e-sc16-14-safety-file-blocked-{desktop,phone}-{light,dark}.png` |
| E-SC16-14 Safety file | Overdue | Badge "Overdue"; a new record starts here; no other state; fields editable within the role | U43 | `u43-event-producer/s-sc16-13-safety-e-sc16-14-safety-file-overdue-{desktop,phone}-{light,dark}.png` |
| E-SC16-14 Safety file | Complete | Badge "Complete"; a new record starts here; no other state; fields editable within the role | U43 | `u43-event-producer/s-sc16-13-safety-e-sc16-14-safety-file-complete-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC16-04 On site](../../flows/fl-sc16-04-on-site.md)

## Open questions

None.

---

⬅️ [S-SC16-12 Bars and merchandise](s-sc16-12-bars-and-merchandise.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-14 Copyright](../05-declarations-and-reports/s-sc16-14-copyright.md)

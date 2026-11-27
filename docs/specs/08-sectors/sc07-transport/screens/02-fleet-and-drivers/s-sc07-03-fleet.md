🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-02 Fleet and drivers](README.md) › 🖥️ S-SC07-03 Fleet

# 🖥️ S-SC07-03 Fleet

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Used to manage the fleet and trailers
([UC-SC07-03](../../use-cases/02-fleet-and-drivers/uc-sc07-03-manage-the-fleet-and-trailers.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-02 step 1, U29 | desktop | ![FL-SC07-02 step 1, U29, light](../../images/02-fleet-and-drivers/u29-dispatcher/1-fleet-desktop-light.png) | ![FL-SC07-02 step 1, U29, dark](../../images/02-fleet-and-drivers/u29-dispatcher/1-fleet-desktop-dark.png) |
| FL-SC07-02 step 1, U29 | phone | ![FL-SC07-02 step 1, U29, light](../../images/02-fleet-and-drivers/u29-dispatcher/1-fleet-phone-light.png) | ![FL-SC07-02 step 1, U29, dark](../../images/02-fleet-and-drivers/u29-dispatcher/1-fleet-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-03-fleet-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-03-fleet-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-03-fleet-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-03-fleet-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-03-fleet-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-03-fleet-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-03-fleet-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-03-fleet-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-03 Fleet vehicle](../../data/e-sc07-03-fleet-vehicle.md), shown as the entity pages list them,
with their examples.

## Actions

- Add a vehicle: [UC-SC07-03](../../use-cases/02-fleet-and-drivers/uc-sc07-03-manage-the-fleet-and-trailers.md), step 1.
- Link its licence copy: [UC-SC07-03](../../use-cases/02-fleet-and-drivers/uc-sc07-03-manage-the-fleet-and-trailers.md),
  step 2.
- Set its plan: [UC-SC07-03](../../use-cases/02-fleet-and-drivers/uc-sc07-03-manage-the-fleet-and-trailers.md), step 3.
- Make it assignable: [UC-SC07-03](../../use-cases/02-fleet-and-drivers/uc-sc07-03-manage-the-fleet-and-trailers.md),
  step 4.

## States

- Normal: vehicles and trailers with licence copy, inspection and state.
- Empty: "No vehicle".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no licence copy: it is not assignable for hire or reward.
- Read-only: drivers see their vehicle.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-03 Fleet vehicle](../../data/e-sc07-03-fleet-vehicle.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-03 Fleet vehicle | Blocked | Badge "Blocked"; a new record starts here; next: Overdue (UC-SC07-11); fields editable within the role | U29 | `u29-dispatcher/s-sc07-03-fleet-e-sc07-03-fleet-vehicle-blocked-{desktop,phone}-{light,dark}.png` |

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

## Shown in

- [FL-SC07-02 Fleet and drivers](../../flows/fl-sc07-02-fleet-and-drivers.md)

## Open questions

None.

---

⬅️ [S-SC07-02 Trip planning](../01-orders-and-planning/s-sc07-02-trip-planning.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-04 Drivers](s-sc07-04-drivers.md)

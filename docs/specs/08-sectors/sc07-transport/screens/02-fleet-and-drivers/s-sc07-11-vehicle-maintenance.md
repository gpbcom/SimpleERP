🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-02 Fleet and drivers](README.md) › 🖥️ S-SC07-11 Vehicle maintenance

# 🖥️ S-SC07-11 Vehicle maintenance

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Used to maintain vehicles and their inspections,
[UC-SC07-11](../../use-cases/02-fleet-and-drivers/uc-sc07-11-maintain-vehicles-and-their-inspections.md).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-02 step 3, U29 | desktop | ![FL-SC07-02 step 3, U29, light](../../images/02-fleet-and-drivers/u29-dispatcher/3-maintenance-desktop-light.png) | ![FL-SC07-02 step 3, U29, dark](../../images/02-fleet-and-drivers/u29-dispatcher/3-maintenance-desktop-dark.png) |
| FL-SC07-02 step 3, U29 | phone | ![FL-SC07-02 step 3, U29, light](../../images/02-fleet-and-drivers/u29-dispatcher/3-maintenance-phone-light.png) | ![FL-SC07-02 step 3, U29, dark](../../images/02-fleet-and-drivers/u29-dispatcher/3-maintenance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-11-vehicle-maintenance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-11-vehicle-maintenance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-11-vehicle-maintenance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-11-vehicle-maintenance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-11-vehicle-maintenance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-11-vehicle-maintenance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-11-vehicle-maintenance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-11-vehicle-maintenance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-03 Fleet vehicle](../../data/e-sc07-03-fleet-vehicle.md),
[E-SC07-11 Vehicle repair](../../data/e-sc07-11-vehicle-repair.md), shown as the entity pages list them, with their
examples.

## Actions

- Plan: [UC-SC07-11](../../use-cases/02-fleet-and-drivers/uc-sc07-11-maintain-vehicles-and-their-inspections.md), step
  1.
- Repair: [UC-SC07-11](../../use-cases/02-fleet-and-drivers/uc-sc07-11-maintain-vehicles-and-their-inspections.md), step
  2.
- Record: [UC-SC07-11](../../use-cases/02-fleet-and-drivers/uc-sc07-11-maintain-vehicles-and-their-inspections.md), step
  3.
- Free the vehicle:
  [UC-SC07-11](../../use-cases/02-fleet-and-drivers/uc-sc07-11-maintain-vehicles-and-their-inspections.md), step 4.

## States

- Normal: maintenance plan, repairs, costs and next dates.
- Empty: "No maintenance planned".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an overdue inspection: the vehicle cannot start a trip
  ([BR-SC07-10](../../business-rules/br-sc07-10-vehicles-inspected-on-time.md)).
- Read-only: recorded work is read-only.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-03 Fleet vehicle](../../data/e-sc07-03-fleet-vehicle.md),
[E-SC07-11 Vehicle repair](../../data/e-sc07-11-vehicle-repair.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-03 Fleet vehicle | Blocked | Badge "Blocked"; a new record starts here; next: Overdue (UC-SC07-11); fields editable within the role | U29 | `u29-dispatcher/s-sc07-11-vehicle-maintenance-e-sc07-03-fleet-vehicle-blocked-{desktop,phone}-{light,dark}.png` |
| E-SC07-03 Fleet vehicle | Overdue | Badge "Overdue"; next: Blocked (UC-SC07-11); fields editable within the role | U29 | `u29-dispatcher/s-sc07-11-vehicle-maintenance-e-sc07-03-fleet-vehicle-overdue-{desktop,phone}-{light,dark}.png` |
| E-SC07-11 Vehicle repair | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U29 | `u29-dispatcher/s-sc07-11-vehicle-maintenance-e-sc07-11-vehicle-repair-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC07-02 Fleet and drivers](../../flows/fl-sc07-02-fleet-and-drivers.md)

## Open questions

None.

---

⬅️ [S-SC07-10 Fuel and tolls](../05-billing-and-performance/s-sc07-10-fuel-and-tolls.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-12 Chartering](../01-orders-and-planning/s-sc07-12-chartering.md)

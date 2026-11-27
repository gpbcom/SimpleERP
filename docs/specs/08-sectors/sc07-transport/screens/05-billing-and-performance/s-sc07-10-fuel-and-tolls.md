🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-05 Billing and performance](README.md) › 🖥️ S-SC07-10 Fuel and tolls

# 🖥️ S-SC07-10 Fuel and tolls

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to manage fuel cards and tolls
([UC-SC07-10](../../use-cases/05-billing-and-performance/uc-sc07-10-manage-fuel-cards-and-tolls.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-05 step 1, U29 | desktop | ![FL-SC07-05 step 1, U29, light](../../images/05-billing-and-performance/u29-dispatcher/1-fuel-tolls-desktop-light.png) | ![FL-SC07-05 step 1, U29, dark](../../images/05-billing-and-performance/u29-dispatcher/1-fuel-tolls-desktop-dark.png) |
| FL-SC07-05 step 1, U29 | phone | ![FL-SC07-05 step 1, U29, light](../../images/05-billing-and-performance/u29-dispatcher/1-fuel-tolls-phone-light.png) | ![FL-SC07-05 step 1, U29, dark](../../images/05-billing-and-performance/u29-dispatcher/1-fuel-tolls-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-10-fuel-and-tolls-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-10-fuel-and-tolls-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-10-fuel-and-tolls-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-10-fuel-and-tolls-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-10-fuel-and-tolls-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-10-fuel-and-tolls-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-10-fuel-and-tolls-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-10-fuel-and-tolls-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-10 Fuel and toll line](../../data/e-sc07-10-fuel-and-toll-line.md), shown as the entity pages list
them, with their examples.

## Actions

- Import: [UC-SC07-10](../../use-cases/05-billing-and-performance/uc-sc07-10-manage-fuel-cards-and-tolls.md), step 1.
- Match to trips: [UC-SC07-10](../../use-cases/05-billing-and-performance/uc-sc07-10-manage-fuel-cards-and-tolls.md),
  step 2.
- Check anomalies: [UC-SC07-10](../../use-cases/05-billing-and-performance/uc-sc07-10-manage-fuel-cards-and-tolls.md),
  step 3.
- Post: [UC-SC07-10](../../use-cases/05-billing-and-performance/uc-sc07-10-manage-fuel-cards-and-tolls.md), step 4.

## States

- Normal: fuel and toll lines with vehicle, trip and anomalies.
- Empty: "No line imported".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, fuel off the route: the line is flagged.
- Read-only: posted lines are read-only.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-10 Fuel and toll line](../../data/e-sc07-10-fuel-and-toll-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-10 Fuel and toll line | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05, U29 | `u05-accounting/s-sc07-10-fuel-and-tolls-e-sc07-10-fuel-and-toll-line-recorded-desktop-{light,dark}.png`, `u29-dispatcher/s-sc07-10-fuel-and-tolls-e-sc07-10-fuel-and-toll-line-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC07-05 Billing and performance](../../flows/fl-sc07-05-billing-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC07-09 Dangerous goods](../04-compliance/s-sc07-09-dangerous-goods.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-11 Vehicle maintenance](../02-fleet-and-drivers/s-sc07-11-vehicle-maintenance.md)

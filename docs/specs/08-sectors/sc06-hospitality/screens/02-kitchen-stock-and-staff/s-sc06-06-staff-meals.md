🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-02 Kitchen stock and staff](README.md) › 🖥️ S-SC06-06 Staff meals

# 🖥️ S-SC06-06 Staff meals

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to record staff meals ([UC-SC06-06](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-06-record-staff-meals.md)).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-02 step 3, U23 | desktop | ![FL-SC06-02 step 3, U23, light](../../images/02-kitchen-stock-and-staff/u23-store-manager/3-staff-meals-desktop-light.png) | ![FL-SC06-02 step 3, U23, dark](../../images/02-kitchen-stock-and-staff/u23-store-manager/3-staff-meals-desktop-dark.png) |
| FL-SC06-02 step 3, U23 | phone | ![FL-SC06-02 step 3, U23, light](../../images/02-kitchen-stock-and-staff/u23-store-manager/3-staff-meals-phone-light.png) | ![FL-SC06-02 step 3, U23, dark](../../images/02-kitchen-stock-and-staff/u23-store-manager/3-staff-meals-phone-dark.png) |
| FL-SC06-02 step 3, U23 | tablet | ![FL-SC06-02 step 3, U23, light](../../images/02-kitchen-stock-and-staff/u23-store-manager/3-staff-meals-tablet-light.png) | ![FL-SC06-02 step 3, U23, dark](../../images/02-kitchen-stock-and-staff/u23-store-manager/3-staff-meals-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-06-staff-meals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-06-staff-meals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-06-staff-meals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-06-staff-meals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-06-staff-meals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-06-staff-meals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-06-staff-meals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-06-staff-meals-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC06-05 Staff benefit](../../data/e-sc06-05-staff-benefit.md), shown as the entity pages list them,
with their examples.

## Actions

- Record: [UC-SC06-06](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-06-record-staff-meals.md), step 1.
- Check: [UC-SC06-06](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-06-record-staff-meals.md), step 2.
- Send to payroll: [UC-SC06-06](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-06-record-staff-meals.md), step 3.
- Lock the month: [UC-SC06-06](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-06-record-staff-meals.md), step 4.

## States

- Normal: meals per person and day and their payroll state.
- Empty: "No meal recorded".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a person unknown: the meal is refused.
- Read-only: a locked month is read-only.
- Offline: not available offline: front-office and back-office work on live bookings and shared figures. Offline work is
  kept for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC06-05 Staff benefit](../../data/e-sc06-05-staff-benefit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-05 Staff benefit | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U23 | `u23-store-manager/s-sc06-06-staff-meals-e-sc06-05-staff-benefit-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC06-02 Kitchen stock and staff](../../flows/fl-sc06-02-kitchen-stock-and-staff.md)

## Open questions

None.

---

⬅️ [S-SC06-05 Tips](s-sc06-05-tips.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-07 Rooms and rates](../03-rooms-and-bookings/s-sc06-07-rooms-and-rates.md)

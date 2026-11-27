🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-01 Appointments](README.md) › 🖥️ S-SC09-01 Agenda

# 🖥️ S-SC09-01 Agenda

**Status:** ✅ specified

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to book appointments online and at the desk
([UC-SC09-01](../../use-cases/01-appointments/uc-sc09-01-book-appointments-online-and-at-the-desk.md)); to teleconsult
([UC-SC09-11](../../use-cases/04-health-exchanges/uc-sc09-11-teleconsult.md)).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-01 step 1, U33 | desktop | ![FL-SC09-01 step 1, U33, light](../../images/01-appointments/u33-medical-secretary/1-agenda-desktop-light.png) | ![FL-SC09-01 step 1, U33, dark](../../images/01-appointments/u33-medical-secretary/1-agenda-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-01-agenda-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-01-agenda-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-01-agenda-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-01-agenda-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-01-agenda-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-01-agenda-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-01-agenda-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-01-agenda-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC09-01 Appointment](../../data/e-sc09-01-appointment.md),
[E-F2-18 Resource booking](../../../../02-functional/f02-no-code-configuration/data/e-f02-18-resource-booking.md),
[E-SC09-03 Clinical record entry](../../data/e-sc09-03-clinical-record-entry.md), shown as the entity pages list them,
with their examples.

## Actions

- Find a slot: [UC-SC09-01](../../use-cases/01-appointments/uc-sc09-01-book-appointments-online-and-at-the-desk.md),
  step 1.
- Book at the desk:
  [UC-SC09-01](../../use-cases/01-appointments/uc-sc09-01-book-appointments-online-and-at-the-desk.md), step 2.
- Check it is free:
  [UC-SC09-01](../../use-cases/01-appointments/uc-sc09-01-book-appointments-online-and-at-the-desk.md), step 3.
- Confirm: [UC-SC09-01](../../use-cases/01-appointments/uc-sc09-01-book-appointments-online-and-at-the-desk.md), step 4.
- Book: [UC-SC09-11](../../use-cases/04-health-exchanges/uc-sc09-11-teleconsult.md), step 1.

## States

- Normal: the day per practitioner and room with appointments and free slots.
- Empty: "No appointment today".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the slot taken meanwhile: another slot is proposed.
- Read-only: patients see only their own appointments.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-01 Appointment](../../data/e-sc09-01-appointment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-01 Appointment | Booked | Badge "Booked"; a new record starts here; next: Confirmed or Cancelled (UC-SC09-01, UC-SC09-02); fields editable within the role | U09, U33 | `u09-customer/s-sc09-01-agenda-e-sc09-01-appointment-booked-phone-{light,dark}.png`, `u33-medical-secretary/s-sc09-01-agenda-e-sc09-01-appointment-booked-desktop-{light,dark}.png` |
| E-SC09-01 Appointment | Confirmed | Badge "Confirmed"; next: Done, No-show or Cancelled (UC-SC09-11, UC-SC09-01, UC-SC09-02); fields editable within the role | U09, U33 | `u09-customer/s-sc09-01-agenda-e-sc09-01-appointment-confirmed-phone-{light,dark}.png`, `u33-medical-secretary/s-sc09-01-agenda-e-sc09-01-appointment-confirmed-desktop-{light,dark}.png` |
| E-SC09-01 Appointment | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U09, U33 | `u09-customer/s-sc09-01-agenda-e-sc09-01-appointment-cancelled-phone-{light,dark}.png`, `u33-medical-secretary/s-sc09-01-agenda-e-sc09-01-appointment-cancelled-desktop-{light,dark}.png` |
| E-SC09-01 Appointment | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U09, U33 | `u09-customer/s-sc09-01-agenda-e-sc09-01-appointment-done-phone-{light,dark}.png`, `u33-medical-secretary/s-sc09-01-agenda-e-sc09-01-appointment-done-desktop-{light,dark}.png` |
| E-SC09-01 Appointment | No-show | Badge "No-show"; final: read-only, no next state; the history shows how it got here | U09, U33 | `u09-customer/s-sc09-01-agenda-e-sc09-01-appointment-no-show-phone-{light,dark}.png`, `u33-medical-secretary/s-sc09-01-agenda-e-sc09-01-appointment-no-show-desktop-{light,dark}.png` |

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

- [FL-SC09-01 Appointments](../../flows/fl-sc09-01-appointments.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC09-02 Reminders](s-sc09-02-reminders.md)

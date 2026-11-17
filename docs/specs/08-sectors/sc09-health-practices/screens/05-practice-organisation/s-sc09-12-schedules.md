🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-05 Practice organisation](README.md) › 🖥️ S-SC09-12 Schedules

# 🖥️ S-SC09-12 Schedules

**Status:** 🔄 waiting for the owner

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to manage schedules, rooms and equipment,
[UC-SC09-12](../../use-cases/05-practice-organisation/uc-sc09-12-manage-schedules-rooms-and-equipment.md).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-05 step 1, U33 | desktop | ![FL-SC09-05 step 1, U33, light](../../images/05-practice-organisation/u33-medical-secretary/1-schedules-desktop-light.png) | ![FL-SC09-05 step 1, U33, dark](../../images/05-practice-organisation/u33-medical-secretary/1-schedules-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-12-schedules-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-12-schedules-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-12-schedules-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-12-schedules-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-12-schedules-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-12-schedules-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-12-schedules-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-12-schedules-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC09-01 Appointment](../../data/e-sc09-01-appointment.md),
[E-SC09-09 Consulting room](../../data/e-sc09-09-consulting-room.md),
[E-F2-17 Bookable resource setting](../../../../02-functional/f02-no-code-configuration/data/e-f02-17-bookable-resource-setting.md),
shown as the entity pages list them, with their examples.

## Actions

- Set schedules:
  [UC-SC09-12](../../use-cases/05-practice-organisation/uc-sc09-12-manage-schedules-rooms-and-equipment.md), step 1.
- Book rooms: [UC-SC09-12](../../use-cases/05-practice-organisation/uc-sc09-12-manage-schedules-rooms-and-equipment.md),
  step 2.
- Check: [UC-SC09-12](../../use-cases/05-practice-organisation/uc-sc09-12-manage-schedules-rooms-and-equipment.md), step
  3.
- Publish: [UC-SC09-12](../../use-cases/05-practice-organisation/uc-sc09-12-manage-schedules-rooms-and-equipment.md),
  step 4.

## States

- Normal: schedules per practitioner, rooms and equipment bookings.
- Empty: "No schedule".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a room double-booked: the second booking is refused,
  [BR-F2-18](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-18-one-booking-per-resource-and-slot.md).
- Read-only: practitioners read their own week.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-09 Consulting room](../../data/e-sc09-09-consulting-room.md),
[E-F2-17 Bookable resource setting](../../../../02-functional/f02-no-code-configuration/data/e-f02-17-bookable-resource-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-09 Consulting room | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U33 | `u13-owner/s-sc09-12-schedules-e-sc09-09-consulting-room-active-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-12-schedules-e-sc09-09-consulting-room-active-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-18); fields editable within the role | U13, U33 | `u13-owner/s-sc09-12-schedules-e-f02-17-bookable-resource-setting-draft-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-12-schedules-e-f02-17-bookable-resource-setting-draft-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Published | Badge "Published"; next: Archived (UC-F2-18); fields editable within the role | U13, U33 | `u13-owner/s-sc09-12-schedules-e-f02-17-bookable-resource-setting-published-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-12-schedules-e-f02-17-bookable-resource-setting-published-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U13, U33 | `u13-owner/s-sc09-12-schedules-e-f02-17-bookable-resource-setting-archived-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-12-schedules-e-f02-17-bookable-resource-setting-archived-desktop-{light,dark}.png` |

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

- [FL-SC09-05 Practice organisation](../../flows/fl-sc09-05-practice-organisation.md)

## Open questions

None.

---

⬅️ [S-SC09-11 Teleconsultation](../04-health-exchanges/s-sc09-11-teleconsultation.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-13 Cost sharing](s-sc09-13-cost-sharing.md)

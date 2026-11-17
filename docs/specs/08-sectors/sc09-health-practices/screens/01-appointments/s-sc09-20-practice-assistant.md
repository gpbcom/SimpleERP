🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-01 Appointments](README.md) › 🖥️ S-SC09-20 Practice assistant

# 🖥️ S-SC09-20 Practice assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to ask the AI assistant about the practice
([UC-SC09-20](../../use-cases/01-appointments/uc-sc09-20-ask-the-assistant-about-the-practice.md)).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-01 step 3, U33 | desktop | ![FL-SC09-01 step 3, U33, light](../../images/01-appointments/u33-medical-secretary/3-assistant-desktop-light.png) | ![FL-SC09-01 step 3, U33, dark](../../images/01-appointments/u33-medical-secretary/3-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-20-practice-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-20-practice-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-20-practice-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-20-practice-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-20-practice-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-20-practice-assistant-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-20-practice-assistant-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-20-practice-assistant-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC09-01 Appointment](../../data/e-sc09-01-appointment.md),
[E-SC09-03 Clinical record entry](../../data/e-sc09-03-clinical-record-entry.md), shown as the entity pages list them,
with their examples.

## Actions

- Ask: [UC-SC09-20](../../use-cases/01-appointments/uc-sc09-20-ask-the-assistant-about-the-practice.md), step 1.
- Summarise a record: [UC-SC09-20](../../use-cases/01-appointments/uc-sc09-20-ask-the-assistant-about-the-practice.md),
  step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, clinical data to a cloud model: it is refused.
- Read-only: no clinical content for secretaries.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC09-01 Appointment](../../data/e-sc09-01-appointment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-01 Appointment | Confirmed | Badge "Confirmed"; next: Done, No-show or Cancelled (UC-SC09-11, UC-SC09-01, UC-SC09-02); fields editable within the role | U13, U33 | `u13-owner/s-sc09-20-practice-assistant-e-sc09-01-appointment-confirmed-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-20-practice-assistant-e-sc09-01-appointment-confirmed-desktop-{light,dark}.png` |

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

- [FL-SC09-01 Appointments](../../flows/fl-sc09-01-appointments.md)

## Open questions

None.

---

⬅️ [S-SC09-19 Certifications](../06-compliance-and-certification/s-sc09-19-certifications.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-21 Pharmacy](../07-pharmacy-vets-dental-and-centres/s-sc09-21-pharmacy.md)

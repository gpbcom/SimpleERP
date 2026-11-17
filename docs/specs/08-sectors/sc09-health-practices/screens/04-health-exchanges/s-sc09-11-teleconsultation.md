🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-04 Health exchanges](README.md) › 🖥️ S-SC09-11 Teleconsultation

# 🖥️ S-SC09-11 Teleconsultation

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to teleconsult ([UC-SC09-11](../../use-cases/04-health-exchanges/uc-sc09-11-teleconsult.md)).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-04 step 3, U13 | desktop | ![FL-SC09-04 step 3, U13, light](../../images/04-health-exchanges/u13-owner/3-teleconsultation-desktop-light.png) | ![FL-SC09-04 step 3, U13, dark](../../images/04-health-exchanges/u13-owner/3-teleconsultation-desktop-dark.png) |
| FL-SC09-04 step 3, U13 | phone | ![FL-SC09-04 step 3, U13, light](../../images/04-health-exchanges/u13-owner/3-teleconsultation-phone-light.png) | ![FL-SC09-04 step 3, U13, dark](../../images/04-health-exchanges/u13-owner/3-teleconsultation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-11-teleconsultation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-11-teleconsultation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-11-teleconsultation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-11-teleconsultation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-11-teleconsultation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-11-teleconsultation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-11-teleconsultation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-11-teleconsultation-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC09-01 Appointment](../../data/e-sc09-01-appointment.md),
[E-SC09-03 Clinical record entry](../../data/e-sc09-03-clinical-record-entry.md), shown as the entity pages list them,
with their examples.

## Actions

- Consult by video: [UC-SC09-11](../../use-cases/04-health-exchanges/uc-sc09-11-teleconsult.md), step 2.
- Report: [UC-SC09-11](../../use-cases/04-health-exchanges/uc-sc09-11-teleconsult.md), step 3.
- Bill: [UC-SC09-11](../../use-cases/04-health-exchanges/uc-sc09-11-teleconsult.md), step 4.

## States

- Normal: the video call, the patient's record and the report.
- Empty: "No teleconsultation".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, outside the rules: the practitioner is warned before billing.
- Read-only: a billed act is read-only.
- Offline: not available offline: a video call needs the network.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC09-04 Health exchanges](../../flows/fl-sc09-04-health-exchanges.md)

## Open questions

None.

---

⬅️ [S-SC09-10 Results](s-sc09-10-results.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-12 Schedules](../05-practice-organisation/s-sc09-12-schedules.md)

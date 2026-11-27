🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-04 Quality system](README.md) › 🖥️ S-SC05-12 Calibration

# 🖥️ S-SC05-12 Calibration

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to calibrate measuring equipment
([UC-SC05-12](../../use-cases/04-quality-system/uc-sc05-12-calibrate-measuring-equipment.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-04 step 4, U27 | desktop | ![FL-SC05-04 step 4, U27, light](../../images/04-quality-system/u27-quality-manager/4-calibration-desktop-light.png) | ![FL-SC05-04 step 4, U27, dark](../../images/04-quality-system/u27-quality-manager/4-calibration-desktop-dark.png) |
| FL-SC05-04 step 4, U27 | tablet | ![FL-SC05-04 step 4, U27, light](../../images/04-quality-system/u27-quality-manager/4-calibration-tablet-light.png) | ![FL-SC05-04 step 4, U27, dark](../../images/04-quality-system/u27-quality-manager/4-calibration-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-12-calibration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-12-calibration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-12-calibration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-12-calibration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-12-calibration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-12-calibration-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-12-calibration-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-12-calibration-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-12 Instrument](../../data/e-sc05-12-instrument.md),
[E-F12-16 Calibration](../../../../02-functional/f12-manufacturing/data/e-f12-16-calibration.md), shown as the entity
pages list them, with their examples.

## Actions

- Plan: [UC-SC05-12](../../use-cases/04-quality-system/uc-sc05-12-calibrate-measuring-equipment.md), step 1.
- Calibrate or send out: [UC-SC05-12](../../use-cases/04-quality-system/uc-sc05-12-calibrate-measuring-equipment.md),
  step 2.
- Record the result: [UC-SC05-12](../../use-cases/04-quality-system/uc-sc05-12-calibrate-measuring-equipment.md), step
  3.
- Plan the next date: [UC-SC05-12](../../use-cases/04-quality-system/uc-sc05-12-calibrate-measuring-equipment.md), step
  4.

## States

- Normal: instruments with last and next calibration, results and certificates.
- Empty: "No instrument".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an overdue instrument: it cannot record checks,
  [BR-SC05-12](../../business-rules/br-sc05-12-instruments-calibrated-before-use.md),
  [BR-F12-16](../../../../02-functional/f12-manufacturing/business-rules/br-f12-16-only-calibrated-instruments-record-checks.md).
- Read-only: operators read the state only.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC05-04 Quality system](../../flows/fl-sc05-04-quality-system.md)

## Open questions

None.

---

⬅️ [S-SC05-11 Complaints 8D](../05-suppliers-and-customers/s-sc05-11-complaints-8d.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-13 Qualifications](../05-suppliers-and-customers/s-sc05-13-qualifications.md)

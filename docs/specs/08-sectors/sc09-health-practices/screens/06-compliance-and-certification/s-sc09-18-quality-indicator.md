🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-06 Compliance and certification](README.md) ›
🖥️ S-SC09-18 Quality indicator

# 🖥️ S-SC09-18 Quality indicator

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to report activity and quality indicators,
[UC-SC09-18](../../use-cases/06-compliance-and-certification/uc-sc09-18-report-activity-and-quality-indicators.md).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-06 step 2, U13 | desktop | ![FL-SC09-06 step 2, U13, light](../../images/06-compliance-and-certification/u13-owner/2-indicators-desktop-light.png) | ![FL-SC09-06 step 2, U13, dark](../../images/06-compliance-and-certification/u13-owner/2-indicators-desktop-dark.png) |
| FL-SC09-06 step 2, U13 | phone | ![FL-SC09-06 step 2, U13, light](../../images/06-compliance-and-certification/u13-owner/2-indicators-phone-light.png) | ![FL-SC09-06 step 2, U13, dark](../../images/06-compliance-and-certification/u13-owner/2-indicators-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-18-indicators-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-18-indicators-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-18-indicators-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-18-indicators-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-18-indicators-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-18-indicators-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-18-indicators-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-18-indicators-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC09-05 Care sheet](../../data/e-sc09-05-care-sheet.md), shown as the entity pages list them, with
their examples.

## Actions

- Compute:
  [UC-SC09-18](../../use-cases/06-compliance-and-certification/uc-sc09-18-report-activity-and-quality-indicators.md),
  step 1.
- Review:
  [UC-SC09-18](../../use-cases/06-compliance-and-certification/uc-sc09-18-report-activity-and-quality-indicators.md),
  step 2.
- Declare:
  [UC-SC09-18](../../use-cases/06-compliance-and-certification/uc-sc09-18-report-activity-and-quality-indicators.md),
  step 3.
- Compare:
  [UC-SC09-18](../../use-cases/06-compliance-and-certification/uc-sc09-18-report-activity-and-quality-indicators.md),
  step 4.

## States

- Normal: indicators per practitioner and specialty.
- Empty: "No data in this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, data missing: it is listed.
- Read-only: declared years are read-only.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC09-06 Compliance and certification](../../flows/fl-sc09-06-compliance-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC09-17 Patients' rights](s-sc09-17-patients-rights.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-19 Certifications](s-sc09-19-certifications.md)

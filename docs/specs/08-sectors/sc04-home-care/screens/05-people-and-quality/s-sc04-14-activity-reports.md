🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-05 People and quality](README.md) › 🖥️ S-SC04-14 Activity reports

# 🖥️ S-SC04-14 Activity reports

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to report activity to funders and authorities,
[UC-SC04-14](../../use-cases/05-people-and-quality/uc-sc04-14-report-activity-to-funders-and-authorities.md).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-05 step 4, U25 | desktop | ![FL-SC04-05 step 4, U25, light](../../images/05-people-and-quality/u25-care-coordinator/4-report-desktop-light.png) | ![FL-SC04-05 step 4, U25, dark](../../images/05-people-and-quality/u25-care-coordinator/4-report-desktop-dark.png) |
| FL-SC04-05 step 4, U25 | phone | ![FL-SC04-05 step 4, U25, light](../../images/05-people-and-quality/u25-care-coordinator/4-report-phone-light.png) | ![FL-SC04-05 step 4, U25, dark](../../images/05-people-and-quality/u25-care-coordinator/4-report-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-14-activity-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-14-activity-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-14-activity-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-14-activity-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-14-activity-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-14-activity-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-14-activity-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-14-activity-reports-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-12 Activity report](../../data/e-sc04-12-activity-report.md),
[E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md), shown as the entity pages list them,
with their examples.

## Actions

- Generate the report:
  [UC-SC04-14](../../use-cases/05-people-and-quality/uc-sc04-14-report-activity-to-funders-and-authorities.md), step 1.
- Check: [UC-SC04-14](../../use-cases/05-people-and-quality/uc-sc04-14-report-activity-to-funders-and-authorities.md),
  step 2.
- Send or file:
  [UC-SC04-14](../../use-cases/05-people-and-quality/uc-sc04-14-report-activity-to-funders-and-authorities.md), step 3.
- Update the grant:
  [UC-SC04-14](../../use-cases/05-people-and-quality/uc-sc04-14-report-activity-to-funders-and-authorities.md), step 4.

## States

- Normal: the report's hours by funder and activity, and grant conditions.
- Empty: "No activity in this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, missing data: the missing items are listed.
- Read-only: a filed report is read-only.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
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

- [FL-SC04-05 People and quality](../../flows/fl-sc04-05-people-and-quality.md)

## Open questions

None.

---

⬅️ [S-SC04-13 Carer skills](s-sc04-13-carer-skills.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-15 Rounds assistant](../03-visit/s-sc04-15-rounds-assistant.md)

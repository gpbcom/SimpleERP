🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-04 Customers and staff](README.md) › 🖥️ S-SC02-12 Schedules

# 🖥️ S-SC02-12 Schedules

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to plan staff schedules and Sunday openings,
[UC-SC02-12](../../use-cases/04-customers-and-staff/uc-sc02-12-plan-staff-schedules-and-sunday-openings.md).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-04 step 3, U23 | desktop | ![FL-SC02-04 step 3, U23, light](../../images/04-customers-and-staff/u23-store-manager/3-schedule-desktop-light.png) | ![FL-SC02-04 step 3, U23, dark](../../images/04-customers-and-staff/u23-store-manager/3-schedule-desktop-dark.png) |
| FL-SC02-04 step 3, U23 | phone | ![FL-SC02-04 step 3, U23, light](../../images/04-customers-and-staff/u23-store-manager/3-schedule-phone-light.png) | ![FL-SC02-04 step 3, U23, dark](../../images/04-customers-and-staff/u23-store-manager/3-schedule-phone-dark.png) |
| FL-SC02-04 step 3, U23 | tablet | ![FL-SC02-04 step 3, U23, light](../../images/04-customers-and-staff/u23-store-manager/3-schedule-tablet-light.png) | ![FL-SC02-04 step 3, U23, dark](../../images/04-customers-and-staff/u23-store-manager/3-schedule-tablet-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/04-customers-and-staff/u23-store-manager/e1-sunday-no-consent-desktop-light.png) | ![Error E1, U23, dark](../../images/04-customers-and-staff/u23-store-manager/e1-sunday-no-consent-desktop-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/04-customers-and-staff/u23-store-manager/e1-sunday-no-consent-phone-light.png) | ![Error E1, U23, dark](../../images/04-customers-and-staff/u23-store-manager/e1-sunday-no-consent-phone-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/04-customers-and-staff/u23-store-manager/e1-sunday-no-consent-tablet-light.png) | ![Error E1, U23, dark](../../images/04-customers-and-staff/u23-store-manager/e1-sunday-no-consent-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-12-schedules-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-12-schedules-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-12-schedules-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-12-schedules-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-12-schedules-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-12-schedules-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-12-schedules-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-12-schedules-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-01 Store](../../data/e-sc02-01-store.md), shown as the entity pages list them, with their
examples.

## Actions

- Draft the week:
  [UC-SC02-12](../../use-cases/04-customers-and-staff/uc-sc02-12-plan-staff-schedules-and-sunday-openings.md), step 1.
- Check the rules:
  [UC-SC02-12](../../use-cases/04-customers-and-staff/uc-sc02-12-plan-staff-schedules-and-sunday-openings.md), step 2.
- Publish: [UC-SC02-12](../../use-cases/04-customers-and-staff/uc-sc02-12-plan-staff-schedules-and-sunday-openings.md),
  step 3.
- Send Sunday pay inputs:
  [UC-SC02-12](../../use-cases/04-customers-and-staff/uc-sc02-12-plan-staff-schedules-and-sunday-openings.md), step 4.

## States

- Normal: the week's shifts per employee with rest times, Sundays and warnings.
- Empty: "No shift this week", with Draft the week.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a Sunday shift without the employee's written consent: the shift
  is refused ([BR-SC02-11](../../business-rules/br-sc02-11-sunday-work-needs-the-exemption.md)).
- Read-only: staff see their own shifts.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
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

- [FL-SC02-04 Customers and staff](../../flows/fl-sc02-04-customers-and-staff.md)

## Open questions

None.

---

⬅️ [S-SC02-11 Targets](s-sc02-11-targets.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-13 Unsold goods](../05-unsold-goods-and-performance/s-sc02-13-unsold-goods.md)

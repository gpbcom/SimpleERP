🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-04 Bill and recognise](README.md) › 🖥️ S-SC03-10 Engagement margin

# 🖥️ S-SC03-10 Engagement margin

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to follow the engagement's budget and margin,
[UC-SC03-10](../../use-cases/04-bill-and-recognise/uc-sc03-10-follow-the-engagement-s-budget-and-margin.md).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-04 step 4, U24 | desktop | ![FL-SC03-04 step 4, U24, light](../../images/04-bill-and-recognise/u24-engagement-manager/4-foreign-client-desktop-light.png) | ![FL-SC03-04 step 4, U24, dark](../../images/04-bill-and-recognise/u24-engagement-manager/4-foreign-client-desktop-dark.png) |
| FL-SC03-04 step 4, U24 | phone | ![FL-SC03-04 step 4, U24, light](../../images/04-bill-and-recognise/u24-engagement-manager/4-foreign-client-phone-light.png) | ![FL-SC03-04 step 4, U24, dark](../../images/04-bill-and-recognise/u24-engagement-manager/4-foreign-client-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-10-engagement-margin-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-10-engagement-margin-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-10-engagement-margin-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-10-engagement-margin-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-10-engagement-margin-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-10-engagement-margin-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-10-engagement-margin-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-10-engagement-margin-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-01 Engagement](../../data/e-sc03-01-engagement.md), shown as the entity pages list them, with
their examples.

## Actions

- Open the engagement:
  [UC-SC03-10](../../use-cases/04-bill-and-recognise/uc-sc03-10-follow-the-engagement-s-budget-and-margin.md), step 1.
- Update the estimate:
  [UC-SC03-10](../../use-cases/04-bill-and-recognise/uc-sc03-10-follow-the-engagement-s-budget-and-margin.md), step 2.
- Act on alerts:
  [UC-SC03-10](../../use-cases/04-bill-and-recognise/uc-sc03-10-follow-the-engagement-s-budget-and-margin.md), step 3.
- Record the decision:
  [UC-SC03-10](../../use-cases/04-bill-and-recognise/uc-sc03-10-follow-the-engagement-s-budget-and-margin.md), step 4.

## States

- Normal: budget, consumed, estimate at completion and margin, with alerts.
- Empty: "No time recorded yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the estimate crosses a threshold: the engagement manager and the
  owner are alerted ([BR-SC03-11](../../business-rules/br-sc03-11-budget-alerts.md)).
- Read-only: consultants do not see margins.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
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

- [FL-SC03-04 Bill and recognise](../../flows/fl-sc03-04-bill-and-recognise.md)

## Open questions

None.

---

⬅️ [S-SC03-09 Freelancers](../03-deliver-and-record/s-sc03-09-freelancers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-11 Client portal](../05-client-and-people/s-sc03-11-client-portal.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-03 Farm business](README.md) › 🖥️ S-SC13-09 Seasonal work

# 🖥️ S-SC13-09 Seasonal work

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Used to employ seasonal workers ([UC-SC13-09](../../use-cases/03-farm-business/uc-sc13-09-employ-seasonal-workers.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-03 step 3, U40 | desktop | ![FL-SC13-03 step 3, U40, light](../../images/03-farm-business/u40-farmer/3-seasonal-desktop-light.png) | ![FL-SC13-03 step 3, U40, dark](../../images/03-farm-business/u40-farmer/3-seasonal-desktop-dark.png) |
| FL-SC13-03 step 3, U40 | phone | ![FL-SC13-03 step 3, U40, light](../../images/03-farm-business/u40-farmer/3-seasonal-phone-light.png) | ![FL-SC13-03 step 3, U40, dark](../../images/03-farm-business/u40-farmer/3-seasonal-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-09-seasonal-work-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-09-seasonal-work-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-09-seasonal-work-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-09-seasonal-work-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-09-seasonal-work-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-09-seasonal-work-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-09-seasonal-work-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-09-seasonal-work-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-08 Seasonal contract](../../data/e-sc13-08-seasonal-contract.md), shown as the entity pages list
them, with their examples.

## Actions

- Hire: [UC-SC13-09](../../use-cases/03-farm-business/uc-sc13-09-employ-seasonal-workers.md), step 1.
- Record time: [UC-SC13-09](../../use-cases/03-farm-business/uc-sc13-09-employ-seasonal-workers.md), step 2.
- Check: [UC-SC13-09](../../use-cases/03-farm-business/uc-sc13-09-employ-seasonal-workers.md), step 3.
- Send to payroll: [UC-SC13-09](../../use-cases/03-farm-business/uc-sc13-09-employ-seasonal-workers.md), step 4.

## States

- Normal: seasonal contracts, time and pay state.
- Empty: "No seasonal worker".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over the ceiling: no exemption applies.
- Read-only: sent inputs are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the day's workers are kept on the phone; hours wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC13-03 Farm business](../../flows/fl-sc13-03-farm-business.md)

## Open questions

None.

---

⬅️ [S-SC13-08 Machinery](s-sc13-08-machinery.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-10 Direct sales](../04-sales-and-certification/s-sc13-10-direct-sales.md)

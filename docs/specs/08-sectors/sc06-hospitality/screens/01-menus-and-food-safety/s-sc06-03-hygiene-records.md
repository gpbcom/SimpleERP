🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-01 Menus and food safety](README.md) › 🖥️ S-SC06-03 Hygiene records

# 🖥️ S-SC06-03 Hygiene records

**Status:** 🔄 waiting for the owner

## Personas

- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to keep food-hygiene records
([UC-SC06-03](../../use-cases/01-menus-and-food-safety/uc-sc06-03-keep-food-hygiene-records.md)).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-01 step 3, U19 | desktop | ![FL-SC06-01 step 3, U19, light](../../images/01-menus-and-food-safety/u19-kitchen-staff/3-hygiene-desktop-light.png) | ![FL-SC06-01 step 3, U19, dark](../../images/01-menus-and-food-safety/u19-kitchen-staff/3-hygiene-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-03-hygiene-records-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-03-hygiene-records-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-03-hygiene-records-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-03-hygiene-records-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-03-hygiene-records-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-03-hygiene-records-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc06-03-hygiene-records-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc06-03-hygiene-records-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC06-03 Hygiene record](../../data/e-sc06-03-hygiene-record.md), shown as the entity pages list them,
with their examples.

## Actions

- Take the reading: [UC-SC06-03](../../use-cases/01-menus-and-food-safety/uc-sc06-03-keep-food-hygiene-records.md), step
  1.
- Record it: [UC-SC06-03](../../use-cases/01-menus-and-food-safety/uc-sc06-03-keep-food-hygiene-records.md), step 2.
- Act if out of range: [UC-SC06-03](../../use-cases/01-menus-and-food-safety/uc-sc06-03-keep-food-hygiene-records.md),
  step 3.
- Review: [UC-SC06-03](../../use-cases/01-menus-and-food-safety/uc-sc06-03-keep-food-hygiene-records.md), step 4.

## States

- Normal: today's readings due and done, values, deviations and actions.
- Empty: "No reading due".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a missed reading: the manager is alerted.
- Read-only: past days are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the day's schedule is kept on the tablet; readings wait and sync in order,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md);
  alerts are sent once synced.

Shown entities (VD-15): [E-SC06-03 Hygiene record](../../data/e-sc06-03-hygiene-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-03 Hygiene record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U19, U23 | `u19-kitchen-staff/s-sc06-03-hygiene-records-e-sc06-03-hygiene-record-recorded-desktop-{light,dark}.png`, `u23-store-manager/s-sc06-03-hygiene-records-e-sc06-03-hygiene-record-recorded-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC06-01 Menus and food safety](../../flows/fl-sc06-01-menus-and-food-safety.md)

## Open questions

None.

---

⬅️ [S-SC06-02 Allergens](s-sc06-02-allergens.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-04 Perishables](../02-kitchen-stock-and-staff/s-sc06-04-perishables.md)

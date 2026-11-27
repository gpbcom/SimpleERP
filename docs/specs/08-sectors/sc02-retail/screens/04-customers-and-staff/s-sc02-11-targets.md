🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-04 Customers and staff](README.md) › 🖥️ S-SC02-11 Targets

# 🖥️ S-SC02-11 Targets

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to set store targets and follow sales per staff,
[UC-SC02-11](../../use-cases/04-customers-and-staff/uc-sc02-11-set-store-targets-and-follow-sales-per-staff.md).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-04 step 2, U23 | desktop | ![FL-SC02-04 step 2, U23, light](../../images/04-customers-and-staff/u23-store-manager/2-targets-desktop-light.png) | ![FL-SC02-04 step 2, U23, dark](../../images/04-customers-and-staff/u23-store-manager/2-targets-desktop-dark.png) |
| FL-SC02-04 step 2, U23 | phone | ![FL-SC02-04 step 2, U23, light](../../images/04-customers-and-staff/u23-store-manager/2-targets-phone-light.png) | ![FL-SC02-04 step 2, U23, dark](../../images/04-customers-and-staff/u23-store-manager/2-targets-phone-dark.png) |
| FL-SC02-04 step 2, U23 | tablet | ![FL-SC02-04 step 2, U23, light](../../images/04-customers-and-staff/u23-store-manager/2-targets-tablet-light.png) | ![FL-SC02-04 step 2, U23, dark](../../images/04-customers-and-staff/u23-store-manager/2-targets-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-11-targets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-11-targets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-11-targets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-11-targets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-11-targets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-11-targets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-11-targets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-11-targets-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-09 Store target](../../data/e-sc02-09-store-target.md), shown as the entity pages list them, with
their examples.

## Actions

- Set store targets:
  [UC-SC02-11](../../use-cases/04-customers-and-staff/uc-sc02-11-set-store-targets-and-follow-sales-per-staff.md), step
  1.
- Split by day and staff:
  [UC-SC02-11](../../use-cases/04-customers-and-staff/uc-sc02-11-set-store-targets-and-follow-sales-per-staff.md), step
  2.
- Follow live:
  [UC-SC02-11](../../use-cases/04-customers-and-staff/uc-sc02-11-set-store-targets-and-follow-sales-per-staff.md), step
  3.
- Review the month:
  [UC-SC02-11](../../use-cases/04-customers-and-staff/uc-sc02-11-set-store-targets-and-follow-sales-per-staff.md), step
  4.

## States

- Normal: targets per store, day and staff with sales to date and the share reached.
- Empty: "No target set", with Set targets.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no staff signed in at the till: the sale counts for the store
  only.
- Read-only: staff see only their own figures.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC02-09 Store target](../../data/e-sc02-09-store-target.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-09 Store target | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U23 | `u13-owner/s-sc02-11-targets-e-sc02-09-store-target-active-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-11-targets-e-sc02-09-store-target-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

⬅️ [S-SC02-10 Customer profile](s-sc02-10-customer-profile.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-12 Schedules](s-sc02-12-schedules.md)

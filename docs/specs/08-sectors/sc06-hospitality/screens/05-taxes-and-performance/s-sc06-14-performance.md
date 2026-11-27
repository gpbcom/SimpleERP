🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-05 Taxes and performance](README.md) › 🖥️ S-SC06-14 Performance

# 🖥️ S-SC06-14 Performance

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to follow occupancy, revenue per room and covers,
[UC-SC06-14](../../use-cases/05-taxes-and-performance/uc-sc06-14-follow-occupancy-revenue-per-room-and-covers.md).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-05 step 3, U13 | desktop | ![FL-SC06-05 step 3, U13, light](../../images/05-taxes-and-performance/u13-owner/3-performance-desktop-light.png) | ![FL-SC06-05 step 3, U13, dark](../../images/05-taxes-and-performance/u13-owner/3-performance-desktop-dark.png) |
| FL-SC06-05 step 3, U13 | phone | ![FL-SC06-05 step 3, U13, light](../../images/05-taxes-and-performance/u13-owner/3-performance-phone-light.png) | ![FL-SC06-05 step 3, U13, dark](../../images/05-taxes-and-performance/u13-owner/3-performance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-14-performance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-14-performance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-14-performance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-14-performance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-14-performance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-14-performance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-14-performance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-14-performance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC06-07 Rate plan](../../data/e-sc06-07-rate-plan.md),
[E-SC06-09 Folio](../../data/e-sc06-09-folio.md), shown as the entity pages list them, with their examples.

## Actions

- Open the dashboard:
  [UC-SC06-14](../../use-cases/05-taxes-and-performance/uc-sc06-14-follow-occupancy-revenue-per-room-and-covers.md),
  step 1.
- Compare:
  [UC-SC06-14](../../use-cases/05-taxes-and-performance/uc-sc06-14-follow-occupancy-revenue-per-room-and-covers.md),
  step 2.
- Drill into covers:
  [UC-SC06-14](../../use-cases/05-taxes-and-performance/uc-sc06-14-follow-occupancy-revenue-per-room-and-covers.md),
  step 3.
- Export:
  [UC-SC06-14](../../use-cases/05-taxes-and-performance/uc-sc06-14-follow-occupancy-revenue-per-room-and-covers.md),
  step 4.

## States

- Normal: occupancy, average rate, revenue per available room and covers per venue.
- Empty: "No data in this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no rates set: revenue per room is not shown.
- Read-only: managers see their own venue.
- Offline: not available offline: front-office and back-office work on live bookings and shared figures. Offline work is
  kept for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC06-07 Rate plan](../../data/e-sc06-07-rate-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-07 Rate plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U23 | `u13-owner/s-sc06-14-performance-e-sc06-07-rate-plan-active-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc06-14-performance-e-sc06-07-rate-plan-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC06-05 Taxes and performance](../../flows/fl-sc06-05-taxes-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC06-13 Meal vouchers](s-sc06-13-meal-vouchers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-15 Hospitality assistant](../03-rooms-and-bookings/s-sc06-15-hospitality-assistant.md)

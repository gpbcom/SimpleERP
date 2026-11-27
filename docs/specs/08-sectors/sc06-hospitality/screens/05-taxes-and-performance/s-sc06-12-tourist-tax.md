🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-05 Taxes and performance](README.md) › 🖥️ S-SC06-12 Tourist tax

# 🖥️ S-SC06-12 Tourist tax

**Status:** ✅ specified

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to collect the tourist tax
([UC-SC06-12](../../use-cases/05-taxes-and-performance/uc-sc06-12-collect-the-tourist-tax.md)).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-05 step 1, U28 | desktop | ![FL-SC06-05 step 1, U28, light](../../images/05-taxes-and-performance/u28-hotel-receptionist/1-tourist-tax-desktop-light.png) | ![FL-SC06-05 step 1, U28, dark](../../images/05-taxes-and-performance/u28-hotel-receptionist/1-tourist-tax-desktop-dark.png) |
| FL-SC06-05 step 1, U28 | tablet | ![FL-SC06-05 step 1, U28, light](../../images/05-taxes-and-performance/u28-hotel-receptionist/1-tourist-tax-tablet-light.png) | ![FL-SC06-05 step 1, U28, dark](../../images/05-taxes-and-performance/u28-hotel-receptionist/1-tourist-tax-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-12-tourist-tax-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-12-tourist-tax-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-12-tourist-tax-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-12-tourist-tax-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-12-tourist-tax-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-12-tourist-tax-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc06-12-tourist-tax-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc06-12-tourist-tax-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC06-11 Tourist tax line](../../data/e-sc06-11-tourist-tax-line.md), shown as the entity pages list
them, with their examples.

## Actions

- Apply per night: [UC-SC06-12](../../use-cases/05-taxes-and-performance/uc-sc06-12-collect-the-tourist-tax.md), step 1.
- Show apart: [UC-SC06-12](../../use-cases/05-taxes-and-performance/uc-sc06-12-collect-the-tourist-tax.md), step 2.
- Declare: [UC-SC06-12](../../use-cases/05-taxes-and-performance/uc-sc06-12-collect-the-tourist-tax.md), step 3.
- Pay: [UC-SC06-12](../../use-cases/05-taxes-and-performance/uc-sc06-12-collect-the-tourist-tax.md), step 4.

## States

- Normal: nights, guests, rate and tax per folio, and the declarations.
- Empty: "No taxable night".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the commune's rate missing: the night is blocked.
- Read-only: a declared period is read-only.
- Offline: not available offline: front-office and back-office work on live bookings and shared figures. Offline work is
  kept for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC06-11 Tourist tax line](../../data/e-sc06-11-tourist-tax-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-11 Tourist tax line | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05, U28 | `u05-accounting/s-sc06-12-tourist-tax-e-sc06-11-tourist-tax-line-recorded-desktop-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-12-tourist-tax-e-sc06-11-tourist-tax-line-recorded-{desktop,tablet}-{light,dark}.png` |

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

⬅️ [S-SC06-11 Folio](../04-stay-and-folio/s-sc06-11-folio.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-13 Meal vouchers](s-sc06-13-meal-vouchers.md)

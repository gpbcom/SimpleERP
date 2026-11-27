🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-04 Import and suppliers](README.md) › 🖥️ S-SC15-13 EU statistics

# 🖥️ S-SC15-13 EU statistics

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to declare EU trade statistics
([UC-SC15-13](../../use-cases/04-import-and-suppliers/uc-sc15-13-declare-eu-trade-statistics.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-04 step 3, U05 | desktop | ![FL-SC15-04 step 3, U05, light](../../images/04-import-and-suppliers/u05-accounting/3-statistics-desktop-light.png) | ![FL-SC15-04 step 3, U05, dark](../../images/04-import-and-suppliers/u05-accounting/3-statistics-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-13-eu-statistics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-13-eu-statistics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-13-eu-statistics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-13-eu-statistics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-13-eu-statistics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-13-eu-statistics-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-13-eu-statistics-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-13-eu-statistics-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC15-10 Statistics return](../../data/e-sc15-10-statistics-return.md), shown as the entity pages list
them, with their examples.

## Actions

- Compile: [UC-SC15-13](../../use-cases/04-import-and-suppliers/uc-sc15-13-declare-eu-trade-statistics.md), step 1.
- Check: [UC-SC15-13](../../use-cases/04-import-and-suppliers/uc-sc15-13-declare-eu-trade-statistics.md), step 2.
- File: [UC-SC15-13](../../use-cases/04-import-and-suppliers/uc-sc15-13-declare-eu-trade-statistics.md), step 3.
- Keep: [UC-SC15-13](../../use-cases/04-import-and-suppliers/uc-sc15-13-declare-eu-trade-statistics.md), step 4.

## States

- Normal: monthly lines and filing state.
- Empty: "No EU delivery".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, data missing: it is listed.
- Read-only: filed months are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-10 Statistics return](../../data/e-sc15-10-statistics-return.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-10 Statistics return | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-sc15-13-eu-statistics-e-sc15-10-statistics-return-recorded-desktop-{light,dark}.png` |

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

- [FL-SC15-04 Import and suppliers](../../flows/fl-sc15-04-import-and-suppliers.md)

## Open questions

None.

---

⬅️ [S-SC15-12 Imports](s-sc15-12-imports.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-14 Visits](../05-sales-force-and-performance/s-sc15-14-visits.md)

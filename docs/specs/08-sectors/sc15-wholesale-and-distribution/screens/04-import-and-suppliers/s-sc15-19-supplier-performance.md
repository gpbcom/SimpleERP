🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-04 Import and suppliers](README.md) › 🖥️ S-SC15-19 Supplier performance

# 🖥️ S-SC15-19 Supplier performance

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Used to follow supplier performance
([UC-SC15-19](../../use-cases/04-import-and-suppliers/uc-sc15-19-follow-supplier-performance.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-04 step 4, U04 | desktop | ![FL-SC15-04 step 4, U04, light](../../images/04-import-and-suppliers/u04-purchasing/4-scorecard-desktop-light.png) | ![FL-SC15-04 step 4, U04, dark](../../images/04-import-and-suppliers/u04-purchasing/4-scorecard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-19-supplier-performance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-19-supplier-performance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-19-supplier-performance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-19-supplier-performance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-19-supplier-performance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-19-supplier-performance-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-19-supplier-performance-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-19-supplier-performance-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC15-13 Supplier scorecard](../../data/e-sc15-13-supplier-scorecard.md), shown as the entity pages list
them, with their examples.

## Actions

- Measure: [UC-SC15-19](../../use-cases/04-import-and-suppliers/uc-sc15-19-follow-supplier-performance.md), step 1.
- Review: [UC-SC15-19](../../use-cases/04-import-and-suppliers/uc-sc15-19-follow-supplier-performance.md), step 2.
- Send the scorecard: [UC-SC15-19](../../use-cases/04-import-and-suppliers/uc-sc15-19-follow-supplier-performance.md),
  step 3.
- Act: [UC-SC15-19](../../use-cases/04-import-and-suppliers/uc-sc15-19-follow-supplier-performance.md), step 4.

## States

- Normal: supplier scores per period.
- Empty: "No score".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, data missing: it is shown.
- Read-only: sent scorecards are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-13 Supplier scorecard](../../data/e-sc15-13-supplier-scorecard.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-13 Supplier scorecard | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-sc15-19-supplier-performance-e-sc15-13-supplier-scorecard-recorded-desktop-{light,dark}.png` |

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

⬅️ [S-SC15-18 B2B portal](../02-orders/s-sc15-18-b2b-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-20 Sales assistant](../05-sales-force-and-performance/s-sc15-20-sales-assistant.md)

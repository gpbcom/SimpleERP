🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-03 Warehouse](README.md) › 🖥️ S-SC15-10 Returns

# 🖥️ S-SC15-10 Returns

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to manage returns and credit notes
([UC-SC15-10](../../use-cases/03-warehouse/uc-sc15-10-manage-returns-and-credit-notes.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-03 step 3, U03 | desktop | ![FL-SC15-03 step 3, U03, light](../../images/03-warehouse/u03-sales/3-returns-desktop-light.png) | ![FL-SC15-03 step 3, U03, dark](../../images/03-warehouse/u03-sales/3-returns-desktop-dark.png) |
| FL-SC15-03 step 3, U03 | phone | ![FL-SC15-03 step 3, U03, light](../../images/03-warehouse/u03-sales/3-returns-phone-light.png) | ![FL-SC15-03 step 3, U03, dark](../../images/03-warehouse/u03-sales/3-returns-phone-dark.png) |
| FL-SC15-03 step 3, U03 | tablet | ![FL-SC15-03 step 3, U03, light](../../images/03-warehouse/u03-sales/3-returns-tablet-light.png) | ![FL-SC15-03 step 3, U03, dark](../../images/03-warehouse/u03-sales/3-returns-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-10-returns-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-10-returns-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-10-returns-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-10-returns-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-10-returns-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-10-returns-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-10-returns-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-10-returns-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-07 Return authorisation](../../data/e-sc15-07-return-authorisation.md), shown as the entity pages
list them, with their examples.

## Actions

- Authorise: [UC-SC15-10](../../use-cases/03-warehouse/uc-sc15-10-manage-returns-and-credit-notes.md), step 1.
- Inspect: [UC-SC15-10](../../use-cases/03-warehouse/uc-sc15-10-manage-returns-and-credit-notes.md), step 2.
- Credit: [UC-SC15-10](../../use-cases/03-warehouse/uc-sc15-10-manage-returns-and-credit-notes.md), step 3.
- Restock or scrap: [UC-SC15-10](../../use-cases/03-warehouse/uc-sc15-10-manage-returns-and-credit-notes.md), step 4.

## States

- Normal: authorisations, inspections and credit notes.
- Empty: "No return".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no authorisation: the return is refused.
- Read-only: credited ones are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-07 Return authorisation](../../data/e-sc15-07-return-authorisation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-07 Return authorisation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U15 | `u03-sales/s-sc15-10-returns-e-sc15-07-return-authorisation-active-{desktop,phone,tablet}-{light,dark}.png`, `u15-warehouse-operator/s-sc15-10-returns-e-sc15-07-return-authorisation-active-{phone,tablet}-{light,dark}.png` |

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

- [FL-SC15-03 Warehouse](../../flows/fl-sc15-03-warehouse.md)

## Open questions

None.

---

⬅️ [S-SC15-09 Pallets](s-sc15-09-pallets.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-11 Supplier funds](../01-prices-and-agreements/s-sc15-11-supplier-funds.md)

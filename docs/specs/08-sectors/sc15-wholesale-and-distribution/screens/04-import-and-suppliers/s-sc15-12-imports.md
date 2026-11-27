🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-04 Import and suppliers](README.md) › 🖥️ S-SC15-12 Imports

# 🖥️ S-SC15-12 Imports

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to import goods ([UC-SC15-12](../../use-cases/04-import-and-suppliers/uc-sc15-12-import-goods.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-04 step 2, U04 | desktop | ![FL-SC15-04 step 2, U04, light](../../images/04-import-and-suppliers/u04-purchasing/2-import-desktop-light.png) | ![FL-SC15-04 step 2, U04, dark](../../images/04-import-and-suppliers/u04-purchasing/2-import-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-12-imports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-12-imports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-12-imports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-12-imports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-12-imports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-12-imports-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-12-imports-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-12-imports-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC15-09 Import file](../../data/e-sc15-09-import-file.md), shown as the entity pages list them, with
their examples.

## Actions

- Prepare the declaration: [UC-SC15-12](../../use-cases/04-import-and-suppliers/uc-sc15-12-import-goods.md), step 1.
- Pay duties: [UC-SC15-12](../../use-cases/04-import-and-suppliers/uc-sc15-12-import-goods.md), step 2.
- Receive: [UC-SC15-12](../../use-cases/04-import-and-suppliers/uc-sc15-12-import-goods.md), step 3.
- Cost: [UC-SC15-12](../../use-cases/04-import-and-suppliers/uc-sc15-12-import-goods.md), step 4.

## States

- Normal: import files with EORI, duties and receipt.
- Empty: "No import".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the EORI missing: the declaration is blocked.
- Read-only: cleared files are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
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

- [FL-SC15-04 Import and suppliers](../../flows/fl-sc15-04-import-and-suppliers.md)

## Open questions

None.

---

⬅️ [S-SC15-11 Supplier funds](../01-prices-and-agreements/s-sc15-11-supplier-funds.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-13 EU statistics](s-sc15-13-eu-statistics.md)

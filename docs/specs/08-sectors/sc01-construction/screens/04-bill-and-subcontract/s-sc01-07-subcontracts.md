🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-04 Bill and subcontract](README.md) › 🖥️ S-SC01-07 Subcontracts

# 🖥️ S-SC01-07 Subcontracts

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Used to subcontract ([UC-SC01-07](../../use-cases/04-bill-and-subcontract/uc-sc01-07-subcontract.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-04 step 2, U22 | desktop | ![FL-SC01-04 step 2, U22, light](../../images/04-bill-and-subcontract/u22-site-manager/2-subcontract-desktop-light.png) | ![FL-SC01-04 step 2, U22, dark](../../images/04-bill-and-subcontract/u22-site-manager/2-subcontract-desktop-dark.png) |
| FL-SC01-04 step 2, U22 | phone | ![FL-SC01-04 step 2, U22, light](../../images/04-bill-and-subcontract/u22-site-manager/2-subcontract-phone-light.png) | ![FL-SC01-04 step 2, U22, dark](../../images/04-bill-and-subcontract/u22-site-manager/2-subcontract-phone-dark.png) |
| FL-SC01-04 step 2, U22 | tablet | ![FL-SC01-04 step 2, U22, light](../../images/04-bill-and-subcontract/u22-site-manager/2-subcontract-tablet-light.png) | ![FL-SC01-04 step 2, U22, dark](../../images/04-bill-and-subcontract/u22-site-manager/2-subcontract-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-07-subcontracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-07-subcontracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-07-subcontracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-07-subcontracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-07-subcontracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-07-subcontracts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-07-subcontracts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-07-subcontracts-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-07 Subcontract](../../data/e-sc01-07-subcontract.md), shown as the entity pages list them, with
their examples.

## Actions

- Create the subcontract: [UC-SC01-07](../../use-cases/04-bill-and-subcontract/uc-sc01-07-subcontract.md), step 1.
- Collect the documents: [UC-SC01-07](../../use-cases/04-bill-and-subcontract/uc-sc01-07-subcontract.md), step 2.
- Get the owner's acceptance: [UC-SC01-07](../../use-cases/04-bill-and-subcontract/uc-sc01-07-subcontract.md), step 3.
- Receive and pay its bills: [UC-SC01-07](../../use-cases/04-bill-and-subcontract/uc-sc01-07-subcontract.md), step 4.

## States

- Normal: the subcontracts with lot, amount, acceptance, documents and their dates, invoices and payments.
- Empty: "No subcontract", with New subcontract.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a vigilance certificate older than 6 months: the subcontractor is
  flagged and cannot be planned ([BR-SC01-06](../../business-rules/br-sc01-06-subcontractor-documents-before-work.md)).
- Read-only: a closed subcontract is read-only.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC01-04 Bill and subcontract](../../flows/fl-sc01-04-bill-and-subcontract.md)

## Open questions

None.

---

⬅️ [S-SC01-06 Progress bill](s-sc01-06-progress-bill.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-08 Equipment](../02-prepare-the-site/s-sc01-08-equipment.md)

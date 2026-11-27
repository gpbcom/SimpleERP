🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-05 Suppliers and customers](README.md) ›
🖥️ S-SC05-10 Supplier quality

# 🖥️ S-SC05-10 Supplier quality

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Used to evaluate and qualify suppliers
([UC-SC05-10](../../use-cases/05-suppliers-and-customers/uc-sc05-10-evaluate-and-qualify-suppliers.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-05 step 1, U27 | desktop | ![FL-SC05-05 step 1, U27, light](../../images/05-suppliers-and-customers/u27-quality-manager/1-suppliers-desktop-light.png) | ![FL-SC05-05 step 1, U27, dark](../../images/05-suppliers-and-customers/u27-quality-manager/1-suppliers-desktop-dark.png) |
| FL-SC05-05 step 1, U27 | tablet | ![FL-SC05-05 step 1, U27, light](../../images/05-suppliers-and-customers/u27-quality-manager/1-suppliers-tablet-light.png) | ![FL-SC05-05 step 1, U27, dark](../../images/05-suppliers-and-customers/u27-quality-manager/1-suppliers-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-10-supplier-quality-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-10-supplier-quality-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-10-supplier-quality-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-10-supplier-quality-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-10-supplier-quality-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-10-supplier-quality-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-10-supplier-quality-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-10-supplier-quality-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-10 Supplier rating](../../data/e-sc05-10-supplier-rating.md), shown as the entity pages list them,
with their examples.

## Actions

- Rate: [UC-SC05-10](../../use-cases/05-suppliers-and-customers/uc-sc05-10-evaluate-and-qualify-suppliers.md), step 1.
- Qualify or not: [UC-SC05-10](../../use-cases/05-suppliers-and-customers/uc-sc05-10-evaluate-and-qualify-suppliers.md),
  step 2.
- Review yearly: [UC-SC05-10](../../use-cases/05-suppliers-and-customers/uc-sc05-10-evaluate-and-qualify-suppliers.md),
  step 3.
- Order from the list:
  [UC-SC05-10](../../use-cases/05-suppliers-and-customers/uc-sc05-10-evaluate-and-qualify-suppliers.md), step 4.

## States

- Normal: suppliers with score, status, audits and conditions.
- Empty: "No supplier rated".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a purchase of a critical item from an unqualified supplier: the
  order is blocked ([BR-SC05-10](../../business-rules/br-sc05-10-suppliers-qualified-before-use.md)).
- Read-only: purchasing reads; quality qualifies.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
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

- [FL-SC05-05 Suppliers and customers](../../flows/fl-sc05-05-suppliers-and-customers.md)

## Open questions

None.

---

⬅️ [S-SC05-09 Actions](../04-quality-system/s-sc05-09-actions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-11 Complaints 8D](s-sc05-11-complaints-8d.md)

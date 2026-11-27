🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-04 Rents and landlords](README.md) › 🖥️ S-SC10-09 Indexation

# 🖥️ S-SC10-09 Indexation

**Status:** 🔄 waiting for the owner

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)

## Purpose

Used to index rents within the caps
([UC-SC10-09](../../use-cases/04-rents-and-landlords/uc-sc10-09-index-rents-within-the-caps.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-04 step 2, U34 | desktop | ![FL-SC10-04 step 2, U34, light](../../images/04-rents-and-landlords/u34-property-manager/2-indexation-desktop-light.png) | ![FL-SC10-04 step 2, U34, dark](../../images/04-rents-and-landlords/u34-property-manager/2-indexation-desktop-dark.png) |
| FL-SC10-04 step 2, U34 | tablet | ![FL-SC10-04 step 2, U34, light](../../images/04-rents-and-landlords/u34-property-manager/2-indexation-tablet-light.png) | ![FL-SC10-04 step 2, U34, dark](../../images/04-rents-and-landlords/u34-property-manager/2-indexation-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-09-indexation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-09-indexation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-09-indexation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-09-indexation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-09-indexation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-09-indexation-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-09-indexation-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-09-indexation-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-07 Lease](../../data/e-sc10-07-lease.md), shown as the entity pages list them, with their
examples.

## Actions

- Compute: [UC-SC10-09](../../use-cases/04-rents-and-landlords/uc-sc10-09-index-rents-within-the-caps.md), step 1.
- Check the rules: [UC-SC10-09](../../use-cases/04-rents-and-landlords/uc-sc10-09-index-rents-within-the-caps.md), step
  2.
- Notify: [UC-SC10-09](../../use-cases/04-rents-and-landlords/uc-sc10-09-index-rents-within-the-caps.md), step 3.
- Apply: [UC-SC10-09](../../use-cases/04-rents-and-landlords/uc-sc10-09-index-rents-within-the-caps.md), step 4.

## States

- Normal: leases due, old and new rent and blocks.
- Empty: "No revision due".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a home rated F or G: the revision is blocked.
- Read-only: applied revisions are read-only.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
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

- [FL-SC10-04 Rents and landlords](../../flows/fl-sc10-04-rents-and-landlords.md)

## Open questions

None.

---

⬅️ [S-SC10-08 Rents](s-sc10-08-rents.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-10 Deposits](../03-lettings/s-sc10-10-deposits.md)

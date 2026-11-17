🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-02 Enrol and fund](README.md) › 🖥️ S-SC12-10 Billing

# 🖥️ S-SC12-10 Billing

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Purpose

Used to bill learners, employers and funders
([UC-SC12-10](../../use-cases/02-enrol-and-fund/uc-sc12-10-bill-learners-employers-and-funders.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-02 step 4, U05 | desktop | ![FL-SC12-02 step 4, U05, light](../../images/02-enrol-and-fund/u05-accounting/4-billing-desktop-light.png) | ![FL-SC12-02 step 4, U05, dark](../../images/02-enrol-and-fund/u05-accounting/4-billing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-10-billing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-10-billing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-10-billing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-10-billing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-10-billing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-10-billing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-10-billing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-10-billing-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-10 Training invoice](../../data/e-sc12-10-training-invoice.md), shown as the entity pages list
them, with their examples.

## Actions

- Close the session: [UC-SC12-10](../../use-cases/02-enrol-and-fund/uc-sc12-10-bill-learners-employers-and-funders.md),
  step 1.
- Compute shares: [UC-SC12-10](../../use-cases/02-enrol-and-fund/uc-sc12-10-bill-learners-employers-and-funders.md),
  step 2.
- Attach attendance: [UC-SC12-10](../../use-cases/02-enrol-and-fund/uc-sc12-10-bill-learners-employers-and-funders.md),
  step 3.
- Bill: [UC-SC12-10](../../use-cases/02-enrol-and-fund/uc-sc12-10-bill-learners-employers-and-funders.md), step 4.

## States

- Normal: per session: payers, shares, attendance and invoices.
- Empty: "Nothing to bill".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, attendance missing: the funder's invoice is held.
- Read-only: sent invoices are read-only.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
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

- [FL-SC12-02 Enrol and fund](../../flows/fl-sc12-02-enrol-and-fund.md)

## Open questions

None.

---

⬅️ [S-SC12-09 Satisfaction](../03-deliver-and-assess/s-sc12-09-satisfaction.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-11 Trainers](../01-offer-and-sessions/s-sc12-11-trainers.md)

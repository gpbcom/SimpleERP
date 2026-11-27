🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-06 Logistics for clients](README.md) › 🖥️ S-SC07-15 Storage billing

# 🖥️ S-SC07-15 Storage billing

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to bill storage and handling
([UC-SC07-15](../../use-cases/06-logistics-for-clients/uc-sc07-15-bill-storage-and-handling.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-06 step 2, U05 | desktop | ![FL-SC07-06 step 2, U05, light](../../images/06-logistics-for-clients/u05-accounting/2-storage-billing-desktop-light.png) | ![FL-SC07-06 step 2, U05, dark](../../images/06-logistics-for-clients/u05-accounting/2-storage-billing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-15-storage-billing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-15-storage-billing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-15-storage-billing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-15-storage-billing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-15-storage-billing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-15-storage-billing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc07-15-storage-billing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc07-15-storage-billing-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC07-13 Transport invoice line](../../data/e-sc07-13-transport-invoice-line.md),
[E-SC07-14 Client stock](../../data/e-sc07-14-client-stock.md), shown as the entity pages list them, with their
examples.

## Actions

- Compute: [UC-SC07-15](../../use-cases/06-logistics-for-clients/uc-sc07-15-bill-storage-and-handling.md), step 1.
- Check: [UC-SC07-15](../../use-cases/06-logistics-for-clients/uc-sc07-15-bill-storage-and-handling.md), step 2.
- Bill: [UC-SC07-15](../../use-cases/06-logistics-for-clients/uc-sc07-15-bill-storage-and-handling.md), step 3.
- Follow payment: [UC-SC07-15](../../use-cases/06-logistics-for-clients/uc-sc07-15-bill-storage-and-handling.md), step
  4.

## States

- Normal: pallet-days and movements per client and the invoice.
- Empty: "Nothing to bill".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a rate missing: the invoice is held.
- Read-only: a sent invoice is read-only.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-14 Client stock](../../data/e-sc07-14-client-stock.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-14 Client stock | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-sc07-15-storage-billing-e-sc07-14-client-stock-active-desktop-{light,dark}.png` |

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

- [FL-SC07-06 Logistics for clients](../../flows/fl-sc07-06-logistics-for-clients.md)

## Open questions

None.

---

⬅️ [S-SC07-14 Client warehouse](s-sc07-14-client-warehouse.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-16 Client portal](s-sc07-16-client-portal.md)

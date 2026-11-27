🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-06 Logistics for clients](README.md) › 🖥️ S-SC07-14 Client warehouse

# 🖥️ S-SC07-14 Client warehouse

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Used to run warehouse logistics for clients,
[UC-SC07-14](../../use-cases/06-logistics-for-clients/uc-sc07-14-run-warehouse-logistics-for-clients.md).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-06 step 1, U15 | phone | ![FL-SC07-06 step 1, U15, light](../../images/06-logistics-for-clients/u15-warehouse-operator/1-warehouse-phone-light.png) | ![FL-SC07-06 step 1, U15, dark](../../images/06-logistics-for-clients/u15-warehouse-operator/1-warehouse-phone-dark.png) |
| FL-SC07-06 step 1, U15 | tablet | ![FL-SC07-06 step 1, U15, light](../../images/06-logistics-for-clients/u15-warehouse-operator/1-warehouse-tablet-light.png) | ![FL-SC07-06 step 1, U15, dark](../../images/06-logistics-for-clients/u15-warehouse-operator/1-warehouse-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc07-14-client-warehouse-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc07-14-client-warehouse-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc07-14-client-warehouse-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc07-14-client-warehouse-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc07-14-client-warehouse-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc07-14-client-warehouse-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-14-client-warehouse-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-14-client-warehouse-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-14 Client stock](../../data/e-sc07-14-client-stock.md), shown as the entity pages list them, with
their examples.

## Actions

- Receive: [UC-SC07-14](../../use-cases/06-logistics-for-clients/uc-sc07-14-run-warehouse-logistics-for-clients.md),
  step 1.
- Store: [UC-SC07-14](../../use-cases/06-logistics-for-clients/uc-sc07-14-run-warehouse-logistics-for-clients.md), step
  2.
- Pick and ship:
  [UC-SC07-14](../../use-cases/06-logistics-for-clients/uc-sc07-14-run-warehouse-logistics-for-clients.md), step 3.
- Plan the delivery:
  [UC-SC07-14](../../use-cases/06-logistics-for-clients/uc-sc07-14-run-warehouse-logistics-for-clients.md), step 4.

## States

- Normal: clients' stock by location, receipts and orders to pick.
- Empty: "No client stock".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the client's stock short: the client is told.
- Read-only: a shipped order is read-only.
- Offline: scans are kept on the warehouse phone and sync later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC07-14 Client stock](../../data/e-sc07-14-client-stock.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-14 Client stock | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15, U29 | `u15-warehouse-operator/s-sc07-14-client-warehouse-e-sc07-14-client-stock-active-{phone,tablet}-{light,dark}.png`, `u29-dispatcher/s-sc07-14-client-warehouse-e-sc07-14-client-stock-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC07-13 Transport billing](../05-billing-and-performance/s-sc07-13-transport-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-15 Storage billing](s-sc07-15-storage-billing.md)

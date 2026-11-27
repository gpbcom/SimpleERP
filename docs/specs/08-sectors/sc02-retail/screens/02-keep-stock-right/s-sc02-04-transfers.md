🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-02 Keep stock right](README.md) › 🖥️ S-SC02-04 Transfers

# 🖥️ S-SC02-04 Transfers

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to transfer stock between stores
([UC-SC02-04](../../use-cases/02-keep-stock-right/uc-sc02-04-transfer-stock-between-stores.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-02 step 2, U23 | phone | ![FL-SC02-02 step 2, U23, light](../../images/02-keep-stock-right/u23-store-manager/2-transfer-phone-light.png) | ![FL-SC02-02 step 2, U23, dark](../../images/02-keep-stock-right/u23-store-manager/2-transfer-phone-dark.png) |
| FL-SC02-02 step 2, U23 | desktop | ![FL-SC02-02 step 2, U23, light](../../images/02-keep-stock-right/u23-store-manager/2-transfer-desktop-light.png) | ![FL-SC02-02 step 2, U23, dark](../../images/02-keep-stock-right/u23-store-manager/2-transfer-desktop-dark.png) |
| FL-SC02-02 step 2, U23 | tablet | ![FL-SC02-02 step 2, U23, light](../../images/02-keep-stock-right/u23-store-manager/2-transfer-tablet-light.png) | ![FL-SC02-02 step 2, U23, dark](../../images/02-keep-stock-right/u23-store-manager/2-transfer-tablet-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/02-keep-stock-right/u23-store-manager/e1-transfer-difference-phone-light.png) | ![Error E1, U23, dark](../../images/02-keep-stock-right/u23-store-manager/e1-transfer-difference-phone-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/02-keep-stock-right/u23-store-manager/e1-transfer-difference-desktop-light.png) | ![Error E1, U23, dark](../../images/02-keep-stock-right/u23-store-manager/e1-transfer-difference-desktop-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/02-keep-stock-right/u23-store-manager/e1-transfer-difference-tablet-light.png) | ![Error E1, U23, dark](../../images/02-keep-stock-right/u23-store-manager/e1-transfer-difference-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-04-transfers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-04-transfers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-04-transfers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-04-transfers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-04-transfers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-04-transfers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-04-transfers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-04-transfers-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-06 Store transfer](../../data/e-sc02-06-store-transfer.md), shown as the entity pages list them,
with their examples.

## Actions

- Create or accept the transfer:
  [UC-SC02-04](../../use-cases/02-keep-stock-right/uc-sc02-04-transfer-stock-between-stores.md), step 1.
- Send: [UC-SC02-04](../../use-cases/02-keep-stock-right/uc-sc02-04-transfer-stock-between-stores.md), step 2.
- Receive: [UC-SC02-04](../../use-cases/02-keep-stock-right/uc-sc02-04-transfer-stock-between-stores.md), step 3.
- Close the transfer: [UC-SC02-04](../../use-cases/02-keep-stock-right/uc-sc02-04-transfer-stock-between-stores.md),
  step 4.

## States

- Normal: the transfers with from, to, lines, state and differences.
- Empty: "No transfer", with New transfer.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a difference at receipt: the reason is asked and the difference
  recorded ([BR-SC02-07](../../business-rules/br-sc02-07-transfers-in-transit.md)).
- Read-only: a received transfer is read-only.
- Offline: scans at receipt are kept on the phone and sync when the network is back,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC02-06 Store transfer](../../data/e-sc02-06-store-transfer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-06 Store transfer | Draft | Badge "Draft"; a new record starts here; next: Sent (BR-SC02-07); fields editable within the role | U23 | `u23-store-manager/s-sc02-04-transfers-e-sc02-06-store-transfer-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-06 Store transfer | Sent | Badge "Sent"; next: In transit (UC-SC02-04); fields editable within the role | U23 | `u23-store-manager/s-sc02-04-transfers-e-sc02-06-store-transfer-sent-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-06 Store transfer | In transit | Badge "In transit"; next: Received (UC-SC02-04); fields editable within the role | U23 | `u23-store-manager/s-sc02-04-transfers-e-sc02-06-store-transfer-in-transit-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC02-02 Keep stock right](../../flows/fl-sc02-02-keep-stock-right.md)

## Open questions

None.

---

⬅️ [S-SC02-03 Replenishment](s-sc02-03-replenishment.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-05 Labels](../01-set-up-the-stores/s-sc02-05-labels.md)

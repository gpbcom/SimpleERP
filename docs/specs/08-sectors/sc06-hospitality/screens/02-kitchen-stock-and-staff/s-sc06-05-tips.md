🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-02 Kitchen stock and staff](README.md) › 🖥️ S-SC06-05 Tips

# 🖥️ S-SC06-05 Tips

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)

## Purpose

Share the period's card and cash tips, in full, among the staff in contact with customers, by the key the company set
([UC-SC06-05](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-05-share-tips.md),
[CR-FR-113](../../../../10-country-packs/france/labour/cr-fr-113-tips-sharing.md)).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-02 step 2, U23 | desktop | ![FL-SC06-02 step 2, U23, light](../../images/02-kitchen-stock-and-staff/u23-store-manager/2-tips-desktop-light.png) | ![FL-SC06-02 step 2, U23, dark](../../images/02-kitchen-stock-and-staff/u23-store-manager/2-tips-desktop-dark.png) |
| FL-SC06-02 step 2, U23 | phone | ![FL-SC06-02 step 2, U23, light](../../images/02-kitchen-stock-and-staff/u23-store-manager/2-tips-phone-light.png) | ![FL-SC06-02 step 2, U23, dark](../../images/02-kitchen-stock-and-staff/u23-store-manager/2-tips-phone-dark.png) |
| FL-SC06-02 step 2, U23 | tablet | ![FL-SC06-02 step 2, U23, light](../../images/02-kitchen-stock-and-staff/u23-store-manager/2-tips-tablet-light.png) | ![FL-SC06-02 step 2, U23, dark](../../images/02-kitchen-stock-and-staff/u23-store-manager/2-tips-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-05-tips-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-05-tips-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-05-tips-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-05-tips-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-05-tips-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-05-tips-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-05-tips-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-05-tips-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC06-05 Staff benefit](../../data/e-sc06-05-staff-benefit.md), shown as the entity pages list them,
with their examples.

## Actions

- Record tips: [UC-SC06-05](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-05-share-tips.md), step 1.
- Apply the key: [UC-SC06-05](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-05-share-tips.md), step 2.
- Check shares: [UC-SC06-05](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-05-share-tips.md), step 3.
- Pay out: [UC-SC06-05](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-05-share-tips.md), step 4.

## States

- Normal: the period's tips, the key and the share of each person in contact with customers; staff without contact
  with customers, such as the kitchen, are not in the list.
- Empty: "No tips this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no key set: tips are held until one is set.
- Read-only: staff read their own share.
- Offline: not available offline: front-office and back-office work on live bookings and shared figures. Offline work is
  kept for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC06-05 Staff benefit](../../data/e-sc06-05-staff-benefit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-05 Staff benefit | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U18, U23 | `u18-waiter/s-sc06-05-tips-e-sc06-05-staff-benefit-active-{phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc06-05-tips-e-sc06-05-staff-benefit-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC06-02 Kitchen stock and staff](../../flows/fl-sc06-02-kitchen-stock-and-staff.md)

## Open questions

None.

---

⬅️ [S-SC06-04 Perishables](s-sc06-04-perishables.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-06 Staff meals](s-sc06-06-staff-meals.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-01 Set up the stores](README.md) › 🖥️ S-SC02-01 Stores

# 🖥️ S-SC02-01 Stores

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to set up stores and their assortments
([UC-SC02-01](../../use-cases/01-set-up-the-stores/uc-sc02-01-set-up-stores-and-their-assortments.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-01 step 1, U23 | desktop | ![FL-SC02-01 step 1, U23, light](../../images/01-set-up-the-stores/u23-store-manager/1-stores-desktop-light.png) | ![FL-SC02-01 step 1, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/1-stores-desktop-dark.png) |
| FL-SC02-01 step 1, U23 | phone | ![FL-SC02-01 step 1, U23, light](../../images/01-set-up-the-stores/u23-store-manager/1-stores-phone-light.png) | ![FL-SC02-01 step 1, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/1-stores-phone-dark.png) |
| FL-SC02-01 step 1, U23 | tablet | ![FL-SC02-01 step 1, U23, light](../../images/01-set-up-the-stores/u23-store-manager/1-stores-tablet-light.png) | ![FL-SC02-01 step 1, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/1-stores-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-01-stores-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-01-stores-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-01-stores-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-01-stores-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-01-stores-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-01-stores-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-01-stores-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-01-stores-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-01 Store](../../data/e-sc02-01-store.md),
[E-SC02-02 Assortment](../../data/e-sc02-02-assortment.md), shown as the entity pages list them, with their examples.

## Actions

- Create the store:
  [UC-SC02-01](../../use-cases/01-set-up-the-stores/uc-sc02-01-set-up-stores-and-their-assortments.md), step 1.
- Choose its assortment:
  [UC-SC02-01](../../use-cases/01-set-up-the-stores/uc-sc02-01-set-up-stores-and-their-assortments.md), step 2.
- Set its tills: [UC-SC02-01](../../use-cases/01-set-up-the-stores/uc-sc02-01-set-up-stores-and-their-assortments.md),
  step 3.
- Open the store: [UC-SC02-01](../../use-cases/01-set-up-the-stores/uc-sc02-01-set-up-stores-and-their-assortments.md),
  step 4.

## States

- Normal: the stores with address, surface, hours, exemptions, tills, assortment and state.
- Empty: "No store yet", with New store.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a product outside the assortment is scanned at the till: the sale
  goes through and the store manager is warned.
- Read-only: store staff read their own store only.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC02-02 Assortment](../../data/e-sc02-02-assortment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-02 Assortment | New | Badge "New"; a new record starts here; next: Active (UC-SC02-01); fields editable within the role | U13, U23 | `u13-owner/s-sc02-01-stores-e-sc02-02-assortment-new-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-01-stores-e-sc02-02-assortment-new-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC02-01 Set up the stores](../../flows/fl-sc02-01-set-up-the-stores.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC02-02 Collections](s-sc02-02-collections.md)

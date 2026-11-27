🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-02 Prepare the site](README.md) › 🖥️ S-SC01-08 Equipment

# 🖥️ S-SC01-08 Equipment

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Used to rent and track equipment on sites
([UC-SC01-08](../../use-cases/02-prepare-the-site/uc-sc01-08-rent-and-track-equipment-on-sites.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-02 step 2, U22 | desktop | ![FL-SC01-02 step 2, U22, light](../../images/02-prepare-the-site/u22-site-manager/2-equipment-desktop-light.png) | ![FL-SC01-02 step 2, U22, dark](../../images/02-prepare-the-site/u22-site-manager/2-equipment-desktop-dark.png) |
| FL-SC01-02 step 2, U22 | phone | ![FL-SC01-02 step 2, U22, light](../../images/02-prepare-the-site/u22-site-manager/2-equipment-phone-light.png) | ![FL-SC01-02 step 2, U22, dark](../../images/02-prepare-the-site/u22-site-manager/2-equipment-phone-dark.png) |
| FL-SC01-02 step 2, U22 | tablet | ![FL-SC01-02 step 2, U22, light](../../images/02-prepare-the-site/u22-site-manager/2-equipment-tablet-light.png) | ![FL-SC01-02 step 2, U22, dark](../../images/02-prepare-the-site/u22-site-manager/2-equipment-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-08-equipment-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-08-equipment-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-08-equipment-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-08-equipment-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-08-equipment-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-08-equipment-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-08-equipment-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-08-equipment-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-08 Equipment assignment](../../data/e-sc01-08-equipment-assignment.md), shown as the entity pages
list them, with their examples.

## Actions

- Book equipment for the phase:
  [UC-SC01-08](../../use-cases/02-prepare-the-site/uc-sc01-08-rent-and-track-equipment-on-sites.md), step 1.
- Rent from an outside firm:
  [UC-SC01-08](../../use-cases/02-prepare-the-site/uc-sc01-08-rent-and-track-equipment-on-sites.md), step 2.
- Move it between sites:
  [UC-SC01-08](../../use-cases/02-prepare-the-site/uc-sc01-08-rent-and-track-equipment-on-sites.md), step 3.
- Return it: [UC-SC01-08](../../use-cases/02-prepare-the-site/uc-sc01-08-rent-and-track-equipment-on-sites.md), step 4.

## States

- Normal: the equipment with its site, dates, owned or rented and daily cost.
- Empty: "No equipment booked".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the equipment is already booked: the booking is refused with the
  free dates,
  [BR-F2-18](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-18-one-booking-per-resource-and-slot.md).
- Read-only: a returned booking is read-only.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC01-08 Equipment assignment](../../data/e-sc01-08-equipment-assignment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-08 Equipment assignment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04, U22 | `u04-purchasing/s-sc01-08-equipment-e-sc01-08-equipment-assignment-active-desktop-{light,dark}.png`, `u22-site-manager/s-sc01-08-equipment-e-sc01-08-equipment-assignment-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC01-02 Prepare the site](../../flows/fl-sc01-02-prepare-the-site.md)

## Open questions

None.

---

⬅️ [S-SC01-07 Subcontracts](../04-bill-and-subcontract/s-sc01-07-subcontracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-09 Works declarations](s-sc01-09-works-declarations.md)

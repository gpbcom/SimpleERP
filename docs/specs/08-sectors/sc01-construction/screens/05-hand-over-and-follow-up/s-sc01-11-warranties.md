🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-05 Hand over and follow up](README.md) › 🖥️ S-SC01-11 Warranties

# 🖥️ S-SC01-11 Warranties

**Status:** ✅ specified

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to hand over the as-built file and follow the warranties,
[UC-SC01-11](../../use-cases/05-hand-over-and-follow-up/uc-sc01-11-hand-over-the-as-built-file-and-follow-the-warranties.md).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-05 step 2, U22 | desktop | ![FL-SC01-05 step 2, U22, light](../../images/05-hand-over-and-follow-up/u22-site-manager/2-warranties-desktop-light.png) | ![FL-SC01-05 step 2, U22, dark](../../images/05-hand-over-and-follow-up/u22-site-manager/2-warranties-desktop-dark.png) |
| FL-SC01-05 step 2, U22 | phone | ![FL-SC01-05 step 2, U22, light](../../images/05-hand-over-and-follow-up/u22-site-manager/2-warranties-phone-light.png) | ![FL-SC01-05 step 2, U22, dark](../../images/05-hand-over-and-follow-up/u22-site-manager/2-warranties-phone-dark.png) |
| FL-SC01-05 step 2, U22 | tablet | ![FL-SC01-05 step 2, U22, light](../../images/05-hand-over-and-follow-up/u22-site-manager/2-warranties-tablet-light.png) | ![FL-SC01-05 step 2, U22, dark](../../images/05-hand-over-and-follow-up/u22-site-manager/2-warranties-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-11-warranties-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-11-warranties-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-11-warranties-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-11-warranties-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-11-warranties-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-11-warranties-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-11-warranties-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-11-warranties-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-11 Warranty](../../data/e-sc01-11-warranty.md),
[E-SC01-10 Acceptance record](../../data/e-sc01-10-acceptance-record.md), shown as the entity pages list them, with
their examples.

## Actions

- Assemble the file:
  [UC-SC01-11](../../use-cases/05-hand-over-and-follow-up/uc-sc01-11-hand-over-the-as-built-file-and-follow-the-warranties.md),
  step 1.
- Hand it over:
  [UC-SC01-11](../../use-cases/05-hand-over-and-follow-up/uc-sc01-11-hand-over-the-as-built-file-and-follow-the-warranties.md),
  step 2.
- Make a claim:
  [UC-SC01-11](../../use-cases/05-hand-over-and-follow-up/uc-sc01-11-hand-over-the-as-built-file-and-follow-the-warranties.md),
  step 3.
- Handle the claim:
  [UC-SC01-11](../../use-cases/05-hand-over-and-follow-up/uc-sc01-11-hand-over-the-as-built-file-and-follow-the-warranties.md),
  step 4.

## States

- Normal: the as-built file's documents, the three warranties with their end dates, and the claims.
- Empty: "No claim".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a claim after the warranty's end: it is refused with the end
  date.
- Read-only: the customer reads the file and the claims on the portal.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC01-13 As-built file](../../data/e-sc01-13-as-built-file.md),
[E-SC01-11 Warranty](../../data/e-sc01-11-warranty.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-13 As-built file | Active | Badge "Active"; a new record starts here; next: Handed over (UC-SC01-11); fields editable within the role | U09, U22 | `u09-customer/s-sc01-11-warranties-e-sc01-13-as-built-file-active-phone-{light,dark}.png`, `u22-site-manager/s-sc01-11-warranties-e-sc01-13-as-built-file-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-13 As-built file | Handed over | Badge "Handed over"; final: read-only, no next state; the history shows how it got here | U09, U22 | `u09-customer/s-sc01-11-warranties-e-sc01-13-as-built-file-handed-over-phone-{light,dark}.png`, `u22-site-manager/s-sc01-11-warranties-e-sc01-13-as-built-file-handed-over-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-11 Warranty | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U22 | `u09-customer/s-sc01-11-warranties-e-sc01-11-warranty-active-phone-{light,dark}.png`, `u22-site-manager/s-sc01-11-warranties-e-sc01-11-warranty-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-05 Hand over and follow up](../../flows/fl-sc01-05-hand-over-and-follow-up.md)

## Open questions

None.

---

⬅️ [S-SC01-10 Acceptance](s-sc01-10-acceptance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-12 Renovation sale](../01-win-the-work/s-sc01-12-renovation-sale.md)

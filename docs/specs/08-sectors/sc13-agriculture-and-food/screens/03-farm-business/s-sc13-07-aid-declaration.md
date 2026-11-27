🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-03 Farm business](README.md) › 🖥️ S-SC13-07 Aid declaration

# 🖥️ S-SC13-07 Aid declaration

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to declare CAP aid ([UC-SC13-07](../../use-cases/03-farm-business/uc-sc13-07-declare-cap-aid.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-03 step 1, U40 | desktop | ![FL-SC13-03 step 1, U40, light](../../images/03-farm-business/u40-farmer/1-aid-desktop-light.png) | ![FL-SC13-03 step 1, U40, dark](../../images/03-farm-business/u40-farmer/1-aid-desktop-dark.png) |
| FL-SC13-03 step 1, U40 | phone | ![FL-SC13-03 step 1, U40, light](../../images/03-farm-business/u40-farmer/1-aid-phone-light.png) | ![FL-SC13-03 step 1, U40, dark](../../images/03-farm-business/u40-farmer/1-aid-phone-dark.png) |
| Error E1, U40 | desktop | ![Error E1, U40, light](../../images/03-farm-business/u40-farmer/e1-aid-plot-changed-desktop-light.png) | ![Error E1, U40, dark](../../images/03-farm-business/u40-farmer/e1-aid-plot-changed-desktop-dark.png) |
| Error E1, U40 | phone | ![Error E1, U40, light](../../images/03-farm-business/u40-farmer/e1-aid-plot-changed-phone-light.png) | ![Error E1, U40, dark](../../images/03-farm-business/u40-farmer/e1-aid-plot-changed-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-07-aid-declaration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-07-aid-declaration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-07-aid-declaration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-07-aid-declaration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-07-aid-declaration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-07-aid-declaration-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-07-aid-declaration-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-07-aid-declaration-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-01 Plot](../../data/e-sc13-01-plot.md), [E-SC13-05 Animal](../../data/e-sc13-05-animal.md),
[E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md), shown as the entity pages list them,
with their examples.

## Actions

- Prepare from records: [UC-SC13-07](../../use-cases/03-farm-business/uc-sc13-07-declare-cap-aid.md), step 1.
- Check: [UC-SC13-07](../../use-cases/03-farm-business/uc-sc13-07-declare-cap-aid.md), step 2.
- File: [UC-SC13-07](../../use-cases/03-farm-business/uc-sc13-07-declare-cap-aid.md), step 3.
- Account for the aid: [UC-SC13-07](../../use-cases/03-farm-business/uc-sc13-07-declare-cap-aid.md), step 4.

## States

- Normal: the declaration prepared from plots and herds.
- Empty: "No declaration".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, plots changed: the declaration is checked again.
- Read-only: a filed declaration is read-only.
- Offline: not available offline: office work on aid, accounts and margins. Offline work is kept for the phone forms of
  the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC13-16 CAP aid declaration](../../data/e-sc13-16-cap-aid-declaration.md),
[E-SC13-01 Plot](../../data/e-sc13-01-plot.md), [E-SC13-05 Animal](../../data/e-sc13-05-animal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-16 CAP aid declaration | Draft | Badge "Draft"; a new record starts here; next: Held or Filed (UC-SC13-07); fields editable within the role | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-draft-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-draft-{desktop,phone}-{light,dark}.png` |
| E-SC13-16 CAP aid declaration | Held | Badge "Held"; next: Draft (UC-SC13-07); fields editable within the role | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-held-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-held-{desktop,phone}-{light,dark}.png` |
| E-SC13-16 CAP aid declaration | Filed | Badge "Filed"; next: Corrected (UC-SC13-07); fields editable within the role | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-filed-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-filed-{desktop,phone}-{light,dark}.png` |
| E-SC13-16 CAP aid declaration | Corrected | Badge "Corrected"; final: read-only, no next state; the history shows how it got here | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-corrected-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-16-cap-aid-declaration-corrected-{desktop,phone}-{light,dark}.png` |
| E-SC13-01 Plot | New | Badge "New"; a new record starts here; next: Refused (UC-SC13-01); fields editable within the role | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-01-plot-new-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-01-plot-new-{desktop,phone}-{light,dark}.png` |
| E-SC13-01 Plot | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-01-plot-refused-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-01-plot-refused-{desktop,phone}-{light,dark}.png` |
| E-SC13-05 Animal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U40 | `u05-accounting/s-sc13-07-aid-declaration-e-sc13-05-animal-active-desktop-{light,dark}.png`, `u40-farmer/s-sc13-07-aid-declaration-e-sc13-05-animal-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-03 Farm business](../../flows/fl-sc13-03-farm-business.md)

## Open questions

None.

---

⬅️ [S-SC13-06 Veterinary](../02-livestock/s-sc13-06-veterinary.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-08 Machinery](s-sc13-08-machinery.md)

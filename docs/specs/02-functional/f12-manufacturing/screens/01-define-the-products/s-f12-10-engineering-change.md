🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-01 Define the products](README.md) › 🖥️ S-F12-10 Engineering change

# 🖥️ S-F12-10 Engineering change

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Manage engineering changes.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-01 step 3, U21 | desktop | ![FL-F12-01 step 3, U21, light](../../images/01-define-the-products/u21-production-planner/3-engineering-change-desktop-light.png) | ![FL-F12-01 step 3, U21, dark](../../images/01-define-the-products/u21-production-planner/3-engineering-change-desktop-dark.png) |
| FL-F12-01 step 3, U21 | phone | ![FL-F12-01 step 3, U21, light](../../images/01-define-the-products/u21-production-planner/3-engineering-change-phone-light.png) | ![FL-F12-01 step 3, U21, dark](../../images/01-define-the-products/u21-production-planner/3-engineering-change-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-10-engineering-change-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-10-engineering-change-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-10-engineering-change-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-10-engineering-change-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-10-engineering-change-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-10-engineering-change-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-10-engineering-change-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-10-engineering-change-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Manage engineering changes, as the wireframe shows.
- Empty: No engineering change yet, with New change.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-01 Bill of materials](../../data/e-f12-01-bill-of-materials.md),
[E-F12-11 Engineering change](../../data/e-f12-11-engineering-change.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-01 Bill of materials | Draft | Badge "Draft"; a new record starts here; next: Approved (UC-F12-01); fields editable within the role | U02, U21 | `u02-manager/s-f12-10-engineering-change-e-f12-01-bill-of-materials-draft-{desktop,phone}-{light,dark}.png`, `u21-production-planner/s-f12-10-engineering-change-e-f12-01-bill-of-materials-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-01 Bill of materials | Approved | Badge "Approved"; next: Retired (BR-F12-02); fields editable within the role | U02, U21 | `u02-manager/s-f12-10-engineering-change-e-f12-01-bill-of-materials-approved-{desktop,phone}-{light,dark}.png`, `u21-production-planner/s-f12-10-engineering-change-e-f12-01-bill-of-materials-approved-{desktop,phone}-{light,dark}.png` |
| E-F12-01 Bill of materials | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U02, U21 | `u02-manager/s-f12-10-engineering-change-e-f12-01-bill-of-materials-retired-{desktop,phone}-{light,dark}.png`, `u21-production-planner/s-f12-10-engineering-change-e-f12-01-bill-of-materials-retired-{desktop,phone}-{light,dark}.png` |
| E-F12-11 Engineering change | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U21 | `u02-manager/s-f12-10-engineering-change-e-f12-11-engineering-change-active-{desktop,phone}-{light,dark}.png`, `u21-production-planner/s-f12-10-engineering-change-e-f12-11-engineering-change-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F12-01 Define the products](../../flows/fl-f12-01-define-the-products.md)

## Open questions

None.

---

⬅️ [S-F12-09 Subcontracting](../05-subcontracting-and-costs/s-f12-09-subcontracting.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-11 Unbuild and repair](../03-make-the-products/s-f12-11-unbuild-and-repair.md)

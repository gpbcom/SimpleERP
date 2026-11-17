🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-07 Compliance and safety](README.md) › 🖥️ S-F12-16 Compliance file

# 🖥️ S-F12-16 Compliance file

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Record product compliance.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-07 step 1, U21 | desktop | ![FL-F12-07 step 1, U21, light](../../images/07-compliance-and-safety/u21-production-planner/1-compliance-file-desktop-light.png) | ![FL-F12-07 step 1, U21, dark](../../images/07-compliance-and-safety/u21-production-planner/1-compliance-file-desktop-dark.png) |
| FL-F12-07 step 1, U21 | phone | ![FL-F12-07 step 1, U21, light](../../images/07-compliance-and-safety/u21-production-planner/1-compliance-file-phone-light.png) | ![FL-F12-07 step 1, U21, dark](../../images/07-compliance-and-safety/u21-production-planner/1-compliance-file-phone-dark.png) |
| Error E1, U21 | desktop | ![Error E1, U21, light](../../images/07-compliance-and-safety/u21-production-planner/e1-file-incomplete-desktop-light.png) | ![Error E1, U21, dark](../../images/07-compliance-and-safety/u21-production-planner/e1-file-incomplete-desktop-dark.png) |
| Error E1, U21 | phone | ![Error E1, U21, light](../../images/07-compliance-and-safety/u21-production-planner/e1-file-incomplete-phone-light.png) | ![Error E1, U21, dark](../../images/07-compliance-and-safety/u21-production-planner/e1-file-incomplete-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-16-compliance-file-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-16-compliance-file-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-16-compliance-file-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-16-compliance-file-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-16-compliance-file-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-16-compliance-file-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-16-compliance-file-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-16-compliance-file-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Record product compliance, as the wireframe shows.
- Empty: No compliance file yet, with New file.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-14 Product compliance file](../../data/e-f12-14-product-compliance-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-14 Product compliance file | Complete | Badge "Complete"; a new record starts here; next: Incomplete (UC-F12-16); fields editable within the role | U07, U21 | `u07-administrator/s-f12-16-compliance-file-e-f12-14-product-compliance-file-complete-desktop-{light,dark}.png`, `u21-production-planner/s-f12-16-compliance-file-e-f12-14-product-compliance-file-complete-{desktop,phone}-{light,dark}.png` |
| E-F12-14 Product compliance file | Incomplete | Badge "Incomplete"; next: Complete (UC-F12-16); fields editable within the role | U07, U21 | `u07-administrator/s-f12-16-compliance-file-e-f12-14-product-compliance-file-incomplete-desktop-{light,dark}.png`, `u21-production-planner/s-f12-16-compliance-file-e-f12-14-product-compliance-file-incomplete-{desktop,phone}-{light,dark}.png` |

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

- [FL-F12-07 Compliance and safety](../../flows/fl-f12-07-compliance-and-safety.md)

## Open questions

None.

---

⬅️ [S-F12-15 Pick for production](../02-plan-production/s-f12-15-pick-for-production.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-17 Safety registers](s-f12-17-safety-registers.md)

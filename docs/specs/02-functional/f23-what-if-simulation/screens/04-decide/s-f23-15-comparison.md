🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-04 Decide](README.md) › 🖥️ S-F23-15 Comparison

# 🖥️ S-F23-15 Comparison

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Compare scenarios side by side.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-04 step 2, U13 | desktop | ![FL-F23-04 step 2, U13, light](../../images/04-decide/u13-owner/2-compare-desktop-light.png) | ![FL-F23-04 step 2, U13, dark](../../images/04-decide/u13-owner/2-compare-desktop-dark.png) |
| FL-F23-04 step 2, U13 | phone | ![FL-F23-04 step 2, U13, light](../../images/04-decide/u13-owner/2-compare-phone-light.png) | ![FL-F23-04 step 2, U13, dark](../../images/04-decide/u13-owner/2-compare-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/04-decide/u13-owner/e1-horizons-desktop-light.png) | ![Error E1, U13, dark](../../images/04-decide/u13-owner/e1-horizons-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/04-decide/u13-owner/e1-horizons-phone-light.png) | ![Error E1, U13, dark](../../images/04-decide/u13-owner/e1-horizons-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-15-comparison-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-15-comparison-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-15-comparison-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-15-comparison-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-15-comparison-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-15-comparison-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-15-comparison-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-15-comparison-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: scenarios side by side.
- Empty: "Pick scenarios".
- Loading: the frame and titles show at once with placeholder rows for the comparison; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: The comparison last loaded stays visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F23-06 Sensitivity](../../data/e-f23-06-sensitivity.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-06 Sensitivity | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f23-15-comparison-e-f23-06-sensitivity-active-{desktop,phone}-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F23-04 Decide](../../flows/fl-f23-04-decide.md)

## Open questions

None.

---

⬅️ [S-F23-14 Sensitivity](s-f23-14-sensitivity.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-16 Counter-measures](s-f23-16-counter-measures.md)

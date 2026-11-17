🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-03 Analyse and arm sales](README.md) › 🖥️ S-F17-11 Comparison

# 🖥️ S-F17-11 Comparison

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Compare side by side.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-03 step 1, U13 | desktop | ![FL-F17-03 step 1, U13, light](../../images/03-analyse-and-arm-sales/u13-owner/1-compare-desktop-light.png) | ![FL-F17-03 step 1, U13, dark](../../images/03-analyse-and-arm-sales/u13-owner/1-compare-desktop-dark.png) |
| FL-F17-03 step 1, U13 | phone | ![FL-F17-03 step 1, U13, light](../../images/03-analyse-and-arm-sales/u13-owner/1-compare-phone-light.png) | ![FL-F17-03 step 1, U13, dark](../../images/03-analyse-and-arm-sales/u13-owner/1-compare-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/03-analyse-and-arm-sales/u13-owner/e1-not-comparable-desktop-light.png) | ![Error E1, U13, dark](../../images/03-analyse-and-arm-sales/u13-owner/e1-not-comparable-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/03-analyse-and-arm-sales/u13-owner/e1-not-comparable-phone-light.png) | ![Error E1, U13, dark](../../images/03-analyse-and-arm-sales/u13-owner/e1-not-comparable-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-11-comparison-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-11-comparison-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-11-comparison-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-11-comparison-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-11-comparison-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-11-comparison-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-11-comparison-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-11-comparison-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the grid of offers and figures with each value's date and source.
- Empty: "Pick competitors and criteria".
- Loading: the frame and titles show at once with placeholder rows for the grid; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: shared grids are read-only for sales.
- Offline: The grid last loaded stays readable with its date. Nothing else is queued: D38 keeps only today's schedule,
  time and intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F17-10 Analysis](../../data/e-f17-10-analysis.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-10 Analysis | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U13 | `u03-sales/s-f17-11-comparison-e-f17-10-analysis-active-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-11-comparison-e-f17-10-analysis-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F17-03 Analyse and arm sales](../../flows/fl-f17-03-analyse-and-arm-sales.md)

## Open questions

None.

---

⬅️ [S-F17-10 Data providers](../01-set-up-and-profiles/s-f17-10-data-providers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-12 SWOT and positioning](s-f17-12-swot-and-positioning.md)

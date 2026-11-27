🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-03 See the impact](README.md) › 🖥️ S-F23-07 Cash impact

# 🖥️ S-F23-07 Cash impact

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

See the impact on cash and treasury.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-03 step 2, U31 | desktop | ![FL-F23-03 step 2, U31, light](../../images/03-see-the-impact/u31-treasurer/2-cash-desktop-light.png) | ![FL-F23-03 step 2, U31, dark](../../images/03-see-the-impact/u31-treasurer/2-cash-desktop-dark.png) |
| FL-F23-03 step 2, U31 | phone | ![FL-F23-03 step 2, U31, light](../../images/03-see-the-impact/u31-treasurer/2-cash-phone-light.png) | ![FL-F23-03 step 2, U31, dark](../../images/03-see-the-impact/u31-treasurer/2-cash-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-07-cash-impact-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-07-cash-impact-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-07-cash-impact-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-07-cash-impact-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-07-cash-impact-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-07-cash-impact-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-07-cash-impact-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-07-cash-impact-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: cash with the lowest point and range.
- Empty: "Run the scenario first".
- Loading: the frame and titles show at once with placeholder rows for the cash; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: within rights.
- Offline: Results last loaded stay visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F23-05 Impact result](../../data/e-f23-05-impact-result.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-05 Impact result | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05, U31 | `u05-accounting/s-f23-07-cash-impact-e-f23-05-impact-result-recorded-desktop-{light,dark}.png`, `u31-treasurer/s-f23-07-cash-impact-e-f23-05-impact-result-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F23-03 See the impact](../../flows/fl-f23-03-see-the-impact.md)

## Open questions

None.

---

⬅️ [S-F23-06 Sales impact](s-f23-06-sales-impact.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-08 Statements impact](s-f23-08-statements-impact.md)

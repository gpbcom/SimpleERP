🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-06 Benchmark additions](README.md) › 🖥️ S-F8-18 Cards and spend

# 🖥️ S-F8-18 Cards and spend

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Control spend with cards and limits.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-06 step 4, U05 | desktop | ![FL-F8-06 step 4, U05, light](../../images/06-benchmark-additions/u05-accounting/4-cards-desktop-light.png) | ![FL-F8-06 step 4, U05, dark](../../images/06-benchmark-additions/u05-accounting/4-cards-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/06-benchmark-additions/u05-accounting/e1-card-limit-desktop-light.png) | ![Error E1, U05, dark](../../images/06-benchmark-additions/u05-accounting/e1-card-limit-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-18-cards-and-spend-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-18-cards-and-spend-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-18-cards-and-spend-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-18-cards-and-spend-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-18-cards-and-spend-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-18-cards-and-spend-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-18-cards-and-spend-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-18-cards-and-spend-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Control spend with cards and limits, as the wireframe shows.
- Empty: No card yet for the period, with Order a card.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-15 Company card](../../data/e-f08-15-company-card.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-15 Company card | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U05 | `u01-employee/s-f08-18-cards-and-spend-e-f08-15-company-card-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-18-cards-and-spend-e-f08-15-company-card-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F8-06 Benchmark additions](../../flows/fl-f08-06-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F8-17 Continuous close](s-f08-17-continuous-close.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-19 Planning](s-f08-19-planning.md)

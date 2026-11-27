🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-06 Benchmark additions](README.md) › 🖥️ S-F8-17 Continuous close

# 🖥️ S-F8-17 Continuous close

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Close continuously with agents.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-06 step 3, U05 | desktop | ![FL-F8-06 step 3, U05, light](../../images/06-benchmark-additions/u05-accounting/3-continuous-close-desktop-light.png) | ![FL-F8-06 step 3, U05, dark](../../images/06-benchmark-additions/u05-accounting/3-continuous-close-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-17-continuous-close-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-17-continuous-close-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-17-continuous-close-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-17-continuous-close-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-17-continuous-close-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-17-continuous-close-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-17-continuous-close-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-17-continuous-close-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Close continuously with agents, as the wireframe shows.
- Empty: No agent task yet for the period, with Turn on an agent.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-F8-16 Revenue schedules](s-f08-16-revenue-schedules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-18 Cards and spend](s-f08-18-cards-and-spend.md)

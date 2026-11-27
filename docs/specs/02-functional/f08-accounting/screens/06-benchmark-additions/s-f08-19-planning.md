🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-06 Benchmark additions](README.md) › 🖥️ S-F8-19 Planning

# 🖥️ S-F8-19 Planning

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Plan and forecast.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-06 step 5, U05 | desktop | ![FL-F8-06 step 5, U05, light](../../images/06-benchmark-additions/u05-accounting/5-planning-desktop-light.png) | ![FL-F8-06 step 5, U05, dark](../../images/06-benchmark-additions/u05-accounting/5-planning-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-19-planning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-19-planning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-19-planning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-19-planning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-19-planning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-19-planning-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-19-planning-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-19-planning-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Plan and forecast, as the wireframe shows.
- Empty: No plan yet for the period, with New plan.
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

⬅️ [S-F8-18 Cards and spend](s-f08-18-cards-and-spend.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-20 Profitability](s-f08-20-profitability.md)

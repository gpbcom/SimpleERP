🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-10 Benchmark additions](README.md) › 🖥️ S-F4-17 Call routing

# 🖥️ S-F4-17 Call routing

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Route incoming calls.

## Entry points

Meetings in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-10 step 3, U07 | desktop | ![FL-F4-10 step 3, U07, light](../../images/10-benchmark-additions/u07-administrator/3-call-routing-desktop-light.png) | ![FL-F4-10 step 3, U07, dark](../../images/10-benchmark-additions/u07-administrator/3-call-routing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-17-call-routing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-17-call-routing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-17-call-routing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-17-call-routing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-17-call-routing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-17-call-routing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f04-17-call-routing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f04-17-call-routing-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Route incoming calls, as the wireframe shows.
- Empty: No routing rule: every call rings the main line.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users other than administrators.
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

- [FL-F4-10 Benchmark additions](../../flows/fl-f04-10-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F4-16 Booking page](s-f04-16-booking-page.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-18 Topics](../11-insights-and-accessibility/s-f04-18-topics.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-06 Benchmark additions](README.md) › 🖥️ S-F7-15 Group trade

# 🖥️ S-F7-15 Group trade

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Trade between group companies.

## Entry points

Purchasing and stock in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-06 step 2, U04 | desktop | ![FL-F7-06 step 2, U04, light](../../images/06-benchmark-additions/u04-purchasing/2-group-trade-desktop-light.png) | ![FL-F7-06 step 2, U04, dark](../../images/06-benchmark-additions/u04-purchasing/2-group-trade-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-15-group-trade-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-15-group-trade-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-15-group-trade-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-15-group-trade-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-15-group-trade-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-15-group-trade-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-15-group-trade-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-15-group-trade-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Trade between group companies, as the wireframe shows.
- Empty: No group company to trade with yet, with Set up group trade.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
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

- [FL-F7-06 Benchmark additions](../../flows/fl-f07-06-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F7-14 Tenders](s-f07-14-tenders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-16 Third-party stock](s-f07-16-third-party-stock.md)

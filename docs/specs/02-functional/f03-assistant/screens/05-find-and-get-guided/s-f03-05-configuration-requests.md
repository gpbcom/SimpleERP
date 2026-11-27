🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-05 Find and get guided](README.md) › 🖥️ S-F3-05 Configuration requests

# 🖥️ S-F3-05 Configuration requests

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Purpose

See and answer what users asked the ERP to do (D168).

## Entry points

Configuration › Requests; the notification of a new request.

## Wireframe

```text
+------------------------------------------------------------------+
| Requests                       [Open v]  [Search...]              |
|------------------------------------------------------------------|
| Request                         | From        | Votes | Status   |
| Add a Vehicle field to visits   | Paul Martin | 3     | Open     |
| A Returns screen for the shop   | Lea Morel   | 1     | Planned  |
|------------------------------------------------------------------|
| [Answer]  [Mark planned]  [Mark done]  [Decline]                  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-05 step 5, U07 | desktop | ![FL-F3-05 step 5, U07, light](../../images/05-find-and-get-guided/u07-administrator/5-answer-requests-desktop-light.png) | ![FL-F3-05 step 5, U07, dark](../../images/05-find-and-get-guided/u07-administrator/5-answer-requests-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-05-configuration-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-05-configuration-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-05-configuration-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-05-configuration-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-05-configuration-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-05-configuration-requests-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-05-configuration-requests-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-05-configuration-requests-offline-desktop-dark.png) |

## Fields and columns

As [E-F3-06 Configuration request](../../data/e-f03-06-configuration-request.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Answer | configurator | The requester is told |
| Mark planned, done, declined | configurator | The requester and voters are told |

## States

- Normal: See and answer what users asked the ERP to do (D168), as the wireframe shows.
- Empty: "No requests yet."
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: requests already answered.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- List.

Shown entities (VD-15): [E-F3-06 Configuration request](../../data/e-f03-06-configuration-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-06 Configuration request | Planned | Badge "Planned"; next: Done (UC-F3-05); fields editable within the role | U07 | `u07-administrator/s-f03-05-configuration-requests-e-f03-06-configuration-request-planned-desktop-{light,dark}.png` |
| E-F3-06 Configuration request | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f03-05-configuration-requests-e-f03-06-configuration-request-done-desktop-{light,dark}.png` |
| E-F3-06 Configuration request | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f03-05-configuration-requests-e-f03-06-configuration-request-declined-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

A data table with headers; status changes are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F3-05 Find and get guided](../../flows/fl-f03-05-find-and-get-guided.md)

## Open questions

None.

---

⬅️ [S-F3-04 Show me overlay](s-f03-04-show-me-overlay.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-06 My connections](../06-use-an-outside-tool/s-f03-06-my-connections.md)

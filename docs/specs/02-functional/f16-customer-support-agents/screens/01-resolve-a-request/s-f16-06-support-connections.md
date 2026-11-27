🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-01 Resolve a request](README.md) › 🖥️ S-F16-06 Support connections

# 🖥️ S-F16-06 Support connections

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Connect the helpdesk and back-office tools.

## Entry points

Support in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-01 step 2, U16 | desktop | ![FL-F16-01 step 2, U16, light](../../images/01-resolve-a-request/u16-office-worker/2-audit-trail-desktop-light.png) | ![FL-F16-01 step 2, U16, dark](../../images/01-resolve-a-request/u16-office-worker/2-audit-trail-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-06-support-connections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-06-support-connections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-06-support-connections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-06-support-connections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-06-support-connections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-06-support-connections-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f16-06-support-connections-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f16-06-support-connections-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: helpdesks and back-office tools with their state and the actions they offer.
- Empty: "No connection yet": the built-in inbox works alone.
- Loading: the frame and titles show at once with placeholder rows for the connections; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: other roles do not see connections; credentials are never shown.
- Offline: not available offline: connections are tested on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; the review queue also on the phone.

## Accessibility

Labelled controls; modes and scores as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-01 Resolve a request](../../flows/fl-f16-01-resolve-a-request.md)

## Open questions

None.

---

⬅️ [S-F16-05 Support dashboard](../03-review-and-monitor/s-f16-05-support-dashboard.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-07 Service levels](../04-human-agent-workspace/s-f16-07-service-levels.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-10 Benchmark additions](README.md) › 🖥️ S-F3-17 Chat apps

# 🖥️ S-F3-17 Chat apps

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Use the AI assistant in chat apps.

## Entry points

Assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-10 step 4, U01 | phone | ![FL-F3-10 step 4, U01, light](../../images/10-benchmark-additions/u01-employee/4-chat-apps-phone-light.png) | ![FL-F3-10 step 4, U01, dark](../../images/10-benchmark-additions/u01-employee/4-chat-apps-phone-dark.png) |
| FL-F3-10 step 4, U01 | desktop | ![FL-F3-10 step 4, U01, light](../../images/10-benchmark-additions/u01-employee/4-chat-apps-desktop-light.png) | ![FL-F3-10 step 4, U01, dark](../../images/10-benchmark-additions/u01-employee/4-chat-apps-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-17-chat-apps-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-17-chat-apps-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-17-chat-apps-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-17-chat-apps-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-17-chat-apps-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-17-chat-apps-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-17-chat-apps-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-17-chat-apps-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Use the AI assistant in chat apps, as the wireframe shows.
- Empty: No chat app connected, with Connect.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users other than administrators.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F3-10 Benchmark additions](../../flows/fl-f03-10-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F3-16 AI fields](s-f03-16-ai-fields.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-18 Evaluation set](../11-trust-the-answers/s-f03-18-evaluation-set.md)

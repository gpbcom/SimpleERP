🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-03 Act through the AI assistant](README.md) ›
🖥️ S-F3-12 Assistant settings

# 🖥️ S-F3-12 Assistant settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Group the AI assistant's company settings (D187).

## Entry points

Administration › Assistant.

## Wireframe

```text
+------------------------------------------------------------------+
| Assistant                                              [Save]     |
|------------------------------------------------------------------|
| Providers         8 AI features, see AI settings  [Open]          |
| Batch size        [100 v]  (20, 50, 100, 500, No limit)           |
| Keep conversations [12 months v] after the last message           |
| Writing style     Professional, formal          [Edit]            |
| Personal services [Google Calendar] [Outlook mail] [+]            |
| Sharing           [on]   Configuration requests [on]              |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-03 step 4, U07 | desktop | ![FL-F3-03 step 4, U07, light](../../images/03-act-through-the-assistant/u07-administrator/4-assistant-settings-desktop-light.png) | ![FL-F3-03 step 4, U07, dark](../../images/03-act-through-the-assistant/u07-administrator/4-assistant-settings-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-12-assistant-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-12-assistant-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-12-assistant-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-12-assistant-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-12-assistant-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-12-assistant-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-12-assistant-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-12-assistant-settings-offline-desktop-dark.png) |

## Fields and columns

Batch size (BR-F3-09), retention (BR-F3-27), writing style (S-F3-03), allowed personal services (BR-F3-19), sharing
(BR-F3-26), configuration requests (BR-F3-16).

## Actions

| Action | Who | Result |
|---|---|---|
| Save | administrator, owner | Applied at once |
| Open AI settings | administrator, owner | F1's per-feature providers (S-F1) |

## States

- Normal: Group the AI assistant's company settings (D187), as the wireframe shows.
- Empty: never: the defaults are shown until changed.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: for users who are not administrators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Defaults: 100, 12 months, professional and formal, no personal services, sharing on, requests on.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop.

## Accessibility

Labelled fields; each setting's effect is described under it.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)

## Shown in

- [FL-F3-03 Act through the AI assistant](../../flows/fl-f03-03-act-through-the-assistant.md)
- [FL-F3-08 Manage and share conversations](../../flows/fl-f03-08-manage-and-share-conversations.md)

## Open questions

None.

---

⬅️ [S-F3-11 Phone assistant](../09-assistant-on-a-phone/s-f03-11-phone-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-13 Assistant usage dashboard](../01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md)

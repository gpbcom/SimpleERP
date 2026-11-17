🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-06 Choose an AI provider](README.md) › 🖥️ S-F1-08 AI settings

# 🖥️ S-F1-08 AI settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Choose the provider of each AI feature, or turn AI off.

## Entry points

Administration › Connections › AI.

## Wireframe

```text
+------------------------------------------------------------------+
| AI settings                                  AI for the company: [on]|
|------------------------------------------------------------------|
| Assistant (F3)                   (o) local  ( ) external [          ] |
| Meetings: speech-to-text (F4)    (o) local  ( ) external [          ] |
| Meetings: summaries (F4)         (o) local  ( ) external [          ] |
| Legal assistant (F15)            (o) local  ( ) external [          ] |
| Social media drafts (F5)         (o) local  ( ) external [          ] |
|------------------------------------------------------------------|
| ! With an external provider, each question and the passages it  |
|   needs leave your server.                                       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-06 step 1, U07 | desktop | ![FL-F1-06 step 1, U07, light](../../images/06-choose-an-ai-provider/u07-administrator/1-pick-a-feature-and-provider-desktop-light.png) | ![FL-F1-06 step 1, U07, dark](../../images/06-choose-an-ai-provider/u07-administrator/1-pick-a-feature-and-provider-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/06-choose-an-ai-provider/u07-administrator/e1-key-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/06-choose-an-ai-provider/u07-administrator/e1-key-refused-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/06-choose-an-ai-provider/u07-administrator/e2-provider-down-fallback-desktop-light.png) | ![Error E2, U07, dark](../../images/06-choose-an-ai-provider/u07-administrator/e2-provider-down-fallback-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-08-ai-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-08-ai-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-08-ai-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-08-ai-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-08-ai-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-08-ai-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-08-ai-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-08-ai-settings-offline-desktop-dark.png) |

## Fields and columns

As [E-F1-09 AI feature setting](../../data/e-f01-09-ai-feature-setting.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Choose local or external | administrator | UC-F1-08 |
| Test key | administrator | Accepted or refused |
| Turn AI off | administrator | Every AI feature stops (D22) |

## States

- Normal: Choose the provider of each AI feature, or turn AI off, as the wireframe shows.
- Empty: never: every AI feature has a line, local by default.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: key refused.
- Read-only: for users other than administrators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Default: every feature local.
- A feature in fallback: a badge with the last failure.

Shown entities (VD-15): [E-F1-09 AI feature setting](../../data/e-f01-09-ai-feature-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-09 AI feature setting | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f01-08-ai-settings-e-f01-09-ai-feature-setting-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Each feature's choice is a radio group with the feature as its label.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F1-06 Choose an AI provider](../../flows/fl-f01-06-choose-an-ai-provider.md)

## Open questions

None.

---

⬅️ [S-F1-07 Connections](../05-connect-an-external-tool/s-f01-07-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-09 Single sign-on](../07-set-up-single-sign-on/s-f01-09-single-sign-on.md)

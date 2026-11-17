🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-04 Summarise or draft](README.md) › 🖥️ S-F3-03 Writing style settings

# 🖥️ S-F3-03 Writing style settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Set how the AI assistant writes for the company (D162, D164).

## Entry points

Administration › Assistant › Writing style.

## Wireframe

```text
+------------------------------------------------------------------+
| Writing style                                         [Save]     |
|------------------------------------------------------------------|
| Tone            ( ) Warm  (o) Professional  ( ) Very formal      |
| Address         (o) Formal (vous, Sie)  ( ) Informal (tu, du)    |
| Words to use    [our team] [quote] [+]                           |
| Words to avoid  [cheap] [+]                                      |
| Sample texts    [Upload or paste examples]                       |
| 'Written with AI help' on emails and documents  [ off ]          |
|   (always on for social media posts, F5)                         |
|------------------------------------------------------------------|
| Try it: [Write a reminder for an invoice]   -> preview           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-04 step 4, U07 | desktop | ![FL-F3-04 step 4, U07, light](../../images/04-summarise-or-draft/u07-administrator/4-writing-style-desktop-light.png) | ![FL-F3-04 step 4, U07, dark](../../images/04-summarise-or-draft/u07-administrator/4-writing-style-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-03-writing-style-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-03-writing-style-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-03-writing-style-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-03-writing-style-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-03-writing-style-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-03-writing-style-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-03-writing-style-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-03-writing-style-settings-offline-desktop-dark.png) |

## Fields and columns

As [E-F3-05 Company writing style](../../data/e-f03-05-company-writing-style.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Save | administrator, owner | Applied to the next drafts |
| Try it | administrator, owner | A sample draft with the style |

## States

- Normal: Set how the AI assistant writes for the company (D162, D164), as the wireframe shows.
- Empty: never: the defaults are shown until changed.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: a sample file not readable, the error message pattern (D122).
- Read-only: for users who are not administrators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Default: professional, formal, no word lists, mention off.
- Saved.

Shown entities (VD-15): [E-F3-22 AI assistant request](../../data/e-f03-22-ai-assistant-request.md),
[E-F3-02 Assistant answer](../../data/e-f03-02-assistant-answer.md),
[E-F3-05 Company writing style](../../data/e-f03-05-company-writing-style.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-22 AI assistant request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f03-03-writing-style-settings-e-f03-22-ai-assistant-request-active-desktop-{light,dark}.png`, `u13-owner/s-f03-03-writing-style-settings-e-f03-22-ai-assistant-request-active-{desktop,phone}-{light,dark}.png` |
| E-F3-02 Assistant answer | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f03-03-writing-style-settings-e-f03-02-assistant-answer-recorded-desktop-{light,dark}.png`, `u13-owner/s-f03-03-writing-style-settings-e-f03-02-assistant-answer-recorded-{desktop,phone}-{light,dark}.png` |
| E-F3-05 Company writing style | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f03-03-writing-style-settings-e-f03-05-company-writing-style-active-desktop-{light,dark}.png`, `u13-owner/s-f03-03-writing-style-settings-e-f03-05-company-writing-style-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Each setting is a labelled group; word lists are editable chips reachable by keyboard.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)

## Shown in

- [FL-F3-04 Summarise or draft](../../flows/fl-f03-04-summarise-or-draft.md)

## Open questions

None.

---

⬅️ [S-F3-02 Change confirmation card](../03-act-through-the-assistant/s-f03-02-change-confirmation-card.md) ·
⬆️ [Up](README.md) · ➡️ [S-F3-04 Show me overlay](../05-find-and-get-guided/s-f03-04-show-me-overlay.md)

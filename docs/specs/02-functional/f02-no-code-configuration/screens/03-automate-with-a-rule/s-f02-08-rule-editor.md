🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-03 Automate with a rule](README.md) › 🖥️ S-F2-08 Rule editor

# 🖥️ S-F2-08 Rule editor

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Purpose

Write, test and publish a "when, if, then" rule.

## Entry points

Configuration › Automations.

## Wireframe

```text
+------------------------------------------------------------------+
| Remind after 3 days                DRAFT     [Test] [Publish]    |
|------------------------------------------------------------------|
| WHEN  a Quote has been in status [Sent v] for [3] days           |
| IF    Amount [is over v] [1,000 EUR]   and  Site [is v] [Lyon]   |
| THEN  Notify [the quote's sales person v] in-app and email       |
|       Create a task [Follow up {quote.number}] for [sales person] |
|       [+ action]                                                  |
| RUNS AS  rule account with: Quotes See, Tasks Create              |
|------------------------------------------------------------------|
| Test: would notify 4 people and create 4 tasks (nothing done)    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-03 step 1, U07 | desktop | ![FL-F2-03 step 1, U07, light](../../images/03-automate-with-a-rule/u07-administrator/1-when-if-then-desktop-light.png) | ![FL-F2-03 step 1, U07, dark](../../images/03-automate-with-a-rule/u07-administrator/1-when-if-then-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-08-rule-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-08-rule-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-08-rule-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-08-rule-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-08-rule-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-08-rule-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-08-rule-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-08-rule-editor-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-08 Automation rule](../../data/e-f02-08-automation-rule.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Test | configurator | What it would do, nothing done |
| Publish | configurator | UC-F2-09 |
| Pause, resume | configurator | The rule stops or runs again |
| Run log | configurator | Every run, with its outcome |

## States

- Normal: Write, test and publish a "when, if, then" rule, as the wireframe shows.
- Empty: No rule yet, with Create a rule and the gallery of examples.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: rights above the author's; a failed run marked in the log.
- Read-only: a published rule until it is paused or copied to a draft.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Draft, published, paused.

Shown entities (VD-15): [E-F2-08 Automation rule](../../data/e-f02-08-automation-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-08 Automation rule | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-07); fields editable within the role | U07 | `u07-administrator/s-f02-08-rule-editor-e-f02-08-automation-rule-draft-desktop-{light,dark}.png` |
| E-F2-08 Automation rule | Published | Badge "Published"; next: Paused (UC-F2-07); fields editable within the role | U07 | `u07-administrator/s-f02-08-rule-editor-e-f02-08-automation-rule-published-desktop-{light,dark}.png` |
| E-F2-08 Automation rule | Paused | Badge "Paused"; next: Published (UC-F2-07); fields editable within the role | U07 | `u07-administrator/s-f02-08-rule-editor-e-f02-08-automation-rule-paused-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Each part (when, if, then) is a labelled group; the sentence reads aloud as written.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md) (run log)

## Shown in

- [FL-F2-03 Automate with a rule](../../flows/fl-f02-03-automate-with-a-rule.md)

## Open questions

None.

---

⬅️ [S-F2-07 Email template editor](../02-customise-documents-and-emails/s-f02-07-email-template-editor.md) ·
⬆️ [Up](README.md) · ➡️ [S-F2-09 Workflow designer](../04-design-a-visual-workflow/s-f02-09-workflow-designer.md)

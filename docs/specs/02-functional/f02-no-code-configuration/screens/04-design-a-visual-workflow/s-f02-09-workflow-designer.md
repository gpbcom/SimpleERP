🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-04 Design a visual workflow](README.md) › 🖥️ S-F2-09 Workflow designer

# 🖥️ S-F2-09 Workflow designer

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Purpose

Draw a workflow from blocks that read as sentences.

## Entry points

Configuration › Automations › Workflows.

## Wireframe

```text
+------------------------------------------------------------------+
| Supplier invoices by email        DRAFT   [Test] [Publish]       |
|------------------------------------------------------------------|
| [When] an email arrives at invoices@acme-batiment.fr              |
|   |                                                              |
| [AI] Read the email: give its category and urgency               |
|   |                                                              |
| [If] category is invoice --------------- else: [Notify] Office   |
|   |                                                              |
| [Ask] Manager approves, within 2 days, else escalate             |
|   |                                                              |
| [Call] GitHub: open an issue (always ask)                        |
| Blocks: Branch, Wait, Parallel, Ask a person, Call outside, AI   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-04 step 1, U07 | desktop | ![FL-F2-04 step 1, U07, light](../../images/04-design-a-visual-workflow/u07-administrator/1-trigger-and-blocks-desktop-light.png) | ![FL-F2-04 step 1, U07, dark](../../images/04-design-a-visual-workflow/u07-administrator/1-trigger-and-blocks-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/04-design-a-visual-workflow/u07-administrator/e1-incomplete-block-desktop-light.png) | ![Error E1, U07, dark](../../images/04-design-a-visual-workflow/u07-administrator/e1-incomplete-block-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/04-design-a-visual-workflow/u07-administrator/e2-ai-answer-out-of-format-desktop-light.png) | ![Error E2, U07, dark](../../images/04-design-a-visual-workflow/u07-administrator/e2-ai-answer-out-of-format-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-09-workflow-designer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-09-workflow-designer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-09-workflow-designer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-09-workflow-designer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-09-workflow-designer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-09-workflow-designer-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-09-workflow-designer-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-09-workflow-designer-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-09 Workflow](../../data/e-f02-09-workflow.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Add a block | configurator | A sentence to fill |
| Ask the AI assistant | configurator | Explains or drafts a block |
| Test | configurator | Step by step on a real record |
| Publish | configurator | UC-F2-09 |

## States

- Normal: Draw a workflow from blocks that read as sentences, as the wireframe shows.
- Empty: an empty canvas with the trigger block and Add block.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: a published workflow; changes go to a new draft.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Draft; incomplete blocks in red with a plain explanation.

Shown entities (VD-15): [E-F2-29 Workflow template](../../data/e-f02-29-workflow-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-29 Workflow template | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-09-workflow-designer-e-f02-29-workflow-template-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

The workflow is also a numbered list of sentences, navigable by keyboard.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)

## Shown in

- [FL-F2-04 Design a visual workflow](../../flows/fl-f02-04-design-a-visual-workflow.md)

## Open questions

None.

---

⬅️ [S-F2-08 Rule editor](../03-automate-with-a-rule/s-f02-08-rule-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-10 Publish and versions](../05-publish-and-roll-back/s-f02-10-publish-and-versions.md)

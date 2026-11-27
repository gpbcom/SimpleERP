🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-13 Low code, bulk work and data cleaning](README.md) › 🖥️ S-F2-31 Script step editor

# 🖥️ S-F2-31 Script step editor

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the scripts of their company.
- - [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md): the scripts of the client
  companies they support.

## Purpose

Write, test and publish the script of a workflow step, with its inputs, its outputs and its limits.

## Entry points

Workflow designer › add a step › Script; Rule editor › Script; the AI assistant
([BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Script step: delivery date             Workflow: Order to delivery        State: Tested  [Publish] |
| ------------------------------------------------------------------------------------------- |
| INPUTS  order date (date)  lead time (days)         OUTPUTS  delivery date (date)           |
|   1  delivery = add_days(order_date, lead_time)                                             |
|   2  while is_weekend(delivery): delivery = add_days(delivery, 1)                           |
| TEST  Sample: order 2031  [Run]   Result 2026-11-24   12 ms of 2 s   3 MB of 64 MB          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-13 step 1, U07 | desktop | ![FL-F2-13 step 1, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/1-script-step-editor-desktop-light.png) | ![FL-F2-13 step 1, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/1-script-step-editor-desktop-dark.png) |
| FL-F2-13 step 1, U07 | desktop | ![FL-F2-13 step 1, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/1-script-step-editor-desktop-light.png) | ![FL-F2-13 step 1, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/1-script-step-editor-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/e1-a-script-goes-over-its-limit-desktop-light.png) | ![Error E1, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/e1-a-script-goes-over-its-limit-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-31-script-step-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-31-script-step-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-31-script-step-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-31-script-step-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-31-script-step-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-31-script-step-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-31-script-step-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-31-script-step-editor-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Name | E-F2-30 name | text | yes | yes |
| Inputs | E-F2-30 inputs | list with types | yes | no |
| Script | E-F2-30 source | code | yes | yes |
| Outputs | E-F2-30 outputs | list with types | yes | yes |
| Limits | E-F2-30 time and memory limits | seconds and MB | within the maximum | yes |
| Test result | E-F2-30 last test | outputs, time, memory | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Run test | test panel | the author | runs on the sample record in the sandbox |
| Publish | header | the author | the step is published with the draft (UC-F2-09) |
| Draft with the AI assistant | editor | the author | a draft script to read and test |
| Roll back | versions | the author | a previous version becomes the draft |

## States

- Normal: the editor with the inputs and outputs, the test panel and the limits.
- Empty: No script yet: write one, or describe it to the AI assistant.
- Loading: The editor loads first; the sample records follow.
- Error: the error message pattern (D122); a syntax error is shown on its line, an over-limit test under the test panel
  ([BR-F2-28](../../business-rules/br-f02-28-scripts-run-sandboxed-within-time-and-memory-limits.md)).
- Read-only: a published version: the script, its limits and its test, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-30 Script step](../../data/e-f02-30-script-step.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-30 Script step | Draft | Badge "Draft"; a new record starts here; next: Tested (UC-F2-31); fields editable within the role | U07, U11 | `u07-administrator/s-f02-31-script-step-editor-e-f02-30-script-step-draft-desktop-{light,dark}.png`, `u11-provider-admin/s-f02-31-script-step-editor-e-f02-30-script-step-draft-desktop-{light,dark}.png` |
| E-F2-30 Script step | Tested | Badge "Tested"; next: Draft or Published (UC-F2-31, UC-F2-09); fields editable within the role | U07, U11 | `u07-administrator/s-f02-31-script-step-editor-e-f02-30-script-step-tested-desktop-{light,dark}.png`, `u11-provider-admin/s-f02-31-script-step-editor-e-f02-30-script-step-tested-desktop-{light,dark}.png` |
| E-F2-30 Script step | Published | Badge "Published"; next: Failed or Retired (BR-F2-28, UC-F2-10); fields editable within the role | U07, U11 | `u07-administrator/s-f02-31-script-step-editor-e-f02-30-script-step-published-desktop-{light,dark}.png`, `u11-provider-admin/s-f02-31-script-step-editor-e-f02-30-script-step-published-desktop-{light,dark}.png` |
| E-F2-30 Script step | Failed | Badge "Failed"; next: Draft (UC-F2-31); fields editable within the role | U07, U11 | `u07-administrator/s-f02-31-script-step-editor-e-f02-30-script-step-failed-desktop-{light,dark}.png`, `u11-provider-admin/s-f02-31-script-step-editor-e-f02-30-script-step-failed-desktop-{light,dark}.png` |
| E-F2-30 Script step | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07, U11 | `u07-administrator/s-f02-31-script-step-editor-e-f02-30-script-step-retired-desktop-{light,dark}.png`, `u11-provider-admin/s-f02-31-script-step-editor-e-f02-30-script-step-retired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

The editor is keyboard only, with errors announced by line; the test result is text; the limits are read as numbers with
their units.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-13 Low code, bulk work and data cleaning](../../flows/fl-f02-13-low-code-bulk-and-cleaning.md)

## Open questions

None.

---

⬅️ [S-F2-30 Custom report](../10-change-safely/s-f02-30-custom-report.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-32 Bulk edit](s-f02-32-bulk-edit.md)

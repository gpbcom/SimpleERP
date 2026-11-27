🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-15 Security and group data](README.md) › 🖥️ S-F1-29 Group sharing

# 🖥️ S-F1-29 Group sharing

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the rules of the company.
- - [U13 Owner](../../../../01-users/personas/u13-owner.md): approves the rules of their company.

## Purpose

Choose which master data the group shares, with which companies and in which mode.

## Entry points

Administration › Group › Sharing; the duplicate found by the cleaning tool
([S-F2-35](../../../f02-no-code-configuration/screens/13-low-code-bulk-and-cleaning/s-f02-35-data-cleaning.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Group sharing: Paris company (owner)                                [New rule] [Approve]    |
| ------------------------------------------------------------------------------------------- |
| RECORD TYPE   FIELDS SHARED               SHARED WITH             MODE            STATE     |
| Customer      name, address, tax number   Lyon, Nantes            Read and use    Active    |
| Product       name, unit, tax class       all companies           Read only       Draft     |
| Preview: 1,240 records shared, 86 match existing records of Lyon [Link them] [Leave apart]  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-15 step 3, U07 | desktop | ![FL-F1-15 step 3, U07, light](../../images/15-security-and-group-data/u07-administrator/3-group-sharing-desktop-light.png) | ![FL-F1-15 step 3, U07, dark](../../images/15-security-and-group-data/u07-administrator/3-group-sharing-desktop-dark.png) |
| FL-F1-15 step 3, U07 | desktop | ![FL-F1-15 step 3, U07, light](../../images/15-security-and-group-data/u07-administrator/3-group-sharing-desktop-light.png) | ![FL-F1-15 step 3, U07, dark](../../images/15-security-and-group-data/u07-administrator/3-group-sharing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-29-group-sharing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-29-group-sharing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-29-group-sharing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-29-group-sharing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-29-group-sharing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-29-group-sharing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-29-group-sharing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-29-group-sharing-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Record type | E-F1-25 record type | text | yes | yes |
| Fields shared | E-F1-25 fields | list | yes | yes |
| Shared with | E-F1-25 companies | list of companies | yes | yes |
| Mode | E-F1-25 mode | read only, use and propose | yes | yes |
| State | E-F1-25 state | badge | approve, pause | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New rule | header | the administrator | a draft rule |
| Approve | row | the owner | the rule becomes active (BR-F1-35) |
| Pause | row | the administrator, the owner | no new record is shared |
| Link matches | preview | the administrator | matching records are linked to the shared one |

## States

- Normal: the rules of the owner company, the preview of the chosen one and the proposals waiting.
- Empty: No rule yet: each company keeps its own records. New rule starts one.
- Loading: The rules load first; the preview counts follow.
- Error: the error message pattern (D122); a rule that reaches outside the group is refused under its field.
- Read-only: an ended rule: its fields, its companies and its history.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-25 Sharing rule](../../data/e-f01-25-sharing-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-25 Sharing rule | Draft | Badge "Draft"; a new record starts here; next: Active (BR-F1-35); fields editable within the role | U07, U13 | `u07-administrator/s-f01-29-group-sharing-e-f01-25-sharing-rule-draft-desktop-{light,dark}.png`, `u13-owner/s-f01-29-group-sharing-e-f01-25-sharing-rule-draft-{desktop,phone}-{light,dark}.png` |
| E-F1-25 Sharing rule | Active | Badge "Active"; next: Paused or Ended (UC-F1-26, BR-F1-35); fields editable within the role | U07, U13 | `u07-administrator/s-f01-29-group-sharing-e-f01-25-sharing-rule-active-desktop-{light,dark}.png`, `u13-owner/s-f01-29-group-sharing-e-f01-25-sharing-rule-active-{desktop,phone}-{light,dark}.png` |
| E-F1-25 Sharing rule | Paused | Badge "Paused"; next: Active or Ended (UC-F1-26, BR-F1-35); fields editable within the role | U07, U13 | `u07-administrator/s-f01-29-group-sharing-e-f01-25-sharing-rule-paused-desktop-{light,dark}.png`, `u13-owner/s-f01-29-group-sharing-e-f01-25-sharing-rule-paused-{desktop,phone}-{light,dark}.png` |
| E-F1-25 Sharing rule | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f01-29-group-sharing-e-f01-25-sharing-rule-ended-desktop-{light,dark}.png`, `u13-owner/s-f01-29-group-sharing-e-f01-25-sharing-rule-ended-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Each shared field is a labelled check box; the preview counts are announced; keyboard: next rule, approve.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-15 Security and group data](../../flows/fl-f01-15-security-and-group-data.md)

## Open questions

None.

---

⬅️ [S-F1-28 Retention policies](s-f01-28-retention-policies.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-30 Act as a user](s-f01-30-act-as-user.md)

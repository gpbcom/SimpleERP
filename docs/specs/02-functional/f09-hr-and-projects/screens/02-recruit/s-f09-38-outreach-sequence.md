🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-02 Recruit](README.md) ›
🖥️ S-F9-38 Outreach sequence

# 🖥️ S-F9-38 Outreach sequence

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): the sequences of their searches.

## Purpose

Set the steps and the templates of an outreach sequence and approve them once with the shortlist.

## Entry points

S-F9-37 › Build the sequence; HR and projects › Recruitment › Outreach sequences.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Outreach sequence: site manager (12 prospects)        State: draft     [Approve and start]   |
|---------------------------------------------------------------------------------------------|
| STEPS                          | TEMPLATE                                                    |
| Day 0   Invitation with a note | Hello {first name}, I am Claire, HR at Acme Bâtiment...      |
| Day 7   Follow-up 1            | Your profile was found on LinkedIn: how we use it [notice]  |
| Day 21  Follow-up 2            |                                                             |
| Day 60  End                    | On a positive reply: booking link                            |
| Replies checked every 4 hours  | On a refusal: thank-you                                      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-14 step 4, U06 | desktop | ![FL-F9-14 step 4, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/4-outreach-sequence-desktop-light.png) | ![FL-F9-14 step 4, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/4-outreach-sequence-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/e1-limit-reached-desktop-light.png) | ![Error E1, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/e1-limit-reached-desktop-dark.png) |
| Error E2, U06 | desktop | ![Error E2, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/e2-sign-in-needed-desktop-light.png) | ![Error E2, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/e2-sign-in-needed-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-38-outreach-sequence-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-38-outreach-sequence-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-38-outreach-sequence-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-38-outreach-sequence-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-38-outreach-sequence-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-38-outreach-sequence-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-38-outreach-sequence-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-38-outreach-sequence-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Steps | E-F9-46 steps | day and kind | the days, within day 60 | yes |
| Templates | E-F9-46 templates | text with fields | yes, before approval | yes |
| Privacy notice link | E-F9-46 privacy notice link | web address | yes | yes |
| State | E-F9-46 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve and start | header | HR | the shortlist and the templates approved once (BR-F9-36) |
| Draft with the AI assistant | template | HR | a draft to edit |
| Pause, restart | header | HR | sending stops or goes on |
| Review shortlist | header | HR | back to S-F9-37 |

## States

- Normal: the steps, the templates and the rules, with the approval at the top.
- Empty: No prospect shortlisted yet, with Review shortlist.
- Loading: The templates load first; the counts follow.
- Error: the error message pattern (D122); a template without the notice link cannot be approved
  ([BR-F9-38](../../business-rules/br-f09-38-sourced-people-told-at-the-first-contact.md)).
- Read-only: an ended sequence: its steps, templates and results.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-46 Outreach sequence](../../data/e-f09-46-outreach-sequence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-46 Outreach sequence | Draft | the badge, the approval or pause button, the pause reason | U06 | `u06-hr/s-f09-38-outreach-sequence-e-f09-46-outreach-sequence-draft-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Running | the badge, the approval or pause button, the pause reason | U06 | `u06-hr/s-f09-38-outreach-sequence-e-f09-46-outreach-sequence-running-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Paused | the badge, the approval or pause button, the pause reason | U06 | `u06-hr/s-f09-38-outreach-sequence-e-f09-46-outreach-sequence-paused-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Ended | the badge, the approval or pause button, the pause reason | U06 | `u06-hr/s-f09-38-outreach-sequence-e-f09-46-outreach-sequence-ended-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Each step says its day in words; the template fields are labelled; the approval is announced.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-14 Source candidates on LinkedIn](../../flows/fl-f09-14-source-candidates-on-linkedin.md)
- [FL-F9-02 Recruit](../../flows/fl-f09-02-recruit.md)

## Open questions

None.

---

⬅️ [S-F9-37 LinkedIn sourcing search](s-f09-37-linkedin-sourcing-search.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-39 Prospect conversations](s-f09-39-prospect-conversations.md)

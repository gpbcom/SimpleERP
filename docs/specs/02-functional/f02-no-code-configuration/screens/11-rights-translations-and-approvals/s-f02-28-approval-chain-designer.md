🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-11 Rights, translations and approvals](README.md) › 🖥️ S-F2-28 Approval chain designer

# 🖥️ S-F2-28 Approval chain designer

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Set the levels, approvers and time limits of a record type's approvals.

## Entry points

A record type › Approvals.

## Wireframe

```text
+------------------------------------------------------------------+
| Purchase request › Approvals                                     |
| Level 1  up to 5,000 EUR   [Manager v]        one                |
| Level 2  above 5,000 EUR   [Owner v]          one                |
| Time limit [48 h]   then [escalate to next level v]              |
|                              [Test with amounts] [Publish]       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-11 step 3, U07 | desktop | ![FL-F2-11 step 3, U07, light](../../images/11-rights-translations-and-approvals/u07-administrator/3-approval-chain-designer-desktop-light.png) | ![FL-F2-11 step 3, U07, dark](../../images/11-rights-translations-and-approvals/u07-administrator/3-approval-chain-designer-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-28-approval-chain-designer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-28-approval-chain-designer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-28-approval-chain-designer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-28-approval-chain-designer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-28-approval-chain-designer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-28-approval-chain-designer-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-28-approval-chain-designer-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-28-approval-chain-designer-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Levels, approvers, time limit, escalation | E-F2-24 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Test | configurator | Sample amounts routed |
| Publish | configurator | Chain in force |

## States

- Normal: set the levels, approvers and time limits of a record type's approvals.
- Empty: no approval: "Records of this type need no approval", with Add a level.
- Loading: placeholders in the levels.
- Error: the error message pattern (D122).
- Read-only: for users who are not configurators; the owner reads it.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-24 Approval chain](../../data/e-f02-24-approval-chain.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-24 Approval chain | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-29); fields editable within the role | U07 | `u07-administrator/s-f02-28-approval-chain-designer-e-f02-24-approval-chain-draft-desktop-{light,dark}.png` |
| E-F2-24 Approval chain | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-28-approval-chain-designer-e-f02-24-approval-chain-published-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-11 Rights, translations and approvals](../../flows/fl-f02-11-rights-translations-and-approvals.md)

## Open questions

None.

---

⬅️ [S-F2-27 Translations](s-f02-27-translations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-29 Request type settings](../12-set-up-request-types/s-f02-29-request-type-settings.md)

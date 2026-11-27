🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-12 Set up request types](README.md) › 🖥️ S-F2-29 Request type settings

# 🖥️ S-F2-29 Request type settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every request type.
- Configurators ([D96](../../../../06-decisions/f02-no-code-configuration/d96-configurator-role.md)): the request types
  of the record types their other roles can see.

## Purpose

Set what scheduling takes into account for one type of customer request.

## Entry points

Configuration › Request types; a work request's type › Settings (for configurators); the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Request types › Bathing help                                    Draft · version 3 published  |
|---------------------------------------------------------------------------------------------|
| Default duration [60 min]                                                                   |
|                                                                                             |
| REQUIRED BY LAW (from the France pack, locked)                                              |
|   none for this type                                                                        |
|                                                                                             |
| ATTRIBUTES                          Required / Preferred       Weight                        |
|  Degrees and qualifications                                                                 |
|   Carer qualification            (x) Required ( ) Preferred                                 |
|  Skills and languages                                                                       |
|   French, B2 or more             ( ) Required (x) Preferred    [ 4 v ]                       |
|  Place and travel                                                                           |
|   Within the person's zones      ( ) Required (x) Preferred    [ 3 v ]                       |
|  Person and contract                                                                        |
|   [+ Add an attribute]                                                                      |
|                                                                                             |
| OBJECTIVES (drag to order)   1 Lateness  2 Travel  3 Customer preferences  4 Fairness  5 Cost |
| Automatic mode               [x] Allowed for this type                                      |
|                                                                                             |
| Preview: 9 of 14 carers eligible today          [Save draft] [Publish]           |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-12 step 1, U07 | desktop | ![FL-F2-12 step 1, U07, light](../../images/12-set-up-request-types/u07-administrator/1-request-type-settings-desktop-light.png) | ![FL-F2-12 step 1, U07, dark](../../images/12-set-up-request-types/u07-administrator/1-request-type-settings-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/12-set-up-request-types/u07-administrator/e1-a-legal-requirement-cannot-be-removed-desktop-light.png) | ![Error E1, U07, dark](../../images/12-set-up-request-types/u07-administrator/e1-a-legal-requirement-cannot-be-removed-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/12-set-up-request-types/u07-administrator/e2-nobody-is-eligible-desktop-light.png) | ![Error E2, U07, dark](../../images/12-set-up-request-types/u07-administrator/e2-nobody-is-eligible-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-29-request-type-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-29-request-type-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-29-request-type-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-29-request-type-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-29-request-type-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-29-request-type-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-29-request-type-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-29-request-type-settings-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Name | E-F2-25 name | text | yes | yes |
| Default duration | E-F2-25 default duration | minutes | yes | yes |
| Required by law | E-F2-25 legal requirements, from E-F9-30 and the packs | list | no | as the packs say |
| Attribute | E-F2-25 attributes, from the four families | picker | yes | no |
| Required or preferred | E-F2-25 attribute kind | choice | yes | yes, per attribute |
| Weight | E-F2-25 attribute weight | 1 to 5 (D517) | yes, if preferred | yes, if preferred |
| Objectives | E-F2-25 objective weights | ordered list | yes | yes |
| Automatic mode allowed | E-F2-25 flag | yes or no | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add an attribute | attributes | administrator, configurators | attribute row added |
| Save draft | footer | administrator, configurators | draft kept, not used |
| Publish | footer | administrator, configurators on their own drafts | new version used by new work requests (UC-F2-09) |
| Preview | footer | administrator, configurators | count of people eligible today |
| Retire | menu | administrator | type no longer offered; open work requests keep it |

## States

- Normal: the type's settings, editable as a draft.
- Empty: no request type yet: "Create your first request type", with the sector pack's templates.
- Loading: skeleton blocks; actions disabled until loaded.
- Error: the error message pattern (D122); the draft typed stays.
- Read-only: a configurator outside the type's record types; a retired type.
- Offline: not available offline (configuration).

Shown entities (VD-15): [E-F2-25 Request type](../../data/e-f02-25-request-type.md),
[E-F9-30 Qualification type](../../../f09-hr-and-projects/data/e-f09-30-qualification-type.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-25 Request type | Draft | Badge "Draft"; Save draft, Publish | U07 | `u07-administrator/s-f02-29-request-type-settings-e-f02-25-request-type-draft-desktop-{light,dark}.png` |
| E-F2-25 Request type | Published | Badge with the version; editing starts a new draft | U07 | `u07-administrator/s-f02-29-request-type-settings-e-f02-25-request-type-published-desktop-{light,dark}.png` |
| E-F2-25 Request type | Retired | Read-only; "Offer again" for the administrator | U07 | `u07-administrator/s-f02-29-request-type-settings-e-f02-25-request-type-retired-desktop-{light,dark}.png` |
| E-F9-30 Qualification type | Active | Badge "Active"; a new record starts here; next: Retired (UC-F9-38); fields editable within the role | U07 | `u07-administrator/s-f02-29-request-type-settings-e-f09-30-qualification-type-active-desktop-{light,dark}.png` |

The states are those of the entity draft.

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop first; on a tablet the same layout in one column; on a phone read-only (configuration).

## Accessibility

The objective order can be changed with the keyboard (move up, move down), not only by dragging; the locked legal
requirements say "required by law" in words; radio groups have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-12 Set up request types](../../flows/fl-f02-12-set-up-request-types.md)

## Open questions

None.

---

⬅️ [S-F2-28 Approval chain designer](../11-rights-translations-and-approvals/s-f02-28-approval-chain-designer.md) ·
⬆️ [Up](README.md) · ➡️ [S-F2-30 Custom report](../10-change-safely/s-f02-30-custom-report.md)

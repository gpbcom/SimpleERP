🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-11 Rights, translations and approvals](README.md) › 🖥️ S-F2-26 Field rights and validation

# 🖥️ S-F2-26 Field rights and validation

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md)

## Purpose

Set a field's rights per role and its validation.

## Entry points

A field › Rights and validation.

## Wireframe

```text
+------------------------------------------------------------------+
| Employee › Salary                                                |
| Role          Hidden  Masked  Read   Change                      |
| Manager       (o)                                                |
| HR                                   (o)                         |
| Validation  [range v]  min [0]  max [ ]                          |
| Message     [Salary cannot be negative]   [Preview as v] [Publish]|
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-11 step 1, U07 | desktop | ![FL-F2-11 step 1, U07, light](../../images/11-rights-translations-and-approvals/u07-administrator/1-field-rights-and-validation-desktop-light.png) | ![FL-F2-11 step 1, U07, dark](../../images/11-rights-translations-and-approvals/u07-administrator/1-field-rights-and-validation-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/11-rights-translations-and-approvals/u07-administrator/e1-field-rights-and-validation-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/11-rights-translations-and-approvals/u07-administrator/e1-field-rights-and-validation-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-26-field-rights-and-validation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-26-field-rights-and-validation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-26-field-rights-and-validation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-26-field-rights-and-validation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-26-field-rights-and-validation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-26-field-rights-and-validation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-26-field-rights-and-validation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-26-field-rights-and-validation-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Rights per role, validation, message | E-F2-22 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Preview as a role | configurator | The field as that role sees it |
| Publish | configurator | Applied on every channel |

## States

- Normal: set a field's rights per role and its validation.
- Empty: default rights: as the role ([BR-F2-03](../../business-rules/br-f02-03-field-visibility-per-role.md)).
- Loading: placeholders in the matrix.
- Error: the error message pattern (D122).
- Read-only: core fields' rights that the law fixes.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-22 Field rule](../../data/e-f02-22-field-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-22 Field rule | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-27); fields editable within the role | U06, U07 | `u06-hr/s-f02-26-field-rights-and-validation-e-f02-22-field-rule-draft-desktop-{light,dark}.png`, `u07-administrator/s-f02-26-field-rights-and-validation-e-f02-22-field-rule-draft-desktop-{light,dark}.png` |
| E-F2-22 Field rule | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U06, U07 | `u06-hr/s-f02-26-field-rights-and-validation-e-f02-22-field-rule-published-desktop-{light,dark}.png`, `u07-administrator/s-f02-26-field-rights-and-validation-e-f02-22-field-rule-published-desktop-{light,dark}.png` |

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

⬅️ [S-F2-25 Unused configuration report](../10-change-safely/s-f02-25-unused-configuration-report.md) ·
⬆️ [Up](README.md) · ➡️ [S-F2-27 Translations](s-f02-27-translations.md)

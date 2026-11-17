🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-11 Rights, translations and approvals](README.md) › 🖥️ S-F2-27 Translations

# 🖥️ S-F2-27 Translations

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Translate custom labels, statuses, values and messages.

## Entry points

Configuration › Translations.

## Wireframe

```text
+------------------------------------------------------------------+
| Translations  [English v]   42 items, 12 empty   [Import] [Export]|
| Item                    Français          English                |
| Status À planifier      À planifier       [To plan          ]    |
| Field Chantier          Chantier          [                 ]    |
|                     [Propose with the assistant] [Publish]       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-11 step 2, U07 | desktop | ![FL-F2-11 step 2, U07, light](../../images/11-rights-translations-and-approvals/u07-administrator/2-translations-desktop-light.png) | ![FL-F2-11 step 2, U07, dark](../../images/11-rights-translations-and-approvals/u07-administrator/2-translations-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-27-translations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-27-translations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-27-translations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-27-translations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-27-translations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-27-translations-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-27-translations-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-27-translations-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Item, company language, translation | E-F2-23 | translation |

## Actions

| Action | Who | Result |
|---|---|---|
| Propose | configurator | Drafts from the AI assistant |
| Publish | configurator | Shown to users |

## States

- Normal: translate custom labels, statuses, values and messages.
- Empty: one company language only: "Add a language to translate".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: core labels, translated by simple-ERP.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-23 Translation](../../data/e-f02-23-translation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-23 Translation | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-28); fields editable within the role | U07 | `u07-administrator/s-f02-27-translations-e-f02-23-translation-draft-desktop-{light,dark}.png` |
| E-F2-23 Translation | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-27-translations-e-f02-23-translation-published-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-11 Rights, translations and approvals](../../flows/fl-f02-11-rights-translations-and-approvals.md)

## Open questions

None.

---

⬅️ [S-F2-26 Field rights and validation](s-f02-26-field-rights-and-validation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-28 Approval chain designer](s-f02-28-approval-chain-designer.md)

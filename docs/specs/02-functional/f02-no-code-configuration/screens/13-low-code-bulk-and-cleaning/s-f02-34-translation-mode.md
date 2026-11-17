🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-13 Low code, bulk work and data cleaning](README.md) › 🖥️ S-F2-34 Translation mode

# 🖥️ S-F2-34 Translation mode

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the translations of their company.

## Purpose

Translate the texts of a screen where they appear and publish them as a language pack.

## Entry points

Any screen › Translate this screen; No-code configuration › Translations.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Translation mode: German                 62 % translated          [Next untranslated] [Publish] |
| ------------------------------------------------------------------------------------------- |
|    [Quotes]   [ Send quote ]   [Status: Draft]        <- every text on the screen is outlined |
| ------------------------------------------------------------------------------------------- |
| SOURCE   Send quote                      SCREEN  S-F6-04 Quote                              |
| GERMAN   Angebot senden                  State    Draft   [Suggest] [Save] [Mark reviewed]  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-13 step 4, U07 | desktop | ![FL-F2-13 step 4, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/4-translation-mode-desktop-light.png) | ![FL-F2-13 step 4, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/4-translation-mode-desktop-dark.png) |
| FL-F2-13 step 4, U07 | desktop | ![FL-F2-13 step 4, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/4-translation-mode-desktop-light.png) | ![FL-F2-13 step 4, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/4-translation-mode-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-34-translation-mode-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-34-translation-mode-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-34-translation-mode-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-34-translation-mode-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-34-translation-mode-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-34-translation-mode-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-34-translation-mode-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-34-translation-mode-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Source text | E-F2-33 source text | text | no | yes |
| Translation | E-F2-33 translated text | text with placeholders | yes | yes |
| Screen | E-F2-33 screen | link | no | yes |
| State | E-F2-33 state | badge | review | yes |
| Progress | texts translated | percent | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Suggest | editor | the editor | a machine suggestion, a draft |
| Save | editor | the editor | the entry is saved as a draft |
| Mark reviewed | editor | the reviewer | the entry can be published |
| Publish | header | the administrator | the reviewed entries show in the screens |
| Export or import a pack | menu | the administrator | a language pack file |

## States

- Normal: the real screen with its texts outlined, and the editor of the chosen text.
- Empty: Every text of this screen is translated.
- Loading: The screen loads first; the outlines and the progress follow.
- Error: the error message pattern (D122); a dropped placeholder is shown under the field.
- Read-only: a published pack of a retired language: its entries, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-33 Translation entry](../../data/e-f02-33-translation-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-33 Translation entry | Draft | Badge "Draft"; a new record starts here; next: Reviewed (UC-F2-34); fields editable within the role | U07 | `u07-administrator/s-f02-34-translation-mode-e-f02-33-translation-entry-draft-desktop-{light,dark}.png` |
| E-F2-33 Translation entry | Reviewed | Badge "Reviewed"; next: Published (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-34-translation-mode-e-f02-33-translation-entry-reviewed-desktop-{light,dark}.png` |
| E-F2-33 Translation entry | Published | Badge "Published"; next: Outdated or Draft (BR-F2-31, UC-F2-34); fields editable within the role | U07 | `u07-administrator/s-f02-34-translation-mode-e-f02-33-translation-entry-published-desktop-{light,dark}.png` |
| E-F2-33 Translation entry | Outdated | Badge "Outdated"; next: Draft or Reviewed (UC-F2-34); fields editable within the role | U07 | `u07-administrator/s-f02-34-translation-mode-e-f02-33-translation-entry-outdated-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

The outlines are not the only marker: the list of the screen's texts is also available as a table; keyboard: next text,
save.

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

⬅️ [S-F2-33 Time-based rule](s-f02-33-time-based-rule.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-35 Data cleaning](s-f02-35-data-cleaning.md)

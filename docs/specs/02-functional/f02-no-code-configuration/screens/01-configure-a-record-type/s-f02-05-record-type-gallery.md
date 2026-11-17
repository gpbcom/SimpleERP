🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-01 Configure a record type](README.md) › 🖥️ S-F2-05 Record type gallery

# 🖥️ S-F2-05 Record type gallery

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Purpose

Start a new record type from a model or blank.

## Entry points

Configuration › Record types › New.

## Wireframe

```text
+------------------------------------------------------------------+
| New record type                                [search models...]|
|------------------------------------------------------------------|
| [Blank]  [Vehicles]  [Equipment]  [Interventions]  [Members]      |
|          transport   construction home care        non-profit    |
| [Donations] [Contracts] ...                                      |
|------------------------------------------------------------------|
| Vehicles: plate, model, driver, next service date, statuses      |
|   In service -> In repair -> Retired          [Use this model]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-01 step 5, U07 | desktop | ![FL-F2-01 step 5, U07, light](../../images/01-configure-a-record-type/u07-administrator/5-new-record-type-desktop-light.png) | ![FL-F2-01 step 5, U07, dark](../../images/01-configure-a-record-type/u07-administrator/5-new-record-type-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-05-record-type-gallery-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-05-record-type-gallery-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-05-record-type-gallery-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-05-record-type-gallery-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-05-record-type-gallery-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-05-record-type-gallery-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-05-record-type-gallery-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-05-record-type-gallery-offline-desktop-dark.png) |

## Fields and columns

Model name, its sector pack, its fields and statuses.

## Actions

| Action | Who | Result |
|---|---|---|
| Use this model | configurator | A draft record type, copied |
| Blank | configurator | A draft with a name field only |

## States

- Normal: Start a new record type from a model or blank, as the wireframe shows.
- Empty: nothing to show yet.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: the gallery's models, which are copied, never changed.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Empty search: "No model: start blank or ask the assistant."

Shown entities (VD-15): [E-F2-05 Record type](../../data/e-f02-05-record-type.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-05 Record type | Draft | Badge "Draft"; a new record starts here; next: Live (UC-F2-04); fields editable within the role | U07 | `u07-administrator/s-f02-05-record-type-gallery-e-f02-05-record-type-draft-desktop-{light,dark}.png` |
| E-F2-05 Record type | Live | Badge "Live"; next: Archived (UC-F2-04); fields editable within the role | U07 | `u07-administrator/s-f02-05-record-type-gallery-e-f02-05-record-type-live-desktop-{light,dark}.png` |
| E-F2-05 Record type | Archived | Badge "Archived"; next: Live (UC-F2-04); fields editable within the role | U07 | `u07-administrator/s-f02-05-record-type-gallery-e-f02-05-record-type-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Models are a list of buttons with their description.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)

## Shown in

- [FL-F2-01 Configure a record type](../../flows/fl-f02-01-configure-a-record-type.md)

## Open questions

None.

---

⬅️ [S-F2-04 List view settings](s-f02-04-list-view-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-06 Document template editor](../02-customise-documents-and-emails/s-f02-06-document-template-editor.md)

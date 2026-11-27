🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-07 Benchmark additions](README.md) › 🖥️ S-F2-12 Spreadsheet

# 🖥️ S-F2-12 Spreadsheet

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Build live spreadsheets and dashboards.

## Entry points

No-code configuration in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-07 step 1, U02 | desktop | ![FL-F2-07 step 1, U02, light](../../images/07-benchmark-additions/u02-manager/1-spreadsheet-desktop-light.png) | ![FL-F2-07 step 1, U02, dark](../../images/07-benchmark-additions/u02-manager/1-spreadsheet-desktop-dark.png) |
| FL-F2-07 step 1, U02 | phone | ![FL-F2-07 step 1, U02, light](../../images/07-benchmark-additions/u02-manager/1-spreadsheet-phone-light.png) | ![FL-F2-07 step 1, U02, dark](../../images/07-benchmark-additions/u02-manager/1-spreadsheet-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-12-spreadsheet-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-12-spreadsheet-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-12-spreadsheet-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-12-spreadsheet-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-12-spreadsheet-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-12-spreadsheet-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f02-12-spreadsheet-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f02-12-spreadsheet-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Build live spreadsheets and dashboards, as the wireframe shows.
- Empty: a blank sheet with Add data from a record type.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a sheet shared with the user without the edit right.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F2-12 Spreadsheet](../../data/e-f02-12-spreadsheet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-12 Spreadsheet | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U05, U13 | `u02-manager/s-f02-12-spreadsheet-e-f02-12-spreadsheet-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-12-spreadsheet-e-f02-12-spreadsheet-active-desktop-{light,dark}.png`, `u13-owner/s-f02-12-spreadsheet-e-f02-12-spreadsheet-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F2-07 Benchmark additions](../../flows/fl-f02-07-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F2-11 Packs](../06-share-a-configuration/s-f02-11-packs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-13 Documents workspace](s-f02-13-documents-workspace.md)

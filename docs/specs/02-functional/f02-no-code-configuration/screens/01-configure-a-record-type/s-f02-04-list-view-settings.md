🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-01 Configure a record type](README.md) › 🖥️ S-F2-04 List view settings

# 🖥️ S-F2-04 List view settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role
- Every user, for personal views

## Purpose

Arrange a list: columns, filters, sort, grouping; save as a personal or shared view.

## Entry points

The view menu of any list.

## Wireframe

```text
+-------------------------------------------+
| View: [ My open quotes v ]   [Save as...] |
|-------------------------------------------|
| Columns  [x] Customer [x] Amount [ ] Margin |
| Filter   Status is Sent or Draft          |
| Sort     Amount, high first               |
| Group by Customer                          |
| Share with roles [ Sales x ] (configurators)|
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-01 step 4, U01 | desktop | ![FL-F2-01 step 4, U01, light](../../images/01-configure-a-record-type/u01-employee/4-personal-list-view-desktop-light.png) | ![FL-F2-01 step 4, U01, dark](../../images/01-configure-a-record-type/u01-employee/4-personal-list-view-desktop-dark.png) |
| FL-F2-01 step 4, U01 | phone | ![FL-F2-01 step 4, U01, light](../../images/01-configure-a-record-type/u01-employee/4-personal-list-view-phone-light.png) | ![FL-F2-01 step 4, U01, dark](../../images/01-configure-a-record-type/u01-employee/4-personal-list-view-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-04-list-view-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-04-list-view-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-04-list-view-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-04-list-view-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-04-list-view-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-04-list-view-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-04-list-view-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-04-list-view-settings-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-04 List view](../../data/e-f02-04-list-view.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Save as personal | every user | Their view |
| Share with roles | configurator | Shared view, after publishing |

## States

- Normal: Arrange a list: columns, filters, sort, grouping; save as a personal or shared view, as the wireframe shows.
- Empty: no saved view yet: the default columns, with Save as a view.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: shared views for their non-owners.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Shared views are marked; personal views can be deleted by their owner.

Shown entities (VD-15): [E-F2-03 Form layout](../../data/e-f02-03-form-layout.md),
[E-F2-04 List view](../../data/e-f02-04-list-view.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-03 Form layout | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-03); fields editable within the role | U01 | `u01-employee/s-f02-04-list-view-settings-e-f02-03-form-layout-draft-{desktop,phone}-{light,dark}.png` |
| E-F2-03 Form layout | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U01 | `u01-employee/s-f02-04-list-view-settings-e-f02-03-form-layout-published-{desktop,phone}-{light,dark}.png` |
| E-F2-04 List view | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-03); fields editable within the role | U01, U07 | `u01-employee/s-f02-04-list-view-settings-e-f02-04-list-view-draft-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f02-04-list-view-settings-e-f02-04-list-view-draft-desktop-{light,dark}.png` |
| E-F2-04 List view | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U01, U07 | `u01-employee/s-f02-04-list-view-settings-e-f02-04-list-view-published-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f02-04-list-view-settings-e-f02-04-list-view-published-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

On a phone, a view chooses the fields shown on each card.

## Accessibility

Each setting is a labelled control.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [Search and filter pattern](../../../../04-ux/design-system/patterns/search-and-filter.md)

## Shown in

- [FL-F2-01 Configure a record type](../../flows/fl-f02-01-configure-a-record-type.md)

## Open questions

None.

---

⬅️ [S-F2-03 Form designer](s-f02-03-form-designer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-05 Record type gallery](s-f02-05-record-type-gallery.md)

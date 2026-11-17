🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-01 Configure a record type](README.md) › 🖥️ S-F2-03 Form designer

# 🖥️ S-F2-03 Form designer

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role

## Purpose

Arrange a record type's form per role and for phones.

## Entry points

Record type editor (S-F2-01) › Form; "Customise this form" on a form.

## Wireframe

```text
+------------------------------------------------------------------+
| Quotes > Form     Layout for [ Sales v ]   [Phone] [Preview as v]|
|------------------------------------------------------------------|
| Fields             | Section: Customer                          |
|  Customer   [drag] |   Customer        [ ............ ]          |
|  Vehicle    [drag] |   Contact         [ ............ ]          |
|  Margin     [drag] | Section: Lines                             |
|                    |   Lines table                              |
|                    | Vehicle: show when Delivery is filled       |
|                    | Price: read-only from Sent                 |
|                                          [Publish]               |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-01 step 3, U07 | desktop | ![FL-F2-01 step 3, U07, light](../../images/01-configure-a-record-type/u07-administrator/3-arrange-the-form-desktop-light.png) | ![FL-F2-01 step 3, U07, dark](../../images/01-configure-a-record-type/u07-administrator/3-arrange-the-form-desktop-dark.png) |
| Error E6, U07 | desktop | ![Error E6, U07, light](../../images/01-configure-a-record-type/u07-administrator/e6-required-field-missing-desktop-light.png) | ![Error E6, U07, dark](../../images/01-configure-a-record-type/u07-administrator/e6-required-field-missing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-03-form-designer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-03-form-designer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-03-form-designer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-03-form-designer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-03-form-designer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-03-form-designer-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-03-form-designer-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-03-form-designer-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-03 Form layout](../../data/e-f02-03-form-layout.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Drag a field into a section | configurator | Draft |
| Condition, read-only from a status | configurator | Draft |
| Preview as a role | configurator | The form as that role sees it |
| Publish | configurator | UC-F2-09 |

## States

- Normal: Arrange a record type's form per role and for phones, as the wireframe shows.
- Empty: a single section holding every field, until the configurator arranges it.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: for configurators without the right on that record type.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Draft banner.
- Warning: a condition on a missing field; refused: a required field missing from a role's layout.

Shown entities (VD-15): [E-F2-03 Form layout](../../data/e-f02-03-form-layout.md),
[E-F2-04 List view](../../data/e-f02-04-list-view.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-03 Form layout | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-03); fields editable within the role | U07 | `u07-administrator/s-f02-03-form-designer-e-f02-03-form-layout-draft-desktop-{light,dark}.png` |
| E-F2-03 Form layout | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-03-form-designer-e-f02-03-form-layout-published-desktop-{light,dark}.png` |
| E-F2-04 List view | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-03); fields editable within the role | U07 | `u07-administrator/s-f02-03-form-designer-e-f02-04-list-view-draft-desktop-{light,dark}.png` |
| E-F2-04 List view | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-03-form-designer-e-f02-04-list-view-published-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the phone tab previews the phone layout.

## Accessibility

Every drag has a keyboard alternative (move up, move down, move to section).

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)

## Shown in

- [FL-F2-01 Configure a record type](../../flows/fl-f02-01-configure-a-record-type.md)

## Open questions

None.

---

⬅️ [S-F2-02 Status designer](s-f02-02-status-designer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-04 List view settings](s-f02-04-list-view-settings.md)

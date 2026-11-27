🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-09 Portals and offline forms](README.md) › 🖥️ S-F2-21 Offline form

# 🖥️ S-F2-21 Offline form

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U26 Carer](../../../../01-users/personas/u26-carer.md)
- [U30 Driver](../../../../01-users/personas/u30-driver.md)

## Purpose

Set a phone form to work offline, and fill it offline on the phone.

## Entry points

A record type › Offline (configurator); the record on the phone (field staff).

## Wireframe

```text
Settings (desktop)
  Site diary › Offline  Keep [my sites, next 7 days v]
  Conflict [merge field by field v]  Size per phone 12 MB  [Publish]
Phone (390 px)
  +----------------------------+
  | Offline · 2 waiting        |
  | Site diary, Lyon yard      |
  | Weather [rain v]           |
  | Workers [6]                |
  | Notes [concrete poured   ] |
  | [Photo] [Signature]        |
  | [Save]                     |
  +----------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-09 step 3, U07 | desktop | ![FL-F2-09 step 3, U07, light](../../images/09-portals-and-offline-forms/u07-administrator/3-offline-form-desktop-light.png) | ![FL-F2-09 step 3, U07, dark](../../images/09-portals-and-offline-forms/u07-administrator/3-offline-form-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-21-offline-form-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-21-offline-form-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-21-offline-form-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-21-offline-form-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-21-offline-form-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-21-offline-form-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-21-offline-form-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-21-offline-form-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Records kept, conflict rule, roles | E-F2-20 | configurator |
| The form's fields | the record type's phone layout | field staff |

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | configurator | Phones download at next sync |
| Save | field staff | Queued offline |
| Sync now | field staff | Queue sent |

## States

- Normal: set a phone form to work offline, and fill it offline on the phone.
- Empty: no record for today on the phone: "Nothing kept for today; sync when you have network".
- Loading: the form's fields greyed while the record opens from the phone's store.
- Error: the error message pattern (D122).
- Read-only: records the user may only read, and records already synced and closed.
- Offline: Works offline: the records kept stay on the phone, saved records wait in a queue shown with its count, and
  sync in order when the network is back,
  [BR-F2-21](../../business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-F2-03 Form layout](../../data/e-f02-03-form-layout.md),
[E-F2-28 Offline change queue](../../data/e-f02-28-offline-change-queue.md),
[E-F2-20 Offline form setting](../../data/e-f02-20-offline-form-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-03 Form layout | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-03); fields editable within the role | U07, U14, U26 | `u07-administrator/s-f02-21-offline-form-e-f02-03-form-layout-draft-desktop-{light,dark}.png`, `u14-field-worker/s-f02-21-offline-form-e-f02-03-form-layout-draft-phone-{light,dark}.png`, `u26-carer/s-f02-21-offline-form-e-f02-03-form-layout-draft-phone-{light,dark}.png` |
| E-F2-03 Form layout | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07, U14, U26 | `u07-administrator/s-f02-21-offline-form-e-f02-03-form-layout-published-desktop-{light,dark}.png`, `u14-field-worker/s-f02-21-offline-form-e-f02-03-form-layout-published-phone-{light,dark}.png`, `u26-carer/s-f02-21-offline-form-e-f02-03-form-layout-published-phone-{light,dark}.png` |
| E-F2-28 Offline change queue | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U14, U26 | `u07-administrator/s-f02-21-offline-form-e-f02-28-offline-change-queue-active-desktop-{light,dark}.png`, `u14-field-worker/s-f02-21-offline-form-e-f02-28-offline-change-queue-active-phone-{light,dark}.png`, `u26-carer/s-f02-21-offline-form-e-f02-28-offline-change-queue-active-phone-{light,dark}.png` |
| E-F2-20 Offline form setting | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-21); fields editable within the role | U07, U14, U26 | `u07-administrator/s-f02-21-offline-form-e-f02-20-offline-form-setting-draft-desktop-{light,dark}.png`, `u14-field-worker/s-f02-21-offline-form-e-f02-20-offline-form-setting-draft-phone-{light,dark}.png`, `u26-carer/s-f02-21-offline-form-e-f02-20-offline-form-setting-draft-phone-{light,dark}.png` |
| E-F2-20 Offline form setting | Published | Badge "Published"; next: Archived (UC-F2-21); fields editable within the role | U07, U14, U26 | `u07-administrator/s-f02-21-offline-form-e-f02-20-offline-form-setting-published-desktop-{light,dark}.png`, `u14-field-worker/s-f02-21-offline-form-e-f02-20-offline-form-setting-published-phone-{light,dark}.png`, `u26-carer/s-f02-21-offline-form-e-f02-20-offline-form-setting-published-phone-{light,dark}.png` |
| E-F2-20 Offline form setting | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U07, U14, U26 | `u07-administrator/s-f02-21-offline-form-e-f02-20-offline-form-setting-archived-desktop-{light,dark}.png`, `u14-field-worker/s-f02-21-offline-form-e-f02-20-offline-form-setting-archived-phone-{light,dark}.png`, `u26-carer/s-f02-21-offline-form-e-f02-20-offline-form-setting-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Settings on desktop; the form on a phone.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-09 Portals and offline forms](../../flows/fl-f02-09-portals-and-offline-forms.md)

## Open questions

None.

---

⬅️ [S-F2-20 Portal settings](s-f02-20-portal-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-22 Impact analysis](../10-change-safely/s-f02-22-impact-analysis.md)

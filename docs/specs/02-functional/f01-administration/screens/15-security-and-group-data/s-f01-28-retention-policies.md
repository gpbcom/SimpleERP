🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-15 Security and group data](README.md) › 🖥️ S-F1-28 Retention policies

# 🖥️ S-F1-28 Retention policies

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the policies of the company.

## Purpose

Set how long each kind of personal data is kept, preview a purge and read the purge log.

## Entry points

Administration › Privacy › Retention; the record of processing activities
([UC-F1-12](../../use-cases/09-administration-reports/uc-f01-12-draft-the-record-of-processing-activities.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Retention policies                                                [Preview] [Purge log]     |
| ------------------------------------------------------------------------------------------- |
| RECORD TYPE     STARTS FROM         PERIOD      THEN         LEGAL MINIMUM        STATE     |
| Customer        last contact        3 years     anonymise    none                 Active    |
| Applicant       last contact        2 years     delete       2 years (HR)         Active    |
| Invoice         issue date          10 years    keep         10 years (accounts)  Locked    |
| Preview of the next run: 412 to anonymise, 38 kept for a legal reason   [Switch on]         |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-15 step 2, U07 | desktop | ![FL-F1-15 step 2, U07, light](../../images/15-security-and-group-data/u07-administrator/2-retention-policies-desktop-light.png) | ![FL-F1-15 step 2, U07, dark](../../images/15-security-and-group-data/u07-administrator/2-retention-policies-desktop-dark.png) |
| FL-F1-15 step 2, U07 | desktop | ![FL-F1-15 step 2, U07, light](../../images/15-security-and-group-data/u07-administrator/2-retention-policies-desktop-light.png) | ![FL-F1-15 step 2, U07, dark](../../images/15-security-and-group-data/u07-administrator/2-retention-policies-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-28-retention-policies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-28-retention-policies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-28-retention-policies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-28-retention-policies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-28-retention-policies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-28-retention-policies-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-28-retention-policies-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-28-retention-policies-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Record type | E-F1-24 record type | text | no | yes |
| Starts from | E-F1-24 start event | choice | yes | yes |
| Period | E-F1-24 period | number and unit | yes, not under the legal minimum | yes |
| Then | E-F1-24 action | delete, anonymise | yes | yes |
| Legal minimum | E-F1-24 legal minimum | period and source | no | no |
| State | E-F1-24 state | badge | switch on, pause | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Preview | header | the administrator | counts what the next run would purge |
| Switch on, pause | row | the administrator | the policy runs or stops |
| Purge log | header | the administrator | the runs with their counts |
| Show kept records | preview | the administrator | the records kept and the legal reason |

## States

- Normal: the record types with their periods, the legal minimum and the state of each policy.
- Empty: No policy yet: the country pack's periods are offered to start from.
- Loading: The policies load first; the counts of the preview follow.
- Error: the error message pattern (D122); a period under the legal minimum is refused under its field
  ([BR-F1-34](../../business-rules/br-f01-34-purges-are-logged-and-never-touch-legal-records.md)).
- Read-only: a retired policy: its periods and its runs, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-24 Retention policy](../../data/e-f01-24-retention-policy.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-24 Retention policy | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F1-25); fields editable within the role | U07 | `u07-administrator/s-f01-28-retention-policies-e-f01-24-retention-policy-draft-desktop-{light,dark}.png` |
| E-F1-24 Retention policy | Active | Badge "Active"; next: Paused or Retired (UC-F1-25); fields editable within the role | U07 | `u07-administrator/s-f01-28-retention-policies-e-f01-24-retention-policy-active-desktop-{light,dark}.png` |
| E-F1-24 Retention policy | Paused | Badge "Paused"; next: Active or Retired (UC-F1-25); fields editable within the role | U07 | `u07-administrator/s-f01-28-retention-policies-e-f01-24-retention-policy-paused-desktop-{light,dark}.png` |
| E-F1-24 Retention policy | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f01-28-retention-policies-e-f01-24-retention-policy-retired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Each period is read as a number and a unit; the preview's counts are announced; keyboard: next row, switch on.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-15 Security and group data](../../flows/fl-f01-15-security-and-group-data.md)

## Open questions

None.

---

⬅️ [S-F1-27 Sessions and devices](s-f01-27-sessions-and-devices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-29 Group sharing](s-f01-29-group-sharing.md)

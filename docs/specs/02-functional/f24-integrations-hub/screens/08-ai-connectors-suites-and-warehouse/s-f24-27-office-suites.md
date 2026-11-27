🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-08 AI connectors, office suites, warehouse and firms](README.md) › 🖥️ S-F24-27 Office suites

# 🖥️ S-F24-27 Office suites

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every suite, component and permission of the
  company.

## Purpose

Connect Google Workspace or Microsoft 365 with the fewest permissions the chosen features need.

## Entry points

Integrations › Office suites; a feature that needs a suite; the catalogue.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Office suites    [Google Workspace] [Microsoft 365] [openDesk] [La Suite numerique]           |
|---------------------------------------------------------------------------------------------|
| COMPONENT   USED BY                     PERMISSION                 WHY                STATE  |
| Calendar    meetings, planning          read and write events      create meetings    On    |
| Mail        send quotes from the suite  send as the user           quotes by mail     On    |
| Files       attach documents            read the chosen folder     documents          On    |
| Contacts    -                           none                       not used           Off   |
| [Connect] [Revoke] [Open consent page]                                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-08 step 2, U07 | desktop | ![FL-F24-08 step 2, U07, light](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/2-office-suites-desktop-light.png) | ![FL-F24-08 step 2, U07, dark](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/2-office-suites-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-27-office-suites-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-27-office-suites-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-27-office-suites-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-27-office-suites-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-27-office-suites-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-27-office-suites-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-27-office-suites-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-27-office-suites-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Suite | suite name | tab | no | yes |
| Component | mail, calendar, contacts, files, chat | text | no | yes |
| Used by | features using the component | text | no | yes |
| Permission and why | scopes requested | text per scope | no | yes |
| State | on, off, error | badge | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Connect | header | administrator | sends the administrator to the suite's consent page |
| Revoke | row | administrator | removes the component's permissions at the suite |
| Open consent page | row | administrator | opens the suite's own page for the tenant |

## States

- Normal: the suites and, for the chosen one, each component with its permissions and state.
- Empty: No suite connected, with the four suites to connect.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  consent names the permission refused and offers Connect again.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F24-08](../../flows/fl-f24-08-ai-connectors-suites-and-warehouse.md)

## Open questions

None.

---

⬅️ [S-F24-26 AI connector builder](s-f24-26-ai-connector-builder.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-28 Warehouse export](s-f24-28-warehouse-export.md)

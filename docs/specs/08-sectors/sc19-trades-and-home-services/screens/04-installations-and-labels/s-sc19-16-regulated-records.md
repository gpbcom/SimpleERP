🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-04 Installations and labels](README.md) › 🖥️ S-SC19-16 Regulated records

# 🖥️ S-SC19-16 Regulated records

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the refrigerant records and connections of an
  installation, on the phone.

## Purpose

Record refrigerant handling, leak checks and grid connections with the certificate checked.

## Entry points

Trades and home services › Regulated records; an installation's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Regulated records: N-0210, heat pump Nordic                    [New record]                      |
| Kind              Date      Technician  Quantity   Certificate   State                           |
| Refrigerant charge 5 Feb     Leroy       2.4 kg     valid         Closed                         |
| Leak check         5 Feb     Leroy       none       valid         Closed                         |
| Grid connection    22 Feb    Petit       -          conformity    Submitted                      |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-04 step 4, U14 | phone | ![FL-SC19-04 step 4, U14, light](../../images/04-installations-and-labels/u14-field-worker/4-regulated-records-phone-light.png) | ![FL-SC19-04 step 4, U14, dark](../../images/04-installations-and-labels/u14-field-worker/4-regulated-records-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-16-regulated-records-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-16-regulated-records-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-16-regulated-records-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-16-regulated-records-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-16-regulated-records-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-16-regulated-records-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-16-regulated-records-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-16-regulated-records-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind | E-SC19-10 kind | refrigerant, leak check, grid connection | yes while Drafted | yes |
| Equipment | E-SC19-10 equipment | text with its charge | yes while Drafted | yes |
| Quantity | E-SC19-10 quantity | number in kilograms | yes while Drafted | yes for a refrigerant |
| Technician | E-SC19-10 technician | link | no | yes |
| Certificate | E-SC19-10 certificate | link to the qualification | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New record | header | technician | a record is started and the certificate checked |
| Close | row | technician | the record is closed with its quantities |
| Extract | header | owner | the records are exported for an inspector |

## States

- Normal: the records with kind, equipment, quantity, technician, certificate and state.
- Empty: No regulated record yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  certificate, a quantity not entered, with the record named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-10 Regulated record](../../data/e-sc19-10-regulated-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-10 Regulated record | Drafted | Badge "Drafted"; a new record starts here; next: Closed or Refused (BR-SC19-16); fields editable within the role | U14 | `u14-field-worker/s-sc19-16-regulated-records-e-sc19-10-regulated-record-drafted-phone-{light,dark}.png` |
| E-SC19-10 Regulated record | Closed | Badge "Closed"; next: Submitted (UC-SC19-16); fields editable within the role | U14 | `u14-field-worker/s-sc19-16-regulated-records-e-sc19-10-regulated-record-closed-phone-{light,dark}.png` |
| E-SC19-10 Regulated record | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U14 | `u14-field-worker/s-sc19-16-regulated-records-e-sc19-10-regulated-record-refused-phone-{light,dark}.png` |
| E-SC19-10 Regulated record | Submitted | Badge "Submitted"; next: Closed (UC-SC19-16); fields editable within the role | U14 | `u14-field-worker/s-sc19-16-regulated-records-e-sc19-10-regulated-record-submitted-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

- [FL-SC19-04 Installations and labels](../../flows/fl-sc19-04-installations-and-labels.md)

## Open questions

None.

---

⬅️ [S-SC19-15 RGE evidence](s-sc19-15-rge-evidence.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-17 On-call](../05-on-call-warranties-van-stock-and-site-quotes/s-sc19-17-on-call.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-02 On-site intervention](README.md) › 🖥️ S-SC19-06 Site report

# 🖥️ S-SC19-06 Site report

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): the report on the phone, with times, place,
  photos and the work done.

## Purpose

Record an intervention's times, place, photos and work done, and close it for signature.

## Entry points

Trades and home services › My interventions; the dispatched intervention on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Report I-3305: Garcia, leak under the sink                       [Arrived] [Finished]            |
| Arrived 10:22   Place checked: 40 m from address   Left -                                        |
| Photos before: 2   Photos after: 1   [Add photo]                                                 |
| Cause: Worn seal under the sink      Work done: Seal replaced                                    |
| [Read with the customer]                                                                         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-02 step 2, U14 | phone | ![FL-SC19-02 step 2, U14, light](../../images/02-on-site-intervention/u14-field-worker/2-site-report-phone-light.png) | ![FL-SC19-02 step 2, U14, dark](../../images/02-on-site-intervention/u14-field-worker/2-site-report-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-06-site-report-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-06-site-report-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-06-site-report-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-06-site-report-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-06-site-report-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-06-site-report-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-06-site-report-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-06-site-report-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Arrived at | E-SC19-05 arrived | time | no | yes |
| Place check | E-SC19-05 place | distance in metres | no | yes |
| Photos | E-SC19-05 photos | images with a label before or after | yes while Open | yes |
| Cause found | E-SC19-05 cause | text | yes while Open | yes |
| Work done | E-SC19-05 work | text | yes while Open | yes |
| Left at | E-SC19-05 left | time | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Arrived | header | technician | the time and the place check are recorded |
| Add photo | form | technician | a photo is attached with its label |
| Finished | header | technician | the departure time is recorded and the report is closed |

## States

- Normal: the report with its times, place, photos, cause and work.
- Empty: No intervention to report.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  photo, a place far from the address, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-05 Site report](../../data/e-sc19-05-site-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-05 Site report | Open | Badge "Open"; a new record starts here; next: Closed (BR-SC19-06); fields editable within the role | U14 | `u14-field-worker/s-sc19-06-site-report-e-sc19-05-site-report-open-phone-{light,dark}.png` |
| E-SC19-05 Site report | Closed | Badge "Closed"; next: Signed (UC-SC19-08); fields editable within the role | U14 | `u14-field-worker/s-sc19-06-site-report-e-sc19-05-site-report-closed-phone-{light,dark}.png` |
| E-SC19-05 Site report | Signed | Badge "Signed"; final: read-only, no next state; the history shows how it got here | U14 | `u14-field-worker/s-sc19-06-site-report-e-sc19-05-site-report-signed-phone-{light,dark}.png` |

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

- [FL-SC19-02 On-site intervention](../../flows/fl-sc19-02-on-site-intervention.md)

## Open questions

None.

---

⬅️ [S-SC19-05 Dispatch](s-sc19-05-dispatch.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-07 Parts used](s-sc19-07-parts-used.md)

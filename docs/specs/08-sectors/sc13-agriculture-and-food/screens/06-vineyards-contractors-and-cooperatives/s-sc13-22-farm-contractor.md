🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC13-06 Vineyards, contractors, cooperatives, baskets, forests](README.md) ›
🖥️ S-SC13-22 Farm contractor

# 🖥️ S-SC13-22 Farm contractor

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md): the jobs, the machines and the invoices.
- [U30 Driver](../../../../01-users/personas/u30-driver.md): the driver's day on the phone: the job to start, its track
  and its finish.

## Purpose

Plan the jobs on machines and drivers, record what was worked and bill each farm by the hectare or by the hour as
agreed.

## Entry points

Agriculture › Jobs; the planner; the driver's day on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Jobs: week 24                                                   [New job] [Plan] [Invoice farms] |
| Job   Farm          Work        Field   Basis     Quantity   Machine   Driver   State            |
| J-210 Ferme Aubin   Baling      14 ha   Hectare   13.8 ha    Press 2   Lucas    Done             |
| J-211 GAEC Moulin   Spraying    22 ha   Hectare   -          Sprayer   Lucas    Scheduled        |
| J-212 Ferme Aubin   Tillage     -       Hour      6.5 h      Tractor 4 Hugo     Invoiced         |
| To invoice: 1 job, 579.60 EUR                                   [Confirm quantity]               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-06 step 2, U40 | desktop | ![FL-SC13-06 step 2, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/2-farm-contractor-desktop-light.png) | ![FL-SC13-06 step 2, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/2-farm-contractor-desktop-dark.png) |
| FL-SC13-06 step 2, U40 | phone | ![FL-SC13-06 step 2, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/2-farm-contractor-phone-light.png) | ![FL-SC13-06 step 2, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/2-farm-contractor-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-22-farm-contractor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-22-farm-contractor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-22-farm-contractor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-22-farm-contractor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-22-farm-contractor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-22-farm-contractor-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-22-farm-contractor-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-22-farm-contractor-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Farm | E-SC13-18 farm | link | yes while Quoted | yes |
| Work | E-SC13-18 work | text | yes while Quoted | yes |
| Basis | E-SC13-18 basis | hectare or hour | yes while Quoted | yes |
| Price | E-SC13-18 price | amount in EUR | yes while Quoted | yes |
| Quantity | E-SC13-18 quantity | number in hectares or hours | yes while Scheduled | yes to invoice |
| Machine and driver | E-SC13-18 machine, driver | links | yes while Quoted | yes |
| Amount | E-SC13-18 amount | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New job | header | farmer | a job in state Quoted |
| Plan | job | farmer | the machine and driver are booked and the job is Scheduled |
| Finish job | job on the phone | driver | the quantity is confirmed and the job is Done |
| Invoice farms | header | farmer | the Done jobs become invoice lines and are Invoiced |

## States

- Normal: the week's jobs with their farm, basis, quantity, machine, driver and state.
- Empty: No job yet, with New job.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing basis
  or quantity, a clash on a machine or a driver, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC13-18 Field job](../../data/e-sc13-18-field-job.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-18 Field job | Quoted | Badge "Quoted"; a new record starts here; next: Scheduled or Cancelled (UC-SC13-22); fields editable within the role | U40, U30 | `u40-farmer/s-sc13-22-farm-contractor-e-sc13-18-field-job-quoted-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc13-22-farm-contractor-e-sc13-18-field-job-quoted-phone-{light,dark}.png` |
| E-SC13-18 Field job | Scheduled | Badge "Scheduled"; next: Done (BR-SC13-17); fields editable within the role | U40, U30 | `u40-farmer/s-sc13-22-farm-contractor-e-sc13-18-field-job-scheduled-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc13-22-farm-contractor-e-sc13-18-field-job-scheduled-phone-{light,dark}.png` |
| E-SC13-18 Field job | Done | Badge "Done"; next: Invoiced (BR-SC13-17); fields editable within the role | U40, U30 | `u40-farmer/s-sc13-22-farm-contractor-e-sc13-18-field-job-done-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc13-22-farm-contractor-e-sc13-18-field-job-done-phone-{light,dark}.png` |
| E-SC13-18 Field job | Invoiced | Badge "Invoiced"; final: read-only, no next state; the history shows how it got here | U40, U30 | `u40-farmer/s-sc13-22-farm-contractor-e-sc13-18-field-job-invoiced-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc13-22-farm-contractor-e-sc13-18-field-job-invoiced-phone-{light,dark}.png` |
| E-SC13-18 Field job | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U40, U30 | `u40-farmer/s-sc13-22-farm-contractor-e-sc13-18-field-job-cancelled-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc13-22-farm-contractor-e-sc13-18-field-job-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The driver's phone shows one job at a time with large Start and Finish buttons.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC13-06](../../flows/fl-sc13-06-vineyards-contractors-and-cooperatives.md)

## Open questions

None.

---

⬅️ [S-SC13-21 Vineyard](s-sc13-21-vineyard.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-23 Cooperative](s-sc13-23-cooperative.md)

🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-06 Care homes, CESU, agent mode, childcare and nursing](README.md) ›
🖥️ S-SC04-16 Care home

# 🖥️ S-SC04-16 Care home

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md): every resident, room and contract.
- [U26 Carer](../../../../01-users/personas/u26-carer.md): the residents they care for today.

## Purpose

Run the waiting list, admissions, rooms and stays, and open a resident's care record to the people allowed to read it.

## Entry points

Home care › Residents; the room plan; the carer's day list on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Resident: Odette L., room 12                                         Admitted   [Save] [Absent]  |
| Born 1940-05-08   Admitted 2026-09-01   Dependency level 2   Representative: Paul L. (son)       |
| Stay contract  social-aid home: handed over 2026-09-05, signed 2026-09-20                        |
|                withdrawal until 2026-10-05                                                       |
| Rates/day: accommodation 68.40, dependency 21.90, care 0.00                                      |
| Funding  Departmental allowance, health insurance      Care plan  v2, 2026-10-12                 |
| Care today  Morning care done (Aisha T.)   Meals 3/3   Walk 1/1                                  |
| Care record readable by: carers of room 12, coordinator       Access log [Open]                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-06 step 1, U25 | desktop | ![FL-SC04-06 step 1, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/1-care-home-desktop-light.png) | ![FL-SC04-06 step 1, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/1-care-home-desktop-dark.png) |
| FL-SC04-06 step 1, U25 | phone | ![FL-SC04-06 step 1, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/1-care-home-phone-light.png) | ![FL-SC04-06 step 1, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/1-care-home-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-16-care-home-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-16-care-home-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-16-care-home-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-16-care-home-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-16-care-home-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-16-care-home-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-16-care-home-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-16-care-home-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Resident | E-SC04-14 care recipient | link | no | yes |
| Room and dates | E-SC04-14 room, admitted on | text and date | yes while Waiting | yes |
| Dependency level | E-SC04-14 dependency level | level 1 to 6 | yes | yes |
| Representative | E-SC04-14 representative | person | yes | no |
| Social-aid home | E-SC04-14 social-aid home, from the home's settings | yes or no | no | yes |
| Contract handed over | E-SC04-14 contract handed over on | date; within 15 days of admission in a social-aid home | yes while Admitted | yes in a social-aid home |
| Stay contract | E-SC04-14 contract signed on, and the withdrawal deadline | date: within 1 month of admission in a social-aid home, before admission in any other home; withdrawal in writing within 15 days of signing, or of admission if later ([CR-FR-256](../../../../10-country-packs/france/home-care/cr-fr-256-care-home-resident-contract.md)) | no | yes |
| Daily rates | E-SC04-14 rates | amounts per day | yes while Waiting or Admitted | yes |
| Care of the day | E-SC04-06 entries | list | yes for carers | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Admit | waiting list | coordinator | the resident becomes Admitted |
| Sign contract | resident | resident or representative | the contract is signed |
| Mark absent | resident | coordinator | the resident becomes Absent from a date |
| Record departure | resident | coordinator | the resident becomes Left |

## States

- Normal: the resident with their room, contract, rates, care plan and the care of the day.
- Empty: No resident yet, with Add to the waiting list.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a stay contract
  late (in a social-aid home, not handed over within 15 days of admission or not signed within 1 month: the resident
  stays Admitted and the coordinator is alerted; in any other home, not signed before admission: the admission is
  held), or an access refused, with the person to ask.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC04-14 Resident](../../data/e-sc04-14-resident.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-14 Resident | Waiting | Badge "Waiting"; a new record starts here; next: Admitted or Left (UC-SC04-16); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-16-care-home-e-sc04-14-resident-waiting-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-16-care-home-e-sc04-14-resident-waiting-phone-{light,dark}.png` |
| E-SC04-14 Resident | Admitted | Badge "Admitted"; next: Absent or Left (UC-SC04-16); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-16-care-home-e-sc04-14-resident-admitted-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-16-care-home-e-sc04-14-resident-admitted-phone-{light,dark}.png` |
| E-SC04-14 Resident | Absent | Badge "Absent"; next: Admitted (UC-SC04-16); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-16-care-home-e-sc04-14-resident-absent-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-16-care-home-e-sc04-14-resident-absent-phone-{light,dark}.png` |
| E-SC04-14 Resident | Left | Badge "Left"; final: read-only, no next state; the history shows how it got here | U25, U26 | `u25-care-coordinator/s-sc04-16-care-home-e-sc04-14-resident-left-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-16-care-home-e-sc04-14-resident-left-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the carer and the family use the phone, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC04-06](../../flows/fl-sc04-06-care-homes-cesu-and-nursing.md)

## Open questions

None.

---

⬅️ [S-SC04-15 Rounds assistant](../03-visit/s-sc04-15-rounds-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-17 CESU](s-sc04-17-cesu.md)

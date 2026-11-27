🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-05 Council, civil registry, permits and assets](README.md) ›
🖥️ S-SC20-18 Civil registry

# 🖥️ S-SC20-18 Civil registry

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the acts to write, sign and annotate, and the
  extracts to issue.
- [U56 Citizen](../../../../01-users/personas/u56-citizen.md): my extract requests, on the phone.

## Purpose

Keep the acts of the civil registry, annotate them by margin notes and issue extracts to those entitled.

## Entry points

Public bodies › Civil registry; a citizen's extract request.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Civil registry: 2027                                       [Record an act] [Extract]             |
| Number     Kind     Person            Date        Notes   State                                  |
| 2027-B-18  Birth    Roux, Camille     12 Feb      0       Registered                             |
| 2027-M-04  Marriage Faure / Martin    5 Mar       1       Annotated                              |
| 2027-D-07  Death    Garcia, Henri     9 Mar       0       Drafted                                |
| Edit of a registered act: not allowed. A later event is added as a margin note within 3 days; a  |
| rectification follows the tribunal's order, or the officer's for a material error.               |
| [Add a margin note]                                                                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-05 step 2, U16 | desktop | ![FL-SC20-05 step 2, U16, light](../../images/05-council-registry-permits-and-assets/u16-office-worker/2-civil-registry-desktop-light.png) | ![FL-SC20-05 step 2, U16, dark](../../images/05-council-registry-permits-and-assets/u16-office-worker/2-civil-registry-desktop-dark.png) |
| FL-SC20-05 step 2, U16 | phone | ![FL-SC20-05 step 2, U16, light](../../images/05-council-registry-permits-and-assets/u16-office-worker/2-civil-registry-phone-light.png) | ![FL-SC20-05 step 2, U16, dark](../../images/05-council-registry-permits-and-assets/u16-office-worker/2-civil-registry-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-18-civil-registry-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-18-civil-registry-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-18-civil-registry-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-18-civil-registry-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-18-civil-registry-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-18-civil-registry-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc20-18-civil-registry-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc20-18-civil-registry-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Number | E-SC20-13 number | text | no | yes |
| Kind | E-SC20-13 kind | birth, marriage, death | yes while Drafted | yes |
| Persons | E-SC20-13 persons | list | yes while Drafted | yes |
| Date of the event | E-SC20-13 date | date | yes while Drafted | yes |
| Margin notes | E-SC20-13 notes | list of note, basis and date | yes only to add | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record an act | header | office worker | a drafted act is created |
| Sign | row | civil-status officer | the act is signed by the officer, the parties and the witnesses, and registered |
| Add a margin note | row | office worker | a note with its basis is attached: a later event within 3 days (Code civil 49), or a rectification ordered by the president of the tribunal, or made by the officer or on the prosecutor's order for a purely material error (99, 99-1) |
| Extract | header | office worker | a full copy only to those entitled (the person, close family, the legal representative, a mandated person, the prosecutor, the officer, the notary, the authorised administrations), a death act to anyone, the others with the prosecutor's leave; a copy carries its margin notes; every extract is logged ([BR-SC20-18](../../business-rules/br-sc20-18-civil-records-are-corrected-only-by-a-margin-note.md)) |

## States

- Normal: the acts with number, kind, persons, date, notes and state.
- Empty: No act yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an edit of a
  registered act, a person not entitled, with the act named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-13 Civil record](../../data/e-sc20-13-civil-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-13 Civil record | Drafted | Badge "Drafted"; a new record starts here; next: Registered (BR-SC20-18); fields editable within the role | U16, U56 | `u16-office-worker/s-sc20-18-civil-registry-e-sc20-13-civil-record-drafted-{desktop,phone}-{light,dark}.png`, `u56-citizen/s-sc20-18-civil-registry-e-sc20-13-civil-record-drafted-phone-{light,dark}.png` |
| E-SC20-13 Civil record | Registered | Badge "Registered"; next: Annotated or Archived (BR-SC20-18, UC-SC20-18); fields editable within the role | U16, U56 | `u16-office-worker/s-sc20-18-civil-registry-e-sc20-13-civil-record-registered-{desktop,phone}-{light,dark}.png`, `u56-citizen/s-sc20-18-civil-registry-e-sc20-13-civil-record-registered-phone-{light,dark}.png` |
| E-SC20-13 Civil record | Annotated | Badge "Annotated"; next: Archived (UC-SC20-18); fields editable within the role | U16, U56 | `u16-office-worker/s-sc20-18-civil-registry-e-sc20-13-civil-record-annotated-{desktop,phone}-{light,dark}.png`, `u56-citizen/s-sc20-18-civil-registry-e-sc20-13-civil-record-annotated-phone-{light,dark}.png` |
| E-SC20-13 Civil record | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U16, U56 | `u16-office-worker/s-sc20-18-civil-registry-e-sc20-13-civil-record-archived-{desktop,phone}-{light,dark}.png`, `u56-citizen/s-sc20-18-civil-registry-e-sc20-13-civil-record-archived-phone-{light,dark}.png` |

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

- [FL-SC20-05](../../flows/fl-sc20-05-council-registry-permits-and-assets.md)

## Open questions

None.

---

⬅️ [S-SC20-17 Council meetings](s-sc20-17-council-meetings.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-19 Planning permits](s-sc20-19-planning-permits.md)

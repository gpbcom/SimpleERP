🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-13 Keep employees' qualifications](README.md) › 🖥️ S-F9-35 Employee qualifications

# 🖥️ S-F9-35 Employee qualifications

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md): every employee, every field, the proofs; adds, changes, adds
  documents for AI reading.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): their own, read only, with what the AI read and its
  source.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): the team's eligibility per qualification type and the
  expiry dates; never the birth date, the fitness details or the proofs
  ([BR-F9-29](../../business-rules/br-f09-29-planners-see-eligibility-only.md)).

## Purpose

Keep an employee's degrees, qualifications, skills, languages, place and travel, person and contract attributes, with
their proof, status and source.

## Entry points

An employee's record (S-F9-01) › Qualifications; My HR (S-F9-04) › My qualifications; the expiry reminder; the
AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Paul Martin · Electrician · Works                     [+ Add] [Add a document for AI reading] |
|---------------------------------------------------------------------------------------------|
| DEGREES AND QUALIFICATIONS                                                                  |
|  Degree   Vocational diploma, electrician  EQF 3 · RNCP 3   2015   Verified   by hand   [pdf] |
|  Qualif.  Electrical authorisation B1V                      expires 2027-04-30  Verified [pdf]|
|  Qualif.  Driving licence B                                 expires 2033-06-01  To verify  AI |
|  Qualif.  First aid at work                                 expired 2026-10-02  Expired       |
| SKILLS AND LANGUAGES                                                                        |
|  Skills   Low-voltage wiring (expert), heat pumps (intermediate)                            |
|  Languages French (native), English (B1)                                                     |
| PLACE AND TRAVEL                                                                            |
|  Home base Lyon 3e · Zones: Lyon east, Villeurbanne · Maximum travel 45 min · Vehicle: van  |
| PERSON AND CONTRACT                                                                         |
|  Birth date 1992-03-14 (age checks only) · Medical fitness: fit, until 2028-01-15          |
|  Contract: permanent                                                                        |
|  Cost rate 38.00 EUR/h                                                                      |
+---------------------------------------------------------------------------------------------+
Manager's view: one line per person, a column per qualification type: "eligible", "expires in 60 days",
"not eligible: licence expired".
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-13 step 1, U06 | desktop | ![FL-F9-13 step 1, U06, light](../../images/13-keep-qualifications/u06-hr/1-employee-qualifications-desktop-light.png) | ![FL-F9-13 step 1, U06, dark](../../images/13-keep-qualifications/u06-hr/1-employee-qualifications-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/13-keep-qualifications/u06-hr/e1-the-ai-cannot-read-the-document-desktop-light.png) | ![Error E1, U06, dark](../../images/13-keep-qualifications/u06-hr/e1-the-ai-cannot-read-the-document-desktop-dark.png) |
| Error E3, U06 | desktop | ![Error E3, U06, light](../../images/13-keep-qualifications/u06-hr/e3-a-qualification-has-expired-desktop-light.png) | ![Error E3, U06, dark](../../images/13-keep-qualifications/u06-hr/e3-a-qualification-has-expired-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-35-employee-qualifications-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-35-employee-qualifications-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-35-employee-qualifications-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-35-employee-qualifications-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-35-employee-qualifications-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-35-employee-qualifications-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-35-employee-qualifications-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-35-employee-qualifications-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Degree | E-F9-29: title, EQF level, national level, field of study, institution, country, year, proof | row | HR | no (optional, VD-24) |
| Qualification | E-F9-12 generalised: type (E-F9-30), level or category, issued, expires, proof | row | HR | no |
| Status | E-F9-29, E-F9-12 status | to verify, verified, rejected, expired | by verifying (S-F9-36) | yes |
| Source | E-F9-29, E-F9-12 source | by hand, AI reading | no | yes |
| Skills, languages | E-F9-01 with level | list | HR | no |
| Place and travel | E-F9-01 home base, zones, maximum travel, vehicle | text, places | HR | no |
| Age check | E-F9-01 birth date | shown as "18 or more" or "under 18" except to HR | HR | no |
| Medical fitness | E-F9-01 fitness status, dates, restrictions; never a diagnosis | status | HR | no |
| Contract kind, cost rate | E-F9-02, E-F9-01 | text, amount | HR | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add | header | HR | a degree, a qualification or another attribute, verified, by hand |
| Add a document for AI reading | header | HR | document read; readings to verify (UC-F9-39) |
| Edit, remove | row | HR | changed, audited |
| Open proof | row | HR; the employee for their own | the document, the view audited |
| Verify | row "To verify" | HR | opens S-F9-36 on that reading |

## States

- Normal: the four families of the employee.
- Empty: nothing recorded yet: "No qualification yet" with Add and Add a document.
- Loading: skeleton rows; actions disabled until loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: the employee on their own; the manager's eligibility view.
- Offline: not available offline (HR data).

Shown entities (VD-15): [E-F9-29 Degree](../../data/e-f09-29-degree.md),
[E-F9-12 Qualification](../../data/e-f09-12-certification.md),
[E-F9-31 Attribute reading](../../data/e-f09-31-attribute-reading.md),
[E-F9-30 Qualification type](../../data/e-f09-30-qualification-type.md),
[E-F9-01 Employee record](../../data/e-f09-01-employee-record.md), [E-F9-02 Contract](../../data/e-f09-02-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-29 Degree | To verify | Amber badge, "AI"; does not count; Verify | U06, U01 | `u06-hr/s-f09-35-employee-qualifications-e-f09-29-degree-to-verify-desktop-{light,dark}.png`, `u01-employee/s-f09-35-employee-qualifications-e-f09-29-degree-to-verify-{desktop,phone}-{light,dark}.png` |
| E-F9-29 Degree | Verified | Green badge; counts | U06, U01 | `u06-hr/s-f09-35-employee-qualifications-e-f09-29-degree-verified-desktop-{light,dark}.png`, `u01-employee/s-f09-35-employee-qualifications-e-f09-29-degree-verified-{desktop,phone}-{light,dark}.png` |
| E-F9-29 Degree | Rejected | Struck through with the reason; HR only | U06 | `u06-hr/s-f09-35-employee-qualifications-e-f09-29-degree-rejected-desktop-{light,dark}.png` |
| E-F9-12 Qualification | To verify | Amber badge; does not count; Verify | U06, U01 | `u06-hr/s-f09-35-employee-qualifications-e-f09-12-certification-to-verify-desktop-{light,dark}.png`, `u01-employee/s-f09-35-employee-qualifications-e-f09-12-certification-to-verify-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | Verified | Green badge with the expiry date; "expires in n days" from 90 days | U06, U01, U02 | `u06-hr/s-f09-35-employee-qualifications-e-f09-12-certification-verified-desktop-{light,dark}.png`, `u01-employee/s-f09-35-employee-qualifications-e-f09-12-certification-verified-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-35-employee-qualifications-e-f09-12-certification-verified-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | Expired | Red badge; does not count; "Add the new proof" | U06, U01, U02 | `u06-hr/s-f09-35-employee-qualifications-e-f09-12-certification-expired-desktop-{light,dark}.png`, `u01-employee/s-f09-35-employee-qualifications-e-f09-12-certification-expired-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-35-employee-qualifications-e-f09-12-certification-expired-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | Rejected | Struck through with the reason; HR only | U06 | `u06-hr/s-f09-35-employee-qualifications-e-f09-12-certification-rejected-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | Reading | Banner "Reading in progress" | U06 | `u06-hr/s-f09-35-employee-qualifications-e-f09-31-attribute-reading-reading-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | Failed | Banner "The document could not be read"; Try again | U06 | `u06-hr/s-f09-35-employee-qualifications-e-f09-31-attribute-reading-failed-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | To verify | Banner "n readings to verify"; Verify | U06 | `u06-hr/s-f09-35-employee-qualifications-e-f09-31-attribute-reading-to-verify-desktop-{light,dark}.png` |
| E-F9-30 Qualification type | Active | Badge "Active"; a new record starts here; next: Retired (UC-F9-38); fields editable within the role | U06 | `u06-hr/s-f09-35-employee-qualifications-e-f09-30-qualification-type-active-desktop-{light,dark}.png` |
| E-F9-01 Employee record | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-35-employee-qualifications-e-f09-01-employee-record-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-35-employee-qualifications-e-f09-01-employee-record-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-35-employee-qualifications-e-f09-01-employee-record-active-desktop-{light,dark}.png` |
| E-F9-02 Contract | Draft | Badge "Draft"; a new record starts here; next: Running (UC-F9-01); fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-35-employee-qualifications-e-f09-02-contract-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-35-employee-qualifications-e-f09-02-contract-draft-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-35-employee-qualifications-e-f09-02-contract-draft-desktop-{light,dark}.png` |
| E-F9-02 Contract | Running | Badge "Running"; next: Expired (UC-F9-01); fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-35-employee-qualifications-e-f09-02-contract-running-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-35-employee-qualifications-e-f09-02-contract-running-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-35-employee-qualifications-e-f09-02-contract-running-desktop-{light,dark}.png` |
| E-F9-02 Contract | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f09-35-employee-qualifications-e-f09-02-contract-expired-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-35-employee-qualifications-e-f09-02-contract-expired-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-35-employee-qualifications-e-f09-02-contract-expired-desktop-{light,dark}.png` |

The states are those of the entity drafts and of the change note on E-F9-12.

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone: the families as folded sections; HR can add a document by taking a photo.

## Accessibility

Statuses are words, not only colours; the AI source is said in words ("read by the AI, verified by C. Roux"); tables
have headers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F9-13 Keep employees' qualifications](../../flows/fl-f09-13-keep-qualifications.md)

## Open questions

None.

---

⬅️ [S-F9-34 My position](../12-schedule-customer-requests/s-f09-34-my-position.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-36 Readings to verify](s-f09-36-readings-to-verify.md)

🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-15](README.md) ›
🖥️ S-F9-44 Online courses

# 🖥️ S-F9-44 Online courses

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md): builds, publishes and reads
  results.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): the courses of their plan and their results, on a
  phone.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the courses they bought, on a phone.

## Purpose

Build and publish courses, follow learners' progress and certificates, and take a course.

## Entry points

HR and projects › Training › Online courses; the shop's My courses; the AI assistant
([BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Online courses                                                       [New course] [Import]  |
| ------------------------------------------------------------------------------------------- |
| COURSE            AUDIENCE    PRICE   LEARNERS   PASSED   STATE                             |
| Safe lifting      Staff       Free    42         38       Published                         |
| Customer care     Customers   49.00   17         9        Published                         |
| Forklift basics   Staff       Free    0          0        Draft       [Publish]             |
| Safe lifting: module 3 of 4   Final assessment: 86   Certificate issued   [Download]        |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f09-44-online-courses-empty-desktop-{light,dark}.png`,
`s-f09-44-online-courses-empty-phone-{light,dark}.png`, `s-f09-44-online-courses-loading-desktop-{light,dark}.png`,
`s-f09-44-online-courses-loading-phone-{light,dark}.png`, `s-f09-44-online-courses-offline-desktop-{light,dark}.png`,
`s-f09-44-online-courses-offline-phone-{light,dark}.png`, `s-f09-44-online-courses-read-only-desktop-{light,dark}.png`,
`s-f09-44-online-courses-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-15 step 5, U38 | desktop | ![FL-F9-15 step 5, U38, light](../../images/15-work-location-headcount-and-learning/u38-training-coordinator/5-online-courses-desktop-light.png) | ![FL-F9-15 step 5, U38, dark](../../images/15-work-location-headcount-and-learning/u38-training-coordinator/5-online-courses-desktop-dark.png) |
| FL-F9-15 step 5, U38 | desktop | ![FL-F9-15 step 5, U38, light](../../images/15-work-location-headcount-and-learning/u38-training-coordinator/5-online-courses-desktop-light.png) | ![FL-F9-15 step 5, U38, dark](../../images/15-work-location-headcount-and-learning/u38-training-coordinator/5-online-courses-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-44-online-courses-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-44-online-courses-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-44-online-courses-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-44-online-courses-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-44-online-courses-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-44-online-courses-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-44-online-courses-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-44-online-courses-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Course | E-F9-52 title and modules | text and list | draft only | yes |
| Audience and price | E-F9-52 audience and price | choice and money | draft only | yes |
| Pass mark and attempts | E-F9-52 pass mark, attempts | numbers | draft only | yes |
| Learners and results | E-F9-52 learners and results | list | no | no |
| State | E-F9-52 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New course | header | the training coordinator | a Draft course (UC-F9-47) |
| Publish | course | the training coordinator | the course is Published and sold if priced |
| Unpublish | course | the training coordinator | no new enrolment |
| Enrol | course | a manager, HR, the learner | a learner is added |
| Take the assessment | course | the learner | a score and, if passed, a certificate |

## States

- Normal: the courses with their audience, price, learners and passes; a learner sees their modules.
- Empty: No course yet: a hint to create the first or import one.
- Loading: The courses as placeholders, then the counts.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a course with
  no assessment cannot be published as a certificate course.
- Read-only: an archived course, or a role that may only read: shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-52 Online course](../../data/e-f09-52-online-course.md),
[E-F9-12 Qualification](../../data/e-f09-12-certification.md),
[E-F9-22 Training session](../../data/e-f09-22-training-session.md),
[E-F11-03 Online product](../../../f11-online-shop/data/e-f11-03-online-product.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-52 Online course | Draft | Badge "Draft"; a new record starts here; next: Published or Archived (UC-F9-47); fields editable within the role | U38, U01, U09 | `u38-training-coordinator/s-f09-44-online-courses-e-f09-52-online-course-draft-desktop-{light,dark}.png`; `u01-employee/s-f09-44-online-courses-e-f09-52-online-course-draft-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-44-online-courses-e-f09-52-online-course-draft-phone-{light,dark}.png` |
| E-F9-52 Online course | Published | Badge "Published"; next: Unpublished or Archived (UC-F9-47); fields editable within the role | U38, U01, U09 | `u38-training-coordinator/s-f09-44-online-courses-e-f09-52-online-course-published-desktop-{light,dark}.png`; `u01-employee/s-f09-44-online-courses-e-f09-52-online-course-published-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-44-online-courses-e-f09-52-online-course-published-phone-{light,dark}.png` |
| E-F9-52 Online course | Unpublished | Badge "Unpublished"; next: Published or Archived (UC-F9-47); fields editable within the role | U38, U01, U09 | `u38-training-coordinator/s-f09-44-online-courses-e-f09-52-online-course-unpublished-desktop-{light,dark}.png`; `u01-employee/s-f09-44-online-courses-e-f09-52-online-course-unpublished-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-44-online-courses-e-f09-52-online-course-unpublished-phone-{light,dark}.png` |
| E-F9-52 Online course | Archived | Badge "Archived"; final state, read-only | U38, U01, U09 | `u38-training-coordinator/s-f09-44-online-courses-e-f09-52-online-course-archived-desktop-{light,dark}.png`; `u01-employee/s-f09-44-online-courses-e-f09-52-online-course-archived-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-44-online-courses-e-f09-52-online-course-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a phone, the learner sees the modules as a list with the progress bar and the assessment button.

## Accessibility

Progress and results are words and numbers, not only colours; videos have captions; keyboard: next module, start the
assessment.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-15 Work location, headcount, careers and learning](../../flows/fl-f09-15-work-location-headcount-and-learning.md)

## Open questions

None.

---

⬅️ [S-F9-43 Project risks](s-f09-43-project-risks.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L01 Employee records](../00-lists/s-f09-l01-employee-records.md)

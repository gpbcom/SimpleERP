🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
🖥️ [Screens](README.md) › 🖥️ S-F4-24 Employee calendar

# 🖥️ S-F4-24 Employee calendar

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../01-users/personas/u02-manager.md)
- [U03 Sales](../../../01-users/personas/u03-sales.md)
- [U04 Purchasing and stock](../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../01-users/personas/u05-accounting.md)
- [U06 Human resources](../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U12 Marketing and communication](../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)
- [U14 Field worker](../../../01-users/personas/u14-field-worker.md)
- [U15 Warehouse operator](../../../01-users/personas/u15-warehouse-operator.md)
- [U16 Office worker](../../../01-users/personas/u16-office-worker.md)
- [U17 Cashier](../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../01-users/personas/u18-waiter.md)
- [U19 Kitchen staff](../../../01-users/personas/u19-kitchen-staff.md)
- [U20 Production operator](../../../01-users/personas/u20-production-operator.md)
- [U21 Production planner](../../../01-users/personas/u21-production-planner.md)
- [U22 Site manager](../../../01-users/personas/u22-site-manager.md)
- [U23 Store manager](../../../01-users/personas/u23-store-manager.md)
- [U24 Engagement manager](../../../01-users/personas/u24-engagement-manager.md)
- [U25 Care coordinator](../../../01-users/personas/u25-care-coordinator.md)
- [U26 Carer](../../../01-users/personas/u26-carer.md)
- [U27 Quality manager](../../../01-users/personas/u27-quality-manager.md)
- [U28 Hotel receptionist](../../../01-users/personas/u28-hotel-receptionist.md)
- [U29 Dispatcher](../../../01-users/personas/u29-dispatcher.md)
- [U30 Driver](../../../01-users/personas/u30-driver.md)
- [U31 Treasurer](../../../01-users/personas/u31-treasurer.md)
- [U33 Medical secretary](../../../01-users/personas/u33-medical-secretary.md)
- [U34 Property manager](../../../01-users/personas/u34-property-manager.md)
- [U35 Real-estate agent](../../../01-users/personas/u35-real-estate-agent.md)
- [U36 Professional](../../../01-users/personas/u36-professional.md)
- [U37 Professional's assistant](../../../01-users/personas/u37-assistant.md)
- [U38 Training coordinator](../../../01-users/personas/u38-training-coordinator.md)
- [U39 Trainer](../../../01-users/personas/u39-trainer.md)
- [U40 Farmer](../../../01-users/personas/u40-farmer.md)
- [U41 Customer success manager](../../../01-users/personas/u41-customer-success-manager.md)
- [U42 Sales representative](../../../01-users/personas/u42-sales-representative.md)
- [U43 Event producer](../../../01-users/personas/u43-event-producer.md)
- [U44 Box-office agent](../../../01-users/personas/u44-box-office-agent.md)
- [U45 Payroll officer](../../../01-users/personas/u45-payroll-officer.md)

Each persona sees the fields and the actions its roles allow, as on
[S-F4-L26 Employee calendars](00-lists/s-f04-l26-employee-calendars.md): the record rules and field rules of T2.

## Purpose

See one [E-F4-26 Employee calendar](../data/e-f04-26-employee-calendar.md) and act on it: its fields, its
state and the changes its state allows. It is the page the rows of
[S-F4-L26 Employee calendars](00-lists/s-f04-l26-employee-calendars.md) open (VR-13).

## Entry points

- [S-F4-L26 Employee calendars](00-lists/s-f04-l26-employee-calendars.md) › a row's Open ›.
- A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Employee calendars   Léa Moreau                               [Active] |
|--------------------------------------------------------------------------|
| employee               Léa Moreau                                        |
| status                 active                                            |
| calendar sync          Google Calendar, Workspace mode                   |
| working hours          Monday to Friday, 9:00 to 17:30                   |
| time zone              Europe/Paris                                      |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Active (Employee calendar), U01 | desktop | ![Active (Employee calendar), U01, light](../images/states/u01-employee/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-light.png) | ![Active (Employee calendar), U01, dark](../images/states/u01-employee/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-f04-24-employee-calendar-empty-desktop-light.png) | ![Empty, dark](../images/states/s-f04-24-employee-calendar-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-f04-24-employee-calendar-loading-desktop-light.png) | ![Loading, dark](../images/states/s-f04-24-employee-calendar-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-f04-24-employee-calendar-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-f04-24-employee-calendar-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../images/states/s-f04-24-employee-calendar-offline-phone-light.png) | ![Offline, dark](../images/states/s-f04-24-employee-calendar-offline-phone-dark.png) |

## Fields and columns

As [E-F4-26 Employee calendar](../data/e-f04-26-employee-calendar.md#fields). A field is read-only when the
record's state is final or the role's field rules lock it; personal-data fields show only to the roles that may read
them (VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | saves the fields; audited |
| Change state | the personas whose roles may change it | one of the Lifecycle's transitions: Active to Archived (UC-F9-02) |
| Ask the AI assistant | every persona of the page | an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-F4-L26 Employee calendars](00-lists/s-f04-l26-employee-calendars.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-26 Employee calendar](../data/e-f04-26-employee-calendar.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-26 Employee calendar | Active | Badge "Active"; a new record starts here; next: Archived (UC-F9-02); fields editable within the role | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16, U17, U18, U19, U20, U21, U22, U23, U24, U25, U26, U27, U28, U29, U30, U31, U33, U34, U35, U36, U37, U38, U39, U40, U41, U42, U43, U44, U45 | `u01-employee/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u05-accounting/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u06-hr/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u07-administrator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u12-marketing/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-phone-{light,dark}.png`, `u15-warehouse-operator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u18-waiter/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u20-production-operator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-tablet-{light,dark}.png`, `u21-production-planner/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u24-engagement-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u26-carer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-phone-{light,dark}.png`, `u27-quality-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,tablet}-{light,dark}.png`, `u29-dispatcher/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u30-driver/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-phone-{light,dark}.png`, `u31-treasurer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u34-property-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,tablet}-{light,dark}.png`, `u35-real-estate-agent/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u36-professional/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u38-training-coordinator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png`, `u39-trainer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u40-farmer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u41-customer-success-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u42-sales-representative/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone,tablet}-{light,dark}.png`, `u43-event-producer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-active-desktop-{light,dark}.png` |
| E-F4-26 Employee calendar | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U01, U02, U03, U04, U05, U06, U07, U12, U13, U14, U15, U16, U17, U18, U19, U20, U21, U22, U23, U24, U25, U26, U27, U28, U29, U30, U31, U33, U34, U35, U36, U37, U38, U39, U40, U41, U42, U43, U44, U45 | `u01-employee/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u05-accounting/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u06-hr/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u07-administrator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u12-marketing/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-phone-{light,dark}.png`, `u15-warehouse-operator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{phone,tablet}-{light,dark}.png`, `u16-office-worker/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u18-waiter/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u20-production-operator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-tablet-{light,dark}.png`, `u21-production-planner/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u24-engagement-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u26-carer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-phone-{light,dark}.png`, `u27-quality-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,tablet}-{light,dark}.png`, `u29-dispatcher/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u30-driver/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-phone-{light,dark}.png`, `u31-treasurer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u34-property-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,tablet}-{light,dark}.png`, `u35-real-estate-agent/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u36-professional/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u38-training-coordinator/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png`, `u39-trainer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u40-farmer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u41-customer-success-manager/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u42-sales-representative/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone,tablet}-{light,dark}.png`, `u43-event-producer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f04-24-employee-calendar-e-f04-26-employee-calendar-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; on a phone the fields stack in one column and the actions move to a menu.

## Accessibility

The state badge has its state as text; Change state is a menu of buttons named by the next state; the history is a list
whose length is announced.

## Components

- [C-01 Button](../../../04-ux/design-system/components/c-01-button.md)
- [C-02 Form field](../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../04-ux/design-system/components/c-05-modal.md)
- [C-14 Timeline](../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

The list page whose rows open this page (Row opens), then the flows whose Entities and screens table names it:

- [S-F4-L26 Employee calendars](00-lists/s-f04-l26-employee-calendars.md)
- [FL-F4-07 Prepare and capture anywhere](../flows/fl-f04-07-prepare-and-capture-anywhere.md)

## Open questions

None.

---

⬅️ [S-F4-23 Agreed actions](13-outside-people-and-follow-up/s-f04-23-agreed-actions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-25 Video message](14-video-messages-and-webinars/s-f04-25-video-message.md)

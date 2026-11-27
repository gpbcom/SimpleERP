🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F9-47 Outreach message

# 🗃️ E-F9-47 Outreach message

**Status:** ✅ specified

## Purpose

One message of an outreach sequence, sent to a prospect or received from them, with the AI assistant's class for a reply
([D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)).

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| sequence | outreach sequence | yes | - | - | Site manager, Lyon | no | no |
| prospect | prospect | yes | - | - | Julien R. | yes | no |
| direction | sent or received | yes | - | - | received | no | no |
| kind | invitation note, direct message, follow-up, booking-link reply, thank-you, HR's reply, reply | yes | - | - | follow-up 1 | no | no |
| text | text | yes | an approved template, filled in, for what SimpleERP sends | - | Is remote work possible two days a week? | yes | no |
| planned at | date and time | for what SimpleERP sends | by day 60 | - | 2026-11-10 09:30 | no | no |
| prepared at, expires at | date and time | in prepared mode, once the message falls due | expires 7 days after its task was created, unless HR clicked Send (D570) | - | 2026-11-10 09:30, 2026-11-17 09:30 | no | no |
| task | project and task (E-F9-18) | in prepared mode, once the message falls due | the task in the sequence owner's task list, with Send; closed when the message is sent, expires or is cancelled (D570) | - | Send follow-up 1 to Julien R. | yes | no |
| sent or received at | date and time | once sent or received | - | - | 2026-11-12 18:04 | no | no |
| sent by | HR user or the sequence | once sent | the HR user's click in prepared mode, the sequence in automatic mode (D570) | - | Claire P. | yes | no |
| provider message ID | text | once sent or received | unique, as Unipile returns it | - | as Unipile returns it | no | no |
| class | positive, negative, question, unclear | for a reply | - | - | question | yes | no |
| class reason and confidence | text and percent | for a reply | - | - | asks about remote work, 91 % | yes | no |
| classified by | AI assistant or HR | for a reply | - | AI assistant | AI assistant | no | no |
| status | planned, prepared, sent, failed, cancelled, expired, received, classified, reviewed | yes | the lifecycle below | planned | sent | no | no |

## Relations

```mermaid
erDiagram
  OUTREACH_SEQUENCE ||--o{ OUTREACH_MESSAGE : sends
  PROSPECT ||--o{ OUTREACH_MESSAGE : "is written to"
  OUTREACH_MESSAGE |o--o| PROJECT_AND_TASK : "waits as"
```

- [E-F9-46 Outreach sequence](e-f09-46-outreach-sequence.md)
- [E-F9-45 Prospect](e-f09-45-prospect.md)
- [E-F9-18 Project and task](e-f09-18-project-and-task.md): the task of a prepared message

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Planned : the sequence plans it, UC-F9-41
  Planned --> Prepared : falls due in prepared mode, a task for HR, D570
  Prepared --> Sent : HR clicks Send, D570
  Prepared --> Failed : HR clicked Send, refused or a limit reached, BR-F9-41
  Prepared --> Expired : not sent within 7 days, D570
  Prepared --> Cancelled : a reply, a refusal, or day 60, BR-F9-37
  Planned --> Sent : sent on its own in automatic mode, or retried after HR's click, D570
  Planned --> Failed : refused or a limit reached, BR-F9-41
  Failed --> Planned : tried again the next day, BR-F9-41
  Failed --> Cancelled : day 60, BR-F9-37
  Planned --> Cancelled : a reply, a refusal, or day 60, BR-F9-37
  [*] --> Received : a reply found by the check, UC-F9-41
  Received --> Classified : the AI assistant classifies it, UC-F9-41
  Classified --> Reviewed : HR confirms or changes the class, UC-F9-41
  Sent --> [*] : UC-F9-41
  Cancelled --> [*] : BR-F9-37
  Expired --> [*] : D570
  Classified --> [*] : UC-F9-42
  Reviewed --> [*] : UC-F9-41
```

Every message SimpleERP sends is prepared in prepared mode: the invitation or the direct message, the follow-ups, the
booking-link reply and the thank-you on a refusal
([D570](../../../06-decisions/f09-hr-and-projects/d570-linkedin-sending-prepared-by-default.md)). When it falls due it
becomes Prepared and waits as a task in the task list of the HR user who owns the sequence, with Send there and on
[S-F9-39](../screens/02-recruit/s-f09-39-prospect-conversations.md). HR's click stands: a message a limit holds after
the click is tried again the next day without a new click and never expires
([BR-F9-41](../business-rules/br-f09-41-linkedin-account-limits-respected.md)). A message not sent within 7 days of the
creation of its task expires and is never sent; the prospect goes on as if they had not answered, and a prospect whose
first message expired gets no follow-up ([E-F9-45 Prospect](e-f09-45-prospect.md)). HR is not notified per message:
one daily digest lists the messages to send and those expiring within 24 hours
([notifications](../notifications.md)).

## Indexes and search

By prospect and date; unique provider message ID; the replies waiting for HR.

## Retention

With its prospect: erased with them, or kept with the applicant's record
([BR-F9-39](../business-rules/br-f09-39-prospects-kept-only-as-long-as-needed.md),
[BR-F9-11](../business-rules/br-f09-11-candidate-data-has-a-term.md)).

## Audit

Planned, prepared with its task, sent (by HR's click or automatically), failed, cancelled, expired, received; each class
with its source and confidence; each class changed by HR, with the old and the new class.

## Import and export

No import; the person's own copy on request
([CR-FR-195](../../../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md)).

## Used by

- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [UC-F9-42 Turn a positive reply into an applicant](../use-cases/02-recruit/uc-f09-42-turn-a-positive-reply-into-an-applicant.md)

## Open questions

None.

---

⬅️ [E-F9-46 Outreach sequence](e-f09-46-outreach-sequence.md) · ⬆️ [Up](README.md) ·
➡️ [E-F9-48 Work location day](e-f09-48-work-location-day.md)

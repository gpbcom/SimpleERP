🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🎙️ F4 Meetings

# 🎙️ F4 Meetings

**Status:** ✅ specified

Build step: 2. Platform.

## Summary

Meetings, online, in person or by phone, become transcripts, summaries, decisions and tasks linked to the company's
records, with the recordings deleted once checked ([D208](../../06-decisions/f04-meetings/d208-meeting-sources.md) to
[D211](../../06-decisions/f04-meetings/d211-meeting-access.md)).

## Scope

- **Sources:** Teams, Meet and Zoom (their transcripts, or the announced bot,
  [D7](../../06-decisions/foundations/d07-where-meetings-come-from.md),
  [D23](../../06-decisions/foundations/d23-meeting-bot-consent.md)); self-hosted Jitsi and BigBlueButton; in-person
  recording with the phone app or a microphone; phone calls through the company's phone system.
- **Outputs:** transcript with speakers and times; summary; decisions and action items offered as tasks (confirmed,
  UC-F3-03); links to the customer, project, deal or employee; a follow-up email draft.
- **Recordings:** deleted once the transcript is checked, 7 days by default.
- **Access:** participants see everything; the linked record's readers see the summary; HR meetings stay with HR and the
  person concerned.
- **Benchmark additions (D302):** team chat, appointments booked by customers, incoming call routing.
- **Gaps and improvements round ([D461](../../06-decisions/f04-meetings/d461-f04-gaps-and-improvements.md),
  2026-11-12):** topics and trends across calls, live captions and translation, outside speakers' objection and erasure
  rights, transcription accuracy per language and model, meeting rooms through the shared booking engine,
  [UC-F2-18](../f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  client video meetings, the customer's side of agreed actions, two-way sync of actions with F9 tasks, and deeper HR and
  scoring flows.

## Personas

[U01 Employee](../../01-users/personas/u01-employee.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U06 HR](../../01-users/personas/u06-hr.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U04 Purchasing and stock](../../01-users/personas/u04-purchasing.md),
[U09 Customer](../../01-users/personas/u09-customer.md),
[U36 Professional](../../01-users/personas/u36-professional.md),
[U33 Medical secretary](../../01-users/personas/u33-medical-secretary.md).

## Out of scope

- Hosting video calls: SimpleERP records and transcribes, it is not a meeting platform.
- Scheduling and calendars beyond linking a meeting to its invitation (F9 and outside calendars, UC-F3-06).

## Technical capabilities used

- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (speech-to-text and summaries,
  D82)
- [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md) (platform connections)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Assistant](../f03-assistant/README.md) · ⬆️ [Up](../README.md) · ➡️ [Social media](../f05-social-media/README.md)

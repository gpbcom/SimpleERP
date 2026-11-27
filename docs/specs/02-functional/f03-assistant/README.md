🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🤖 F3 Assistant

# 🤖 F3 Assistant

**Status:** ✅ specified

Build step: 2. Platform.

## Summary

The AI assistant in the side panel of every screen (D49): it answers from the company's data, acts for the user after
confirmation, summarises and drafts, and guides. See [D138](../../06-decisions/f03-assistant/d138-f3-scope.md).

## Scope

- **Answer from the ERP's data:** records and documents the user may see, with their sources linked.
- **Act for the user:** create or change records within the user's rights, always shown and confirmed first
  ([D140](../../06-decisions/f03-assistant/d140-assistant-confirms-changes.md)).
- **Summarise and draft:** a record's history, emails, quote texts, reports.
- **Find and guide:** find a record or a screen; explain how to do something, step by step.
- **Sources:** records, attached files, meeting transcripts (F4), the company knowledge base, and outside tools through
  MCP, A2A and APIs, per role ([D139](../../06-decisions/f03-assistant/d139-f3-sources.md)).
- **Conversations:** private by default, shareable with colleagues
  ([D141](../../06-decisions/f03-assistant/d141-shareable-conversations.md)).
- **Where it runs:** local model by default, an external provider if chosen, only what the request needs
  ([D5](../../06-decisions/foundations/d05-where-the-ai-runs.md),
  [D83](../../06-decisions/f01-administration/d83-only-what-the-request-needs.md)).
- **Benchmark additions (D301):** AI agents (always-on, scheduled, on demand), agent governance, AI fields on records,
  the AI assistant in Slack, Teams and Telegram.
- **Gaps and improvements round ([D460](../../06-decisions/f03-assistant/d460-f03-gaps-and-improvements.md),
  2026-11-12):** a quality evaluation set run at every model or prompt change, defences against instructions hidden in
  content (prompt injection), an opt-in personal memory, the query behind each figure, a cost estimate before expensive
  questions, and unanswered topics turned into knowledge proposals. Not chosen: an AI assistant for portal users and
  ready-made sector agents.

## Personas

Every internal persona ([D142](../../06-decisions/f03-assistant/d142-f3-use-cases.md)):
[U01](../../01-users/personas/u01-employee.md), [U02](../../01-users/personas/u02-manager.md),
[U03](../../01-users/personas/u03-sales.md), [U04](../../01-users/personas/u04-purchasing.md),
[U05](../../01-users/personas/u05-accounting.md), [U06](../../01-users/personas/u06-hr.md),
[U07](../../01-users/personas/u07-administrator.md), [U12](../../01-users/personas/u12-marketing.md),
[U13](../../01-users/personas/u13-owner.md), [U14](../../01-users/personas/u14-field-worker.md),
[U15](../../01-users/personas/u15-warehouse-operator.md), [U16](../../01-users/personas/u16-office-worker.md),
[U01 Employee](../../01-users/personas/u01-employee.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U05 Accounting](../../01-users/personas/u05-accounting.md),
[U06 Human resources](../../01-users/personas/u06-hr.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U08 External accountant](../../01-users/personas/u08-external-accountant.md).

## Out of scope

- Answers on the law: the [legal assistant F15](../f15-legal-assistant/README.md), which shares the same panel.
- Choosing the AI provider: [F1](../f01-administration/README.md) (UC-F1-08).

## Technical capabilities used

- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | 🔄 |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | 🔄 |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [No-code configuration](../f02-no-code-configuration/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Meetings](../f04-meetings/README.md)

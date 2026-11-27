🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🎧 F16 Customer support agents

# 🎧 F16 Customer support agents

**Status:** ✅ specified

Build step: 3. Customers and sales.

## Summary

AI agents that resolve customer requests end to end, including complex ones that need the customer's data and actions in
back-office tools, in SimpleERP's own customer service or inside the company's outside helpdesk; each kind of request
is automated only once it proves accurate
([D237](../../06-decisions/f16-customer-support-agents/d237-customer-support-agents.md)).

## Scope

- **Channels:** email, chat and messages, voice (F4's telephony), web forms, the customer portal (F6).
- **Helpdesks:** works in SimpleERP's own requests or in an outside helpdesk (Zendesk, Intercom, HubSpot, Freshdesk,
  Notion and others, T12): it assigns itself, tags, routes and answers like a human agent.
- **Intents:** each request is classified into an intent and a branch (duplicate charge, late-delivery refund, goodwill
  gesture, cancellation within the cooling-off period, pro-rata termination, invoice re-send, payment method update,
  debt recovery, parcel tracking, lost parcel claim, plan upgrade, password reset, claim reopening and others).
- **Procedures:** each intent has a written procedure (SOP) in a versioned library; the agent fetches the procedure and
  the customer's data, follows it, acts and answers.
- **Actions:** refunds, cancellations and terminations, plan changes with usage-based advice, quotes, certificate and
  document sending, beneficiary changes, claim sorting, deposit and payment status checks, onboarding; in SimpleERP or
  in outside tools through T12, with or without an API.
- **Modes per intent:** human, shadow (runs on live requests without acting, measured) or automatic; rollout intent by
  intent after analysing past requests, automatic only above an accuracy threshold.
- **Quality:** every resolution scored by an AI judge and sampled by people; procedures improved from reviews;
  non-regression tests before a procedure change goes live.
- **Static or agentic:** an intent runs as a fixed workflow (F2) or as an agent with tools
  ([D238](../../06-decisions/f16-customer-support-agents/d238-static-or-agentic.md)).
- **Monitoring:** resolved share, automatic versus shadow, accuracy per intent, volumes, in real time; a full audit
  trail of understanding, reasoning and every action.
- **Confirmed** by the owner ([D262](../../06-decisions/f16-customer-support-agents/d262-f16-scope-confirmed.md));
  go-live bar [D261](../../06-decisions/f16-customer-support-agents/d261-go-live-bar.md), helpdesks
  [D263](../../06-decisions/f16-customer-support-agents/d263-built-in-and-outside-helpdesks.md), sampling
  [D264](../../06-decisions/f16-customer-support-agents/d264-human-sampling.md).
- **People and customers:** service levels, the agent workspace with queues, macros and locks, satisfaction surveys, the
  public help centre, languages, the customer's status, person and rating, refund limits, duplicate guard, intent
  discovery and fraud signals (D473).

## Personas

[U09 Customer](../../01-users/personas/u09-customer.md) (asks),
[U16 Office worker](../../01-users/personas/u16-office-worker.md) (handles what stays human),
[U02 Manager](../../01-users/personas/u02-manager.md) (support lead: procedures, rollout, quality),
[U07 Administrator](../../01-users/personas/u07-administrator.md) (connectors, credentials),
[U13 Owner](../../01-users/personas/u13-owner.md).

## Out of scope

- Pricing per resolved request: SimpleERP is self-hosted; the monitoring still counts resolutions.
- Building connectors: T12.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 3, Customers and sales, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the
specifications hold.

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

⬅️ [Legal assistant](../f15-legal-assistant/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Competitive analysis](../f17-competitive-analysis/README.md)

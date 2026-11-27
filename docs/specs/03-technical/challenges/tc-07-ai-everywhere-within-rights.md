🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) ›
🤖 TC-07 The AI assistant can do everything, within the user's rights

# 🤖 TC-07 The AI assistant can do everything, within the user's rights

**Status:** ✅ listed for the technical interviews

## Challenge

Make every action of every capability reachable from the AI assistant and from outside agents (MCP and A2A, both ways),
with the user's rights, confirmations for changes, and an audit of what the AI did.

## Raised by

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [F20 Hosted support assistant (hosted edition)](../../02-functional/f20-hosted-support-assistant/README.md)
- [T6 MCP and A2A gateway](../t06-mcp-and-a2a-gateway/README.md)
- [T7 AI providers and models](../t07-ai-providers-and-models/README.md)

## Why it is hard

- Hundreds of actions across 21 capabilities must be described as tools without drifting from the API.
- An agent acting on its own (support agents, scheduled agents) needs limits: budget, allow-list, confirmation policy.
- Prompt injection from documents, emails and scraped pages can try to make the AI act.

## Already decided

- [D5](../../06-decisions/foundations/d05-where-the-ai-runs.md) Where the AI runs
- [D238](../../06-decisions/f16-customer-support-agents/d238-static-or-agentic.md) Static workflows or agents

## Options to weigh

- Tools generated from the API contract, so that one change updates both.
- A policy layer between the model and the tools (rights, confirmations, budgets) apart from the prompt.
- Separating untrusted content from instructions in every prompt.

## Settled in

- 19d API design and contracts ([chapter](../../../technical/interfaces/api.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- 19f Security ([chapter](../../../technical/security/security.md))
- Then the technical capabilities: [T6 MCP and A2A gateway](../t06-mcp-and-a2a-gateway/README.md),
  [T7 AI providers and models](../t07-ai-providers-and-models/README.md).

## Questions for the interview

- Which actions may an agent take without a person's confirmation?
- How are AI costs capped per company in the hosted edition?

---

⬅️ [TC-06 Offline devices and synchronisation](tc-06-offline-devices-and-sync.md) · ⬆️ [Up](README.md) ·
➡️ [TC-08 Search and RAG that respect rights and erasure](tc-08-permission-aware-search.md)

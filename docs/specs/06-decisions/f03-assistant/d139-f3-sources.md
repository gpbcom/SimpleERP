🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D139 Assistant knowledge sources

# 📜 D139 Assistant knowledge sources

**Status:** ✅ decided

## Context

Which knowledge the AI assistant answers from, besides the records.

## Options

- Attached files.
- Meeting transcripts (F4).
- A company knowledge base.
- Outside tools (MCP, A2A), which the owner said include APIs.

## Choice

All four: files attached to records; meeting transcripts and summaries the user may see; a company knowledge base of
uploaded documents; and outside tools through MCP, A2A and outside APIs, per role.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

F1's connections also accept outside APIs; an outside API is connected from its OpenAPI description. Every
source is indexed by T8 under permissions.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [UC-F1-07](../../02-functional/f01-administration/use-cases/05-connect-an-external-tool/uc-f01-07-connect-an-external-mcp-server-or-a2a-agent.md)
- [T8 RAG platform](../../03-technical/t08-rag-platform/README.md)

---

⬅️ [D138 F3 Assistant scope](d138-f3-scope.md) · ⬆️ [Up](README.md) ·
➡️ [D140 The AI assistant confirms changes](d140-assistant-confirms-changes.md)

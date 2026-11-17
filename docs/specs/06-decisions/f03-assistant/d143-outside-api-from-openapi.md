🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D143 Outside APIs from their OpenAPI description

# 📜 D143 Outside APIs from their OpenAPI description

**Status:** ✅ decided

## Context

How an outside API is connected as a tool (D139).

## Options

- From its OpenAPI description.
- Described by hand.
- Both.

## Choice

From its OpenAPI description: the administrator gives the file or its address and a key; its operations are listed as
tools to review and turn on, like an MCP server (BR-F1-13).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

UC-F1-07 covers outside APIs too.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [UC-F1-07](../../02-functional/f01-administration/use-cases/05-connect-an-external-tool/uc-f01-07-connect-an-external-mcp-server-or-a2a-agent.md)

---

⬅️ [D142 F3 use cases and personas](d142-f3-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D144 Shared conversations show everything](d144-shared-conversations-show-everything.md)

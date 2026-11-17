🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D79 Any external tool, with a warning

# 📜 D79 Any external tool, with a warning

**Status:** ✅ decided

## Context

Which external MCP servers and A2A agents an administrator may connect.

## Options

- Any, with a warning.
- A curated list only.
- Self-hosted only.

## Choice

Any server or agent, by its address: simple-ERP warns that data sent to it leaves the server (D5) and shows the tools it
offers before it is turned on.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Connecting is the administrator's informed choice.

## Related

- [UC-F1-07](../../02-functional/f01-administration/use-cases/05-connect-an-external-tool/uc-f01-07-connect-an-external-mcp-server-or-a2a-agent.md)
- [BR-F1-13](../../02-functional/f01-administration/business-rules/br-f01-13-external-data-warning.md)

---

⬅️ [D78 Ready-made roles are copied](d78-ready-made-roles-copied.md) · ⬆️ [Up](README.md) ·
➡️ [D80 External tools per role](d80-external-tools-per-role.md)

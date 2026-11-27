🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D129 Workflow designer blocks

# 📜 D129 Workflow designer blocks

**Status:** ✅ decided

## Context

Which building blocks the visual workflow designer offers.

## Options

- Branches and conditions.
- Waits and timers.
- Parallel paths and joins.
- Human tasks and forms.
- API, MCP, A2A and connectors, and AI operations (added by the owner).

## Choice

Six kinds of blocks: branches and conditions; waits and timers; parallel paths and joins; human tasks and forms; API,
MCP, A2A and connector calls; AI operations with a custom prompt and output format.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Workflows can call outside systems and AI, under the connections' and AI settings' rules (D80, D81, D83).

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)

---

⬅️ [D128 No level limit on rule chains](d128-no-chain-level-limit.md) · ⬆️ [Up](README.md) ·
➡️ [D130 Workflows for non-technical users](d130-workflows-for-non-technical-users.md)

🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D413 Configuration layers

# 📜 D413 Configuration layers

**Status:** ✅ decided

## Context

Step 19e of the technical interview, from TC-02 and TC-03.

## Options

- Files, environment, database and vault, or a central configuration service.
- Configuration exported and promoted, or live editing only.
- A module registry in the core, or flags per service.
- Workflows on the workflow engine, or simple event rules.

## Choice

Confirmed by the owner on 2026-11-12: the four layers; configuration exported, versioned and promoted; a module registry
in the core; no-code workflows on the durable workflow engine with limits.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The configuration chapter's target design.

## Related

- [Configuration layers](../../../technical/architecture/configuration.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D412 A2A agents](d412-a2a-agents.md) · ⬆️ [Up](README.md) · ➡️ [D414 Security design](d414-security-design.md)

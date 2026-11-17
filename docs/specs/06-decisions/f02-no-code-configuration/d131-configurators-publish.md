🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D131 Configurators publish

# 📜 D131 Configurators publish

**Status:** ✅ decided

## Context

Who publishes a configuration change.

## Options

- The configurator, administrators told.
- An administrator approves.
- The configurator only.

## Choice

Configurators publish their own drafts; administrators are notified with a summary of what changed.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No approval step; the history and roll-back (D132) are the safety net.

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)

---

⬅️ [D130 Workflows for non-technical users](d130-workflows-for-non-technical-users.md) · ⬆️ [Up](README.md) ·
➡️ [D132 Roll-back restores configuration only](d132-roll-back-configuration-only.md)

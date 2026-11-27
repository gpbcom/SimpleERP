🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D132 Roll-back restores configuration only

# 📜 D132 Roll-back restores configuration only

**Status:** ✅ decided

## Context

What a roll-back restores.

## Options

- Configuration only, data kept.
- One change at a time.

## Choice

The configuration returns to the chosen version; records keep their data (values of fields that disappear are archived,
BR-F2-01); records in a status that no longer exists are listed to move.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

A roll-back never loses data.

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)

---

⬅️ [D131 Configurators publish](d131-configurators-publish.md) · ⬆️ [Up](README.md) ·
➡️ [D133 Workflow AI steps setting](../f01-administration/d133-workflow-ai-steps-setting.md)

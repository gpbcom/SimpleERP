🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-24 Local changes are kept unless a legal block changed

# 📏 BR-F2-24 Local changes are kept unless a legal block changed

**Status:** ✅ specified

## Statement

In a pack upgrade, items changed only by the pack merge by themselves, conflicts are decided by the configurator, and
locked legal blocks always take the pack's version.

## Why

Companies keep their changes, while the law's mentions stay right (BR-F2-10).

## Examples

| Case | Result |
|---|---|
| Pack changes a field the company did not touch | Merged |
| Both changed the visit form | Configurator decides |
| Pack fixes a legal mention | Pack's version |

## Applies to

- [UC-F2-25 Merge a sector pack upgrade with local changes](../use-cases/10-change-safely/uc-f02-25-merge-a-sector-pack-upgrade-with-local-changes.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-23 A failing test case blocks the publish](br-f02-23-a-failing-test-case-blocks-the-publish.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F2-25 Field rights apply on every channel](br-f02-25-field-rights-apply-on-every-channel.md)

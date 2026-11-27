🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-19 Exports follow field rights and masking

# 📏 BR-F24-19 Exports follow field rights and masking

**Status:** ✅ specified

## Statement

An export sends only the fields the pipeline's owner may read, applies the masking set for each personal field, never
sends a secret, and writes a run only as a whole: the destination holds the last complete state or the new one, never a
part.

## Why

The destination is outside SimpleERP's rights model, so the rights must be applied before the data leaves. The owner
asked for a data warehouse export
([D543](../../../06-decisions/f24-integrations-hub/d543-benchmark-gaps-f24-integrations-hub.md)); field rights apply on
every channel
([BR-F2-25](../../f02-no-code-configuration/business-rules/br-f02-25-field-rights-apply-on-every-channel.md)).

## Examples

| Case | Result |
|---|---|
| A field the administrator may read | can be exported, masked or not as set |
| A field the administrator may not read | cannot be chosen |
| A password hash or a key | never exported, in no setting |
| A personal field masked with a hash | the destination gets the hash only |
| A run that fails after 300 of 412 rows | the 300 rows are not kept at the destination |

## Applies to

- [UC-F24-30](../use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-30-export-data-to-a-warehouse.md)
- [E-F24-18 Export pipeline](../data/e-f24-18-export-pipeline.md)
- [BR-F2-25](../../f02-no-code-configuration/business-rules/br-f02-25-field-rights-apply-on-every-channel.md)
- [E-F24-06 Sync job](../data/e-f24-06-sync-job.md)

## Exceptions

None.

## Configurable

The fields exported and their masking, by the administrator within their rights.

## Open questions

None.

---

⬅️ [BR-F24-18 Suite access uses the fewest scopes needed](br-f24-18-suite-access-uses-the-fewest-scopes-needed.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F24-20 One side is the master per period](br-f24-20-one-side-is-the-master-per-period.md)

🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-29 Bulk changes are previewed and can be undone

# 📏 BR-F2-29 Bulk changes are previewed and can be undone

**Status:** ✅ specified

## Statement

A bulk change shows a preview with its counts, a sample and the records it will skip before anything is changed, needs a
typed confirmation above the batch size limit, applies each record's own rights, statuses and validations, and can be
undone as a whole for 7 days.

## Why

Changing hundreds of records by mistake is expensive: the user must see the effect first and be able to go back. The
owner's answer: "Bulk edit and mass actions"
([D521](../../../06-decisions/f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md)); it extends
[BR-F3-08](../../f03-assistant/business-rules/br-f03-08-a-batch-is-undone-as-a-whole.md) and
[BR-F3-09](../../f03-assistant/business-rules/br-f03-09-batch-size-limit.md), which already apply to the AI assistant's
batches.

## Examples

| Case | Result |
|---|---|
| 212 records selected, a field the user may change | preview, then apply on confirmation |
| More than 500 records | the confirmation asks to type the number |
| A record on a locked status | skipped, listed with the reason |
| Undo on day 3 | every record changed returns to its old value |
| Undo on day 9 | refused: the 7 days have passed |
| A record changed again after the operation | left as it is when undoing, listed |

## Applies to

- [UC-F2-32 Edit records in bulk](../use-cases/13-low-code-bulk-and-cleaning/uc-f02-32-edit-records-in-bulk.md)
- [E-F2-31 Bulk operation](../data/e-f02-31-bulk-operation.md)
- [UC-F3-03 Have the AI assistant create or change records](../../f03-assistant/use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)

## Exceptions

None.

## Configurable

Yes: the batch size above which a typed confirmation is asked, and the undo window up to 30 days.

## Open questions

None.

---

⬅️ [BR-F2-28](br-f02-28-scripts-run-sandboxed-within-time-and-memory-limits.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-30](br-f02-30-time-based-rules-run-once-per-record-and-period.md)

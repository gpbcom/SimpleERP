🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-08 A batch is undone as a whole

# 📏 BR-F3-08 A batch is undone as a whole

**Status:** ✅ specified

## Statement

After a confirmed batch, an "Undo" on its message reverts every change of the batch at once, as long as no one changed
any of those records since; otherwise Undo is unavailable, says which record changed and by whom, and each record's
history shows what to restore.

## Why

An undo must never overwrite a colleague's later change. See
[D158](../../../06-decisions/f03-assistant/d158-assistant-undo.md).

## Examples

| Case | Result |
|---|---|
| 12 tasks updated, nothing else touched them | Undo restores all 12 |
| A colleague changed one of the 12 since | Undo unavailable: "Paul Martin changed task T-88 at 15:32" |
| A created quote, still a draft, untouched | Undo removes it (the only removal the AI assistant does, of its own creation) |

## Applies to

- [UC-F3-03](../use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-07 No deletes, no irreversible acts](br-f03-07-no-deletes-no-irreversible-acts.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-09 Batch size limit](br-f03-09-batch-size-limit.md)

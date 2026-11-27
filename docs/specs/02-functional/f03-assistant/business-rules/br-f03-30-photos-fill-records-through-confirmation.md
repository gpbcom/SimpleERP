🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-30 Photos fill records through confirmation

# 📏 BR-F3-30 Photos fill records through confirmation

**Status:** ✅ specified

## Statement

A photo or scan taken in the AI assistant is read by the model chosen for it (local by default, D5); what it reads is
shown, and filling a record from it goes through the confirmation card (BR-F3-07 to BR-F3-10); the photo is
attached to the record it fills.

## Why

The phone's camera saves typing in the field. See [D183](../../../06-decisions/f03-assistant/d183-photo-questions.md).

## Examples

| Case | Result |
|---|---|
| A delivery note | Supplier, items and quantities read; "Record this delivery?" card |
| A meter reading | "Meter 0042: 18,452 kWh. Add it to visit V-212?" |
| A blurred photo | "I can't read this photo. Please take it again, closer and with more light." |

## Applies to

- [UC-F3-09](../use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)

## Exceptions

None.

## Configurable

Yes: the model used for photos is an AI feature setting (F1).

## Open questions

None.

---

⬅️ [BR-F3-29 Offline questions wait for the network](br-f03-29-offline-questions-wait-for-the-network.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F3-31 Phone context is the task and the day](br-f03-31-phone-context-is-the-task-and-the-day.md)

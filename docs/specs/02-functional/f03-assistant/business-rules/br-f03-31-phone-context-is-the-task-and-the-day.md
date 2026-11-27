🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-31 Phone context is the task and the day

# 📏 BR-F3-31 Phone context is the task and the day

**Status:** ✅ specified

## Statement

On a phone, the context chip holds the task or visit open and the user's tasks of the day; the user can remove it; the
phone's location is used only if the user allows it, each time or always, and can be withdrawn.

## Why

Field questions are about the job at hand. See [D184](../../../06-decisions/f03-assistant/d184-phone-context.md).

## Examples

| Case | Result |
|---|---|
| On visit V-212, "what did we fit last time?" | The previous visits of that customer |
| "What's next?" | The next task of the day |
| "Nearest customer site?" without location allowed | "Allow location for this question?" |

## Applies to

- [UC-F3-09](../use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)

## Exceptions

None.

## Configurable

Yes: location, by each user.

## Open questions

None.

---

⬅️ [BR-F3-30 Photos fill records through confirmation](br-f03-30-photos-fill-records-through-confirmation.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-32 Retry before an error](br-f03-32-retry-before-an-error.md)

🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-01 Automatic only above the bar

# 📏 BR-F16-01 Automatic only above the bar

**Status:** ✅ specified

## Statement

An intent goes from shadow to automatic only after at least 99 % accuracy on at least 200 real requests run in shadow,
judged by the AI judge and a human sample, and a manager's switch; in automatic, if accuracy falls below 97 % over a
week, the intent falls back to shadow by itself and the support lead is told.

## Why

See [D261](../../../06-decisions/f16-customer-support-agents/d261-go-live-bar.md).

## Examples

| Case | Result |
|---|---|
| 212 shadow cases at 99.1 % | The manager can switch it to automatic |
| 150 cases at 100 % | Not yet: fewer than 200 |
| Automatic, a week at 96.4 % | Back to shadow, lead told |

## Applies to

Every F16 use case concerned.

## Exceptions

None.

## Configurable

No: the bar is 99 % over 200 cases, the fallback 97 % over a week.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F16-02 A sample is always reviewed](br-f16-02-a-sample-is-always-reviewed.md)

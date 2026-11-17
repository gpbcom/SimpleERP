🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-02 A sample is always reviewed

# 📏 BR-F16-02 A sample is always reviewed

**Status:** ✅ specified

## Statement

In automatic mode, a random 5 % of resolutions, plus every resolution the AI judge scores below its bar, is reviewed by
a person; a correction is recorded against the procedure and counts in the intent's accuracy.

## Why

See [D264](../../../06-decisions/f16-customer-support-agents/d264-human-sampling.md).

## Examples

| Case | Result |
|---|---|
| 1,000 automatic resolutions | About 50 sampled, plus the low-scored ones |
| A reviewer corrects a refund amount | The procedure gets a suggested change; accuracy counts the error |

## Applies to

Every F16 use case concerned.

## Exceptions

None.

## Configurable

The sample rate, 5 % at least.

## Open questions

None.

---

⬅️ [BR-F16-01 Automatic only above the bar](br-f16-01-automatic-only-above-the-bar.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-03 Agents act only as their procedure allows](br-f16-03-agents-act-only-as-their-procedure-allows.md)

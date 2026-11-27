🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-16 Fall back to the local model

# 📏 BR-F1-16 Fall back to the local model

**Status:** ✅ specified

## Statement

When an external provider fails or is too slow, the feature answers with the local model and says so.

## Why

AI features keep working, as far as the local model can. See
[D84](../../../06-decisions/f01-administration/d84-fall-back-to-local.md).

## Examples

| Case | Result |
|---|---|
| Provider down | Local answer, marked "answered by the local model" |
| Provider slower than 20 seconds | Local answer, same mark |
| AI turned off (D22) | No answer: the feature says AI is off |

## Applies to

- [UC-F1-08](../use-cases/06-choose-an-ai-provider/uc-f01-08-choose-the-ai-provider-of-a-feature.md); F3, F4, F5, F15.

## Exceptions

AI turned off for the company (D22).

## Configurable

The time limit, per feature.

## Open questions

None.

---

⬅️ [BR-F1-15 Only what the request needs](br-f01-15-only-what-the-request-needs.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-17 Administrators keep a password](br-f01-17-administrators-keep-a-password.md)

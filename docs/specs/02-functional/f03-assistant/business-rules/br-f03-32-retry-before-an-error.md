🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-32 Retry before an error

# 📏 BR-F3-32 Retry before an error

**Status:** ✅ specified

## Statement

A call that fails or times out (the model, an outside tool, a synced origin, a queued question) is retried up to 3 times
with exponential backoff, each wait twice the previous one, 1, 2 and 4 seconds; while retrying, the panel
shows "Still trying..."; only after the third retry fails is the error shown, following the error message pattern
(D122). A refusal (no right, data not allowed, cap reached) is never retried.

## Why

Short outages should not reach users. See [D188](../../../06-decisions/f03-assistant/d188-retry-before-an-error.md).

## Examples

| Case | Result |
|---|---|
| The local model is busy once | Retried after 1 s; the user sees the answer |
| An outside tool down for a minute | 3 retries (1, 2, 4 s), then "The shipping tool is not answering. Try again in a few minutes." with a reference |
| A cap reached | No retry; the cap message at once |

## Applies to

- [UC-F3-01](../use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md),
  [UC-F3-02](../use-cases/02-ask-about-the-screen/uc-f03-02-ask-about-what-is-on-screen.md),
  [UC-F3-04](../use-cases/04-summarise-or-draft/uc-f03-04-summarise-and-draft.md),
  [UC-F3-06](../use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md),
  [UC-F3-07](../use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md),
  [UC-F3-09](../use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)

## Exceptions

Refusals are never retried.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-31 Phone context is the task and the day](br-f03-31-phone-context-is-the-task-and-the-day.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-33 Usage reports never show content](br-f03-33-usage-reports-never-show-content.md)

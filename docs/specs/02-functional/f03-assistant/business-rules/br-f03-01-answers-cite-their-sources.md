🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-01 Answers cite their sources

# 📏 BR-F3-01 Answers cite their sources

**Status:** ✅ specified

## Statement

Every fact taken from a record or a document links to it in the text, and a "Sources" list closes the answer; each
source opens in the side panel without leaving the screen.

## Why

Users must be able to check an answer in one click. See
[D149](../../../06-decisions/f03-assistant/d149-answer-sources.md).

## Examples

| Case | Result |
|---|---|
| "When did we last invoice Durand?" | "On 3 October ([INV-2026-0412](#))", Sources: INV-2026-0412 |
| A summary from 3 documents | 3 inline links, 3 sources |
| A general question, "how do I create a quote?" | No record source; the help page is the source |

## Applies to

- [UC-F3-01](../use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md); every
  assistant answer of F3.
- [UC-F3-14 Run the quality evaluation set](../use-cases/11-trust-the-answers/uc-f03-14-run-the-quality-evaluation-set.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [BR-F3-02 Answers use only what the user may see](br-f03-02-answers-use-only-what-the-user-may-see.md)

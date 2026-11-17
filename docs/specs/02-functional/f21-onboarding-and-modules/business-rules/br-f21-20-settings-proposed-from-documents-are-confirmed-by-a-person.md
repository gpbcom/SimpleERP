🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-20 Settings proposed from documents are confirmed by a person

# 📏 BR-F21-20 Settings proposed from documents are confirmed by a person

**Status:** 🔄 waiting for the owner

## Statement

A setting proposed from the company's documents is applied only after a person confirms that line; the AI never applies
a setting on its own, shows the document and passage each proposal came from, and puts the settings that carry a risk
(VAT regime, financial year, chart of accounts) first and confirmed one by one.

## Why

A wrong guess about the VAT regime or the year end ripples through every document that follows, and an AI can read a
page wrongly. The owner asked to set up from documents
([D540](../../../06-decisions/f21-onboarding-and-modules/d540-benchmark-gaps-f21-onboarding-and-modules.md)).

## Examples

| Case | Result |
|---|---|
| A year end read from the accounts | proposed with its page, applied after the owner accepts |
| A line the owner leaves unanswered | not applied |
| Two documents that disagree | both shown, the owner picks |
| A VAT regime proposed from one invoice | shown first and confirmed alone |
| A document the owner did not upload | never read |

## Applies to

- [UC-F21-29](../use-cases/06-experts-cutover-and-parallel-run/uc-f21-29-set-up-from-last-years-documents.md)
- [E-F21-02 Company profile](../data/e-f21-02-company-profile.md)
- [E-F21-03 Set-up template](../data/e-f21-03-set-up-template.md)

## Exceptions

None.

## Configurable

Whether the documents are kept after the set-up, by the owner.

## Open questions

None.

---

⬅️ [BR-F21-19](br-f21-19-differences-are-explained-before-the-old-tool-stops.md) · ⬆️ [Up](README.md)

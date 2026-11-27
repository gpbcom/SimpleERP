🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-40 No search criterion the law forbids in hiring

# 📏 BR-F9-40 No search criterion the law forbids in hiring

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A sourcing search and its scores use only criteria related to the job; a criterion the law forbids in hiring (an age, a
sex, a family situation, an origin, a state of health, and the other grounds the law lists) is refused, and the AI
assistant's score never uses them, nor a photo or a name.

## Why

Job offers and hiring may not discriminate
([CR-FR-194](../../../10-country-packs/france/labour/cr-fr-194-job-offer-rules.md), which cites the Code pénal, articles
225-1 to 225-4); candidate scoring needs job-related criteria checked for bias
([BR-F4-21](../../f04-meetings/business-rules/br-f04-21-candidate-scoring-is-high-risk-ai.md)). (⚖️ lawyer review before launch, D574)
The full list of grounds is still to read into the France country pack (Code pénal 225-1, Code du travail L1132-1), as
[CR-FR-194](../../../10-country-packs/france/labour/cr-fr-194-job-offer-rules.md) lists only those of job offers.

## Examples

| Case | Result |
|---|---|
| Years of experience 5 to 15 | passes: related to the job |
| Under 35 | fails: an age |
| No children | fails: a family situation |
| French and English B2 for a job with English-speaking clients | passes |
| A graduation year used to guess an age | fails |

## Applies to

- [UC-F9-40 Search and rank LinkedIn profiles](../use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md)
- [E-F9-44 Sourcing search](../data/e-f09-44-sourcing-search.md)

## Exceptions

A legal condition of the job (a driving licence, a minimum legal age for the work) is a requirement of the
job, not a forbidden criterion.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F9-39](br-f09-39-prospects-kept-only-as-long-as-needed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-41 The LinkedIn account's limits are respected](br-f09-41-linkedin-account-limits-respected.md)

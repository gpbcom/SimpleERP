🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-14 Data-subject requests answered within one month

# 📏 BR-F15-14 Data-subject requests answered within one month

**Status:** ✅ specified

## Statement

A request for access to or erasure of personal data is answered within one month of the request, after the identity is
checked; erasure reaches every place the data is, search indexes included.

## Why

[CR-FR-051 Access and erasure](../../../10-country-packs/france/data-protection/cr-fr-051-access-and-erasure.md).

## Examples

| Case | Result |
|---|---|
| Request on 2026-11-12, copy sent on 2026-11-30 | passes |
| Request on 2026-11-12, still open on 2026-12-13 | fails: overdue, administrator and owner told |
| Erasure of a former employee whose payslips must be kept | passes: erased except what the law keeps (BR-F13-13), the person told why |

## Applies to

- [UC-F15-10 Answer a data-subject request](../use-cases/06-privacy-and-ai-duties/uc-f15-10-answer-a-data-subject-request.md)

## Exceptions

Data the law requires to keep is kept and the person is told which and why.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-13 Company-law deadlines kept](br-f15-13-company-law-deadlines-kept.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-15 Every AI use inventoried with its risk class](br-f15-15-every-ai-use-inventoried-with-its-risk-class.md)

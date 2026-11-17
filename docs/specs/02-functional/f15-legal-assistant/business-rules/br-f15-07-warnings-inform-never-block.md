🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-07 Warnings inform, never block

# 📏 BR-F15-07 Warnings inform, never block

**Status:** ✅ specified

## Statement

A legal warning shows next to what triggered it, says what may break which rule (article, version, date), and never
blocks the action; the person can open the explanation, ask a follow-up, or dismiss it with a reason. Warnings go to
whoever is acting, and those who must know (HR for a contract), never revealing another person's private data. Warnings
are on by default; an administrator can turn them off, then the AI assistant answers on demand only (D193).

## Why

A warning helps decide; the law leaves the decision to the company.

Legal values from the France country pack:
[CR-FR-042 Working time and rest](../../../10-country-packs/france/labour/cr-fr-042-working-time-and-rest.md),
[CR-FR-046 Headcount thresholds](../../../10-country-packs/france/labour/cr-fr-046-headcount-thresholds.md).

## Examples

| Case | Result |
|---|---|
| A schedule leaves 9 hours between two shifts | "Daily rest under 11 hours (Code du travail, L3131-1)" on the schedule |
| Headcount reaches 11 | HR and the owner: "Staff representatives (CSE) must be elected" with the deadlines |
| Warnings turned off | Nothing shown; questions still answered |

## Applies to

- [UC-F15-01](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-02](../use-cases/02-receive-a-legal-warning/uc-f15-02-receive-a-legal-warning.md)

## Exceptions

None.

## Configurable

Yes: on or off, per kind of warning, by an administrator.

## Open questions

None.

---

⬅️ [BR-F15-06 A quality drop blocks the update](br-f15-06-a-quality-drop-blocks-the-update.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-08 Document checks list, never rewrite](br-f15-08-document-checks-list-never-rewrite.md)
